#!/bin/bash

sleep 10

mc alias set minio http://minio:9000 minio123 minio123
mc mb minio/crm --ignore-existing
mc mb minio/erp --ignore-existing

mc cp --recursive data/raw/crm/ minio/crm/
mc cp --recursive data/raw/erp/ minio/erp/

