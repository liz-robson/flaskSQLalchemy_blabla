from application import db

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from application.models.items import Items
from application.models.users import Users

engine = create_engine('mysql+pymysql://root:@localhost/blabla', echo=True)
Session = sessionmaker(bind=engine)

session = Session()

# team = Teams(affiliation='X-men', objective='Being eXXXtra cool')
# session.add(team)
# session.commit()

# hero = Heroes(name='Clinton Barton', alias='Hawkeye', superPower='Master Archer', teamID=4)
# session.add(hero)
# session.commit()


# hero = session.query(Heroes).filter_by(id=2).first()
# print(hero.name, hero.superPower, hero.alias, hero.teamID)

item = session.query(Items).filter_by(id=2).first()
print(item.item_name, item.item_description, item.size, item.colour, item.rental_price)

item = session.query(Items).filter_by(colour="black").first()
print(item.item_name, item.item_description, item.size, item.colour, item.rental_price)

user = session.query(Users).filter_by(id=4).first()
print(user.first_name, user.last_name, user.location)
for item in user.items:
    print(item.item_name, 'is owned by', user.user_name)
