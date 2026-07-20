# React con Vite

Stack para crear interfaces React modernas sin instalar Node directamente en el sistema.

## Que incluye

- Node.js dentro del contenedor
- Vite
- React y React DOM
- Volumen para `node_modules`

## Como levantarlo

```bash
cd frontend/react-vite
cp .env.example .env
docker compose config
docker compose up -d
docker compose ps
```

## Como acceder

Abre `http://localhost:5173`.

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

`docker compose ps` debe mostrar el servicio activo y Vite debe responder en el puerto configurado.

## Buenas practicas

- No subas `.env`.
- Mantiene credenciales reales fuera del repositorio.
- Si cambias puertos, actualiza `.env.example` y este README.
- Si agregas servicios, documenta para que sirven.
