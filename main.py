from flask import Flask, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SecuritasRol Pro</title>
    <!-- Add any CSS styles here if needed -->
    <style>
        /* Basic styling for layout */
        body { font-family: Arial, sans-serif; }
        nav { background-color: #f0f0f0; padding: 10px; }
        section { margin: 20px; }
        .dashboard-stats { display: flex; justify-content: space-around; }
        .stat { text-align: center; border: 1px solid #ddd; padding: 10px; width: 20%; }
        form { margin-top: 20px; }
    </style>
</head>
<body>
    <header>
        <h1>SecuritasRol Pro</h1>
    </header>
    
    <nav>
        <ul>
            <li><a href="#dashboard">Dashboard</a></li>
            <li><a href="#consultas">Consultas</a></li>
            <li><a href="#gestiones">Gestiones</a></li>
        </ul>
    </nav>
    
    <section id="dashboard">
        <h2>Dashboard de Control</h2>
        <p>Monitoreo integral de turnos y asignaciones de seguridad</p>
        
        <div class="dashboard-stats">
            <div class="stat">
                <h3>0</h3>
                <p>Instalaciones</p>
            </div>
            <div class="stat">
                <h3>0</h3>
                <p>Guardias</p>
            </div>
            <div class="stat">
                <h3>0</h3>
                <p>En Servicio Hoy</p>
            </div>
            <div class="stat">
                <h3>0</h3>
                <p>Disponibles</p>
            </div>
        </div>
        
        <div>
            <h3>Resumen de Estado Actual</h3>
            <form>
                <label>Filtrar por Instalación:</label>
                <select>
                    <option>Todas</option>
                </select>
                
                <label>Filtrar por Estado:</label>
                <select>
                    <option>Todos</option>
                    <option>Trabajando</option>
                    <option>Libre</option>
                    <option>Turno Extra</option>
                    <option>Licencia Médica</option>
                    <option>Vacaciones</option>
                    <option>Inducción</option>
                    <option>Falta</option>
                    <option>Permiso con Goce</option>
                    <option>Permiso sin Goce</option>
                </select>
            </form>
        </div>
    </section>
    
    <section id="consultas">
        <h2>Centro de Consultas</h2>
        <p>Consulta proyecciones, horarios y estadísticas de guardias e instalaciones</p>
        
        <div>
            <h3>Consulta por Guardia</h3>
            <form>
                <label>Nombre del Guardia:</label>
                <input type="text">
                
                <label>Desde Fecha:</label>
                <input type="date">
                
                <label>Hasta Fecha:</label>
                <input type="date">
                
                <button type="submit">Consultar</button>
            </form>
        </div>
        
        <div>
            <h3>Consulta por Instalación</h3>
            <form>
                <label>Seleccionar Instalación:</label>
                <select></select>
                
                <label>Desde Fecha:</label>
                <input type="date">
                
                <label>Hasta Fecha:</label>
                <input type="date">
                
                <button type="submit">Consultar</button>
            </form>
        </div>
        
        <div>
            <h3>Estadísticas por Guardia</h3>
            <form>
                <label>Nombre del Guardia:</label>
                <input type="text">
                
                <label>Mes y Año:</label>
                <input type="month">
                
                <button type="submit">Consultar Estadísticas</button>
            </form>
        </div>
    </section>
    
    <section id="gestiones">
        <h2>Centro de Gestiones</h2>
        <p>Administra instalaciones, guardias y eventos</p>
        
        <div>
            <h3>Gestionar Instalaciones</h3>
            <form>
                <label>Nombre de la Instalación:</label>
                <input type="text">
                
                <button type="submit">Registrar Instalación</button>
            </form>
        </div>
        
        <div>
            <h3>Gestionar Guardias</h3>
            <form>
                <label>Nombre del Guardia:</label>
                <input type="text">
                
                <label>Número de Teléfono:</label>
                <input type="tel">
                
                <label>Instalación Asignada:</label>
                <select></select>
                
                <label>Tipo de Turno:</label>
                <select>
                    <option>4x4 (4 días servicio, 4 días libres)</option>
                    <option>6x1 (6 días servicio, 1 día libre)</option>
                    <option>7x7 (7 días servicio, 7 días libres)</option>
                    <option>5x2 (5 días servicio, 2 días libres)</option>
                </select>
                
                <label>Fecha de Inicio:</label>
                <input type="date">
                
                <button type="submit">Registrar Guardia</button>
            </form>
        </div>
        
        <div>
            <h3>Gestionar Eventos de Guardias</h3>
            <form>
                <label>Seleccionar Guardia:</label>
                <select></select>
                
                <label>Tipo de Evento:</label>
                <select>
                    <option>Seleccione...</option>
                    <option>Licencia Médica</option>
                    <option>Vacaciones</option>
                    <option>Falta</option>
                    <option>Inducción</option>
                    <option>Permiso con Goce</option>
                    <option>Permiso sin Goce</option>
                    <option>Turno Extra</option>
                </select>
                
                <label>Desde Fecha:</label>
                <input type="date">
                
                <label>Hasta Fecha:</label>
                <input type="date">
                
                <button type="submit">Registrar Evento</button>
            </form>
        </div>
        
        <div>
            <h3>Cambiar Rol de Guardia</h3>
            <form>
                <label>Seleccionar Guardia:</label>
                <select></select>
                
                <label>Nuevo Tipo de Turno:</label>
                <select>
                    <option>Seleccione...</option>
                    <option>4x4 (4 días servicio, 4 días libres)</option>
                    <option>6x1 (6 días servicio, 1 día libre)</option>
                    <option>7x7 (7 días servicio, 7 días libres)</option>
                    <option>5x2 (5 días servicio, 2 días libres)</option>
                </select>
                
                <label>Nueva Instalación (opcional):</label>
                <select>
                    <option>No cambiar</option>
                </select>
                
                <label>Fecha de Cambio:</label>
                <input type="date">
                
                <button type="submit">Cambiar Rol</button>
            </form>
        </div>
    </section>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)