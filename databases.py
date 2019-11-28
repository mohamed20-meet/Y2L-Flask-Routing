from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product( Name, Price, Picture_Link, Description):
	producta = Product(
		Name=name,
		Price=Price,
		Picture_Link= Picture_Link,
		Description= Description)
	session.add(producta)
	session.commit()



def update_name(id, Name):
	producta = session.query(
		Product).filter_by(
		id=id).first()
	producta.name=Name
	session.commit()
update_name(1,'sadeen')




def delete_product(id):
	session.query(Product).filter_by(
		id=id).delete()
	session.commit()

def query_all():

   producta = session.query(
     Product).all()
   return producta



def query_by_name(id):
   producta = session.query(
       Product).filter_by(
       id=id).first()
   return producta


def add_Cart( ProductID):
	carta = Product(
		ProductID=ProductID)
	session.add(carta)
	session.commit()


				





	