# When ORM gets awkward, drop to raw SQL.

from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///rawsql.db', echo=False)
Base = declarative_base()

class Sale(Base):
    __tablename__ = 'sales'
    
    id = Column(Integer, primary_key=True)
    product = Column(String(100))
    amount = Column(Integer)
    region = Column(String(50))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add sample sales
sales_data = [
    Sale(product="Laptop", amount=1200, region="North"),
    Sale(product="Mouse", amount=25, region="North"),
    Sale(product="Laptop", amount=1200, region="South"),
    Sale(product="Desk", amount=300, region="South"),
    Sale(product="Mouse", amount=25, region="North"),
]
session.add_all(sales_data)
session.commit()

# Complex aggregation - easier in raw SQL
sql = text("""
    SELECT region, product, SUM(amount) as total_sales, COUNT(*) as num_sales
    FROM sales
    GROUP BY region, product
    ORDER BY total_sales DESC
""")

result = session.execute(sql)
print("Sales by region and product:")
for row in result:
    print(f"  {row.region} - {row.product}: ${row.total_sales} ({row.num_sales} sales)")

# Raw SQL with parameters (safe from SQL injection)
region_filter = "North"
sql = text("SELECT * FROM sales WHERE region = :region")
result = session.execute(sql, {"region": region_filter})
print(f"\nSales in {region_filter}:")
for row in result:
    print(f"  {row.product}: ${row.amount}")

session.close()

# When to use raw SQL:
# ✅ Complex aggregations (GROUP BY, window functions)
# ✅ Performance-critical queries that need optimization
# ✅ Database-specific features (PostgreSQL's full-text search)
# ✅ When ORM query builder gets too complex
#
# When to use ORM:
# ✅ Simple CRUD operations
# ✅ Standard filtering and joins
# ✅ When you want database portability
# ✅ Most of the time
#
# Use ORM by default, raw SQL when you need it.
