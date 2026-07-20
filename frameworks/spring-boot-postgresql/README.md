# Spring Boot con PostgreSQL

Stack completo para trabajar Spring Boot con PostgreSQL en local con servicios complementarios listos.

## Que incluye

- Servicio Spring Boot
- PostgreSQL
- Adminer
- Variables listas para `spring.datasource`

## Como levantarlo

```bash
cd frameworks/spring-boot-postgresql
cp .env.example .env
docker compose config
docker compose up -d
docker compose ps
```

## Como acceder

Aplicacion: `http://localhost:8095`. Adminer: `http://localhost:8096`.

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
