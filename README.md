# applicationProject
Hello, it's my first project, that was written on python with PostgreSQL.
--------------------------------------------------------------------------------------------------------------------------------------------------------

SQL-code for create database

CREATE DATABASE applications_db
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Russian_Russia.1251'
    LC_CTYPE = 'Russian_Russia.1251'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
    
SQL-code for create tables:

CREATE TABLE IF NOT EXISTS public.applications
(
    application_id smallint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 32767 CACHE 1 ),
    description text COLLATE pg_catalog."default" NOT NULL,
    status character varying(32) COLLATE pg_catalog."default" DEFAULT 'Новая'::character varying,
    date_of_creation date NOT NULL,
    date_of_adoption date,
    creator smallint NOT NULL,
    responsible character varying(128) COLLATE pg_catalog."default",
    responsible_mngr smallint,
    address character varying(256) COLLATE pg_catalog."default" NOT NULL,
    closing_date date,
    region character varying(100) COLLATE pg_catalog."default" NOT NULL,
    city character varying(150) COLLATE pg_catalog."default" NOT NULL,
    street character varying(150) COLLATE pg_catalog."default" NOT NULL,
    house_number character varying(6) COLLATE pg_catalog."default" NOT NULL,
    fio character varying(70) COLLATE pg_catalog."default",
    room character varying(6) COLLATE pg_catalog."default" NOT NULL,
    city_type character varying(16) COLLATE pg_catalog."default",
    CONSTRAINT applications_pkey PRIMARY KEY (application_id),
    CONSTRAINT fk_creator FOREIGN KEY (creator)
        REFERENCES public.users (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fk_responsible_mngr FOREIGN KEY (responsible_mngr)
        REFERENCES public.users (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
TABLESPACE pg_default;
ALTER TABLE IF EXISTS public.applications
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.city
(
    city_id smallint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 32767 CACHE 1 ),
    city_name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    region_id smallint NOT NULL,
    CONSTRAINT area_pkey PRIMARY KEY (city_id),
    CONSTRAINT fk_region_id FOREIGN KEY (region_id)
        REFERENCES public.region (region_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
TABLESPACE pg_default;
ALTER TABLE IF EXISTS public.city
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.locality
(
    locality_id smallint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 32767 CACHE 1 ),
    locality_name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    region_id smallint NOT NULL,
    CONSTRAINT locality_pkey PRIMARY KEY (locality_id),
    CONSTRAINT fk_region_id FOREIGN KEY (region_id)
        REFERENCES public.region (region_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
TABLESPACE pg_default;
ALTER TABLE IF EXISTS public.locality
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.region
(
    region_id smallint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 32767 CACHE 1 ),
    region_name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT region_pkey PRIMARY KEY (region_id)
)
TABLESPACE pg_default;
ALTER TABLE IF EXISTS public.region
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.responsibles
(
    responsible_id smallint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 32767 CACHE 1 ),
    name character varying(128) COLLATE pg_catalog."default",
    CONSTRAINT responsibles_pkey PRIMARY KEY (responsible_id)
)
TABLESPACE pg_default;
ALTER TABLE IF EXISTS public.responsibles
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.street
(
    street_id smallint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 32767 CACHE 1 ),
    street_name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    city_id smallint,
    locality_id smallint,
    CONSTRAINT street_pkey PRIMARY KEY (street_id),
    CONSTRAINT fk_city_id FOREIGN KEY (city_id)
        REFERENCES public.city (city_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fk_locality_id FOREIGN KEY (locality_id)
        REFERENCES public.locality (locality_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
TABLESPACE pg_default;
ALTER TABLE IF EXISTS public.street
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.users
(
    user_id smallint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 32767 CACHE 1 ),
    role character varying(20) COLLATE pg_catalog."default" NOT NULL DEFAULT 'user'::character varying,
    full_name character varying(128) COLLATE pg_catalog."default" NOT NULL,
    login character varying(128) COLLATE pg_catalog."default" NOT NULL,
    password character varying(256) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (user_id)
)
TABLESPACE pg_default;
ALTER TABLE IF EXISTS public.users
    OWNER to postgres;

