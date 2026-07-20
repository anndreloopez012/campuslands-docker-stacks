# Docker en Linux

## Instalacion generica

```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
newgrp docker
docker --version
docker compose version
docker run hello-world
```

## Si usas Fedora o Arch

Puedes instalar Docker desde el gestor de paquetes de tu distribucion. Lo importante es que `docker` y `docker compose` funcionen sin usar `sudo` en cada comando.
