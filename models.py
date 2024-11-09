from sqlalchemy import Column, Integer, String
from database import Base

class Point(Base):
    __tablename__ = 'points'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(String, nullable=False)
    order_id = Column(String, nullable=False)
    points = Column(Integer, nullable=False)
