# Build complex queries with multiple filters, sorting, pagination.

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///complex.db', echo=False)
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    category = Column(String(50))
    price = Column(Integer)
    in_stock = Column(Boolean)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add sample products
products = [
    Product(name="Laptop", category="electronics", price=1200, in_stock=True),
    Product(name="Mouse", category="electronics", price=25, in_stock=True),
    Product(name="Desk", category="furniture", price=300, in_stock=False),
    Product(name="Chair", category="furniture", price=150, in_stock=True),
    Product(name="Monitor", category="electronics", price=400, in_stock=True),
]
session.add_all(products)
session.commit()

# Complex query: electronics, in stock, under $500, ordered by price, limit 2
query = (
    session.query(Product)
    .filter(Product.category == "electronics")
    .filter(Product.in_stock == True)
    .filter(Product.price < 500)
    .order_by(Product.price.asc())
    .limit(2)
)

results = query.all()
print("Affordable electronics in stock:")
for p in results:
    print(f"  {p.name}: ${p.price}")

# Pagination: get page 2, 2 items per page
page = 2
per_page = 2
offset_value = (page - 1) * per_page

paginated = (
    session.query(Product)
    .order_by(Product.id)
    .limit(per_page)
    .offset(offset_value)
    .all()
)
print(f"\nPage {page}:")
for p in paginated:
    print(f"  {p.name}")

# Build a query yourself:
# Find furniture items that are in stock, ordered by price descending

...

session.close()

# Expected output:
# Affordable electronics in stock:
#   Mouse: $25
#   Monitor: $400
# 
# Page 2:
#   Desk
#   Chair
