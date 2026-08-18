-- ============================================================
-- FINANCE ANALYTICS
-- ============================================================

-- 1. Total Revenue
SELECT
    ROUND(SUM("Transaction_Amount_EUR")::numeric, 2) AS total_revenue
FROM "01_core_raw_transactional_business_operations_data";


-- 2. Total VAT
SELECT
    ROUND(SUM("Tax_VAT_Amount_EUR")::numeric, 2) AS total_vat
FROM "01_core_raw_transactional_business_operations_data";


-- 3. Average Transaction Value
SELECT
    ROUND(AVG("Transaction_Amount_EUR")::numeric, 2) AS average_transaction
FROM "01_core_raw_transactional_business_operations_data";


-- 4. Revenue by Department
SELECT
    "Department_Code",
    COUNT(*) AS transaction_count,
    ROUND(SUM("Transaction_Amount_EUR")::numeric, 2) AS revenue
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Department_Code"
ORDER BY revenue DESC;


-- 5. Revenue by Customer Segment
SELECT
    "Customer_Segment",
    COUNT(*) AS transaction_count,
    ROUND(SUM("Transaction_Amount_EUR")::numeric, 2) AS revenue
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Customer_Segment"
ORDER BY revenue DESC;


-- 6. Revenue by Currency
SELECT
    "Currency",
    COUNT(*) AS transaction_count,
    ROUND(SUM("Transaction_Amount_EUR")::numeric, 2) AS revenue
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Currency"
ORDER BY revenue DESC;