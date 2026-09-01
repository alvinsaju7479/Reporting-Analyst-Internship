-- Top Performing Employees
SELECT
    "Employee_ID",
    COUNT(*) AS transactions_processed,
    ROUND(AVG("Data_Quality_Score")::numeric,3) AS quality_score,
    ROUND(AVG("System_Ingestion_Latency_MS")::numeric,2) AS avg_latency
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Employee_ID"
ORDER BY quality_score DESC
LIMIT 10;