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
-- Data for Name: city; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.city (city_id, city_name, region_id) FROM stdin;
1	Хабаровск	1
2	Бикин	1
3	Амурск	1
4	Комсомольск-на-Амуре	1
5	Белогорск	2
6	Благовещенск	2
7	Зея	2
8	Свободный	2
9	Александровск-Сахалинский	3
10	Анива	3
11	Южно-Сахалинск	3
12	Корсаков	3
\.


--
-- Name: area_area_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.area_area_id_seq', 12, true);


--
-- PostgreSQL database dump complete
--

