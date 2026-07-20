# Guia de contribucion

## Flujo obligatorio

1. Actualiza `dev`:

```bash
git checkout dev
git pull origin dev
```

2. Crea tu rama personal:

```bash
git checkout -b nombre-apellido/descripcion-corta
```

3. Modifica solo la carpeta relacionada con tu cambio.
4. Verifica que el stack levante correctamente.
5. Haz commit con mensaje profesional.
6. Sube tu rama y abre Pull Request hacia `dev`.

## Estructura minima por stack

Cada stack debe tener:

- `README.md`
- `docker-compose.yml`
- `.env.example`

Si el stack necesita archivos extra, deben quedar dentro de la misma carpeta.

## Commits recomendados

Usa esta estructura:

```text
tipo(scope): descripcion corta
```

Ejemplos:

```text
feat(mysql): agregar variables de conexion local
fix(n8n): corregir puerto de postgres
docs(docker): mejorar guia para windows
chore(repo): ajustar validacion de estructura
```

## Tipos permitidos

- `feat`: nueva configuracion o nuevo stack.
- `fix`: correccion de un error.
- `docs`: cambios de documentacion.
- `chore`: mantenimiento del repositorio.
- `refactor`: mejora interna sin cambiar comportamiento.
- `test`: validaciones o pruebas.

## Pull Requests que se rechazan

- PR hacia `main`.
- Cambios fuera de la estructura del repositorio.
- Archivos `.env` con credenciales reales.
- Carpetas `data`, `volumes`, `node_modules` o archivos pesados generados por Docker.
- Stacks sin `README.md`, `docker-compose.yml` o `.env.example`.
- Documentacion insuficiente para levantar el servicio.

## Antes de pedir revision

```bash
docker compose config
docker compose up -d
docker compose ps
docker compose down
```
