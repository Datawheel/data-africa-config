--createuser readonly
alter user readonly password '<placeholder>';
GRANT connect ON database data_africa to readonly;
GRANT USAGE on SCHEMA public TO readonly;
GRANT USAGE on SCHEMA attrs TO readonly;
GRANT USAGE on SCHEMA health TO readonly;
GRANT USAGE on SCHEMA crops TO readonly;
GRANT USAGE on SCHEMA poverty TO readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA crops GRANT SELECT ON TABLES TO readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA attrs GRANT SELECT ON TABLES TO readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA health GRANT SELECT ON TABLES TO readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA poverty GRANT SELECT ON TABLES TO readonly;
