from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from OpenNews import app, utils, login


@app.route('/')
def home():
    news = utils.load_news()
    categories = utils.load_categories()
    return render_template('index.html', news=news, cates=categories)
    # cates = utils.load_categories()
    # cate_id = request.args.get('category_id')
    # kw = request.args.get('keyword')
    # products = utils.load_products(cate_id=cate_id, kw=kw)
    # return render_template('index.html', categories=cates, products=products)

@app.route('/<int:cate_id>')
def news_cate(cate_id):
    cates = utils.load_news(cate_id)
    print(cates)
    return render_template('index.html', news=cates)
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    if request.method == 'POST':
        name = request.form.get('name')

        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        repassword = request.form.get('repassword')
        avatar = request.form.get('avatar')
        try:
            if password.strip() == repassword.strip():
                utils.add_user(name=name, username=username, password=password, email=email, avatar=avatar)
                return redirect(url_for('login'))
            else:
                error = "Passwords do not match"
        except Exception as e: error = 'He thong co lôi' + str(e)


    return render_template('register.html', error=error)

    # @app.route('/products')
    # def product_list():
    #     cate_id = request.args.get("category_id")
    #     kw = request.args.get("keyword")
    #     from_price = request.args.get("from_price")
    #     to_price = request.args.get("to_price")
    #
    #     products = utils.load_products(cate_id=cate_id, kw=kw, from_price=from_price, to_price=to_price)
    #     return render_template('products.html', products=products)
    #
    #
    # @app.route('/products/<int:product_id>')
    # def product_detail(product_id):
    #     product = utils.get_product_by_id(product_id)
    #     return render_template('product_detail.html', product=product)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        print(username, password)
        user = User.query.filter(User.username == username, User.password == password).first()
        if user:
            # login_user(user=user)
            # return render_template('index.html')
            return redirect("/")

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/dashboard')
# @login_required
def dashboard():
    return f'Chào mừng, {current_user.username}!'


if __name__ == '__main__':
    from OpenNews.admin import *

    app.run(debug=False)
