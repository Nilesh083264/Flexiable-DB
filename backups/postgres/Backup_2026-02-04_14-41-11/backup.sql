--
-- PostgreSQL database dump
--

\restrict cO8Z7ErIiJcCZV5SWv1xYu3D84ktqpQPRGnk8iVpZv18fYoSMakw8ViYVjF3cyB

-- Dumped from database version 16.11 (Ubuntu 16.11-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.11 (Ubuntu 16.11-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: apollophonenumbers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.apollophonenumbers (
    index integer NOT NULL,
    id character varying(255),
    phone character varying(255)
);


ALTER TABLE public.apollophonenumbers OWNER TO postgres;

--
-- Name: apollophonenumbers_index_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.apollophonenumbers_index_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.apollophonenumbers_index_seq OWNER TO postgres;

--
-- Name: apollophonenumbers_index_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.apollophonenumbers_index_seq OWNED BY public.apollophonenumbers.index;


--
-- Name: candidates; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.candidates (
    candidate_id bigint NOT NULL,
    linkedin_url character varying NOT NULL,
    candidate_name character varying,
    address character varying,
    experience_history jsonb[],
    current_company character varying,
    job_role character varying,
    total_experience_months integer,
    email character varying,
    phone character varying,
    skills character varying[],
    higher_qualification character varying,
    year_of_passing character varying,
    status character varying,
    created_date text,
    search text
);


ALTER TABLE public.candidates OWNER TO postgres;

--
-- Name: candidates_candidate_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.candidates_candidate_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.candidates_candidate_id_seq OWNER TO postgres;

--
-- Name: candidates_candidate_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.candidates_candidate_id_seq OWNED BY public.candidates.candidate_id;


--
-- Name: choices; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.choices (
    id integer NOT NULL,
    choice_txt character varying,
    is_correct boolean,
    question_id integer
);


ALTER TABLE public.choices OWNER TO postgres;

--
-- Name: choices_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.choices_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.choices_id_seq OWNER TO postgres;

--
-- Name: choices_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.choices_id_seq OWNED BY public.choices.id;


--
-- Name: comments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.comments (
    comment_id bigint NOT NULL,
    candidate_id bigint NOT NULL,
    post_id bigint NOT NULL,
    commenter_name character varying,
    comment text NOT NULL,
    created_date text,
    search text
);


ALTER TABLE public.comments OWNER TO postgres;

--
-- Name: comments_comment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.comments_comment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.comments_comment_id_seq OWNER TO postgres;

--
-- Name: comments_comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.comments_comment_id_seq OWNED BY public.comments.comment_id;


--
-- Name: emp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.emp (
    id integer NOT NULL,
    emp_name character varying(100) NOT NULL,
    emp_email character varying(150) NOT NULL,
    emp_phone character varying(20),
    emp_department character varying(100),
    emp_salary numeric(12,2),
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now()
);


ALTER TABLE public.emp OWNER TO postgres;

--
-- Name: emp_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.emp_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.emp_id_seq OWNER TO postgres;

--
-- Name: emp_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.emp_id_seq OWNED BY public.emp.id;


--
-- Name: jobs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jobs (
    job_id bigint NOT NULL,
    post_id bigint NOT NULL,
    job_title character varying NOT NULL,
    required_experience character varying,
    required_skills text,
    salary character varying,
    location character varying,
    job_description text,
    created_date text,
    search text
);


ALTER TABLE public.jobs OWNER TO postgres;

--
-- Name: jobs_job_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.jobs_job_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.jobs_job_id_seq OWNER TO postgres;

--
-- Name: jobs_job_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.jobs_job_id_seq OWNED BY public.jobs.job_id;


--
-- Name: opentowork; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.opentowork (
    id integer NOT NULL,
    job_title character varying(255),
    date_of_application date,
    search_query character varying(255),
    name character varying(255),
    email_id character varying(255),
    phone_number character varying(50),
    company_phone_number character varying(50),
    current_location character varying(255),
    preferred_locations character varying(255),
    total_experience character varying(50),
    curr_company_name character varying(255),
    curr_company_designation character varying(255),
    department character varying(255),
    role character varying(255),
    industry character varying(255),
    key_skills text,
    annual_salary character varying(50),
    notice_period_availability character varying(100),
    headline character varying(500),
    summary text,
    under_graduation_degree character varying(255),
    ug_specialization character varying(255),
    ug_university_name character varying(255),
    ug_graduation_year character varying(10),
    post_graduation_degree character varying(255),
    pg_specialization character varying(255),
    pg_university_name character varying(255),
    pg_graduation_year character varying(10),
    doctorate_degree character varying(255),
    doctorate_specialization character varying(255),
    doctorate_university_name character varying(255),
    doctorate_graduation_year character varying(10),
    gender character varying(20),
    marital_status character varying(20),
    home_town_city character varying(255),
    pin_code character varying(20),
    work_permit_usa character varying(10),
    date_of_birth date,
    permanent_address text,
    source character varying(255),
    candidate_url character varying(500),
    workflow character varying(255),
    pipeline character varying(255),
    download character varying(50),
    viewed character varying(50),
    emailed character varying(50),
    calling character varying(50),
    comment text
);


ALTER TABLE public.opentowork OWNER TO postgres;

--
-- Name: opentowork_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.opentowork_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.opentowork_id_seq OWNER TO postgres;

--
-- Name: opentowork_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.opentowork_id_seq OWNED BY public.opentowork.id;


--
-- Name: posts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.posts (
    post_id bigint NOT NULL,
    post_link character varying NOT NULL,
    linkedin_profile character varying NOT NULL,
    posted_by character varying NOT NULL,
    identity_type character varying,
    description text,
    posted_date date NOT NULL,
    post_text text,
    title text,
    displayed_link text,
    highlights character varying[],
    created_date text,
    search text
);


ALTER TABLE public.posts OWNER TO postgres;

--
-- Name: posts_post_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.posts_post_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.posts_post_id_seq OWNER TO postgres;

--
-- Name: posts_post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.posts_post_id_seq OWNED BY public.posts.post_id;


--
-- Name: questions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.questions (
    id integer NOT NULL,
    question_txt character varying
);


ALTER TABLE public.questions OWNER TO postgres;

--
-- Name: questions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.questions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.questions_id_seq OWNER TO postgres;

--
-- Name: questions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.questions_id_seq OWNED BY public.questions.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying(255) NOT NULL,
    password text NOT NULL,
    created_at timestamp without time zone DEFAULT now()
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: apollophonenumbers index; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apollophonenumbers ALTER COLUMN index SET DEFAULT nextval('public.apollophonenumbers_index_seq'::regclass);


--
-- Name: candidates candidate_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidates ALTER COLUMN candidate_id SET DEFAULT nextval('public.candidates_candidate_id_seq'::regclass);


--
-- Name: choices id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.choices ALTER COLUMN id SET DEFAULT nextval('public.choices_id_seq'::regclass);


--
-- Name: comments comment_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comments ALTER COLUMN comment_id SET DEFAULT nextval('public.comments_comment_id_seq'::regclass);


--
-- Name: emp id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.emp ALTER COLUMN id SET DEFAULT nextval('public.emp_id_seq'::regclass);


--
-- Name: jobs job_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jobs ALTER COLUMN job_id SET DEFAULT nextval('public.jobs_job_id_seq'::regclass);


--
-- Name: opentowork id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opentowork ALTER COLUMN id SET DEFAULT nextval('public.opentowork_id_seq'::regclass);


--
-- Name: posts post_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts ALTER COLUMN post_id SET DEFAULT nextval('public.posts_post_id_seq'::regclass);


--
-- Name: questions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.questions ALTER COLUMN id SET DEFAULT nextval('public.questions_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: apollophonenumbers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.apollophonenumbers (index, id, phone) FROM stdin;
\.


--
-- Data for Name: candidates; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.candidates (candidate_id, linkedin_url, candidate_name, address, experience_history, current_company, job_role, total_experience_months, email, phone, skills, higher_qualification, year_of_passing, status, created_date, search) FROM stdin;
\.


--
-- Data for Name: choices; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.choices (id, choice_txt, is_correct, question_id) FROM stdin;
1	string	t	1
\.


--
-- Data for Name: comments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.comments (comment_id, candidate_id, post_id, commenter_name, comment, created_date, search) FROM stdin;
\.


--
-- Data for Name: emp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.emp (id, emp_name, emp_email, emp_phone, emp_department, emp_salary, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: jobs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jobs (job_id, post_id, job_title, required_experience, required_skills, salary, location, job_description, created_date, search) FROM stdin;
\.


--
-- Data for Name: opentowork; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.opentowork (id, job_title, date_of_application, search_query, name, email_id, phone_number, company_phone_number, current_location, preferred_locations, total_experience, curr_company_name, curr_company_designation, department, role, industry, key_skills, annual_salary, notice_period_availability, headline, summary, under_graduation_degree, ug_specialization, ug_university_name, ug_graduation_year, post_graduation_degree, pg_specialization, pg_university_name, pg_graduation_year, doctorate_degree, doctorate_specialization, doctorate_university_name, doctorate_graduation_year, gender, marital_status, home_town_city, pin_code, work_permit_usa, date_of_birth, permanent_address, source, candidate_url, workflow, pipeline, download, viewed, emailed, calling, comment) FROM stdin;
\.


--
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.posts (post_id, post_link, linkedin_profile, posted_by, identity_type, description, posted_date, post_text, title, displayed_link, highlights, created_date, search) FROM stdin;
\.


--
-- Data for Name: questions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.questions (id, question_txt) FROM stdin;
1	string
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, email, password, created_at) FROM stdin;
\.


--
-- Name: apollophonenumbers_index_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.apollophonenumbers_index_seq', 1, false);


--
-- Name: candidates_candidate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.candidates_candidate_id_seq', 1, false);


--
-- Name: choices_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.choices_id_seq', 3, true);


--
-- Name: comments_comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.comments_comment_id_seq', 1, false);


--
-- Name: emp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.emp_id_seq', 1, false);


--
-- Name: jobs_job_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.jobs_job_id_seq', 1, false);


--
-- Name: opentowork_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.opentowork_id_seq', 1, false);


--
-- Name: posts_post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.posts_post_id_seq', 1, false);


--
-- Name: questions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.questions_id_seq', 2, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: apollophonenumbers apollophonenumbers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apollophonenumbers
    ADD CONSTRAINT apollophonenumbers_pkey PRIMARY KEY (index);


--
-- Name: candidates candidates_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidates
    ADD CONSTRAINT candidates_email_key UNIQUE (email);


--
-- Name: candidates candidates_linkedin_url_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidates
    ADD CONSTRAINT candidates_linkedin_url_key UNIQUE (linkedin_url);


--
-- Name: candidates candidates_phone_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidates
    ADD CONSTRAINT candidates_phone_key UNIQUE (phone);


--
-- Name: candidates candidates_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidates
    ADD CONSTRAINT candidates_pkey PRIMARY KEY (candidate_id);


--
-- Name: choices choices_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.choices
    ADD CONSTRAINT choices_pkey PRIMARY KEY (id);


--
-- Name: comments comments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pkey PRIMARY KEY (comment_id);


--
-- Name: emp emp_emp_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.emp
    ADD CONSTRAINT emp_emp_email_key UNIQUE (emp_email);


--
-- Name: emp emp_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.emp
    ADD CONSTRAINT emp_pkey PRIMARY KEY (id);


--
-- Name: jobs jobs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jobs
    ADD CONSTRAINT jobs_pkey PRIMARY KEY (job_id);


--
-- Name: opentowork opentowork_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opentowork
    ADD CONSTRAINT opentowork_pkey PRIMARY KEY (id);


--
-- Name: posts posts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (post_id);


--
-- Name: posts posts_post_link_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_post_link_key UNIQUE (post_link);


--
-- Name: questions questions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT questions_pkey PRIMARY KEY (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_candidates_candidate_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_candidates_candidate_id ON public.candidates USING btree (candidate_id);


--
-- Name: ix_choices_choice_txt; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_choices_choice_txt ON public.choices USING btree (choice_txt);


--
-- Name: ix_choices_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_choices_id ON public.choices USING btree (id);


--
-- Name: ix_comments_comment_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_comments_comment_id ON public.comments USING btree (comment_id);


--
-- Name: ix_emp_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_emp_id ON public.emp USING btree (id);


--
-- Name: ix_jobs_job_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_jobs_job_id ON public.jobs USING btree (job_id);


--
-- Name: ix_posts_post_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_posts_post_id ON public.posts USING btree (post_id);


--
-- Name: ix_questions_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_questions_id ON public.questions USING btree (id);


--
-- Name: ix_questions_question_txt; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_questions_question_txt ON public.questions USING btree (question_txt);


--
-- Name: choices choices_question_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.choices
    ADD CONSTRAINT choices_question_id_fkey FOREIGN KEY (question_id) REFERENCES public.questions(id);


--
-- Name: comments comments_candidate_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_candidate_id_fkey FOREIGN KEY (candidate_id) REFERENCES public.candidates(candidate_id);


--
-- Name: comments comments_post_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_post_id_fkey FOREIGN KEY (post_id) REFERENCES public.posts(post_id);


--
-- Name: jobs jobs_post_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jobs
    ADD CONSTRAINT jobs_post_id_fkey FOREIGN KEY (post_id) REFERENCES public.posts(post_id);


--
-- PostgreSQL database dump complete
--

\unrestrict cO8Z7ErIiJcCZV5SWv1xYu3D84ktqpQPRGnk8iVpZv18fYoSMakw8ViYVjF3cyB

