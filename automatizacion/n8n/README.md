# n8n con utilidades

Automatizacion local con PostgreSQL, Redis, workers y Mailpit para probar flujos reales.

## Flujo De Trabajo Estandar

Este stack ya incluye `.env` y `.env.example`.

- Usa `.env` para cambiar puertos, usuarios, claves locales o nombres de base de datos segun la necesidad del momento.
- Usa `.env.example` como referencia limpia de los valores recomendados por la academia.
- Las credenciales incluidas son solo para practica local. No reemplazan una configuracion segura de produccion.

## Como Levantarlo

```bash
cd automatizacion/n8n
docker compose config
docker compose up -d
docker compose ps
```

## Como Acceder

Revisa `docker compose ps` para confirmar el puerto publicado y abre el servicio desde tu navegador o cliente correspondiente.

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

- `POSTGRES_PORT=5440` expone el puerto interno `5432`.
- `REDIS_PORT=6381` expone el puerto interno `6379`.
- `MAILPIT_PORT=8026` expone el puerto interno `8025`.
- `N8N_PORT=5678` expone el puerto interno `5678`.

## Que Incluye

- Servicios definidos en `docker-compose.yml` para levantar este entorno local.

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
