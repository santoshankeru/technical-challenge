from flask import Flask, render_template, redirect, flash, url_for, session, request, logging
from data import Products, GiftLinks, UserAuthentication, AddGiftLinks, GetLink, UpdateLink, GetLinkProducts, UpdatePurchase
import secrets
from datetime import datetime
from functools import wraps


Products = Products()
GiftLink = GiftLinks()
UserData = UserAuthentication()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password = request.form['password']

        for item in UserData :
            if item['uid'] == username and item['pwd'] == password :
                # Passed
                session['logged_in'] = True
                session['username'] = username
                flash('You are now logged in', 'success')
                return redirect(url_for('home'))

    return render_template('index.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('index'))
    return wrap

@app.route('/products')
def products():
    return render_template('products.html', products=Products)

@app.route('/home')
def home():
    GiftLink = GiftLinks()
    return render_template('home.html', gl=GiftLink)

@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('index'))



@app.route('/create_link', methods=['GET', 'POST'])
@is_logged_in
def addlink():
    if request.method == 'POST':
        # Get Form Fields
        link_id = request.form['link_id']
        valid_to = request.form['link_valid_to']
        selected_items = request.form.getlist("items_list")
        
        temp_dict = {}
        temp_dict['link_id'] = link_id
        temp_dict['author'] = session['username']
        temp_dict['create_date'] = datetime.today().strftime('%Y-%m-%d')
        temp_dict['valid_till'] = valid_to
        temp_dict['share_url'] = url_for('gift_link', id=link_id,_external=True)
        temp_dict['status'] = 'active'
        temp_dict['products'] = selected_items
        temp_dict['purchases'] = []

        GiftLink.append(temp_dict)

        if AddGiftLinks(GiftLink):
            return redirect(url_for('home'))
    else :
        return render_template('create_link.html', products=Products, lID = secrets.token_hex(15))

@app.route('/edit_list/<string:id>', methods=['GET', 'POST'])
def edit_list(id) :
    if request.method == 'POST':
        # Get Form Fields
        temp_dict = {}
        temp_dict['link_id'] = request.form['link_id']
        temp_dict['valid_till'] = request.form['link_valid_to']
        temp_dict['products'] = request.form.getlist("items_list")

        if UpdateLink(temp_dict) :
            return redirect(url_for('home'))
    else:
        return render_template('edit_list.html', prd_data=GetLink(id))

@app.route('/gift_link/<string:id>', methods=['GET', 'POST'])
def gift_link(id) :
    if request.method == 'POST':
        UpdatePurchase(request.form['gift_now'])

    return render_template('gift_link.html', prd_data = GetLinkProducts(id))

if __name__ == '__main__' :
    app.secret_key='secret123'
    app.run(debug=True)