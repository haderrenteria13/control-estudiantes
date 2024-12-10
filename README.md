# Control de Estudiantes

![481_1x_shots_so](https://github.com/user-attachments/assets/2d187b2f-cef7-4d26-b890-ce589f578974)

Este proyecto es una aplicación web para gestionar estudiantes de primaria y secundaria. Permite agregar, editar, eliminar y listar estudiantes, así como buscar por nombre o apellido. Todo usando los conceptos de POO

## Requisitos

- Python 3.x
- Django 3.x
- Django REST framework

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/control-estudiantes-django.git
    cd control-estudiantes
    ```

2. Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```

5. Crea un superusuario para acceder al panel de administración:
    ```bash
    python manage.py createsuperuser
    ```

6. Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

## Uso

- Accede a la aplicación en `http://127.0.0.1:8000/`.
- Inicia sesión con el superusuario creado.
- Usa la barra de navegación para acceder a las secciones de estudiantes de primaria y secundaria.
- Usa los formularios para agregar, editar y eliminar estudiantes.

## API

La aplicación incluye una API REST para gestionar estudiantes. Los endpoints disponibles son:

- `GET /api/estudiantes-primaria/`: Lista de estudiantes de primaria.
- `GET /api/estudiantes-secundaria/`: Lista de estudiantes de secundaria.
- `POST /api/estudiantes-primaria/`: Crear un nuevo estudiante de primaria.
- `POST /api/estudiantes-secundaria/`: Crear un nuevo estudiante de secundaria.
- `PUT /api/estudiantes-primaria/{id}/`: Actualizar un estudiante de primaria.
- `PUT /api/estudiantes-secundaria/{id}/`: Actualizar un estudiante de secundaria.
- `DELETE /api/estudiantes-primaria/{id}/`: Eliminar un estudiante de primaria.
- `DELETE /api/estudiantes-secundaria/{id}/`: Eliminar un estudiante de secundaria.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request en GitHub.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
