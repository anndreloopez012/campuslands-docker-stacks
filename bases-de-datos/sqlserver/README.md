# SQL Server

SQL Server local para practicar T-SQL y herramientas Microsoft.

## Para que sirve

Este stack permite trabajar la tecnologia en local usando contenedores. La idea es evitar instalaciones directas en el sistema operativo y mantener cada practica aislada.

## Archivos

- `docker-compose.yml`: define los servicios.
- `.env.example`: variables listas para copiar.
- `README.md`: instrucciones del stack.

## Como levantarlo

```bash
cd bases-de-datos/sqlserver
cp .env.example .env
docker compose config
docker compose up -d
docker compose ps
```

## Como apagarlo

```bash
docker compose down
```

## Como borrar datos locales

```bash
docker compose down -v
```

Usa ese comando solo si quieres limpiar volumenes y empezar de cero.

## Puertos y acceso

- Puerto local sugerido: `1434`

Si el puerto esta ocupado, cambia el valor en `.env` y vuelve a levantar el stack.

## Validacion

El stack esta bien levantado cuando `docker compose ps` muestra los servicios en estado `running` o `healthy`.

## Buenas practicas

- No subas el archivo `.env`.
- No subas carpetas de datos generadas por los contenedores.
- Documenta cualquier cambio de puertos o credenciales de practica en este README.
- Si agregas un servicio nuevo, deja claro para que sirve y como se accede.
