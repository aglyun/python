from flask import Blueprint, render_template


users_dp = Blueprint("users", __name__, template_folder='users/templates')


@users_dp.route("/register")
def register():
    return render_template('index.html')