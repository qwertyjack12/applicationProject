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
-- Data for Name: applications; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.applications (application_id, description, status, date_of_creation, date_of_adoption, creator, responsible, responsible_mngr, address, closing_date, region, city, street, house_number, fio, room, city_type) FROM stdin;
2	АААААААААА, застраял в лифте, помогите!	Выполнена	2023-06-09	2023-07-05	4	Google	14	Амурская область, г.Белогорск, ул.Кирова, д.15, кв.1	\N	Амурская область	Белогорск	Кирова	15	Лахтюхов Ян Георгиевич	1	Город
24	abccc	Новая	2023-06-26	\N	4	\N	\N	Хабаровский край, г.Бикин, ул.ДОС, д.32, кв.3	\N	Хабаровский край	Бикин	ДОС	32	Длотовский Семен Романович	3	Город
46	добавил радио батон	В работе	2023-07-11	2023-07-11	4	Google	14	Хабаровский край, н.п.Заветы Ильича, ул.Матросская, д.15, кв.35	\N	Хабаровский край	Заветы Ильича	Матросская	15	Радио Батон Батонович	35	Населенный пункт
38	Я просто проверяю роботоспособность добавления заявки вместе с адресом	Закрыта	2023-06-27	2023-07-06	4	Sigma	17	Хабаровский край, г.Амурск, ул.Центральная, д.52, кв.4	2023-07-06	Хабаровский край	Амурск	Центральная	52	Дозорцев Федор Анатольевич	4	Город
39	Тестим тестим!	Закрыта	2023-06-27	2023-07-05	4	Polyarity	14	Хабаровский край, г.Хабаровск, ул.Волочаевская, д.5, кв.5	2023-07-06	Хабаровский край	Хабаровск	Волочаевская	5	Маршалков Федор Янович	5	Город
40	Застрял в лифте, пожалуйста, вытащите меня из шахты!	Закрыта	2023-06-28	2023-07-05	4	Sigma	14	Сахалинская область, г.Корсаков, ул.Советская, д.85, кв.6	2023-07-03	Сахалинская область	Корсаков	Советская	85	Калагин Эдуард Егорович	6	Город
41	test1234	В работе	2023-06-28	2023-07-05	16	Sigma	14	Амурская область, г.Благовещенск, ул.Амурская, д.2, кв.7	\N	Амурская область	Благовещенск	Амурская	2	Абаева Антонина Антоновна	7	Город
47	второй тест радио батона	Новая	2023-07-11	\N	4	\N	\N	Хабаровский край, н.п.Солнечный, ул.Парковая, д.67, кв.21	\N	Хабаровский край	Солнечный	Парковая	67	Радио Аркадий Батонович	21	Населенный пункт
10	Дорогой дневник, мне не описать ту боль, которую я испытал сегодня...	В работе	2023-06-25	2023-06-27	4	Polyarity	1	Сахалинская область,  г.Анива, ул.Ленина, д.26, кв.2	\N	Сахалинская область	Анива	Ленина	26	Ногтев Федор Данилович	2	Город
51	Perenos statusa	Новая	2023-07-12	\N	4	\N	\N	Амурская область, г.Благовещенск, ул.Зейская, д.14, кв.31	\N	Амурская область	Благовещенск	Зейская	14	Статус Перенос Успехович	31	Город
42	Это было интересно	В работе	2023-07-09	2023-07-09	4	torch.group	14	Хабаровский край, г.Бикин, ул.ДОС, д.123, кв.16	\N	Хабаровский край	Бикин	ДОС	123	Селюнина Полина Марселевна	16	Город
44	some problem	Новая	2023-07-11	\N	4	\N	\N	Сахалинская область, г.Южно-Сахалинск, ул.Маяковского, д.31б, кв.28	\N	Сахалинская область	Южно-Сахалинск	Маяковского	31б	Зигзагов Линад Владимирович	28	Город
52	ttt34	Новая	2023-07-18	\N	4	\N	\N	Амурская область, н.п.Магдагачи, ул.Курбатова, д.21, кв.15a	\N	Амурская область	Магдагачи	Курбатова	21	Tst Test Testt	15a	Населенный пункт
\.


--
-- Name: applications_application_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.applications_application_id_seq', 52, true);


--
-- PostgreSQL database dump complete
--

