-- Total Revenue by Department
SELECT
    "Department_Code",
    ROUND(SUM("Transaction_Amount_EUR")::numeric,2) AS total_revenue,
    ROUND(AVG("Transaction_Amount_EUR")::numeric,2) AS avg_transaction,
    ROUND(SUM("Tax_VAT_Amount_EUR")::numeric,2) AS total_vat
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Department_Code"
ORDER BY total_revenue DESC;