-- ============================================================
-- OPERATIONS ANALYTICS
-- ============================================================

-- 1. Transactions by Department
SELECT
    "Department_Code",
    COUNT(*) AS transactions
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Department_Code"
ORDER BY transactions DESC;


-- 2. Settlement Status
SELECT
    "Settlement_Status",
    COUNT(*) AS transactions
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Settlement_Status"
ORDER BY transactions DESC;


-- 3. Payment Gateway Performance
SELECT
    "Payment_Gateway",
    COUNT(*) AS transactions,
    ROUND(AVG("Transaction_Amount_EUR")::numeric, 2) AS avg_transaction
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Payment_Gateway"
ORDER BY transactions DESC;


-- 4. Reconciliation Status
SELECT
    "Reconciliation_Flag",
    COUNT(*) AS records
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Reconciliation_Flag"
ORDER BY records DESC;


-- 5. Average Processing Latency
SELECT
    "Department_Code",
    ROUND(AVG("System_Ingestion_Latency_MS")::numeric, 2)
        AS average_latency_ms
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Department_Code"
ORDER BY average_latency_ms;