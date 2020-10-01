\c postgres;

drop database source;
drop database data_vault;

create database source;
create database data_vault;

\c data_vault;
create schema zmc;
create schema fcrb;
create schema ustan;

ALTER DATABASE data_vault SET search_path TO fcrb, ustan, zmc, public, pg_catalog;

\c source;
create schema zmc;
create schema fcrb;
create schema ustan;

ALTER DATABASE source SET search_path TO fcrb, ustan, zmc, public, pg_catalog;


