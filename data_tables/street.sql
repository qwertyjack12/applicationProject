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
-- Data for Name: street; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.street (street_id, street_name, city_id, locality_id) FROM stdin;
1	Выборгская	1	\N
2	Волочаевская	1	\N
3	Шевченко	1	\N
4	Ленинградская	1	\N
5	Карла Маркса	1	\N
6	Воронежская	1	\N
7	Дзержинского	1	\N
8	Луговая	2	\N
9	ДОС	2	\N
10	Зачеславского	2	\N
11	Амурская	2	\N
12	Верхняя	2	\N
13	Киевская	2	\N
14	Зеленая	2	\N
15	Лесная	3	\N
17	Пионерская	3	\N
18	Школьная	3	\N
19	Центральная	3	\N
20	Колхозная	4	\N
21	Байкальская	4	\N
22	Хасановская	4	\N
23	Лермонтова	4	\N
24	Коммунаров	4	\N
25	Мичурина	4	\N
26	Кирова	4	\N
34	Кирова	5	\N
35	Победы	5	\N
36	Ленина	5	\N
37	Садовая	5	\N
38	Малиновского	5	\N
39	Чехова	5	\N
40	Почтовая	5	\N
41	Ленина	6	\N
42	Зейская	6	\N
43	Амурская	6	\N
44	Дьяченко	6	\N
45	Октябрьская	6	\N
46	Первомайская	6	\N
47	Кузнечная	6	\N
48	Лесная	7	\N
49	Мухина	7	\N
50	Кленовая	7	\N
51	Народная	7	\N
52	Ленина	8	\N
53	50 Лет Октября	8	\N
54	Карла Маркса	8	\N
55	Комсомольская	8	\N
56	Репина	8	\N
57	Мухина	8	\N
58	Орджоникидзе	8	\N
59	Кирова	9	\N
60	Аболтина	9	\N
61	Баночная	9	\N
62	Герцена	9	\N
63	Лермонтова	9	\N
64	Калинина	10	\N
65	Первомайская	10	\N
66	Ленина	10	\N
67	Гоголя	10	\N
68	Пионерская	10	\N
69	Ленина	11	\N
70	Горького	11	\N
71	Маяковского	11	\N
72	Лермонтова	11	\N
73	Степная	11	\N
74	Зеленая	11	\N
75	Колодезная	11	\N
16	Амурская	3	\N
76	Гвардейская	12	\N
77	Первомайская	12	\N
78	Советская	12	\N
79	Южно-Сахалинская	12	\N
80	Невельская	12	\N
81	Свердлова	12	\N
83	Матросская	\N	1
84	Завойко	\N	1
85	Байкальская	\N	1
86	Алтайская	\N	1
87	Парковая	\N	2
88	Ленина	\N	2
89	Геологов	\N	2
90	Зеленая	\N	2
91	Заводская	\N	3
92	Комарова	\N	3
93	Голубичная	\N	3
94	Агеева	\N	3
95	Лесная	\N	4
96	Крымская	\N	4
97	Краснодарская	\N	4
98	Береговая	\N	4
99	Пятая	\N	5
100	Сиреневая	\N	5
101	Луговая	\N	5
102	Липовая	\N	5
103	Новая	\N	5
104	Пионерская	\N	6
105	Нагорная	\N	6
106	Победы	\N	6
107	Новая	\N	6
108	Гребенькова	\N	6
109	Автомобильная	\N	6
110	Ленина	\N	7
111	Пролетарская	\N	7
112	Советская	\N	7
113	Хвойная	\N	7
114	Курбатова	\N	8
115	Ленина	\N	8
116	Зейская	\N	8
117	Гагарина	\N	8
118	Майская	\N	9
119	Лазурная	\N	9
120	Космонавтов	\N	9
121	Дальневосточная	\N	9
122	Дачная	\N	9
123	Гастелло	\N	10
124	Матросова	\N	10
125	Заречная	\N	10
126	Садовая	\N	10
127	Пирогова	\N	10
128	Победы	\N	11
129	Окружная	\N	11
130	Курильская	\N	11
131	Интернациональная	\N	11
132	Мира	\N	12
133	Победы	\N	12
134	Маленькая	\N	12
135	Карева	\N	12
136	Дружбы	\N	12
\.


--
-- Name: street_street_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.street_street_id_seq', 136, true);


--
-- PostgreSQL database dump complete
--

