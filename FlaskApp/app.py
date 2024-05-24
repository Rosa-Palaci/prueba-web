from flask import Flask, render_template, request, redirect, url_for
from models import db, Estudiante

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudiantes.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/LoginEstudiantes', methods=['GET', 'POST'])
def login_estudiante():
    if request.method == 'POST':
        # Aquí manejarías la autenticación
        pass
    return render_template('login_estudiantes.html')

@app.route('/LoginProfesores', methods=['GET', 'POST'])
def login_profesores():
    if request.method == 'POST':
        # Aquí manejarías la autenticación
        pass
    return render_template('login_profesores.html')

@app.route('/Registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Aquí capturas los datos del formulario
        nuevo_estudiante = Estudiante(
            numero_lista=request.form['numero_lista'],
            grupo=request.form['grupo'],
            genero=request.form['genero'],
            ciclo_escolar=request.form['ciclo_escolar']
        )
        db.session.add(nuevo_estudiante)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('registro.html')

@app.route('/Contexto')
def contexto():
    # Esta vista podría ser para mostrar información relevante
    return 'Información del contexto escolar aquí'

if __name__ == '__main__':
    db.create_all(app=app)
    app.run(debug=True)
