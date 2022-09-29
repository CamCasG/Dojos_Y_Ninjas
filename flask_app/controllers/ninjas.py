from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app import app
from flask import redirect, render_template, request


@app.route('/ninjas')
def ninjas():
    return render_template("crear_ninja.html",dojo=Dojo.get_all())

@app.route('/ninjas/crear', methods=['POST'])
def crear_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/ninjas')
