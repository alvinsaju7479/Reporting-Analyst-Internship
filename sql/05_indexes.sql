-- ============================================================
-- Reporting Analytics - Database Indexes
-- ============================================================

CREATE INDEX IF NOT EXISTS idx_business_record_id
ON "01_core_raw_transactional_business_operations_data"
("Record_ID");

CREATE INDEX IF NOT EXISTS idx_business_report_id
ON "01_core_raw_transactional_business_operations_data"
("Report_ID");

CREATE INDEX IF NOT EXISTS idx_business_employee_id
ON "01_core_raw_transactional_business_operations_data"
("Employee_ID");

CREATE INDEX IF NOT EXISTS idx_business_department_code
ON "01_core_raw_transactional_business_operations_data"
("Department_Code");

CREATE INDEX IF NOT EXISTS idx_business_kpi_category
ON "01_core_raw_transactional_business_operations_data"
("KPI_Category");

CREATE INDEX IF NOT EXISTS idx_business_timestamp
ON "01_core_raw_transactional_business_operations_data"
("Timestamp_UTC");