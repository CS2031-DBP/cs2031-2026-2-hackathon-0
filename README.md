# 🛰️ Hackatón 0 — ARCHIVO 2031

**CS2031 · Desarrollo Basado en Plataformas · UTEC · 2026-2**

---

## Por qué esta hackatón es distinta

Las ediciones anteriores pedían resolver un conflicto y subir una página. Ya no
alcanza: hoy cualquiera le pide a un modelo que le escriba el HTML y lo pega.
Perfecto — **este reto no se gana escribiendo código.**

Aquí hay dos cosas que una IA no puede hacer por ustedes:

1. **La información que necesitan no existe fuera de este repositorio.** Está
   guardada dentro de un archivo binario que van a tener que aprender a abrir
   con Git, en commits que nadie referencia, en el mensaje de una etiqueta y en
   una referencia que ni siquiera se descarga por defecto.
2. **La entrega no es un archivo: es un historial.** Lo que se corrige es la
   forma del grafo de commits que ustedes construyan — que haya merges reales,
   un revert trazable, un cherry-pick trazable, una etiqueta anotada. Eso no se
   pega: se hace.

Usen IA todo lo que quieran para aprender comandos. No les va a servir para
saber **qué buscar, dónde, y en qué orden**.

> 🎯 **Regla de oro:** cada hallazgo se documenta con el comando exacto que lo
> produjo. Si no pueden reproducirlo delante de un TA, no cuenta.

---

## 🧩 El escenario

Heredan el **ARCHIVO 2031**: una terminal web con la bitácora de un proyecto.
Alguien ejecutó un script de "limpieza" sobre el repositorio original y lo que
les queda es el escombro:

- La bitácora está vacía: **seis fragmentos** desaparecieron.
- Un commit rompió el sitio y nadie sabe cuál fue.
- `styles/base.css` perdió su bloque de accesibilidad.
- El glifo del sello y una capa visual completa no están.
- Las tarjetas del equipo tienen datos de relleno.

Pero del repositorio original quedó **una cinta de respaldo**: el archivo
`incidente/equipo-<X>.bundle`. Ahí adentro está toda la historia previa al
incidente. Su trabajo es montarla, excavarla y reconstruir el archivo.

Cuando las seis palabras estén en su sitio, la terminal se sella sola y su
estado pasa de `INCOMPLETO` a `RESTAURADO`.

---

## 👥 Equipos

Equipos de **exactamente 3 integrantes**, con tres roles reales:

| Rol | Responsabilidad |
|---|---|
| 🧭 **Líder / integrador** | Crea el repositorio, abre issues, revisa y mergea los PR, conduce la resolución de conflictos. |
| 🔎 **Arqueólogo** | Excava la cinta. Es quien encuentra los fragmentos. |
| 🧰 **Cirujano** | Ejecuta el revert y el cherry-pick, sanea el árbol, deja el despliegue vivo. |

Los roles no son excusas: **los tres deben tener commits, PRs y revisiones.**
La corrección lo verifica commit por commit.

---

## ⚙️ Fase 0 — Puesta en marcha

El **líder**:

1. En este repositorio, pulsa **`Use this template` → `Create a new repository`**.
   Nombre sugerido: `archivo-2031-<equipo>`.
   > ⚠️ Marquen **Public**. GitHub Pages solo funciona en repositorios privados
   > con planes de pago, y sus cuentas son gratuitas: si lo dejan privado, no
   > van a poder desplegar y pierden el bloque de entrega.
   >
   > Van a recibir un repositorio con **un solo commit**: el suyo. Eso es
   > correcto y es el punto — **su historial empieza en cero y lo construyen
   > ustedes.** La historia que van a investigar viaja aparte, en la cinta.
2. `Settings → Collaborators`: agrega a los otros 2 integrantes.
3. `Settings → General → Pull Requests`: **desactiva "Allow squash merging"** y
   deja activo "Allow merge commits". El squash aplasta el trabajo de sus
   compañeros y la corrección lo penaliza.
4. `Settings → Pages → Source: GitHub Actions`.
5. `Settings → Branches`: protege `main`. Nadie hace push directo.

**Todo cambio entra por Pull Request**, no solo las tarjetas. Esperamos al menos
**6 PR mergeados**: los 3 individuales de la Fase 4, más los de arqueología,
cirugía y entrega. Repártanse el trabajo en ramas desde el principio; dejarlo
todo para tres PR al final cuesta puntos en el bloque A.

Y todo el equipo:

```bash
git clone https://github.com/<usuario>/archivo-2031-<equipo>.git
cd archivo-2031-<equipo>
```

Por último, **declaren su letra de equipo** en `index.html`:

```html
<meta name="equipo" content="C" />
```

Esa letra decide cuál es su cinta y contra qué se corrigen. Cada equipo tiene
fragmentos distintos: copiarle a otro equipo es fallar con más pasos.

---

## 🔭 Fase 1 — Montar la cinta

Lean `incidente/LEEME.md`. Ahí está explicado qué es un `git bundle` y cómo se
monta. En resumen: es un repositorio entero dentro de un archivo, y Git lo trata
como si fuera un remoto.

Antes de montarlo, **inspecciónenlo**:

```bash
git bundle verify incidente/equipo-<X>.bundle
git bundle list-heads incidente/equipo-<X>.bundle
```

Preguntas que deben poder responder por escrito antes de seguir:

1. ¿Cuántas referencias trae la cinta y cuántas de ellas **no** son ramas?
2. Una vez montada, ¿cuántos commits tiene su rama principal y quién los firmó?
3. ¿Hay ramas dentro de la cinta que **no comparten ancestro** con las demás?
   ¿Con qué comando lo comprobaron?
4. ¿Qué archivos existieron en esa historia y ya no están al final de ella?
5. ¿`python3 scripts/audit.py` pasa en su árbol actual? ¿Y en el primer commit
   de la cinta?

La respuesta a la 5 es la que abre la Fase 3. No la salten.

---

## 🏺 Fase 2 — Los seis fragmentos

Cada fragmento está escondido con una técnica **distinta**. Esa es toda la
gracia: si repiten el mismo comando seis veces, encuentran tres como mucho.

| # | Pista (es lo único que van a recibir) |
|---|---|
| **FRAG-01** | Un archivo que estuvo en la rama principal de la cinta y al final ya no está. Los archivos borrados siguen vivos en el commit anterior al que los borró. |
| **FRAG-02** | Un respaldo hecho *antes* del incidente. Está anclado a una referencia que no es una rama, y el texto no está en ningún archivo: está en la referencia misma. |
| **FRAG-03** | Una línea de tiempo que nunca se cruzó con esta. Si intentan fusionarla, Git se va a negar — y va a tener razón. |
| **FRAG-04** | Un archivo que sigue existiendo, pero al que le arrancaron un pedazo. No busquen el archivo: busquen **la línea** a lo largo del tiempo. |
| **FRAG-05** | No toda referencia es una rama o una etiqueta. Hay metadatos que se adjuntan a un commit **sin cambiar su SHA**. Ojo: al montar la cinta, ustedes decidieron dónde aterrizaban. |
| **FRAG-06** | La cinta trae un parche de emergencia: **cuatro commits, y solo uno sirve**. Los otros tres contaminan el proyecto. Este no se copia: se trae. Ver Fase 3. |

Cada fragmento es un bloque de texto con este aspecto:

```
======================================
   ARCHIVO 2031 - FRAGMENTO 0X/06
======================================
origen : ...
palabra: ...
codigo : ...
--------------------------------------
Transcribir tal cual. Se compara linea a linea.
```

**Entregable:** los seis bloques completos, transcritos **sin modificar**, en
`bitacora/frag-01.txt` … `frag-06.txt`.

> 💡 Redirigir la salida de un comando a un archivo (`>`) es más fiable —y más
> honesto— que copiar y pegar del terminal. El `codigo` es aleatorio: no se
> adivina, no se deduce y no se lo saben de memoria.

La cinta también guarda dos archivos que la página necesita y que ustedes no
tienen: una **hoja de estilos** que la rama principal nunca conoció y el
**glifo del sello**. Recupérenlos íntegros y enlacen la hoja desde `index.html`.

---

## 🔪 Fase 3 — Cirugía sobre una historia ajena

Esta es la parte que separa a quien usó Git de quien lo entendió. Van a aplicar
commits que están en una historia **que no comparte ni un ancestro con la
suya**. Git lo permite, y en producción se hace todo el tiempo.

### 3.1 · El commit tóxico

Uno de los commits de la cinta rompió el sitio, y el daño lo heredaron ustedes.
No les vamos a decir cuál. Sí les damos el detector:

```bash
python3 scripts/audit.py     # 0 = sano, 1 = roto, 125 = no evaluable
```

Ese script es **idéntico en todos los commits de la cinta**. No es casualidad:
sirve como oráculo estable para una búsqueda binaria sobre la historia.
Encuentren al culpable en **O(log n)**, no leyendo la historia entera a mano.

Después, **revierta ese commit sobre su propia rama**:

```bash
git revert <sha-del-commit-de-la-cinta>
```

- Sí, funciona aunque ese commit no sea ancestro suyo: `revert` aplica el
  parche inverso, no viaja en el tiempo.
- **Va a generar conflicto.** Es a propósito. Resuélvanlo entre los tres.
- No vale borrar los archivos a mano: queremos ver el revert en el historial.
  El mensaje que Git genera contiene el SHA revertido, y **eso** es lo que se
  corrige.

### 3.2 · El parche envenenado

La rama `parche/urgente` de la cinta tiene cuatro commits. Uno restaura
FRAG-06; los otros tres meten una página promocional, un pixel de seguimiento y
borran atributos de accesibilidad. Si mergean la rama entera, `audit.py` los
delata.

Traigan **solo** el commit sano, y déjenlo trazable:

```bash
git cherry-pick -x <sha-del-commit-sano>
```

La bandera `-x` añade al mensaje la línea `(cherry picked from commit ...)`.
Sin ella no hay forma de demostrar de dónde salió, y la corrección lo nota.

---

## 🧑‍🚀 Fase 4 — Identidad del equipo

Cada integrante, **en su propia rama** `feat/member-<nombre>`, hace dos cosas en
`index.html`:

1. Completa **su** tarjeta: foto, nombre completo, rol, usuario de GitHub y
   enlaces a GitHub y LinkedIn.
2. Añade su nombre a la línea del **turno de guardia**, dentro de
   `<span class="equipo__nombres">`. Los tres escriben en **esa misma línea**.

Los tres abren PR contra `main` **desde la misma base**. El segundo y el tercer
PR **van a chocar** — el paso 2 lo garantiza. Eso es el ejercicio:

- El conflicto se resuelve **entre los tres**, conservando los datos de todos.
- No vale `--ours`, no vale `--theirs`, no vale borrar la tarjeta del otro.
- No vale `git push --force` sobre `main`. Es descalificatorio.

---

## 🚀 Fase 5 — Ensamblaje y entrega

1. Escriban las seis palabras en las seis ranuras de `index.html`.
2. Escriban el sello completo en `#sello-valor`. La página se verifica sola: si
   es correcto, el estado pasa a **RESTAURADO**.
3. `python3 scripts/audit.py` debe pasar en `main`.
4. Etiqueten la entrega con una **etiqueta anotada** (no ligera) cuyo mensaje
   contenga el sello:
   ```bash
   git tag -a v1.0.0 -m "Archivo restaurado. Sello: PALABRA-PALABRA-..."
   git push origin v1.0.0
   ```
5. Dejen una **nota de Git** en el commit de entrega contando qué recuperaron, y
   **empújenla**. Las notas no viajan con un `git push` normal: son una
   referencia aparte y hay que mandarlas a mano. Si no llega al remoto, para
   nosotros no existe.
6. Los dos workflows en verde y la página viva en GitHub Pages, con la URL en el
   README.

---

## 📦 Entregables exactos

En `main`, al cierre de la sesión:

| Ruta | Contenido |
|---|---|
| `bitacora/frag-01.txt` … `frag-06.txt` | Los seis fragmentos transcritos sin alterar. |
| `bitacora/SELLO.txt` | Formato exacto, ver abajo. |
| `bitacora/INFORME.md` | La bitácora de la investigación, ver abajo. |
| `index.html` | Letra del equipo, ranuras, sello, 3 tarjetas reales, capa CRT enlazada. |
| `styles/crt.css`, `assets/sello.svg` | Recuperados, íntegros. |
| `README.md` | Con la URL de GitHub Pages del equipo. |

### `bitacora/SELLO.txt`

```
FRAG-01: PALABRA
FRAG-02: PALABRA
FRAG-03: PALABRA
FRAG-04: PALABRA
FRAG-05: PALABRA
FRAG-06: PALABRA
SELLO: PALABRA-PALABRA-PALABRA-PALABRA-PALABRA-PALABRA
```

### `bitacora/INFORME.md`

Una fila por fragmento, más una por cada operación quirúrgica:

```markdown
| Hallazgo | Dónde estaba | Técnica de Git | Comando exacto | Referencia |
|---|---|---|---|---|
| FRAG-01 | ... | ... | `git ...` | `a1b2c3d` |
```

Y al final, en prosa y en máximo 15 líneas:

- Qué hizo exactamente el commit tóxico y cómo lo encontraron.
- Qué decidieron con la rama huérfana y **por qué**.
- Un error que cometieron con Git durante la sesión y cómo salieron de él.

Esa última pregunta se corrige a mano y se contrasta con su historial real. Un
equipo que dice no haberse equivocado en una sesión entera de Git no está
diciendo la verdad.

---

## 🧾 Rúbrica (100 puntos)

| Bloque | Pts | Qué se mide |
|---|---|---|
| **A · Historia propia** | 25 | Raíz propia y ≥15 commits · los 3 integrantes con ≥3 commits · ≥5 merge commits (nada de squash) · al menos un merge que integra un conflicto real · las 3 ramas `feat/member-*`. |
| **B · Arqueología** | 30 | Los 6 fragmentos transcritos sin una sola alteración (4 c/u) · `crt.css` y `sello.svg` íntegros · sello correcto. |
| **C · Cirugía** | 15 | Revert trazable del commit tóxico de la cinta y daño reparado (8) · cherry-pick `-x` del único commit sano, sin contaminación (7). |
| **D · Sitio** | 10 | Auditoría en verde · ranuras y sello en la página · capa CRT enlazada · 3 tarjetas reales. |
| **E · Entrega** | 15 | Etiqueta anotada con el sello · nota de Git empujada · ≥6 PR mergeados · revisión cruzada · Pages vivo. |
| **F · Informe** | 5 | `INFORME.md` con técnica, comando y referencia por hallazgo. |

La corrección es automática y la ejecuta el equipo docente sobre el repositorio
que entreguen. Ustedes tienen su propio termómetro:

```bash
python3 scripts/autocheck.py
```

No cubre todo lo que se corrige —el proceso en GitHub y la forma de su historial
no los ve—, pero si `autocheck` no pasa, la nota tampoco.

---

## 🚫 Descalificaciones

- `git push --force` sobre `main`.
- Squash de los PR de los compañeros (aplasta su autoría).
- Escribir los fragmentos a mano sin recuperarlos. Se comparan **línea a
  línea**, incluido el `codigo` aleatorio.
- Auto-aprobarse los PR.
- Usar la cinta de otro equipo.

---

## 🧰 Caja de herramientas

Hay más comandos de los que necesitan y **no están en orden**. Parte del reto es
elegir cuál va con cada problema.

```bash
git bundle verify | list-heads <archivo>
git fetch <archivo.bundle> '+refs/*:refs/<destino>/*'
git for-each-ref
git log --all --oneline --graph --decorate
git log --diff-filter=D -- <ruta>
git log -S '<texto>' -p
git show <ref>:<ruta>
git restore --source=<ref> -- <ruta>
git checkout <ref> -- <ruta>
git tag -n99
git tag -a <nombre> -m '<mensaje>'
git cat-file -t | -p <objeto>
git notes list | show <sha>
git notes add -m '<mensaje>' <sha>
git log --notes=<referencia> <ref>
git ls-tree -r <referencia>
git push origin 'refs/notes/*'
git bisect start | bad | good | run <comando>
git cherry-pick -x <sha>
git revert <sha>
git merge --allow-unrelated-histories <rama>
git merge-base --is-ancestor <a> <b>
git reflog
```

Y su propio termómetro, cuando quieran saber cuánto les falta:

```bash
python3 scripts/autocheck.py
```

---

## 💬 Una última cosa

Van a pasar la primera media hora convencidos de que el repositorio está
simplemente roto y de que no hay nada que encontrar. Es exactamente la sensación
de entrar a un proyecto real que alguien más rompió antes de irse.

La diferencia entre alguien que sabe Git y alguien que memorizó `add`, `commit`
y `push` es esta: **saber que la información sigue ahí, y saber preguntarle al
repositorio por ella.**

Suerte. Y documenten todo. 🛰️

— Equipo docente CS2031
