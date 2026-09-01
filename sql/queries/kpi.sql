-- KPI Performance Summary
SELECT
    "KPI_Category",
    COUNT(*) AS records,
    ROUND(AVG("Data_Quality_Score")::numeric,3) AS avg_quality,
    ROUND(AVG("Risk_Fraud_Score")::numeric,3) AS avg_fraud_risk
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "KPI_Category"
ORDER BY avg_quality DESC;