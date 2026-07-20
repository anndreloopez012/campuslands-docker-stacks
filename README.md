# Campuslands Docker Stacks

Catalogo publico de entornos locales con Docker Compose para que los estudiantes puedan trabajar con lenguajes, bases de datos, gestores y herramientas sin instalar todo directamente en el sistema operativo.

## Objetivo

- Levantar entornos de practica con un comando.
- Mantener configuraciones ordenadas por tecnologia.
- Evitar instalaciones largas en Windows, Linux y macOS.
- Estandarizar la forma de trabajar en clase, laboratorios y proyectos personales.

## Estructura

```text
campuslands-docker-stacks/
├── docs/instalacion-docker/
├── lenguajes/
├── bases-de-datos/
├── gestores-bd/
├── automatizacion/
├── plataformas/
└── herramientas/
```

Cada carpeta incluye:

- `docker-compose.yml`: servicios listos para levantar.
- `.env.example`: variables de entorno de practica.
- `README.md`: instrucciones especificas del stack.

## Uso rapido

1. Instala Docker Desktop o Docker Engine siguiendo `docs/instalacion-docker/`.
2. Entra a la carpeta del stack que necesitas.
3. Copia `.env.example` como `.env`.
4. Ejecuta `docker compose up -d`.
5. Revisa el `README.md` de esa carpeta para usuario, clave, puertos y comandos.

## Reglas del repositorio

- `main` queda reservado para version estable.
- `dev` es la rama base para integrar cambios.
- Las ramas principales y las ramas por stack estan protegidas.
- Nadie debe subir directo a `main` o `dev`.
- Todo cambio debe entrar por Pull Request hacia `dev`.
- No se deben subir credenciales reales, datos privados, backups grandes ni carpetas generadas por contenedores.

## Convencion de ramas para estudiantes

```bash
git checkout dev
git pull origin dev
git checkout -b nombre-apellido/stack-que-modifica
```

Ejemplo:

```bash
git checkout -b maria-lopez/mysql-readme
```

## Comando base

```bash
cp .env.example .env
docker compose up -d
docker compose ps
docker compose logs -f
docker compose down
```

## Recomendacion

Usa un stack a la vez al inicio. Cuando necesites combinar tecnologias, levanta solo los servicios necesarios para evitar consumo alto de memoria y puertos ocupados.
