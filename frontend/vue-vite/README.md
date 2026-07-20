# Vue con Vite

Stack para practicar Vue usando Vite y Node.js dentro de Docker.

## Que incluye

- Node.js dentro del contenedor
- Vite
- Vue
- Volumen para `node_modules`

## Como levantarlo

```bash
cd frontend/vue-vite
cp .env.example .env
docker compose config
docker compose up -d
docker compose ps
```

## Como acceder

Abre `http://localhost:5174`.

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

El servidor Vite debe responder en `http://localhost:5174`.

## Buenas practicas

- No subas `.env`.
- Mantiene credenciales reales fuera del repositorio.
- Si cambias puertos, actualiza `.env.example` y este README.
- Si agregas servicios, documenta para que sirven.
