# Java

Entorno para practicar Java puro sin instalar JDK directamente en el sistema operativo.

## Flujo De Trabajo Estandar

Este stack ya incluye `.env` y `.env.example`.

- Usa `.env` para cambiar puertos o nombres locales segun la necesidad del momento.
- Usa `.env.example` como referencia limpia de los valores recomendados por la academia.
- Las configuraciones incluidas son solo para practica local.

## Como Levantarlo

```bash
cd lenguajes/java
docker compose config
docker compose up -d
docker compose ps
```

## Como Acceder

Abre:

```text
http://localhost:8091
```

Si cambias `APP_PORT` en `.env`, usa el puerto que hayas configurado.

## Como Trabajar

Edita el archivo:

```text
src/Main.java
```

Luego reinicia el contenedor:

```bash
docker compose restart app
```

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

- `docker-compose.yml`: define el servicio Java.
- `.env`: configuracion local lista para usar.
- `.env.example`: copia de referencia con valores base.
- `src/Main.java`: aplicacion base de ejemplo.
- `README.md`: instrucciones del stack.

## Variables Principales

- `APP_PORT=8091` expone el puerto local del servicio.

## Que Incluye

- JDK 21 con Eclipse Temurin.
- Compilacion directa con `javac`.
- Servidor HTTP basico para validar que Java responde desde Docker.

## Validacion

El stack queda bien cuando:

- `docker compose config` no muestra errores.
- `docker compose ps` muestra el servicio activo.
- `http://localhost:8091` responde desde el navegador.

## Buenas Practicas

- Cambia primero `.env` antes de tocar `docker-compose.yml`.
- No uses credenciales reales en estos entornos de practica.
- Si un puerto esta ocupado, cambia el puerto local en `.env`.
- No subas carpetas generadas por contenedores.
