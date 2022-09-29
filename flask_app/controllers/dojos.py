from flask_app.models.dojo import Dojo
from flask_app import app
from flask import redirect, render_template, request


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template('crear_dojo.html', dojo=Dojo.get_all())

@app.route('/dojos/crear', methods=['POST'])
def crear_dojos():
    print(request.form)
    dojo_id = Dojo.save(request.form)

    return redirect(f'/dojos/{dojo_id}')

@app.route('/dojos/<int:id>')
def mostrar_dojos(id):

    data = { 
        "id":id
    }

    return render_template('dojos.html', dojo=Dojo.get_dojos_with_ninjas(data))
