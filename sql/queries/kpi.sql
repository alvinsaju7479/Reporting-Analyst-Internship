-- ============================================================
-- KPI ANALYTICS
-- ============================================================

-- 1. KPI performance
SELECT
    "KPI_Category",
    COUNT(*) AS records,
    ROUND(AVG("Data_Quality_Score")::numeric, 4)
        AS average_quality,
    ROUND(AVG("Risk_Fraud_Score")::numeric, 4)
        AS average_fraud_score
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "KPI_Category"
ORDER BY average_quality DESC;


-- 2. Department KPI performance
SELECT
    "Department_Code",
    "KPI_Category",
    COUNT(*) AS records,
    ROUND(AVG("Data_Quality_Score")::numeric, 4)
        AS average_quality
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY
    "Department_Code",
    "KPI_Category"
ORDER BY
    "Department_Code",
    average_quality DESC;