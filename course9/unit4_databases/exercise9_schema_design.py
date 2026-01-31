# Design a database schema for an e-commerce system.
# Think about tables, relationships, and constraints.

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime, Table
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

engine = create_engine('sqlite:///ecommerce.db', echo=False)
Base = declarative_base()

# Design models for:
# - Customers (id, name, email, address)
# - Products (id, name, description, price, stock_quantity)
# - Orders (id, customer_id, order_date, total_amount, status)
# - OrderItems (id, order_id, product_id, quantity, price_at_purchase)
#   ^ Why separate table? Order can have multiple products

# Relationships:
# - Customer has many Orders (one-to-many)
# - Order has many OrderItems (one-to-many)
# - Product appears in many OrderItems (one-to-many)

# Design considerations:
# - What should be unique? (email)
# - What can be null? (address might be optional)
# - What needs defaults? (order_date, status)
# - Foreign keys to link tables

# Implement the models:

class Customer(Base):
    ...

class Product(Base):
    ...

class Order(Base):
    ...

class OrderItem(Base):
    ...

Base.metadata.create_all(engine)

# Test your schema by creating sample data:
# - 2 customers
# - 3 products
# - 1 order with 2 order items
# - Query and print the order with customer and items

...

# Expected output (structure):
# Order #1 for Alice (alice@example.com)
# Date: 2024-01-15
# Items:
#   - Laptop x1 @ $1200
#   - Mouse x2 @ $25
# Total: $1250
