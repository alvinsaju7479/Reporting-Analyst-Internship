-- ============================================================
-- DATA QUALITY ANALYTICS
-- ============================================================

-- 1. Average data quality
SELECT
    ROUND(AVG("Data_Quality_Score")::numeric, 4)
        AS overall_quality_score
FROM "01_core_raw_transactional_business_operations_data";


-- 2. Data quality by department
SELECT
    "Department_Code",
    ROUND(AVG("Data_Quality_Score")::numeric, 4)
        AS quality_score
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Department_Code"
ORDER BY quality_score DESC;


-- 3. GDPR compliance
SELECT
    "Is_GDPR_Compliant",
    COUNT(*) AS records
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Is_GDPR_Compliant";


-- 4. Pipeline status
SELECT
    "Extraction_Pipeline_Status",
    COUNT(*) AS records
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Extraction_Pipeline_Status";