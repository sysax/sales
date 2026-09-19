# Recomendaciones del repositorio

Lecciones de los PRs #7–#11 (bots mergeando sin validación).

## 1. Proteger `main` (prioridad alta)

- Settings → Branches → Add rule para `main`:
  - ✅ Require a pull request before merging (mínimo 1 aprobación humana).
  - ✅ Require status checks to pass (ver §2).
  - ✅ Do not allow bypassing the above settings.
- Sin esto, cualquier bot puede romper el arranque (pasó en PR #11).

## 2. CI mínimo que bloquee merges rotos

Workflow `.github/workflows/ci.yml` sugerido:

```yaml
- python -m compileall screens components data main.py
- timeout 20 python main.py  # debe arrancar sin Traceback
- python -m pytest tests/ -q  # cuando pytest esté en requirements
```

El crash del PR #11 (`md_bg_color` inválido) lo habría atrapado el paso 2.

## 3. `.gitignore`: no reescribirlo, extenderlo

- Ya ocurrió 2 veces: un PR lo reemplaza y se pierden reglas (`*.db`,
  `data/tickets/`, `barcodes/`, `.kivy/`).
- Regla: los PRs solo **agregan** líneas al final, nunca reescriben el archivo.
- Si un `pull` muestra la DB o `data/tickets/` como pendientes, el
  `.gitignore` fue pisado: restaurarlo antes de commitear.

## 4. Nunca versionar

| Qué | Por qué |
|-----|---------|
| `*.db`, `*.sqlite*` | Datos locales; se regenera con seed al iniciar |
| `__pycache__/`, `*.pyc` | Se regeneran solos; además rompen el `pull` (ya abortó 2 veces) |
| `*.log`, `ventas.log` | Logs de ejecución |
| `data/tickets/`, `barcodes/` | Artefactos runtime |
| Tokens/PATs | Van en variables de entorno, jamás en código ni config |

Limpieza si ya entraron:

```bash
git rm -r --cached __pycache__ $(git ls-files '*.pyc' '*.log' '*.db')
```

## 5. Checklist antes de cada merge

1. `python main.py` arranca sin `Traceback` ni `[ERROR]`.
2. Las 14 pantallas construyen (`on_enter` sin excepciones).
3. `git status` limpio de `.db`, `.pyc`, `.log`, `tickets/`.
4. Sin secretos en el diff (`grep -ri "ghp_\|token\|password ="`).
5. Migraciones de DB probadas sobre una copia (tablas nuevas no rompen seed).

## 6. Convenciones

- Ramas: `feature/<tema>`, `fix/<tema>`; un PR = un tema.
- Commits en imperativo corto: `Agrega X`, `Corrige Y`.
- `screens/` no accede a datos directo: todo vía `data/repository.py`.
- Lógica DIAN solo en `data/dian.py`; tema solo en `components/theme.py`.
