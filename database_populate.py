#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import User, Category, Item

engine = create_engine('sqlite:///catalog.db')
Session = sessionmaker(bind=engine)

session = Session()

# Create first user.
user = User(username = 'Chris', email = 'chris@catalog.com')
session.add(user)
session.commit()


# Item categories
category1 = Category(user_id=1, name="Baseball")

session.add(category1)
session.commit()

Item1 = Item(user_id=1, name="Wilson A330 Glove", description="Wilson A330 Glove description",
                     category=category1)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1, name="Nike Pro 200 Pants", description="Nike Pro 200 Pants description",
                     category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="New Balance Zs4 Cleats", description="New Balance Zs4 Cleats description",
                     category=category1)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Dimarini 300 Bat", description="Dimarini 300 Bat description",
                     category=category1)

session.add(Item4)
session.commit()



# Item categories
category2 = Category(user_id=1, name="Soccer")

session.add(category2)
session.commit()

Item1 = Item(user_id=1, name="Mizuno 100 Cleats", description="Mizuno 100 Cleats description",
                     category=category2)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1, name="EPL Replica Ball", description="EPL Replica Ball description",
                     category=category2)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="New Balance Shorts", description="New Balance Shorts description",
                     category=category2)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Reebok Spyder jersey", description="Reebok Spyder jersey description",
                     category=category2)

session.add(Item4)
session.commit()



# Item categories
category3 = Category(user_id=1, name="Tennis")

session.add(category3)
session.commit()

Item1 = Item(user_id=1, name="Wilson Ace Balls", description="Wilson Ace Balls description",
                     category=category3)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1, name="Boboli x300", description="Boboli x300 description",
                     category=category3)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Stan Smith Classic", description="Stan Smith Classic description",
                     category=category3)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Reebok Arthur Ashe Shirt", description="Reebok Arthur Ashe Shirt description",
                     category=category3)

session.add(Item4)
session.commit()




# Item categories
category4 = Category(user_id=1, name="Football")

session.add(category4)
session.commit()

Item1 = Item(user_id=1, name="Riddell Pro Helmet", description="Riddell Pro Helmet description",
                     category=category4)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1, name="Wilson NFL Replica", description="Wilson NFL Replica description",
                     category=category4)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Nike 100 Cleats", description="Nike 100 Cleats description",
                     category=category4)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Wilson Tuff Pro Pads", description="Wilson Tuff Pro Pads description",
                     category=category4)

session.add(Item4)
session.commit()


print ('Database created')
