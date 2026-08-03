#!/usr/bin/env python3
"""Autocomprobación del equipo — ARCHIVO 2031.

    python3 scripts/autocheck.py

Dice qué falta SIN decir las respuestas. El sello se valida por hash: si las
seis palabras son correctas verás ✓, y si no, no hay pistas.

Revisa el repositorio local y, si tienen la CLI `gh` autenticada, también el
estado en GitHub (PRs, revisiones y Pages). Si `gh` no está, lo dice claramente
en vez de dar por bueno lo que no comprobó.

Es un subconjunto de la corrección oficial: pasarla es necesario, no
suficiente. La letra del equipo se lee del `<meta name="equipo">` de
index.html.
"""

import hashlib
import json
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
TOTAL_FRAGMENTOS = 6

VERDE, ROJO, GRIS, RESET = "\033[32m", "\033[31m", "\033[90m", "\033[0m"
if not sys.stdout.isatty():
    VERDE = ROJO = GRIS = RESET = ""

resultados: list[tuple[bool, str, str]] = []


def check(ok: bool, titulo: str, ayuda: str = "") -> None:
    resultados.append((bool(ok), titulo, ayuda))


def leer(rel: str) -> str:
    p = RAIZ / rel
    return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""


def git(*args: str) -> str:
    try:
        r = subprocess.run(["git", "-C", str(RAIZ), *args], capture_output=True, text=True)
    except OSError:
        return ""
    return r.stdout.strip() if r.returncode == 0 else ""


html = leer("index.html")
m_equipo = re.search(r'<meta name="equipo" content="([^"]*)"', html)
equipo = (m_equipo.group(1).strip().upper() if m_equipo else "")

claves_path = RAIZ / "scripts" / "claves.json"
if not claves_path.exists():
    sys.exit("✗ falta scripts/claves.json")
CLAVES = json.loads(claves_path.read_text(encoding="utf-8"))

if equipo not in CLAVES["equipos"]:
    sys.exit(
        f'✗ equipo "{equipo}" desconocido.\n'
        f'  Declaren su letra en el <meta name="equipo" content="?"> de index.html.\n'
        f"  Válidas: {', '.join(CLAVES['equipos'])}"
    )
SELLO_SHA256 = CLAVES["equipos"][equipo]
TAG_ENTREGA = CLAVES["tag_entrega"]

# --- 1. La cinta está montada -------------------------------------------------
refs_locales = git("for-each-ref", "--format=%(refname)").splitlines()
check(
    len(refs_locales) > 2,
    "la cinta del incidente está montada en el repositorio",
)

# --- 2. Auditoría estructural -------------------------------------------------
auditoria = subprocess.run(
    [sys.executable, str(RAIZ / "scripts" / "audit.py")], capture_output=True, text=True
)
ultima = auditoria.stdout.strip().splitlines()
check(auditoria.returncode == 0, "scripts/audit.py pasa", ultima[-1] if ultima else "")

# --- 3. Archivos recuperados --------------------------------------------------
for i in range(1, TOTAL_FRAGMENTOS + 1):
    rel = f"bitacora/frag-{i:02d}.txt"
    check((RAIZ / rel).exists(), f"{rel} presente")

for rel in ("styles/crt.css", "assets/sello.svg"):
    check((RAIZ / rel).exists(), f"{rel} recuperado")

check((RAIZ / "bitacora" / "SELLO.txt").exists(), "bitacora/SELLO.txt existe")
check((RAIZ / "bitacora" / "INFORME.md").exists(), "bitacora/INFORME.md existe")

# --- 4. index.html ------------------------------------------------------------
check("styles/crt.css" in html, "index.html enlaza styles/crt.css")
relleno = ("NOMBRE PENDIENTE", "ROL PENDIENTE", "usuario-github-", "Fotografía pendiente")
check(
    not any(marca in html for marca in relleno),
    "las 3 tarjetas ya no tienen datos de relleno",
)

ranuras = re.findall(
    r'data-frag="(\d{2})".*?<code class="frag__palabra">([^<]*)</code>', html, flags=re.DOTALL
)
llenas = [(n, w.strip().upper()) for n, w in ranuras if w.strip() and w.strip() != "???"]
check(
    len(llenas) == TOTAL_FRAGMENTOS,
    f"las {TOTAL_FRAGMENTOS} ranuras de index.html están llenas",
    f"llenas: {len(llenas)}/{TOTAL_FRAGMENTOS}",
)

# --- 5. Sello -----------------------------------------------------------------
m_sello = re.search(r"^SELLO:\s*(.+)$", leer("bitacora/SELLO.txt"), flags=re.MULTILINE)
sello = m_sello.group(1).strip().upper() if m_sello else ""
sello_ok = bool(sello) and hashlib.sha256(sello.encode()).hexdigest() == SELLO_SHA256
check(sello_ok, "el sello es CORRECTO", "hash no coincide" if sello else "falta la línea SELLO:")

m_html = re.search(r'id="sello-valor"[^>]*>([^<]*)<', html)
check(
    sello_ok and bool(m_html) and m_html.group(1).strip().upper() == sello,
    "index.html muestra el sello correcto",
)

orden = [w for _, w in sorted(llenas, key=lambda t: t[0])]
check(
    len(llenas) == TOTAL_FRAGMENTOS and sello_ok and "-".join(orden) == sello,
    "las ranuras coinciden con SELLO.txt",
)

# --- 6. Informe ---------------------------------------------------------------
informe = leer("bitacora/INFORME.md")
citados = len(set(re.findall(r"FRAG-0[1-6]", informe.upper())))
comandos = len(re.findall(r"git\s+[a-z-]+", informe))
check(
    citados == TOTAL_FRAGMENTOS and comandos >= 7,
    "INFORME.md documenta los 6 fragmentos con su comando",
    f"fragmentos: {citados}/6, comandos: {comandos}",
)

# --- 7. Entrega ---------------------------------------------------------------
tag = TAG_ENTREGA
check(
    git("cat-file", "-t", f"refs/tags/{tag}") == "tag",
    f"existe la etiqueta ANOTADA {tag}",
    "una etiqueta ligera no cuenta",
)
check(
    bool([l for l in git("for-each-ref", "--format=%(refname)").splitlines()
          if l.startswith("refs/notes/")]),
    "dejaron una nota de Git propia",
)

# --- 8. GitHub ----------------------------------------------------------------
MIN_PR = 6
omitido_github = ""


def gh(ruta: str):
    r = subprocess.run(["gh", "api", "--paginate", ruta], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError((r.stderr or "gh falló").strip().splitlines()[0])
    crudo = r.stdout.strip()
    return json.loads(re.sub(r"\]\s*\[", ",", crudo)) if crudo else []


m_slug = re.search(r"github\.com[:/]+([^/]+/[^/.]+)", git("remote", "get-url", "origin"))
if not m_slug:
    omitido_github = "no hay un remoto de GitHub configurado"
elif not shutil.which("gh"):
    omitido_github = "la CLI gh no está instalada (https://cli.github.com)"
else:
    slug = m_slug.group(1)
    try:
        pulls = gh(f"repos/{slug}/pulls?state=all&per_page=100")
        mergeados = [p for p in pulls if p.get("merged_at")]
        check(
            len(mergeados) >= MIN_PR,
            f"al menos {MIN_PR} Pull Requests mergeados",
            f"mergeados: {len(mergeados)}/{MIN_PR}",
        )

        con_revision = 0
        for pr in mergeados:
            autor = (pr.get("user") or {}).get("login", "").lower()
            revisiones = gh(f"repos/{slug}/pulls/{pr['number']}/reviews")
            if any(
                rv.get("state") == "APPROVED"
                and (rv.get("user") or {}).get("login", "").lower() != autor
                for rv in revisiones
            ):
                con_revision += 1
        check(
            bool(mergeados) and con_revision == len(mergeados),
            "cada PR mergeado tiene aprobación de otro integrante",
            f"con revisión cruzada: {con_revision}/{len(mergeados)}",
        )

        url = ""
        try:
            pages = gh(f"repos/{slug}/pages")
            url = pages.get("html_url", "") if isinstance(pages, dict) else ""
        except RuntimeError:
            url = ""
        vivo = False
        if url:
            try:
                with urllib.request.urlopen(url, timeout=15) as resp:
                    vivo = resp.status == 200
            except (urllib.error.URLError, TimeoutError, OSError):
                vivo = False
        check(vivo, "GitHub Pages publicado y respondiendo", url or "Pages no está activo")
    except RuntimeError as exc:
        omitido_github = f"gh no pudo consultar {slug}: {exc}"

# --- Reporte ------------------------------------------------------------------
print(f"\n  ARCHIVO 2031 · autocomprobación — equipo {equipo}")
print("  " + "─" * 56)
for ok, titulo, ayuda in resultados:
    marca = f"{VERDE}✓{RESET}" if ok else f"{ROJO}✗{RESET}"
    extra = f"  {GRIS}{ayuda}{RESET}" if ayuda and not ok else ""
    print(f"  {marca} {titulo}{extra}")

logrados = sum(1 for ok, _, _ in resultados if ok)
completo = logrados == len(resultados)
print("  " + "─" * 56)
print(f"  {logrados}/{len(resultados)} comprobaciones superadas")

if omitido_github:
    print(f"  {ROJO}⚠ GitHub sin revisar{RESET}: {omitido_github}")
    print(f"  {GRIS}  Faltan por comprobar: PRs mergeados, revisión cruzada y Pages.{RESET}")
    completo = False

print()
print(f"  {VERDE}LISTO PARA ENTREGAR{RESET}\n" if completo else f"  {ROJO}TODAVÍA NO{RESET}\n")
sys.exit(0 if completo else 1)
