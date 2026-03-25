-- =============================================================
-- Shreadit Dev -- Role Setup
-- Run with: psql -U postgres -f setup_roles.sql
-- Run once with superuser - saving mostly for production setup
-- =============================================================
-- \prompt 'Password for shreadit_super: ' SUPER_PWD
-- \prompt 'Password for shreadit_user ' OWNER_PWD
-- \prompt 'Password for shreadit_app: ' APP_PWD
-- \prompt 'Password for shreadit_dev: ' DEV_PWD
-- \prompt 'Password for shreadit_migration: ' MIGRATIONS_PWD
-- \prompt 'Password for shreadit_read: ' READONLY_PWD
--
-- -- -------------------------------------------------------------
-- -- 1. Roles
-- -- -------------------------------------------------------------
-- -- Superuser (replaces postgres for all admin tasks)
-- CREATE ROLE shreadit_super
--   WITH LOGIN
--   SUPERUSER
--   CREATEDB
--   CREATEROLE
--   INHERIT
--   PASSWORD :'SUPER_PWD';
--
-- -- Database Owner
-- -- already ran
-- CREATE ROLE shreadit_user
--  WITH LOGIN
--  NOSUPERUSER
--  NOCREATEDB
-- NOCREATEROLE
--  INHERIT
--  PASSWORD :'OWNER_PWD';
--
-- -- Runtime role (FastAPI)
-- CREATE ROLE shreadit_app
--   WITH LOGIN
--   NOSUPERUSER
--   NOCREATEDB
--   NOCREATEROLE
--   INHERIT
--   PASSWORD :'APP_PWD';
--
-- -- Dev role (FastAPI)
-- CREATE ROLE shreadit_dev
--   WITH LOGIN
--   NOSUPERUSER
--   NOCREATEDB
--   NOCREATEROLE
--   INHERIT
--   PASSWORD :'DEV_PWD';
--
-- -- Migrations role (Django)
-- CREATE ROLE shreadit_migration
--   WITH LOGIN
--   NOSUPERUSER
--   NOCREATEDB
--   NOCREATEROLE
--   INHERIT
--   PASSWORD :'MIGRATIONS_PWD';
--
-- -- Read-only role (reporting / debugging)
-- CREATE ROLE shreadit_read
--   WITH LOGIN
--   NOSUPERUSER
--   NOCREATEDB
--   NOCREATEROLE
--   INHERIT
--   PASSWORD :'READONLY_PWD';

-- -------------------------------------------------------------
-- 2. Database-level access
-- -------------------------------------------------------------

GRANT CONNECT ON DATABASE shreadit_dev TO
  shreadit_app,
  shreadit_migration,
  shreadit_read,
  shreadit_super;

-- Migrations needs CREATE to run DDL (CREATE TABLE, ALTER, etc.)
GRANT CREATE ON SCHEMA public TO shreadit_migration;

-- -------------------------------------------------------------
-- 3. Schema-level access
-- -------------------------------------------------------------

GRANT USAGE  ON SCHEMA public TO shreadit_app, shreadit_read;
GRANT USAGE, CREATE ON SCHEMA public TO shreadit_migration;

-- -------------------------------------------------------------
-- 4. Privileges on existing objects
-- (run after your first Alembic migration if tables exist already)
-- -------------------------------------------------------------

-- App: full DML
GRANT SELECT, INSERT, UPDATE, DELETE
  ON ALL TABLES IN SCHEMA public TO shreadit_app;

GRANT USAGE, SELECT
  ON ALL SEQUENCES IN SCHEMA public TO shreadit_app;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO shreadit_app;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO shreadit_app;

ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO shreadit_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO shreadit_app;

-- Migrations: full DDL ownership
GRANT ALL PRIVILEGES
  ON ALL TABLES IN SCHEMA public TO shreadit_migration;

GRANT ALL PRIVILEGES
  ON ALL SEQUENCES IN SCHEMA public TO shreadit_migration;

-- Read-only: SELECT only
GRANT SELECT
  ON ALL TABLES IN SCHEMA public TO shreadit_read;

GRANT SELECT
  ON ALL SEQUENCES IN SCHEMA public TO shreadit_read;

-- -------------------------------------------------------------
-- 5. Default privileges (applies to future objects)
-- Run as the role that will own new objects (shreadit_migration)
-- -------------------------------------------------------------

ALTER DEFAULT PRIVILEGES FOR ROLE shreadit_migration IN SCHEMA public
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO shreadit_app;

ALTER DEFAULT PRIVILEGES FOR ROLE shreadit_migration IN SCHEMA public
  GRANT USAGE, SELECT ON SEQUENCES TO shreadit_app;

ALTER DEFAULT PRIVILEGES FOR ROLE shreadit_migration IN SCHEMA public
  GRANT SELECT ON TABLES TO shreadit_read;

ALTER DEFAULT PRIVILEGES FOR ROLE shreadit_migration IN SCHEMA public
  GRANT SELECT ON SEQUENCES TO shreadit_read;
