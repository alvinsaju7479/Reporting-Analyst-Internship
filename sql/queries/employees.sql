-- ============================================================
-- EMPLOYEE ANALYTICS
-- ============================================================

-- 1. Employee transaction volume
SELECT
    "Employee_ID",
    COUNT(*) AS transactions_processed
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Employee_ID"
ORDER BY transactions_processed DESC;


-- 2. Employee data quality
SELECT
    "Employee_ID",
    ROUND(AVG("Data_Quality_Score")::numeric, 4)
        AS average_quality_score
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Employee_ID"
ORDER BY average_quality_score DESC;


-- 3. Employee processing latency
SELECT
    "Employee_ID",
    ROUND(AVG("System_Ingestion_Latency_MS")::numeric, 2)
        AS average_latency_ms
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Employee_ID"
ORDER BY average_latency_ms;


-- 4. Top 10 employees by transaction volume
SELECT
    "Employee_ID",
    COUNT(*) AS transactions_processed
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Employee_ID"
ORDER BY transactions_processed DESC
LIMIT 10;