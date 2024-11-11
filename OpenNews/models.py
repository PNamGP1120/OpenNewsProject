import datetime

from flask_login import UserMixin
from sqlalchemy import Column, Integer, Enum, String, Boolean, ForeignKey, TEXT, DateTime
from sqlalchemy.orm import relationship

from OpenNews import app, login
from OpenNews import db
from enum import Enum as UserEnum


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(20), nullable=False)
    news = relationship('News', backref='category', lazy=True)

    def __str__(self):
        return self.name

class UserRoles(UserEnum):
    ADMIN = 1
    USER = 2


class User(BaseModel, UserMixin):
    __tablename__ = 'user'

    name = Column(TEXT, nullable=False)
    active = Column(Boolean, default=True)
    username = Column(TEXT, nullable=False)
    password = Column(TEXT, nullable=False)
    email = Column(TEXT, nullable=False)
    avatar = Column(TEXT, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now())
    user_role = Column(Enum(UserRoles), default=UserRoles.USER)

    def __str__(self):
        return self.name


class News(BaseModel):
    __tablename__ = 'news'

    title = Column(TEXT, nullable=False)
    content = Column(TEXT, nullable=False)
    description = Column(TEXT, nullable=False)
    created = Column(DateTime, nullable=False)
    url = Column(TEXT, nullable=False)
    image_url = Column(TEXT, nullable=False)
    author = Column(TEXT, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)



    def __str__(self):
        return self.name

if __name__ == '__main__':
    # print(Category.query.all())
    with app.app_context():
        db.create_all()
    # c = Category.query.filter(Category.id.__eq__(6)).first()
    #
    # for news in load_news()['articles']:
    #     db.session.add(News(title=news['title'],
    #                         content=news['content'],
    #                         description=news['description'],
    #                         url=news['url'],
    #                         image_url=news['urlToImage'] if news['urlToImage'] != None else "NULL",
    #                         author=news['author'] if news['author'] != None else "NULL",
    #                         created=datetime.strptime(news['publishedAt'], "%Y-%m-%dT%H:%M:%SZ"),
    #                         category_id=int(c.id)))
    # db.session.commit()
    # c1 = Category(name='Dien Thoai')
    # c2 = Category(name='Ipad')
    # c3 = Category(name='DOng ho')
    #
    # db.session.add(c1)
    # db.session.add(c2)
    # db.session.add(c3)
    #
    # db.session.commit()
    #
    # products = [
    #     {
    #         "id": 1,
    #         "name": "iPhone 7 Plus",
    #         "description": "Apple, 32GB, RAM: 3GB, iOS13",
    #         "price": 17000000,
    #         "image": "images/p1.jpg",
    #         "category_id": 1
    #     },
    #     {
    #         "id": 2,
    #         "name": "iPad Pro 2020",
    #         "description": "Apple, 128GB, RAM: 6GB",
    #         "price": 37000000,
    #         "image": "images/p2.jpg",
    #         "category_id": 2
    #     },
    #     {
    #         "id": 3,
    #         "name": "Galaxy Note 10 Plus",
    #         "description": "Samsung, 64GB, RAML: 6GB",
    #         "price": 24000000,
    #         "image": "images/p3.jpg",
    #         "category_id": 1
    #     }]
    #
    # for p in products:
    #     pro = Product(name=p['name'], description=p['description'], price=p['price'], image=p['image'], category_id=p['category_id'])
    #     db.session.add(pro)
    #
    # db.session.commit()
