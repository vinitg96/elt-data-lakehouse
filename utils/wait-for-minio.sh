#!/bin/sh
# espera até que o MinIO esteja acessível
until curl -s http://minio:9000 > /dev/null; do
  echo "Aguardando MinIO..."
  sleep 5
done

# depois executa o comando principal
exec "$@"
