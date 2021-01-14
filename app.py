import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_projects")
def get_projects():
    projects = list(mongo.db.projects.find())
    return render_template("projects.html", projects=projects)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "full_name": request.form.get("full_name"),
            "email_address": request.form.get("email_address"),
            "source_languages": request.form.get("source_languages"),
            "target_language": request.form.get("target_language"),
            "billing_info": request.form.get("billing_info"),
            "paypal_account": request.form.get("paypal_account"),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
            
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("add_linguist.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if session["user"]:
        # grab the session linguist's details from db
        linguist = mongo.db.users.find_one(
            {"username": session["user"]})
        return render_template("profile.html", linguist=linguist)

    # no session user, redirect to login page
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_project", methods=["GET", "POST"])
def add_project(): 
    if request.method == "POST":
        project_is_overdue = "on" if request.form.get("project_is_overdue") else "off"
        project = {
            "project_name": request.form.get("project_name"),
            "category_name": request.form.get("category_name"),
            "project_lead": request.form.get("project_lead"),
            "assigned_to": request.form.get("username"),
            "project_description": request.form.get("project_description"),
            "project_languages": request.form.get("project_languages"),
            "project_specialization": request.form.get("project_specialization"),
            "project_software": request.form.get("project_software"),
            "project_due_date": request.form.get("project_due_date"),
            "project_status": request.form.get("project_status"),
            "project_is_overdue": project_is_overdue,
            "created_by": session["user"]

        }
        mongo.db.projects.insert_one(project)
        flash("Project Successfully Created")
        return redirect(url_for("get_projects"))

    categories = mongo.db.categories.find().sort("category_name", 1)  # find all project categories
    leads = mongo.db.leads.find().sort("project_lead", 1) # find all project leads
    users = mongo.db.users.find().sort("username", 1) # find all project linguists
    status = mongo.db.status.find().sort("project_status", 1) # find all project status
    return render_template("add_project.html", categories=categories, users=users, leads=leads, status=status)

@app.route("/edit_project/<project_id>", methods=["GET", "POST"])
def edit_project(project_id):
    if request.method == "POST":
        project_is_overdue = "on" if request.form.get("project_is_overdue") else "off"
        submit = {
            "project_name": request.form.get("project_name"),
            "category_name": request.form.get("category_name"),
            "project_lead": request.form.get("project_lead"),
            "assigned_to": request.form.get("username"),
            "project_description": request.form.get("project_description"),
            "project_languages": request.form.get("project_languages"),
            "project_specialization": request.form.get("project_specialization"),
            "project_software": request.form.get("project_software"),
            "project_due_date": request.form.get("project_due_date"),
            "project_status": request.form.get("project_status"),
            "project_is_overdue": project_is_overdue,
            "created_by": session["user"]

        }
        mongo.db.projects.update({"_id": ObjectId(project_id)}, submit)
        flash("Project Successfully Updated")
    

    project = mongo.db.projects.find_one({"_id": ObjectId(project_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    leads = mongo.db.leads.find().sort("project_lead", 1) # find all project leads
    users = mongo.db.users.find().sort("username", 1) # find all project linguists
    status = mongo.db.status.find().sort("project_status", 1) # find all project status
    return render_template("edit_project.html", project=project, categories=categories, users=users, leads=leads, status=status)

@app.route("/delete_project/<project_id>")
def delete_project(project_id):
    mongo.db.projects.remove({"_id": ObjectId(project_id)})
    flash("Project Successfully Deleted")
    return redirect(url_for("get_projects"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
