--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

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

--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (user_id, role, full_name, login, password) FROM stdin;
14	dispatcher	joni	qwert	1234
1	admin	Zelenin Danil	admin	1234
15	director	ZELENIN D.D.	diOAKWNd	01234
4	user	test	test	1234
17	dispatcher	offfmi	qwert1	1234
16	dispatcher	test1	test1	1234
\.


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_user_id_seq', 17, true);


--
-- PostgreSQL database dump complete
--

