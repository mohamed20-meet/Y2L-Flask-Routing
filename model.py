from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class Product:(Base):
	__tablename__ = 'Product'
   name = Column(String)
   Price = Column(Float)
   Picture_Link = Column(String)
   Description = Column(String)
   id = Column(Integer, primary_key=True)


	