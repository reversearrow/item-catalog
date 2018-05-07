from flask import Blueprint, render_template
from models import Categories, Items

catalog_bp = Blueprint('catalog', __name__)


@catalog_bp.route('/')
def root():
    categories = Categories.query.order_by('name').all()
    items = Items.query.order_by('created_at').all()
    return render_template('root.html', categories=categories, items=items)
