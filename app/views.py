from flask import Blueprint, render_template, url_for, redirect, request, flash
from models import db, Categories, Items
from sqlalchemy import and_
import re
from forms import ItemForm
from wtforms import ValidationError

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
    form = ItemForm()
    if request.method == 'GET':
        return render_template('items.html', form=form)
    if form.validate_on_submit():
        category = Categories.query.filter_by(uuid=form.category.data).first()
        item = Items(name=form.name.data, description=form.description.data)
        item.category = category
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('catalog.root'))
    else:
        errors = form.errors.items()
        for error in errors:
            message = "%(field)s - %(message)s" % ({
                'field': error[0],
                'message': error[1][0]
            })
            flash(message)
        return render_template('items.html', form=form)


@catalog_bp.route('/catalog/<string:category>/<string:item>/edit', methods=['GET', 'POST'])
def edit(category, item):
    category = Categories.query.filter_by(name=category).first_or_404()
    item = Items.query.filter(and_(Items.name.like(
        item)), (Items.category_id.like(category.uuid))).first_or_404()
    form = ItemForm()
    if request.method == 'GET':
        form.name.data = item.name
        form.description.data = item.description
        form.category.process_data(category.uuid)
        return render_template('items.html', form=form)

    if form.validate_on_submit():
        item.name = form.name.data
        item.description = form.description.data
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('catalog.root'))

    else:
        errors = form.errors.items()
        for error in errors:
            message = "%(field)s - %(message)s" % ({
                'field': error[0],
                'message': error[1][0]
            })
            flash(message)
        return render_template('items.html', form=form)


@catalog_bp.route('/catalog/<string:category>/<string:item>/delete', methods=['GET', 'POST'])
def delete(category, item):
    form = ItemForm()
    if request.method == 'POST':
        category = Categories.query.filter_by(name=category).first_or_404()
        item = Items.query.filter(and_(Items.name.like(
            item)), (Items.category_id.like(category.uuid))).first_or_404()
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('catalog.root'))
    return render_template('delete.html', form=form)
