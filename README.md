# infra-equipo

Repositorio de infraestructura del equipo.

## Descripción
Servicios en contenedores con Docker Compose: Pi-hole (DNS), Nginx Proxy Manager y PostgreSQL.

## Requisitos
- Ubuntu o Debian con Docker y docker-compose instalados
- Archivo `.env` creado a partir de `.env.example`

## Cómo desplegar
```bash
cp .env.example .env
nano .env   # cambia las contraseñas
docker-compose up -d
docker-compose ps
```
