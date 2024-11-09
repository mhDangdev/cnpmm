from app.models import Category
def load_categories():
    return Category.query.all()

def load_products():
    return
