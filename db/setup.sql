-- create table:
CREATE TABLE public.test_table (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    description character varying(500),
    done boolean DEFAULT false
);

-- make the id column the primary key
ALTER TABLE ONLY public.test_table ADD CONSTRAINT todos_pkey PRIMARY KEY (id);

-- create sequence (to auto-generated the primary key)
CREATE SEQUENCE public.test_table_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

-- sequence will auto-populate the id column:
ALTER TABLE ONLY public.test_table ALTER COLUMN id SET DEFAULT nextval('public.test_table_id_seq'::regclass);

-- insert some rows: 
INSERT INTO public.test_table(name, description, done) VALUES ('Shopping', 'go to the store', false);
INSERT INTO public.test_table(name, description, done) VALUES ('Lawn', 'mow the lawn', false);
INSERT INTO public.test_table(name, description, done) VALUES ('Dogs', 'feed the dog', false);