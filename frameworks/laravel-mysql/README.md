# Laravel con MySQL y phpMyAdmin

Stack completo para trabajar Laravel con MySQL y phpMyAdmin en local con servicios complementarios listos.

## Que incluye

- PHP 8.3
- Base lista para Laravel
- MySQL
- phpMyAdmin

## Como levantarlo

```bash
cd frameworks/laravel-mysql
cp .env.example .env
docker compose config
docker compose up -d
docker compose ps
```

## Como acceder

Aplicacion: `http://localhost:8097`. phpMyAdmin: `http://localhost:8098`.

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
