-- Table: public.item
-- DROP TABLE IF EXISTS public.item;

CREATE TABLE IF NOT EXISTS public.item
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    "position" integer NOT NULL,
    price money NOT NULL,
    amount real,
    created_by character varying(100) COLLATE pg_catalog."default",
    created_at timestamp without time zone DEFAULT now(),
    updated_by character varying(100) COLLATE pg_catalog."default",
    updated_at timestamp without time zone,
    CONSTRAINT item_pkey PRIMARY KEY (id),
    CONSTRAINT item_name_unique UNIQUE (name)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.item
    OWNER to postgres;

COMMENT ON TABLE public.item
    IS 'Generic items';


-- Table: public.person
-- DROP TABLE IF EXISTS public.person;

CREATE TABLE IF NOT EXISTS public.person
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    email character varying(50) COLLATE pg_catalog."default" NOT NULL,
    created_by character varying(100) COLLATE pg_catalog."default",
    created_at timestamp without time zone DEFAULT now(),
    updated_by character varying(100) COLLATE pg_catalog."default",
    updated_at timestamp without time zone,
    CONSTRAINT person_pkey PRIMARY KEY (id),
    CONSTRAINT person_email_unique UNIQUE (email)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.person
    OWNER to postgres;

COMMENT ON TABLE public.person
    IS 'People';


-- Table: public.comment
-- DROP TABLE IF EXISTS public.comment;

CREATE TABLE IF NOT EXISTS public.comment
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    person_id integer NOT NULL,
    item_id integer NOT NULL,
    comment character varying(10485760) COLLATE pg_catalog."default" NOT NULL,
    created_by character varying(100) COLLATE pg_catalog."default",
    created_at timestamp without time zone DEFAULT now(),
    updated_by character varying(100) COLLATE pg_catalog."default",
    updated_at timestamp without time zone,
    CONSTRAINT comment_pkey PRIMARY KEY (id),
    CONSTRAINT comment_item_fkey FOREIGN KEY (item_id)
        REFERENCES public.item (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT comment_person_fkey FOREIGN KEY (person_id)
        REFERENCES public.person (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.comment
    OWNER to postgres;

COMMENT ON TABLE public.comment
    IS 'Comments on the items made by the people';
