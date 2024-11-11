import json
import os

from OpenNews.models import News, Category, User
from OpenNews import app, db
import hashlib


def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_categories(cate=None):
    with app.app_context():
        if cate == None:
            return Category.query.all()
        return Category.query.filter(Category.name == cate).all()
    # return read_json(os.path.join(app.root_path, 'data/categories.json'))


# def load_user():
#     with app.app_context():
#         return User.query.all()
#
# print(load_user())
# def load_products(cate_id=None, kw=None, from_price=None, to_price=None):
#     # products = read_json(os.path.join(app.root_path, 'data/products.json'))
#     # if cate_id:
#     #     products = [p for p in products if p['category_id'] == int(cate_id)]
#     # if kw:
#     #     products = [p for p in products if p['name'].lower().find(kw.lower()) >= 0]
#     # if from_price:
#     #     products = [p for p in products if p['price'] >= float(from_price)]
#     # if to_price:
#     #     products = [p for p in products if p['price'] <= float(to_price)]
#     # return products
#     products = Product.query.filter(Product.active.__eq__(True))
#     if cate_id:
#         products = products.filter(Product.category_id.__eq__(cate_id))
#     if kw:
#         products = products.filter(Product.name.contains(kw))
#     if from_price:
#         products = products.filter(Product.price.__ge__(from_price))
#     if to_price:
#         products = products.filter(Product.price.__le__(to_price))
#     return products.all()


# def get_product_by_id(product_id):
#     # products = read_json(os.path.join(app.root_path, 'data/products.json'))
#     # for p in products:
#     #     if p['id'] == product_id:
#     #         return p
#     product = Product.query.get(product_id)
def get_name_categories(cate=None):
    with app.app_context():
        if cate != None:
            return Category.query.all(Category.name == cate)
        return None


def add_user(name, username, password, **kwargs):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(name = name.strip(),
                username = username.strip(),
                password = password,
                email = kwargs.get('email'),
                avatar = kwargs.get('avatar'))

    db.session.add(user)
    db.session.commit()

# add_user(name='Nam', username='Nam', password='abc', email='abcd', avatar='nam.png')
def load_news(cate=None):
    with app.app_context():
        if cate == None:
            return News.query.all()
        return News.query.filter(News.image_url.__ne__('NULL') and News.category_id == int(cate)).all()
        # return News.query.all()

# for i in load_news():
#     print(i)
