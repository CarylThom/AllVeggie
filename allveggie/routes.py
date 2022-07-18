from functools import wraps
from flask import flash, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from allveggie import app, db
from allveggie.models import Category, Recipe, Users


# @login_required decorator
# https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/#login-required-decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # no "user" in session
        if "user" not in session:
            flash("You must log in to view this page")
            return redirect(url_for("login"))
        # user is in session
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def home():
    recipes = list(Recipe.query.order_by(Recipe.id).all())
    return render_template("recipes.html", recipes=recipes)


@app.route("/categories")
@login_required
def categories():
    if session["user"].lower() == "admin":
        categories = list(
            Category.query.order_by(Category.category_name).all())
        return render_template("categories.html", categories=categories)

    # user is not admin
    flash("You do not have access to this page!")
    return redirect(url_for("home"))


@app.route("/add_category", methods=["GET", "POST"])
@login_required
def add_category():
    if session["user"].lower() == "admin":
        if request.method == "POST":
            category = Category(
                category_name=request.form.get("category_name"))
            db.session.add(category)
            db.session.commit()
            return redirect(url_for("categories"))
        return render_template("add_category.html")

    # user is not admin
    flash("You do not have access to this page!")
    return redirect(url_for("home"))


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
@login_required
def edit_category(category_id):
    if session["user"].lower() == "admin":
        category = Category.query.get_or_404(category_id)
        if request.method == "POST":
            category.category_name = request.form.get("category_name")
            db.session.commit()
            return redirect(url_for("categories"))
        return render_template("edit_category.html", category=category)

    # user is not admin
    flash("You do not have access to this page!")
    return redirect(url_for("home"))


@app.route("/delete_category/<int:category_id>")
@login_required
def delete_category(category_id):
    if session["user"].lower() == "admin":
        category = Category.query.get_or_404(category_id)
        db.session.delete(category)
        db.session.commit()
        return redirect(url_for("categories"))

    # user is not admin
    flash("You do not have access to this page!")
    return redirect(url_for("home"))


@app.route("/add_recipe", methods=["GET", "POST"])
@login_required
def add_recipe():
    user_id = Users.query.filter(
            Users.user_name == session["user"].lower()).first().id
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        recipe = Recipe(
            recipe_name=request.form.get("recipe_name"),
            recipe_ingredients=request.form.get("recipe_ingredients"),
            recipe_method=request.form.get("recipe_method"),
            is_vegan=bool(True if request.form.get("is_vegan") else False),
            is_gf=bool(True if request.form.get("is_gf") else False),
            category_id=request.form.get("category_id"),
            recipe_author=user_id,
        )
        db.session.add(recipe)
        db.session.commit()
        flash("Recipe successfully added!")
        return redirect(url_for("home"))
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    user = Users.query.filter(
            Users.user_name == session["user"].lower()).first()
    if recipe.recipe_author == user.id:
        categories = list(
            Category.query.order_by(Category.category_name).all())
        if request.method == "POST":
            recipe.recipe_name = request.form.get("recipe_name")
            recipe.recipe_ingredients = request.form.get("recipe_ingredients")
            recipe.recipe_method = request.form.get("recipe_method")
            recipe.is_vegan = bool(
                True if request.form.get("is_vegan") else False)
            recipe.is_gf = bool(True if request.form.get("is_gf") else False)
            recipe.category_id = request.form.get("category_id")
            recipe.recipe_author = user.id

            db.session.commit()
            flash("Recipe successfully updated!")
        return render_template(
            "edit_recipe.html", recipe=recipe, categories=categories)

    # user is not recipe author
    flash("You do not have access to edit this recipe!")
    return redirect(url_for("home"))


@app.route("/delete_recipe/<int:recipe_id>")
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    user = Users.query.filter(
            Users.user_name == session["user"].lower()).first()
    if recipe.recipe_author == user.id:
        db.session.delete(recipe)
        db.session.commit()
        flash("Recipe successfully deleted!")
        return redirect(url_for("home"))

    # user is not recipe author
    flash("You do not have access to delete this recipe!")
    return redirect(url_for("home"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in the database
        existing_user = Users.query.filter(
            Users.user_name == request.form.get("username").lower()).first()

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        user = Users(
            user_name=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
        )

        db.session.add(user)
        db.session.commit()

        # put the new user into session cookie
        session["user"] = request.form.get("username").lower()
        session["user_id"] = user.id
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = Users.query.filter(
            Users.user_name == request.form.get("username").lower()).first()

        if existing_user:
            print(request.form.get("username"))
            # make sure password matches input
            if check_password_hash(
                    existing_user.password, request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                session["user_id"] = existing_user.id
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # password does not match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    recipes = list(Recipe.query.filter(
        Recipe.recipe_author == session["user_id"]).all())
    return render_template(
        "profile.html", username=session["user"], recipes=recipes)


@app.route("/logout")
@login_required
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.clear()
    return redirect(url_for("login"))
