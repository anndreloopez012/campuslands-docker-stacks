# Angular

Stack para practicar Angular CLI sin instalar Node ni Angular directamente en el sistema.

## Que incluye

- Node.js dentro del contenedor
- Angular CLI
- Proyecto Angular minimo
- Volumen para `node_modules`

## Como levantarlo

```bash
cd frontend/angular
cp .env.example .env
docker compose config
docker compose up -d
docker compose ps
```

## Como acceder

Abre `http://localhost:4200`.

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

Angular CLI debe servir la aplicacion en `http://localhost:4200`.

## Buenas practicas

- No subas `.env`.
- Mantiene credenciales reales fuera del repositorio.
- Si cambias puertos, actualiza `.env.example` y este README.
- Si agregas servicios, documenta para que sirven.
