SELECT table_name
FROM information_schema.tables
WHERE table_schema='public'
ORDER BY table_name;
SELECT
table_name,
(
SELECT COUNT(*)
FROM information_schema.columns
WHERE table_name=t.table_name
) AS columns
FROM information_schema.tables t
WHERE table_schema='public'
ORDER BY table_name;