# Comandos basicos de Docker Compose

```bash
docker compose up -d        # levantar servicios
docker compose ps           # ver estado
docker compose logs -f      # ver logs
docker compose restart      # reiniciar servicios
docker compose down         # apagar servicios
docker compose down -v      # apagar y borrar volumenes
docker compose config       # validar configuracion
```

## Cuando algo falla

1. Revisa si el puerto esta ocupado.
2. Revisa los logs con `docker compose logs -f`.
3. Apaga servicios anteriores con `docker compose down`.
4. Si necesitas limpiar datos, usa `docker compose down -v` sabiendo que borra volumenes.
