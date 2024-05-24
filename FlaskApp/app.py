from flask import Flask, g, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
DATABASE = 'estudiantes.sqlite3'

def init_db():
    db = get_db()
    with app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    db.commit()

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/LoginEstudiantes', methods=['GET', 'POST'])
def login_estudiante():
    if request.method == 'POST':
        db = get_db()
        numero_lista = request.form['numero_lista']
        estudiante = db.execute('SELECT * FROM estudiante WHERE numero_lista = ?', (numero_lista,)).fetchone()
        if estudiante:
            session['estudiante_id'] = estudiante['idEstudiante']
            return redirect(url_for('home'))
        else:
            flash('Número de lista no encontrado.')
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
        db = get_db()
        try:
            db.execute('INSERT INTO estudiante (numero_lista, grupo, genero, ciclo_escolar) VALUES (?, ?, ?, ?)',
                       (request.form['numero_lista'], request.form['grupo'], request.form['genero'], request.form['ciclo_escolar']))
            db.commit()
            return redirect(url_for('login_estudiantes'))
        except sqlite3.IntegrityError:
            return 'Error: El estudiante ya está registrado.'
    return render_template('registro.html')

@app.route('/Contexto')
def contexto():
    return render_template('contexto.html')

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)
