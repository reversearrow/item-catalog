from flask import Blueprint, render_template, url_for, redirect, request
from models import db, Categories, Items
from sqlalchemy import and_
import re


catalog_bp = Blueprint('catalog', __name__)


@catalog_bp.route('/catalog/<string:category>/<string:item>')
@catalog_bp.route('/catalog/<string:category>/items')
@catalog_bp.route('/')
def root(category='default', item='default'):
    categories = Categories.query.order_by('name').all()
    if category == 'default':
        items = Items.query.order_by('created_at').all()
        return render_template('root.html', categories=categories, category='Latest', items=items)
    else:
        category = Categories.query.filter_by(name=category).first_or_404()
        if item == 'default':
            return render_template('root.html', categories=categories, category=category.name, items=category.items)
        else:
            item = Items.query.filter(and_(Items.name.like(
                item)), (Items.category_id.like(category.uuid))).first_or_404()
            return render_template('item_details.html', item=item)


@catalog_bp.route('/catalog/add', methods=['GET', 'POST'])
def add():
    categories = Categories.query.order_by('name').all()
    if request.method == 'POST':
        name = request.form.get('title')
        description = request.form.get('description')
        category = request.form.get('categories')
        match_empty_regex = r' +'
        if re.match(match_empty_regex, name) or name == "":
            return render_template('items.html', title=name, description=description, categories=categories, error="Title is not valid!")
        if re.match(match_empty_regex, description) or description == "":
            return render_template('items.html', title=name, description=description, categories=categories, error="Description is not valid!")
        else:
            category = Categories.query.filter_by(name=category).first()
            new_item = Items(name=name, description=description)
            new_item.category = category
            db.session.add(new_item)
            db.session.commit()
            return redirect(url_for('catalog.root'))
    return render_template('items.html', categories=categories)
