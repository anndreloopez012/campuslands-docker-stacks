# Campuslands Docker Stacks

Catalogo publico de entornos locales con Docker Compose para trabajar con lenguajes, bases de datos, gestores y herramientas sin instalar todo directamente en el sistema operativo.

Este README funciona como panel principal de navegacion. Desde aqui puedes ir directo al stack que necesitas, revisar como instalar Docker, entender el flujo de trabajo y levantar servicios con comandos simples.

## Accesos Rapidos

| Necesitas | Ir a |
| --- | --- |
| Instalar Docker | [Guia de instalacion](docs/instalacion-docker/README.md) |
| Ver todos los stacks | [Indice completo](INDICE-DE-STACKS.md) |
| Usar JavaScript, Python, PHP, Java, Go, Rust y otros | [Lenguajes](#lenguajes) |
| Usar HTML/CSS, React, Vue o Angular | [Frontend](#frontend) |
| Usar Express, NestJS, FastAPI, Django, Spring Boot, Laravel o .NET EF | [Frameworks completos](#frameworks-completos) |
| Usar MySQL, PostgreSQL, MongoDB, Redis y otros | [Bases de datos](#bases-de-datos) |
| Administrar bases de datos desde navegador | [Gestores de bases de datos](#gestores-de-bases-de-datos) |
| Levantar n8n | [Automatizacion](#automatizacion) |
| Levantar Supabase | [Plataformas](#plataformas) |
| Usar herramientas de apoyo | [Herramientas](#herramientas) |
| Aprender el flujo del repo | [Reglas de trabajo](#reglas-de-trabajo) |

## Como Usar Cualquier Stack

```bash
cd ruta/del/stack
cp .env.example .env
docker compose config
docker compose up -d
docker compose ps
```

Para apagar:

```bash
docker compose down
```

Para apagar y borrar datos locales del stack:

```bash
docker compose down -v
```

Usa `docker compose down -v` solo cuando quieras reiniciar la informacion guardada en volumenes.

## Mapa Del Repositorio

```text
campuslands-docker-stacks/
├── docs/instalacion-docker/
├── lenguajes/
├── frontend/
├── frameworks/
├── bases-de-datos/
├── gestores-bd/
├── automatizacion/
├── plataformas/
└── herramientas/
```

Cada stack tiene:

- `docker-compose.yml`: servicios listos para levantar.
- `.env.example`: variables de entorno de practica.
- `README.md`: instrucciones especificas, puertos y comandos.

## Selector De Stacks

Abre la categoria que necesitas y entra al README del stack.

<details>
<summary><strong>Lenguajes</strong></summary>

| Stack | Carpeta | Uso principal |
| --- | --- | --- |
| JavaScript con Node.js | [lenguajes/javascript-node](lenguajes/javascript-node/README.md) | Practicar JavaScript moderno, npm y APIs simples |
| TypeScript con Node.js | [lenguajes/typescript-node](lenguajes/typescript-node/README.md) | Practicar tipado, compilacion y servicios con TypeScript |
| Python | [lenguajes/python](lenguajes/python/README.md) | Scripts, logica, FastAPI y automatizacion |
| PHP con Apache | [lenguajes/php-apache](lenguajes/php-apache/README.md) | Paginas PHP clasicas y formularios |
| PHP Laravel | [lenguajes/php-laravel](lenguajes/php-laravel/README.md) | Proyectos Laravel en contenedor |
| Java Spring Boot | [lenguajes/java-spring](lenguajes/java-spring/README.md) | APIs Java con Spring Boot |
| .NET | [lenguajes/dotnet](lenguajes/dotnet/README.md) | APIs y aplicaciones .NET |
| Go | [lenguajes/go](lenguajes/go/README.md) | CLI, APIs y concurrencia basica |
| Rust | [lenguajes/rust](lenguajes/rust/README.md) | Practica con Cargo, ownership y CLI |
| Ruby on Rails | [lenguajes/ruby-rails](lenguajes/ruby-rails/README.md) | Aplicaciones web con Ruby y Rails |
| C y C++ | [lenguajes/c-cpp](lenguajes/c-cpp/README.md) | Compilacion local sin instalar toolchains |
| Bun | [lenguajes/bun](lenguajes/bun/README.md) | Runtime moderno para JavaScript y TypeScript |
| Deno | [lenguajes/deno](lenguajes/deno/README.md) | Runtime seguro para JavaScript y TypeScript |

</details>

<details>
<summary><strong>Frontend</strong></summary>

| Stack | Carpeta | Uso principal |
| --- | --- | --- |
| HTML + CSS con Nginx | [frontend/html-css-nginx](frontend/html-css-nginx/README.md) | Practicar HTML y CSS sirviendo archivos estaticos |
| React con Vite | [frontend/react-vite](frontend/react-vite/README.md) | Crear interfaces React modernas sin instalar Node local |
| Vue con Vite | [frontend/vue-vite](frontend/vue-vite/README.md) | Practicar Vue con servidor Vite |
| Angular | [frontend/angular](frontend/angular/README.md) | Practicar Angular CLI dentro de Docker |

</details>

<details>
<summary><strong>Frameworks Completos</strong></summary>

| Stack | Carpeta | Incluye |
| --- | --- | --- |
| Express con PostgreSQL y Adminer | [frameworks/express-postgresql](frameworks/express-postgresql/README.md) | Express, PostgreSQL y Adminer |
| NestJS con PostgreSQL | [frameworks/nestjs-postgresql](frameworks/nestjs-postgresql/README.md) | NestJS, PostgreSQL y Adminer |
| FastAPI con PostgreSQL | [frameworks/fastapi-postgresql](frameworks/fastapi-postgresql/README.md) | FastAPI, PostgreSQL y Adminer |
| Django con PostgreSQL | [frameworks/django-postgresql](frameworks/django-postgresql/README.md) | Django, PostgreSQL y Adminer |
| Spring Boot con PostgreSQL | [frameworks/spring-boot-postgresql](frameworks/spring-boot-postgresql/README.md) | Spring Boot, PostgreSQL, Maven y Adminer |
| Laravel con MySQL y phpMyAdmin | [frameworks/laravel-mysql](frameworks/laravel-mysql/README.md) | Laravel, MySQL y phpMyAdmin |
| .NET Entity Framework con PostgreSQL | [frameworks/dotnet-entity-framework-postgresql](frameworks/dotnet-entity-framework-postgresql/README.md) | .NET, Entity Framework, PostgreSQL y Adminer |

</details>

<details>
<summary><strong>Bases De Datos</strong></summary>

| Stack | Carpeta | Puerto local sugerido |
| --- | --- | --- |
| MySQL | [bases-de-datos/mysql](bases-de-datos/mysql/README.md) | `3307` |
| PostgreSQL | [bases-de-datos/postgresql](bases-de-datos/postgresql/README.md) | `5433` |
| MongoDB | [bases-de-datos/mongodb](bases-de-datos/mongodb/README.md) | `27018` |
| Redis | [bases-de-datos/redis](bases-de-datos/redis/README.md) | `6380` |
| MariaDB | [bases-de-datos/mariadb](bases-de-datos/mariadb/README.md) | `3308` |
| SQL Server | [bases-de-datos/sqlserver](bases-de-datos/sqlserver/README.md) | `1434` |
| Oracle Database Free | [bases-de-datos/oracle-free](bases-de-datos/oracle-free/README.md) | `1522` |

</details>

<details>
<summary><strong>Gestores De Bases De Datos</strong></summary>

| Stack | Carpeta | Para que sirve |
| --- | --- | --- |
| Adminer | [gestores-bd/adminer](gestores-bd/adminer/README.md) | Gestionar varios motores desde una interfaz ligera |
| phpMyAdmin | [gestores-bd/phpmyadmin](gestores-bd/phpmyadmin/README.md) | Administrar MySQL y MariaDB |
| pgAdmin | [gestores-bd/pgadmin](gestores-bd/pgadmin/README.md) | Administrar PostgreSQL |
| Mongo Express | [gestores-bd/mongo-express](gestores-bd/mongo-express/README.md) | Revisar colecciones y documentos MongoDB |
| Redis Commander | [gestores-bd/redis-commander](gestores-bd/redis-commander/README.md) | Inspeccionar claves y valores Redis |

</details>

<details>
<summary><strong>Automatizacion</strong></summary>

| Stack | Carpeta | Incluye |
| --- | --- | --- |
| n8n con utilidades | [automatizacion/n8n](automatizacion/n8n/README.md) | n8n, PostgreSQL, Redis, worker y Mailpit |

</details>

<details>
<summary><strong>Plataformas</strong></summary>

| Stack | Carpeta | Incluye |
| --- | --- | --- |
| Supabase local | [plataformas/supabase](plataformas/supabase/README.md) | PostgreSQL, Studio, Kong y Mailpit |

</details>

<details>
<summary><strong>Herramientas</strong></summary>

| Stack | Carpeta | Uso principal |
| --- | --- | --- |
| Mailpit | [herramientas/mailpit](herramientas/mailpit/README.md) | Capturar correos locales de prueba |
| MinIO | [herramientas/minio](herramientas/minio/README.md) | Almacenamiento compatible con S3 |
| RabbitMQ | [herramientas/rabbitmq](herramientas/rabbitmq/README.md) | Colas y eventos |
| Redpanda | [herramientas/redpanda](herramientas/redpanda/README.md) | Streaming compatible con Kafka |
| LocalStack | [herramientas/localstack](herramientas/localstack/README.md) | Servicios cloud simulados |
| Portainer | [herramientas/portainer](herramientas/portainer/README.md) | Administrar Docker desde navegador |
| Prometheus y Grafana | [herramientas/prometheus-grafana](herramientas/prometheus-grafana/README.md) | Monitoreo, metricas y dashboards |
| Nginx Reverse Proxy | [herramientas/nginx-reverse-proxy](herramientas/nginx-reverse-proxy/README.md) | Proxy inverso local |
| Traefik | [herramientas/traefik](herramientas/traefik/README.md) | Proxy moderno con dashboard |

</details>

## Rutas Recomendadas

| Si quieres aprender | Empieza por | Luego combina con |
| --- | --- | --- |
| HTML y CSS | [HTML + CSS con Nginx](frontend/html-css-nginx/README.md) | [Nginx Reverse Proxy](herramientas/nginx-reverse-proxy/README.md) |
| Frontend React | [React con Vite](frontend/react-vite/README.md) | [Express con PostgreSQL](frameworks/express-postgresql/README.md) |
| Frontend Vue | [Vue con Vite](frontend/vue-vite/README.md) | [FastAPI con PostgreSQL](frameworks/fastapi-postgresql/README.md) |
| Frontend Angular | [Angular](frontend/angular/README.md) | [.NET Entity Framework con PostgreSQL](frameworks/dotnet-entity-framework-postgresql/README.md) |
| Backend JavaScript | [Express con PostgreSQL](frameworks/express-postgresql/README.md) | [Redis](bases-de-datos/redis/README.md), [Mailpit](herramientas/mailpit/README.md) |
| Backend TypeScript | [NestJS con PostgreSQL](frameworks/nestjs-postgresql/README.md) | [MongoDB](bases-de-datos/mongodb/README.md), [Mongo Express](gestores-bd/mongo-express/README.md) |
| Python backend | [FastAPI con PostgreSQL](frameworks/fastapi-postgresql/README.md) | [Django con PostgreSQL](frameworks/django-postgresql/README.md) |
| PHP | [PHP con Apache](lenguajes/php-apache/README.md) | [MySQL](bases-de-datos/mysql/README.md), [phpMyAdmin](gestores-bd/phpmyadmin/README.md) |
| Laravel | [Laravel con MySQL y phpMyAdmin](frameworks/laravel-mysql/README.md) | [Mailpit](herramientas/mailpit/README.md) |
| Java Spring Boot | [Spring Boot con PostgreSQL](frameworks/spring-boot-postgresql/README.md) | [Prometheus y Grafana](herramientas/prometheus-grafana/README.md) |
| C# y .NET | [.NET Entity Framework con PostgreSQL](frameworks/dotnet-entity-framework-postgresql/README.md) | [SQL Server](bases-de-datos/sqlserver/README.md) |
| Automatizacion | [n8n](automatizacion/n8n/README.md) | [PostgreSQL](bases-de-datos/postgresql/README.md), [Mailpit](herramientas/mailpit/README.md) |
| Backend con servicios cloud locales | [LocalStack](herramientas/localstack/README.md) | [MinIO](herramientas/minio/README.md), [RabbitMQ](herramientas/rabbitmq/README.md) |
| Base de datos como servicio | [Supabase local](plataformas/supabase/README.md) | [pgAdmin](gestores-bd/pgadmin/README.md) |

## Si Es Tu Primera Vez

1. Revisa [instalacion de Docker](docs/instalacion-docker/README.md).
2. Levanta primero [Mailpit](herramientas/mailpit/README.md), porque es liviano y permite probar Docker rapido.
3. Luego levanta una base de datos como [PostgreSQL](bases-de-datos/postgresql/README.md) o [MySQL](bases-de-datos/mysql/README.md).
4. Despues combina un lenguaje con una base de datos.
5. Cuando ya entiendas el flujo, prueba stacks mas completos como [n8n](automatizacion/n8n/README.md) o [Supabase](plataformas/supabase/README.md).

## Reglas De Trabajo

- `main` queda reservado para version estable.
- `dev` es la rama base para integrar cambios.
- Las ramas principales y las ramas por stack estan protegidas.
- Nadie debe subir directo a `main` o `dev`.
- Todo cambio debe entrar por Pull Request hacia `dev`.
- No se deben subir credenciales reales, datos privados, backups grandes ni carpetas generadas por contenedores.

## Convencion De Ramas Para Estudiantes

```bash
git checkout dev
git pull origin dev
git checkout -b nombre-apellido/stack-que-modifica
```

Ejemplo:

```bash
git checkout -b maria-lopez/mysql-readme
```

## Comandos Utiles

| Accion | Comando |
| --- | --- |
| Validar configuracion | `docker compose config` |
| Levantar servicios | `docker compose up -d` |
| Ver servicios activos | `docker compose ps` |
| Ver logs | `docker compose logs -f` |
| Apagar servicios | `docker compose down` |
| Apagar y borrar volumenes | `docker compose down -v` |

## Recomendacion Final

Usa un stack a la vez al inicio. Cuando necesites combinar tecnologias, levanta solo los servicios necesarios para evitar consumo alto de memoria y puertos ocupados.
