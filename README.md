# 🚀 Hackatón 0 – CS2031

¡Bienvenidos! 🎉
Desde el curso **CS2031** les damos una cordial bienvenida al ciclo **2026-2**. El foco sigue siendo el mismo que siempre: colaboración bajo presión, conflictos de Git y trabajo en equipo real.

## 🤔 ¿Qué trae esta Hackatón?

Esta **Hackatón 0** es una primera muestra del concepto de hackatones. Los equipos son de **exactamente 3 integrantes**, tienen **2 horas** y el repositorio que heredan está roto a propósito. El foco:

> **Git + GitHub + trabajo en equipo**

No hace falta saber programar backend. Ni siquiera hace falta escribir mucho HTML. El reto está en **usar Git de verdad, coordinarse y dejar un historial que se sostenga solo**.

Si aún no viste el video de introducción a Git y GitHub, **este es el momento**: [👉 Video de introducción a Git y GitHub](https://www.youtube.com/watch?v=8CmZysIzcbc)

Todo lo que necesitan ya lo vieron ahí: clonar, ramas, commits, push, Pull Requests y conflictos. Lo demás lo van a aprender hoy, buscando.

### ⚠️ Sobre usar IA

Van a usarla igual, así que hablemos claro: **está permitida**. Úsenla para aprender comandos, que para eso es buenísima.

Lo que no les va a resolver son dos cosas:

1. **La información que necesitan no existe fuera de este repositorio.** No está en internet y no se deduce razonando. Está guardada dentro de un archivo que van a tener que aprender a abrir con Git.
2. **La entrega no es un archivo: es un historial.** Se corrige la forma del grafo de commits que ustedes construyan — que haya merges de verdad, un revert trazable, un cherry-pick trazable. Eso no se pega desde un chat: se hace.

> 🎯 **Regla de oro:** cada hallazgo se documenta con el comando exacto que lo produjo. Si no pueden reproducirlo delante de un TA, no cuenta.

---

## 👥 Trabajo en equipo

Los equipos son de **3 integrantes fijos**. Repártanse estos roles al empezar:

| Rol | Responsabilidad |
|---|---|
| 🧭 **Líder** | Crea el repositorio y los issues, revisa y mergea los PR, conduce la resolución de conflictos. |
| 🔎 **Arqueólogo** | Busca los fragmentos perdidos en la historia. |
| 🧰 **Cirujano** | Deshace lo que rompió el sitio y deja el despliegue vivo. |

Los roles no son excusas: **los tres deben tener commits, PRs y revisiones**. La corrección lo verifica commit por commit.

Coordínense antes de empezar a pushear. El repositorio incluye **GitHub Actions**: una audita el sitio en cada PR y otra despliega en GitHub Pages en cada push a `main`.

---

## ⏱️ Plan de las 2 horas

No improvisen el orden. Este reparto está medido:

| Tiempo | Qué |
|---|---|
| 0:00 – 0:15 | Issue **#1** — Crear el repo, configurarlo y montar la cinta |
| 0:15 – 0:55 | Issue **#2** — Los cuatro fragmentos (repártanselos: uno cada uno y el cuarto entre todos) |
| 0:55 – 1:15 | Issue **#3** — Encontrar y revertir el commit que rompió el sitio |
| 1:15 – 1:40 | Issue **#4** — Datos personales y el conflicto |
| 1:40 – 2:00 | Issue **#5** — Sello, informe, etiqueta y despliegue |

Si a los 55 minutos les falta más de un fragmento, **salten al issue #3 y vuelvan después**. El commit tóxico bloquea el despliegue: sin eso no hay nota de entrega.

---

## 📜 El reto

Un TA (que no diremos quién 🤫) volvió a meter mano en el repositorio, pero esta vez se le fue la mano de verdad. Ejecutó un script de "limpieza" sobre el **ARCHIVO 2031**, una terminal web con la bitácora del proyecto, y lo que ustedes heredan es el escombro:

- La bitácora está vacía: sus **fragmentos** desaparecieron del árbol de trabajo.
- Un commit rompió el sitio y nadie sabe cuál fue.
- `styles/base.css` perdió su bloque de accesibilidad.
- El glifo del sello y una capa visual completa no están por ningún lado.
- Las tarjetas del equipo siguen con datos de relleno.

Pero del repositorio original quedó **una cinta de respaldo**: el archivo `incidente/equipo-<X>.bundle`. Ahí adentro está toda la historia previa al incidente.

🎯 **Tu objetivo:** montar la cinta, recuperar los **cuatro fragmentos** del sello, deshacer el daño y desplegar la página en **GitHub Pages**.

Cuando las cuatro palabras estén en su sitio, la terminal se sella sola y su estado pasa de `INCOMPLETO` a `RESTAURADO`.

---

## 👑 Organización del equipo

- Elijan un **líder** que cree el repositorio con **`Use this template` → `Create a new repository`**. Nombre sugerido: `archivo-2031-<equipo>`.
  > ⚠️ **Márquenlo Public.** GitHub Pages solo funciona en repositorios privados con planes de pago, y sus cuentas son gratuitas: si lo dejan privado, no van a poder desplegar.
  >
  > Van a recibir un repositorio con **un solo commit**: el suyo. Eso es correcto y es el punto — **su historial empieza en cero y lo construyen ustedes.** La historia que van a investigar viaja aparte, en la cinta.
- El líder da acceso de colaborador a los otros 2 integrantes.
- En `Settings → General → Pull Requests`: **desactiven "Allow squash merging"**. El squash aplasta el trabajo de sus compañeros y la corrección lo penaliza.
- En `Settings → Pages → Source`: seleccionen **GitHub Actions**.
- Cada integrante trabaja en **su propia rama** y abre un **PR** para que otro lo revise y acepte. **Nadie se auto-aprueba.**
- Esperamos **al menos 4 PR mergeados**. Los conflictos se resuelven en equipo, **no individualmente**.

Y lo primero de todo, ya dentro de su clon: **averigüen cuál es su cinta**.

```bash
python3 scripts/micinta.py
```

Ese comando mira el nombre de **su** repositorio, deduce qué cinta le toca y lo anota en el `<meta name="equipo">` de `index.html`. Commiteen ese cambio: es lo que decide contra qué se les corrige.

No hay nada que pedirle a nadie ni que esperar. Cada repositorio tiene su propia cinta con palabras distintas, siempre la misma, y se deduce sola. Cambiarla a mano para que coincida con la de otro equipo se detecta y anula la entrega.

---

## ✅ Checklist del equipo (issues a crear por el líder)

### #1 — Montar la cinta

Si todavía no lo hicieron, corran `python3 scripts/micinta.py` para saber cuál de las cintas es la suya.

Lean `incidente/LEEME.md`. Un **git bundle** es un repositorio entero dentro de un solo archivo: commits, ramas, etiquetas y todo lo demás. Git lo trata como si fuera un remoto, así que se le puede hacer `fetch`.

Empiecen mirando qué trae, antes de tocarlo:

```bash
git bundle verify incidente/equipo-<X>.bundle
git bundle list-heads incidente/equipo-<X>.bundle
```

Antes de seguir, respondan estas tres en el issue:

1. ¿Cuántas referencias trae la cinta y cuántas de ellas **no** son ramas?
2. Una vez montada, ¿cuántos commits tiene su rama principal y quién los firmó?
3. ¿`python3 scripts/audit.py` pasa en su árbol actual? ¿Y en el primer commit de la cinta?

La respuesta a la 3 es la que abre el issue #3.

---

### #2 — Los cuatro fragmentos (repártanselos)

Cada fragmento está escondido con una técnica **distinta**. Esa es toda la gracia: si repiten el mismo comando cuatro veces, encuentran uno.

| # | Pista (es lo único que van a recibir) |
|---|---|
| **FRAG-01** | Un archivo que estuvo en la rama principal de la cinta y al final ya no está. Los archivos borrados siguen vivos en el commit **anterior** al que los borró. |
| **FRAG-02** | Un respaldo hecho *antes* del incidente. Está anclado a una referencia que **no es una rama**, y el texto no está en ningún archivo: está en la referencia misma. |
| **FRAG-03** | Una línea de tiempo que nunca se cruzó con esta. Si intentan fusionarla, Git se va a negar — y va a tener razón. No hace falta fusionarla para sacarle un archivo. |
| **FRAG-04** | La cinta trae un parche de emergencia: **cuatro commits, y solo uno sirve**. Los otros tres meten una página promocional, un pixel de seguimiento y borran atributos de accesibilidad. Traigan **solo** el bueno, con `git cherry-pick -x` para que quede trazable. Si mergean la rama entera, `audit.py` los delata. |

Cada fragmento es un bloque de texto con este aspecto:

```text
======================================
   ARCHIVO 2031 - FRAGMENTO 0X/06
======================================
origen : ...
palabra: ...
codigo : ...
--------------------------------------
Transcribir tal cual. Se compara linea a linea.
```

**Entregable:** los cuatro bloques completos, transcritos **sin modificar**, en `bitacora/frag-01.txt` … `frag-04.txt`.

> 💡 Redirigir la salida de un comando a un archivo (`>`) es más fiable —y más honesto— que copiar y pegar del terminal. El `codigo` es aleatorio: no se adivina y no se deduce.

La cinta también guarda dos archivos que la página necesita y que ustedes no tienen: una **hoja de estilos** que la rama principal nunca conoció y el **glifo del sello**. Recupérenlos íntegros y enlacen la hoja desde `index.html`.

---

### #3 — El commit que rompió el sitio (1 PR)

Uno de los commits de la cinta rompió la página, y el daño lo heredaron ustedes. No les vamos a decir cuál. Sí les damos el detector:

```bash
python3 scripts/audit.py     # 0 = sano, 1 = roto
```

Ese script es **idéntico en todos los commits de la cinta**. No es casualidad: sirve como oráculo para encontrar al culpable sin leer la historia entera. Busquen `git bisect` — está hecho exactamente para esto y es la forma elegante. Si se les complica, cualquier método vale, pero cuéntenlo en el informe.

Después, **reviertan ese commit sobre su propia rama**:

```bash
git revert <sha-del-commit-de-la-cinta>
```

- Sí, funciona aunque ese commit no sea ancestro suyo: `revert` aplica el parche inverso.
- **Va a generar conflicto.** Es a propósito, y es pequeño: sobra una línea. Resuélvanlo entre los tres.
- No vale borrar los archivos a mano: queremos ver el revert en el historial.

---

### #4 — Datos personales (1 PR por persona)

Cada integrante, **en su propia rama** `feat/member-<nombre>`, hace dos cosas en `index.html`:

1. Completa **su** tarjeta: foto (`src` y `alt` del `<img>`), nombre (`<h3 class="tarjeta__nombre">`), rol (`<p class="tarjeta__rol">`), usuario y los `href` de GitHub y LinkedIn.
2. Añade su nombre a la línea del **turno de guardia**, dentro de `<span class="equipo__nombres">`.

**Conflicto esperado:** los tres escriben en **esa misma línea** y salen de la misma base → el segundo y el tercer PR van a chocar sí o sí. Deberán resolverlo conservando los tres nombres.

Ejemplo de tarjeta correctamente completada:

```html
<article class="tarjeta">
  <img
    class="tarjeta__foto"
    src="https://avatars.githubusercontent.com/u/0000000"
    alt="Foto de Sparky García"
  />
  <h3 class="tarjeta__nombre">Sparky García</h3>
  <p class="tarjeta__rol">Backend Developer</p>
  <p class="tarjeta__usuario">@sparkygarcia</p>
  <ul class="tarjeta__enlaces">
    <li><a class="tarjeta__enlace" href="https://github.com/sparkygarcia">GitHub</a></li>
    <li><a class="tarjeta__enlace" href="https://www.linkedin.com/in/sparkygarcia">LinkedIn</a></li>
  </ul>
</article>
```

---

### #5 — Sello, informe y entrega (1 PR)

1. Escriban las cuatro palabras en las cuatro ranuras de `index.html`.
2. Escriban el sello completo en `#sello-valor`. La página se verifica sola: si es correcto, el estado pasa a **RESTAURADO**.
3. `python3 scripts/audit.py` debe pasar en `main`.
4. Etiqueten la entrega con una **etiqueta anotada** (no ligera) cuyo mensaje contenga el sello:

   ```bash
   git tag -a v1.0.0 -m "Archivo restaurado. Sello: PALABRA-PALABRA-PALABRA-PALABRA"
   git push origin v1.0.0
   ```

**Archivos que deben quedar en `main`:**

| Ruta | Contenido |
|---|---|
| `bitacora/frag-01.txt` … `frag-04.txt` | Los cuatro fragmentos transcritos sin alterar. |
| `bitacora/SELLO.txt` | Formato exacto, ver abajo. |
| `bitacora/INFORME.md` | La bitácora de la investigación, ver abajo. |
| `index.html` | Letra del equipo, ranuras, sello, 3 tarjetas y turno de guardia. |
| `styles/crt.css`, `assets/sello.svg` | Recuperados, íntegros, y la hoja enlazada. |
| `README.md` | Con la URL de GitHub Pages del equipo. |

`bitacora/SELLO.txt`:

```text
FRAG-01: PALABRA
FRAG-02: PALABRA
FRAG-03: PALABRA
FRAG-04: PALABRA
SELLO: PALABRA-PALABRA-PALABRA-PALABRA
```

`bitacora/INFORME.md`: una fila por hallazgo, más una para el commit tóxico.

```markdown
| Hallazgo | Dónde estaba | Técnica de Git | Comando exacto | Referencia |
|---|---|---|---|---|
| FRAG-01 | ... | ... | `git ...` | `a1b2c3d` |
```

Y al final, en tres o cuatro líneas: **un error que cometieron con Git durante la sesión y cómo salieron de él.** Se corrige a mano y se contrasta con su historial real. Un equipo que dice no haberse equivocado en dos horas de Git no está diciendo la verdad.

---

### ✅ Publicado en GitHub Pages

El deploy es **automático** gracias al workflow `.github/workflows/pages.yml`. Cada push a `main` despliega la página.

Eso sí: ese workflow **corre la auditoría antes de desplegar**. Mientras el sitio siga roto, no se publica nada. Es intencional.

Solo necesitan habilitarlo una vez:

1. Ir a **Settings → Pages**
2. En *Source* seleccionar **GitHub Actions**
3. A partir de ahí, cada merge a `main` despliega automáticamente

La URL aparece en la pestaña **Environments → github-pages**.

---

## 🎁 Bonus (si les sobra tiempo)

La cinta esconde **dos fragmentos más**, y ninguno de los dos hace falta para el sello. Son para equipos que terminaron y quieren más:

| # | Pista | Puntos |
|---|---|---|
| **FRAG-05** | Un archivo que sigue existiendo, pero al que le arrancaron un pedazo. No busquen el archivo: busquen **la línea** a lo largo del tiempo. | +3 |
| **FRAG-06** | No toda referencia es una rama o una etiqueta. Hay metadatos que se adjuntan a un commit **sin cambiar su SHA**. Ojo: al montar la cinta, ustedes decidieron dónde aterrizaban. | +4 |
| **Nota propia** | Dejen una nota de Git en el commit de entrega y **empújenla**. Las notas no viajan con un `git push` normal: hay que mandarlas a mano. | +3 |

Guárdenlos en `bitacora/frag-05.txt` y `bitacora/frag-06.txt`.

---

## ⚡ Ejemplo de conflicto en `index.html`

Cuando los tres editan la línea del turno de guardia, Git genera algo así:

```html
<<<<<<< HEAD
<p class="equipo__lista">Turno de guardia: <span class="equipo__nombres">Ana Torres</span></p>
=======
<p class="equipo__lista">Turno de guardia: <span class="equipo__nombres">Luis Ríos</span></p>
>>>>>>> feat/member-luisrios
```

La tarea del equipo es **resolverlo manualmente**, eliminando los marcadores y preservando los datos de ambos:

```html
<p class="equipo__lista">Turno de guardia: <span class="equipo__nombres">Ana Torres, Luis Ríos</span></p>
```

No vale `--ours`, no vale `--theirs`, y no vale borrar el nombre del otro para volver a escribirlo después.

---

## 🗂️ Resumen de ramas y PRs

| Rama | Responsable | Tipo | PR |
|---|---|---|---|
| `feat/member-<nombre>` | Cada integrante | Datos personales | 1 por persona |
| `arqueo/fragmentos` | Arqueólogo | Los fragmentos y los activos | 1 PR |
| `fix/cirugia` | Cirujano | Revert del commit tóxico | 1 PR |
| `feat/sello` | Líder | Sello, informe y entrega | 1 PR |

> Los nombres son sugerencias, salvo `feat/member-<nombre>`, que sí se revisa. Lo que **no** es negociable: todo entra por Pull Request, y esperamos **al menos 4 PR mergeados**.

## ⚙️ GitHub Actions incluidas

| Workflow | Archivo | Se ejecuta en |
|---|---|---|
| Auditoría del sitio | `.github/workflows/audit.yml` | Cada PR hacia `main` y cada push |
| Deploy a GitHub Pages | `.github/workflows/pages.yml` | Cada push a `main` |

**`audit.yml`** revisa que no queden marcadores de conflicto sin resolver y corre `scripts/audit.py`: enlaces internos que apunten a un `id` real, sin scripts no autorizados, imágenes con `alt`, y el bloque de accesibilidad del CSS en su sitio.

**`pages.yml`** despliega tras cada merge a `main`, y **se niega a desplegar si la auditoría falla**.

---

## 🧪 Los tests: cómo saber si ya terminaron

No adivinen. Pregúntenle al repositorio. Hay dos scripts y se corren desde la raíz del proyecto:

```bash
python3 scripts/audit.py       # ¿está sano el sitio?
python3 scripts/autocheck.py   # ¿está completa la entrega?
```

**`scripts/audit.py`** es el detector: revisa que los enlaces internos apunten a un `id` real, que no haya scripts no autorizados, que las imágenes tengan `alt` y que el bloque de accesibilidad del CSS siga en su sitio. Devuelve `0` si está sano y `1` si está roto. Es el mismo que corre en cada PR y el que decide si la página se despliega.

**`scripts/autocheck.py`** es la autocomprobación de la entrega: fragmentos, sello, tarjetas, turno de guardia, informe y etiqueta. Si además tienen la [CLI de GitHub](https://cli.github.com) autenticada (`gh auth login`), revisa también sus PRs mergeados, las revisiones cruzadas y si Pages está vivo. Termina con un veredicto:

```
  18/18 comprobaciones superadas

  LISTO PARA ENTREGAR
```

Si `gh` no está instalado se los dice y **no** da la entrega por buena: prefiere avisar antes que darles un falso verde.

Córranlo cada vez que mergeen algo. Es un subconjunto de la corrección oficial, así que pasarlo es **necesario pero no suficiente** — el bloque A (la forma de su historial) y el proceso en GitHub se corrigen aparte.

### 🔒 Los tests no se tocan

> **Modificar cualquiera de estos archivos es nota 0 en toda la hackatón:**
>
> - `scripts/audit.py`
> - `scripts/autocheck.py`
> - `scripts/micinta.py`
> - `scripts/sello.js`
> - `scripts/claves.json`
> - `incidente/*.bundle`
>
> No es una amenaza vacía: la corrección compara esos archivos y su cinta contra
> los originales **antes** de puntuar. Si algo cambió, lo dice, lista qué
> tocaron y pone la nota en cero.

Están probados: no tienen falsos positivos, toleran finales de línea de Windows y espacios sobrantes, y no dependen de nada que ustedes tengan que instalar salvo Python 3 y Git. **Si creen que un test falla injustamente, no lo editen: llamen a un TA.** Si tienen razón, lo arreglamos nosotros y todos ganan; si lo editan, no hay nada que discutir.

Lo que sí pueden (y deben) tocar es todo lo demás: `index.html`, `styles/`, `bitacora/`, `README.md`.

---

## 🧾 Rúbrica (100 puntos + 10 de bonus)

| Bloque | Pts | Qué se mide |
|---|---|---|
| **A · Historia propia** | 25 | Raíz propia y ≥10 commits · los 3 integrantes con ≥2 commits · ≥4 merge commits (nada de squash) · al menos un merge que integra un conflicto real · las 3 ramas `feat/member-*`. |
| **B · Los fragmentos** | 30 | Los 4 fragmentos transcritos sin una sola alteración (6 c/u) · `crt.css` y `sello.svg` íntegros · sello correcto. |
| **C · Cirugía** | 15 | Revert trazable del commit tóxico y daño reparado (8) · cherry-pick `-x` del único commit sano, sin contaminación (7). |
| **D · Sitio** | 10 | Auditoría en verde · ranuras y sello en la página · capa CRT enlazada · 3 tarjetas y turno de guardia completos. |
| **E · Entrega** | 15 | Etiqueta anotada con el sello (5) · ≥4 PR mergeados (4) · revisión cruzada (3) · Pages vivo (3). |
| **F · Informe** | 5 | `INFORME.md` con técnica, comando y referencia por hallazgo. |
| 🎁 **Bonus** | +10 | FRAG-05 (+3) · FRAG-06 (+4) · nota de Git propia empujada (+3). |

## 🚫 Descalificaciones

Son pocas y son claras:

- `git push --force` sobre `main`.
- Squash de los PR de los compañeros (aplasta su autoría).
- Escribir los fragmentos a mano sin recuperarlos. Se comparan **línea a línea**, incluido el `codigo` aleatorio.
- Auto-aprobarse los PR.
- Modificar cualquier archivo de `scripts/` o cualquier `.bundle`.
- Cambiar a mano la letra del equipo para usar la cinta de otro.

---

## 🧰 Caja de herramientas

Hay más comandos de los que necesitan y **no están en orden**. Parte del reto es elegir cuál va con cada problema.

```bash
git bundle verify | list-heads <archivo>
git fetch <archivo.bundle> '+refs/*:refs/<destino>/*'
git for-each-ref
git log --all --oneline --graph --decorate
git log --diff-filter=D -- <ruta>
git log -S '<texto>' -p
git show <ref>:<ruta>
git checkout <ref> -- <ruta>
git tag -n99
git tag -a <nombre> -m '<mensaje>'
git cat-file -t | -p <objeto>
git ls-tree -r <referencia>
git notes list | show <sha>
git push origin 'refs/notes/*'
git bisect start | bad | good | run <comando>
git cherry-pick -x <sha>
git revert <sha>
git merge --allow-unrelated-histories <rama>
git merge-base <a> <b>
git reflog
```

---

💡 Recuerden: la página es **estática**. No hay backend, y el HTML que van a escribir cabe en una pantalla. El desafío está en **investigar, coordinarse y dejar un historial que cuente la verdad de lo que hicieron**.

Van a pasar los primeros quince minutos convencidos de que el repositorio está simplemente roto y de que no hay nada que encontrar. Es exactamente la sensación de entrar a un proyecto real que alguien más rompió antes de irse. La diferencia entre quien sabe Git y quien memorizó `add`, `commit` y `push` es saber que la información sigue ahí, y saber preguntarle al repositorio por ella.

¡Éxito equipo! 💪 Con cariño, el equipo docente de CS2031.
