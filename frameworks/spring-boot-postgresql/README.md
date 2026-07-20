# Spring Boot con PostgreSQL

Stack completo para trabajar Spring Boot con PostgreSQL en local con servicios complementarios listos.

## Flujo De Trabajo Estandar

Este stack ya incluye `.env` y `.env.example`.

- Usa `.env` para cambiar puertos, usuarios, claves locales o nombres de base de datos segun la necesidad del momento.
- Usa `.env.example` como referencia limpia de los valores recomendados por la academia.
- Las credenciales incluidas son solo para practica local. No reemplazan una configuracion segura de produccion.

## Como Levantarlo

```bash
cd frameworks/spring-boot-postgresql
docker compose config
docker compose up -d
docker compose ps
```

## Como Acceder

Aplicacion: `http://localhost:8095`. Adminer: `http://localhost:8096`.

## Como Apagarlo

```bash
docker compose down
```

## Reinicio Limpio

```bash
docker compose down -v
docker compose up -d
```

Usa `docker compose down -v` solo cuando quieras borrar volumenes y datos locales para empezar de cero.

## Archivos Del Stack

- `docker-compose.yml`: define los servicios del stack.
- `.env`: configuracion local lista para usar y modificar en clase.
- `.env.example`: copia de referencia con valores base.
- `README.md`: instrucciones del stack.

## Variables Principales

- `APP_PORT=8095` expone el puerto interno `8095`.
- `POSTGRES_PORT=5454` expone el puerto interno `5432`.
- `ADMINER_PORT=8096` expone el puerto interno `8080`.

## Que Incluye

- Servicio Spring Boot
- PostgreSQL
- Adminer
- Variables listas para `spring.datasource`

## Validacion

El stack queda bien cuando:

- `docker compose config` no muestra errores.
- `docker compose ps` muestra los servicios activos.
- La URL o cliente indicado en `Como Acceder` responde correctamente.
- Los cambios necesarios se hacen en `.env` sin editar directamente el YAML para casos normales.

## Buenas Practicas

- Cambia primero `.env` antes de tocar `docker-compose.yml`.
- No uses credenciales reales en estos entornos de practica.
- Si un puerto esta ocupado, cambia el puerto local en `.env`.
- Si agregas un servicio nuevo, documenta su uso y sus variables.
- No subas carpetas generadas por contenedores como `data/`, `volumes/`, `node_modules/`, `vendor/`, `dist/` o `build/`.
