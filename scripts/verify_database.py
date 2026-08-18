import psycopg2

DB_NAME = "reporting_analytics"
DB_USER = "alvinsaju"
DB_HOST = "localhost"
DB_PORT = "5432"

connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    host=DB_HOST,
    port=DB_PORT
)

cursor = connection.cursor()

print("=" * 70)
print("POSTGRESQL DATABASE VERIFICATION")
print("=" * 70)

# Check tables
cursor.execute("""
    SELECT COUNT(*)
    FROM information_schema.tables
    WHERE table_schema = 'public';
""")

table_count = cursor.fetchone()[0]

print(f"\nTables found: {table_count}")

# Check views
cursor.execute("""
    SELECT COUNT(*)
    FROM information_schema.views
    WHERE table_schema = 'public';
""")

view_count = cursor.fetchone()[0]

print(f"Views found: {view_count}")

# Main table row count
cursor.execute("""
    SELECT COUNT(*)
    FROM "01_core_raw_transactional_business_operations_data";
""")

row_count = cursor.fetchone()[0]

print(f"Core transaction rows: {row_count}")

# List tables
cursor.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
    ORDER BY table_name;
""")

print("\nTables:")
for table in cursor.fetchall():
    print(f" - {table[0]}")

# List views
cursor.execute("""
    SELECT table_name
    FROM information_schema.views
    WHERE table_schema = 'public'
    ORDER BY table_name;
""")

print("\nViews:")
for view in cursor.fetchall():
    print(f" - {view[0]}")

cursor.close()
connection.close()

print("\n" + "=" * 70)
print("DATABASE VERIFICATION COMPLETE")
print("=" * 70)