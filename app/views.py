from flask import Blueprint, render_template, url_for, redirect, request
from models import db, Categories, Items

catalog_bp = Blueprint('catalog', __name__)


@catalog_bp.route('/')
def root():
    categories = Categories.query.order_by('name').all()
    items = Items.query.order_by('created_at').all()
    return render_template('root.html', categories=categories, items=items)


@catalog_bp.route('/catalog/<string:category>/items')
def display_category_items(category):
    categories = Categories.query.order_by('name').all()
    category = Categories.query.filter_by(name=category).first()
    print category.items
    return "category"


@catalog_bp.route('/catalog/add', methods=['GET', 'POST'])
def add():
    categories = Categories.query.order_by('name').all()
    if request.method == 'POST':
        name = request.form.get('title').replace(" ", "")
        description = request.form.get('description').replace(" ", "")
        category = request.form.get('categories')
        print category
        if not name or name == "":
            return render_template('items.html', title=name, categories=categories, error="Title is not valid!")
        if not description or description == "":
            return render_template('items.html', description=description, categories=categories, error="Description is not valid!")
        else:
            category = Categories.query.filter_by(name=category).first()
            new_item = Items(name=name, description=description)
            new_item.category = category
            db.session.add(new_item)
            db.session.commit()
            return redirect(url_for('catalog.root'))
    return render_template('items.html', categories=categories)
