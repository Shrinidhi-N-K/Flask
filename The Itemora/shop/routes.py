from flask import flash,Blueprint,request, redirect, url_for, render_template
from flask_login import login_user, logout_user, login_required, current_user

from shop import db
from shop.models import Item, User
from shop.views import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home_page():
    return render_template('home.html')


@main.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()
    if request.method == 'POST':
        #Purchase logic
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first()

        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f'Successfully Purchased {p_item_object.name} for {p_item_object.price}$', category='success')
            else:
                flash("Insufficient balance.", category='danger')

        #Sell logic
        sold_item = request.form.get('sold_item')
        s_item_object = Item.query.filter_by(name=sold_item).first()

        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"successfully sold {s_item_object.name}!", category='success')
            else:
                flash(f"Couldn't Sell Item {s_item_object.name} Try Again!.", category='danger')

        # Redirect to avoid form resubmission on refresh
        return redirect(url_for('main.market_page'))


    items = Item.query.filter_by(owner=None).all()
    owned_items = Item.query.filter_by(owner=current_user.id).all()
    return render_template('market.html', items=items, purchase_form=purchase_form, owned_items=owned_items, selling_form=selling_form)


@main.route('/register', methods=['GET', 'POST'])
def register_page():

    form = RegisterForm()

    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash("Registered and Logged in Successfully!", category='success')
        return redirect(url_for('main.market_page'))

    if form.errors != {}:
        for field_errors in form.errors.values():
            for err in field_errors:
                flash(f'Error: {err}', category='danger')

    return  render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(form.password.data):
            login_user(attempted_user)
            flash(f'Login Successful! Logged in as {attempted_user.username}', category='success')
            return redirect(url_for('main.market_page'))
        else:
            flash('Login Failed!', category='danger')

    if form.errors != {}:
        for field_errors in form.errors.values():
            for err in field_errors:
                flash(f'Error: {err}', category='danger')
    return render_template('login.html', form=form)


@main.route('/logout')
def logout_page():
    logout_user()
    flash('Logged out successfully!', category='info')
    return redirect(url_for('main.home_page'))