# Laravel con MySQL y phpMyAdmin

Stack completo para trabajar Laravel con MySQL y phpMyAdmin en local con servicios complementarios listos.

## Flujo De Trabajo Estandar

Este stack ya incluye `.env` y `.env.example`.

- Usa `.env` para cambiar puertos, usuarios, claves locales o nombres de base de datos segun la necesidad del momento.
- Usa `.env.example` como referencia limpia de los valores recomendados por la academia.
- Las credenciales incluidas son solo para practica local. No reemplazan una configuracion segura de produccion.

## Como Levantarlo

```bash
cd frameworks/laravel-mysql
docker compose config
docker compose up -d
docker compose ps
```

## Como Acceder

Aplicacion: `http://localhost:8097`. phpMyAdmin: `http://localhost:8098`.

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

- `APP_PORT=8097` expone el puerto interno `8097`.
- `MYSQL_PORT=3310` expone el puerto interno `3306`.
- `PHPMYADMIN_PORT=8098` expone el puerto interno `80`.

## Que Incluye

- PHP 8.3
- Base lista para Laravel
- MySQL
- phpMyAdmin

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
