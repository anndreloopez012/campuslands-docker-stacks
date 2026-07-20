# Docker en Windows

## Requisitos

- Windows 10/11 de 64 bits.
- Virtualizacion habilitada en BIOS/UEFI.
- WSL 2 instalado.

## Pasos

1. Descarga Docker Desktop desde el sitio oficial de Docker.
2. Instala Docker Desktop con soporte para WSL 2.
3. Reinicia el equipo si el instalador lo pide.
4. Abre Docker Desktop y espera que el motor quede activo.
5. Abre PowerShell y valida:

```powershell
docker --version
docker compose version
docker run hello-world
```

## Recomendacion

Trabaja tus proyectos dentro de una carpeta simple como `C:\campuslands\` para evitar rutas largas o permisos raros.
