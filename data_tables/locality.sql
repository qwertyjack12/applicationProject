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
-- Data for Name: locality; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.locality (locality_id, locality_name, region_id) FROM stdin;
1	Заветы Ильича	1
2	Солнечный	1
4	Ванино	1
5	Тамбовка	2
6	Архара	2
7	Екатеринославка	2
8	Магдагачи	2
9	Ноглики	3
10	Смирных	3
12	Южно-Курильск	3
3	Чегдомын	1
11	Шахтёрск	3
\.


--
-- Name: locality_locality_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.locality_locality_id_seq', 12, true);


--
-- PostgreSQL database dump complete
--

