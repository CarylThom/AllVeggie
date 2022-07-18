from allveggie import db


class Users(db.Model):
    # users model
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(260), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.user_name


class Category(db.Model):
    # Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), unique=True, nullable=False)
    recipes = db.relationship(
        "Recipe", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Recipe(db.Model):
    #  Recipe model
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), unique=True, nullable=False)
    recipe_ingredients = db.Column(db.Text, nullable=False)
    recipe_method = db.Column(db.Text, nullable=False)
    is_vegan = db.Column(db.Boolean, default=False, nullable=False)
    is_gf = db.Column(db.Boolean, default=False, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        Category.id, ondelete="CASCADE"), nullable=False)
    recipe_author = db.Column(db.Integer, db.ForeignKey(
        Users.id, ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Recipe: {1} | Urgent: {2}".format(
            self._id, self.recipe_name, self.is_vegan
        )
