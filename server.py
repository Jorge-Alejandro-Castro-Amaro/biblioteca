from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        'index.html',
        titulo='Inicio',
        mensaje='Te damos la bienvenida a la biblioteca de nuestra comunidad universitaria: un espacio abierto al conocimiento, la lectura y la investigación.'
    )

@app.route('/catalogo')
def catalogo():
    return render_template(
        'catalogo.html',
        titulo='Catálogo',
        mensaje='Encuentra recursos para tus cursos, proyectos de investigación y lectura personal.'
    )

@app.route('/servicios')
def servicios():
    return render_template(
        'servicios.html',
        titulo='Servicios',
        mensaje='Te acompañamos en cada etapa de tu aprendizaje con espacios, recursos y apoyo especializado.'
    )

@app.route('/contacto')
def contacto():
    return render_template(
        'contacto.html',
        titulo='Contacto',
        mensaje='Comunícate con nuestro equipo o visítanos durante el horario de atención. Con gusto te orientaremos.'
    )

if __name__ == '__main__':
    app.run(debug=True, port=5050)