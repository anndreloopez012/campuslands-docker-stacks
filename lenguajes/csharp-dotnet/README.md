# C# Con .NET

Entorno para practicar C# y APIs basicas con .NET sin instalar el SDK directamente en el sistema operativo.

## Flujo De Trabajo Estandar

Este stack ya incluye `.env` y `.env.example`.

- Usa `.env` para cambiar puertos o nombres locales segun la necesidad del momento.
- Usa `.env.example` como referencia limpia de los valores recomendados por la academia.
- Las configuraciones incluidas son solo para practica local.

## Como Levantarlo

```bash
cd lenguajes/csharp-dotnet
docker compose config
docker compose up -d
docker compose ps
```

## Como Acceder

Abre:

```text
http://localhost:8092
```

Si cambias `APP_PORT` en `.env`, usa el puerto que hayas configurado.

## Como Trabajar

Edita el archivo:

```text
app/Program.cs
```

El contenedor usa `dotnet watch`, por lo que detecta cambios comunes mientras esta activo.

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

- `docker-compose.yml`: define el servicio C# con .NET.
- `.env`: configuracion local lista para usar.
- `.env.example`: copia de referencia con valores base.
- `app/`: proyecto C# base.
- `README.md`: instrucciones del stack.

## Variables Principales

- `APP_PORT=8092` expone el puerto local del servicio.

## Que Incluye

- SDK .NET 8.
- Proyecto C# minimo con API HTTP.
- Recarga durante desarrollo con `dotnet watch`.

## Validacion

El stack queda bien cuando:

- `docker compose config` no muestra errores.
- `docker compose ps` muestra el servicio activo.
- `http://localhost:8092` responde desde el navegador.

## Buenas Practicas

- Cambia primero `.env` antes de tocar `docker-compose.yml`.
- No uses credenciales reales en estos entornos de practica.
- Si un puerto esta ocupado, cambia el puerto local en `.env`.
- No subas carpetas generadas por contenedores como `bin/` u `obj/`.
