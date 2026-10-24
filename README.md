# Biblioteca Universitaria Central

Sitio web informativo para una biblioteca universitaria, creado con **Flask** y plantillas **Jinja**. Incluye páginas de inicio, catálogo, servicios y contacto con navegación compartida.

## Estructura del proyecto

- `server.py`: punto de entrada de la aplicación Flask; define las rutas y renderiza las plantillas.
- `templates/layout.html`: plantilla base con la estructura HTML, Bootstrap, título dinámico, navegación y el bloque `content`.
- `templates/index.html`: bienvenida, propósito de la biblioteca y horario general.
- `templates/catalogo.html`: categorías de materiales disponibles: libros, revistas, tesis y recursos digitales.
- `templates/servicios.html`: descripción de los servicios de la biblioteca.
- `templates/contacto.html`: dirección, correo electrónico y horario de atención.

## Elementos implementados

### Rutas de Flask

La aplicación define cuatro rutas. Cada función envía las variables `titulo` y `mensaje` a su plantilla mediante `render_template()`:

| Página | Ruta | Plantilla |
| --- | --- | --- |
| Inicio | `/` | `index.html` |
| Catálogo | `/catalogo` | `catalogo.html` |
| Servicios | `/servicios` | `servicios.html` |
| Contacto | `/contacto` | `contacto.html` |

### Plantilla base y navegación

Las cuatro páginas extienden `layout.html` con `{% extends "layout.html" %}` y colocan su contenido dentro de `{% block content %}`. La plantilla base proporciona:

- Estructura HTML compartida y título del documento basado en `titulo`.
- Hoja de estilos de Bootstrap 5.
- Barra de navegación horizontal con el nombre de la biblioteca y enlaces a las cuatro páginas.
- Enlaces generados con `url_for()` para usar los endpoints de Flask.
- Contenedor `container-fluid` para organizar el contenido.

### Contenido de las páginas

- **Inicio:** mensaje de bienvenida, propósito de la biblioteca y horario de atención.
- **Catálogo:** introducción y breve descripción de libros, revistas, tesis y recursos digitales.
- **Servicios:** préstamo de libros, consulta en sala, acceso a recursos digitales y orientación bibliográfica.
- **Contacto:** dirección, correo institucional ficticio y horario de atención.

## Requisitos

- Python 3
- Dependencias de Flask indicadas en `requirements.txt`

## Ejecución

Sigue estos pasos en Windows para iniciar el sitio por primera vez:

1. Abre la carpeta del proyecto en **Visual Studio Code** y selecciona **Terminal > New Terminal**. La terminal se abrirá en la carpeta del proyecto; comprueba que allí aparecen `server.py` y `requirements.txt`.

2. Si todavía no existe la carpeta `.venv`, crea un entorno virtual para instalar las dependencias sin afectar otros proyectos:

   ```powershell
   py -m venv .venv
   ```

3. Activa el entorno virtual e instala Flask y las demás dependencias del proyecto:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   ```

4. Inicia el servidor:

   ```powershell
   python server.py
   ```

5. Cuando PowerShell indique que el servidor está ejecutándose, abre **http://127.0.0.1:5050/** en tu navegador. Desde la barra de navegación puedes entrar al catálogo, los servicios y la página de contacto.

Para detener el servidor, vuelve a PowerShell y presiona **Ctrl+C**. La próxima vez que quieras ejecutar el sitio, abre PowerShell en la carpeta del proyecto, activa `.venv` y ejecuta `python server.py`; no hace falta crear de nuevo el entorno virtual.