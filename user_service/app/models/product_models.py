from sqlalchemy import Column, Integer, String, Text, Numeric, Date, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Product():
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    sku = Column(String(50), unique=True, nullable=False)
    short_description = Column(String(100), nullable=False)
    long_description = Column(Text)
    price = Column(Numeric(14, 2), default=1.0, nullable=False)
    special_price = Column(Numeric(14, 2), nullable=True)
    special_price_from = Column(Date, nullable=True)
    special_price_to = Column(Date, nullable=True)
    quantity = Column(Integer, default=1, nullable=False)
    meta_title = Column(String(45), nullable=True)
    meta_description = Column(Text, nullable=True)
    meta_keywords = Column(Text, nullable=True)
    status = Column(Boolean, default=True)
    created_by_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    created_by = relationship('User', foreign_keys=[created_by_id], back_populates='product_created_by')
    created_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    modify_by_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    modify_by = relationship('User', foreign_keys=[modify_by_id], back_populates='product_modified_by')
    modify_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    is_featured = Column(Boolean, default=False)
