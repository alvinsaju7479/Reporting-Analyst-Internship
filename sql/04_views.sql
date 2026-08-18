-- ============================================================
-- Reporting Analytics - SQL Views
-- ============================================================

-- 1. Financial Summary
CREATE OR REPLACE VIEW vw_financial_summary AS
SELECT
    "Department_Code",
    COUNT(*) AS total_transactions,
    ROUND(SUM("Transaction_Amount_EUR")::numeric, 2) AS revenue,
    ROUND(AVG("Transaction_Amount_EUR")::numeric, 2) AS average_transaction,
    ROUND(SUM("Tax_VAT_Amount_EUR")::numeric, 2) AS total_vat
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Department_Code";


-- 2. Employee Performance
CREATE OR REPLACE VIEW vw_employee_performance AS
SELECT
    "Employee_ID",
    COUNT(*) AS transactions_processed,
    ROUND(AVG("Data_Quality_Score")::numeric, 4) AS avg_quality,
    ROUND(AVG("System_Ingestion_Latency_MS")::numeric, 2) AS avg_latency
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Employee_ID";


-- 3. KPI Summary
CREATE OR REPLACE VIEW vw_kpi_summary AS
SELECT
    "KPI_Category",
    COUNT(*) AS records,
    ROUND(AVG("Data_Quality_Score")::numeric, 4) AS quality,
    ROUND(AVG("Risk_Fraud_Score")::numeric, 4) AS fraud_score
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "KPI_Category";