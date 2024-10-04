
# Ejecución del Proyecto

**Requisitos previos:**
- Asegúrate de tener instalados **Python** y **pip**.
- Si el comando `python` no funciona en tu sistema, utiliza `python3`.

## Pasos para ejecutar el proyecto

1. **Instalar las dependencias:**
   Ejecuta el siguiente comando para instalar las dependencias del proyecto desde el archivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

2. **Aplicar las migraciones:**
   Antes de ejecutar el servidor, aplica las migraciones necesarias para configurar la base de datos:
   ```bash
   python manage.py migrate
   python manage.py makemigrations
   ```

3. **Iniciar el servidor:**
   Ejecuta el siguiente comando para iniciar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

4. **Acceso a la API:**
   Una vez iniciado el servidor, puedes acceder a la API de productos a través de las siguientes rutas:
   - **Listado y creación de productos:** Dirígete a `http://localhost:8000/api/products` para ver el listado de productos o crear uno nuevo.
   - **Ver/Actualizar/Eliminar un producto específico:** Para interactuar con un producto específico, usa la ruta `http://localhost:8000/api/products/:id`, reemplazando `:id` con el identificador del producto correspondiente.

---

# Proceso de Aprendizaje

1. **Configurar el entorno de desarrollo:**
   Como parte del aprendizaje inicial, se configuró el entorno de desarrollo utilizando **virtualenv** para aislar las dependencias del proyecto.

2. **Seguimiento de un tutorial CRUD:**
   Se siguió un tutorial en línea para aprender a implementar operaciones CRUD en Django. Tras completar el tutorial, se replicó el conocimiento adquirido en este proyecto.

## Recursos utilizados:
- [Video Tutorial CRUD en Django](https://www.youtube.com/watch?v=Xts8NmyAc8c)
- **ChatGPT**: Se utilizó para obtener explicaciones sobre conceptos fundamentales de Django, como **Serializers** y **ViewSets**.
- **StackOverflow**: Ayudó a resolver errores relacionados con la instalación y compatibilidad de dependencias.

---

## Desafíos Encontrados

- **Familiarización con el entorno Python:**
   Como era mi primera vez trabajando con el entorno Python/Django, tuve dificultades al principio con la instalación de los paquetes y la gestión de dependencias.

---

## Explicación de Elecciones

- **Uso de la estructura predeterminada de Django:**
   Decidí mantener la estructura base generada por Django para este proyecto, dado que tengo poca experiencia con el framework y preferí evitar cambios innecesarios.

- **Uso de ModelViewSet:**
   Opté por utilizar `ModelViewSet` ya que era la opción más adecuada para implementar un CRUD sencillo, como lo solicitaba la prueba técnica.

- **Organización del proyecto:**
   Reorganicé los archivos dentro de la carpeta **api**, creando subcarpetas específicas para `models`, `serializers`, y `views` para mantener una estructura de código más limpia y modular, evitando que la carpeta **api** estuviera sobrecargada de archivos.