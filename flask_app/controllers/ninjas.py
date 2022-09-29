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
    id_ninja = Ninja.save(request.form)

    data = {
        "id_ninja":id_ninja
    }
    
    resultado = Ninja.get_un_ninja(data)
    print(resultado, "SI TODO ESTA BIEN")
    return redirect(f'/dojos/{resultado["dojo_id"]}')

# @app.route('/dojos/tabla')
# def mostrar_ninjas_en_dojos():

#     return render_template("dojos.html",dojo=Dojo.get_all())
