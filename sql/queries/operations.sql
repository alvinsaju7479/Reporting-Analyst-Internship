-- Transactions by Customer Segment
SELECT
    "Customer_Segment",
    COUNT(*) AS transactions,
    ROUND(SUM("Transaction_Amount_EUR")::numeric,2) AS revenue
FROM "01_core_raw_transactional_business_operations_data"
GROUP BY "Customer_Segment"
ORDER BY revenue DESC;