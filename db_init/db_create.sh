#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER "partner_user";
    ALTER USER "partner_user" WITH ENCRYPTED PASSWORD 'partnerPa55w0rD';
    ALTER USER "partner_user" CREATEDB;
    CREATE DATABASE "partner" WITH OWNER "partner_user"
EOSQL
