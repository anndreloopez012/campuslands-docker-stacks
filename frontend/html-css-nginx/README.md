# HTML + CSS con Nginx

Stack para practicar maquetacion HTML y CSS sirviendo archivos estaticos con Nginx.

## Que incluye

- Nginx para servir archivos estaticos
- Carpeta `src/` para HTML y CSS
- Puerto configurable por `.env`

## Como levantarlo

```bash
cd frontend/html-css-nginx
cp .env.example .env
docker compose config
docker compose up -d
docker compose ps
```

## Como acceder

Abre `http://localhost:8090`.

## Como apagarlo

```bash
docker compose down
```

## Limpieza completa

```bash
docker compose down -v
```

Usa `down -v` solo si quieres borrar volumenes y datos locales.

## Validacion

El navegador debe mostrar la pagina inicial y cualquier cambio en `src/` debe verse al recargar.

## Buenas practicas

- No subas `.env`.
- Mantiene credenciales reales fuera del repositorio.
- Si cambias puertos, actualiza `.env.example` y este README.
- Si agregas servicios, documenta para que sirven.
