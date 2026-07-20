# NestJS con PostgreSQL

Stack completo para trabajar NestJS con PostgreSQL en local con servicios complementarios listos.

## Que incluye

- API NestJS
- PostgreSQL
- Adminer
- TypeScript

## Como levantarlo

```bash
cd frameworks/nestjs-postgresql
cp .env.example .env
docker compose config
docker compose up -d
docker compose ps
```

## Como acceder

API: `http://localhost:3331`. Adminer: `http://localhost:8092`.

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

Ejecuta `docker compose config`, luego `docker compose up -d` y verifica la URL indicada en la seccion de acceso.

## Buenas practicas

- No subas `.env`.
- Mantiene credenciales reales fuera del repositorio.
- Si cambias puertos, actualiza `.env.example` y este README.
- Si agregas servicios, documenta para que sirven.
