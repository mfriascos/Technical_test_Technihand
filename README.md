# Technical_test_Technihand
## Prueba Técnica: Gestión de Repositorios de Código Fuente en Odoo 


El módulo Technical_test_technihand está pensado para registrar y gestionar información de repositorios de clientes. Este módulo se desarrollo con el fin de mantener información revelante de la gestión de repositorios como lo es su enlace, hash, commits realizados, fecha de estos commits, el desarrollo se realizó en odoo v16 

**Tabla de Contenido**

- [Instalación](##Instalación)
- [Funcionalidades](#Funcionalidaes)


- ## Instalación

  **Clonar el repositorio del módulo**
  ```bash
  git clone https://github.com/mfriascos/Technical_test_Technihand.git
  ```

  **Mover el módulo al directorio de addons de odoo**
  ```bash
  mv code_repository_management ruta/ddons/
  ```
  **Actualizar la lista de módulos:**

  Iniciar sesión en Odoo como administrador, ir a Aplicaciones, y hacer clic en Actualizar Lista.

  **Instalar el módulo:**

  Buscar Code Repository Management en la lista de aplicaciones y hacer clic en Instalar.

  **Otorgar Permisos**

  Para visualizar el módulo por favor ingrese a ajustes usuarios y grupoos y asigne un grupo, el cual puede ser adminisitrador de repositorios o usuario de repositorio. 

- ## Funcionalidades
  
  **Gestión de Repositorios**
  - Crear y editar repositorios: Incluye campos como nombre, enlace, usuario responsable y estados (Borrador, Activo, Inactivo, Cancelado).
    ![image](https://github.com/mfriascos/Technical_test_Technihand/assets/90413990/98fff20f-0e6e-4942-9701-6164be0f7703)

  - Visualizar commits: Se muestra una lista de commits asociados a cada repositorio
    ![image](https://github.com/mfriascos/Technical_test_Technihand/assets/90413990/94005d0d-7f30-45f8-9395-ea2d05121461)

  - Inclusión de funcionalidades para menejo de estados: Se incluyen botones para manejra los estados, iniciando de la siguiente forma, en borrador cuando se crea el commit, luego existe un botón llamado activar, que indica que el repositorio está activo, cuando se encuentra en activo hay un botón llamado desactivar para indicar que el repositorio está inactivo y finalmente el botón de cancelar para cancelar un repositorio.
    
    ![image](https://github.com/mfriascos/Technical_test_Technihand/assets/90413990/de270042-24d6-4fca-aeb2-77a48fa7d73c)

  En la vista tree, estos estados tienen colores diferentes para indicar su estado
  
  **Borrador**
  ![image](https://github.com/mfriascos/Technical_test_Technihand/assets/90413990/a8019556-774c-4806-a62c-796ea69fa31e)
  **Activo**
  ![image](https://github.com/mfriascos/Technical_test_Technihand/assets/90413990/553e27cf-9bc3-4059-899e-0208f32a2d1f)
  **Inactivo**
  ![image](https://github.com/mfriascos/Technical_test_Technihand/assets/90413990/1424b2c1-99c3-489e-bd6d-a0802c3f7b70)
  **Cancelado**
  ![image](https://github.com/mfriascos/Technical_test_Technihand/assets/90413990/64fba12e-1d44-43cc-abb9-fcb0c1030666)
  
  - Acceso rápido al último commit: Botón en la vista de lista que redirige al último commit en GitHub.
  ![image](https://github.com/mfriascos/Technical_test_Technihand/assets/90413990/d17080bc-47a6-4367-a3d0-a0ad2f309134)
  ![Odoo - Repositorios - Personal_ Microsoft_ Edge 2024-06-06 09-11-49](https://github.com/mfriascos/Technical_test_Technihand/assets/90413990/3fa1d9f7-7751-42dd-9129-8750f46b190c)

  
  **Visualización en res.partner**
  - Pestaña adicional: En el modelo res.partner, se agrega una pestaña llamada "Code Repositories" donde se listan los repositorios asociados al cliente.
  ![image](https://github.com/mfriascos/Technical_test_Technihand/assets/90413990/6e681448-60f6-4487-b82b-8c780e95fce3)
  ![image](https://github.com/mfriascos/Technical_test_Technihand/assets/90413990/c118611f-337d-4ba8-9b13-99d63969210f)

  **Reportes**
  - Informe en PDF: Generar un reporte PDF con los detalles de los commits (fecha, responsable, mensaje).
  ![image](https://github.com/mfriascos/Technical_test_Technihand/assets/90413990/021b4da1-1879-4234-ab4a-33e028ee2988)
  ![image](https://github.com/mfriascos/Technical_test_Technihand/assets/90413990/3d65c12d-d032-4110-b97f-171de32a1bfb)


  **Seguridad**
  - Permisos diferenciados:
  - Administradores: Pueden editar y generar reportes.
  - Usuarios: Solo tienen permisos de visualización.
  ![image](https://github.com/mfriascos/Technical_test_Technihand/assets/90413990/f995d47c-4f43-41f0-ac83-ddbf92943819)

- ## Uso
  
  **Crear un nuevo repositorio**
  
  Ir al menú Repositorios y hacer clic en Crear.
  
  Llenar los campos necesarios y guardar el registro.
  
  Agregar commits manualmente.
  
  **Visualizar repositorios en res.partner**

  Ir al menú Contactos y seleccionar un contacto.
  
  Navegar a la pestaña Code Repositories para ver los repositorios asociados.

  **Generar reporte PDF**

  Seleccionar un repositorio.

  Hacer clic en el botón Imprimir y seleccionar Commits Report.
  

