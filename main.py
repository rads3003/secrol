from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

DB_PATH = 'secrol.db'

def get_db():
    return sqlite3.connect(DB_PATH)

def create_tables():
    with get_db() as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS instalaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS guardias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT,
            instalacion_id INTEGER,
            tipo_turno TEXT,
            fecha_inicio TEXT,
            FOREIGN KEY (instalacion_id) REFERENCES instalaciones(id)
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS eventos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            guardia_id INTEGER,
            tipo_evento TEXT,
            desde_fecha TEXT,
            hasta_fecha TEXT,
            FOREIGN KEY (guardia_id) REFERENCES guardias(id)
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            accion TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.commit()

create_tables()

@app.route('/')
def home():
    with get_db() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM instalaciones')
        instalaciones = c.fetchall()
        c.execute('SELECT * FROM guardias')
        guardias = c.fetchall()
    return render_template("index.html", instalaciones=instalaciones, guardias=guardias)

@app.route('/add_instalacion', methods=['POST'])
def add_instalacion():
    nombre = request.form['nombre']
    with get_db() as conn:
        c = conn.cursor()
        c.execute('INSERT INTO instalaciones (nombre) VALUES (?)', (nombre,))
        c.execute('INSERT INTO logs (accion) VALUES (?)', (f"Agregada instalación: {nombre}",))
        conn.commit()
    return redirect('/')

@app.route('/add_guardia', methods=['POST'])
def add_guardia():
    nombre = request.form['nombre']
    telefono = request.form.get('telefono')
    instalacion_id = request.form.get('instalacion_id') or None
    tipo_turno = request.form.get('tipo_turno')
    fecha_inicio = request.form.get('fecha_inicio')
    with get_db() as conn:
        c = conn.cursor()
        c.execute('''
            INSERT INTO guardias (nombre, telefono, instalacion_id, tipo_turno, fecha_inicio)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, telefono, instalacion_id, tipo_turno, fecha_inicio))
        c.execute('INSERT INTO logs (accion) VALUES (?)', (f"Agregado guardia: {nombre}",))
        conn.commit()
    return redirect('/')

@app.route('/add_evento', methods=['POST'])
def add_evento():
    guardia_id = request.form.get('guardia_id')
    tipo_evento = request.form.get('tipo_evento')
    desde_fecha = request.form.get('desde_fecha')
    hasta_fecha = request.form.get('hasta_fecha')
    with get_db() as conn:
        c = conn.cursor()
        c.execute('''
            INSERT INTO eventos (guardia_id, tipo_evento, desde_fecha, hasta_fecha)
            VALUES (?, ?, ?, ?)
        ''', (guardia_id, tipo_evento, desde_fecha, hasta_fecha))
        c.execute('INSERT INTO logs (accion) VALUES (?)', (f"Agregado evento: {tipo_evento} para guardia id {guardia_id}",))
        conn.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
