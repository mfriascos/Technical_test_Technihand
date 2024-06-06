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

- ## Funcionalidades
  
  **Gestión de Repositorios**
  - Crear y editar repositorios: Incluye campos como nombre, enlace, usuario responsable y estados (Borrador, Activo, Inactivo, Cancelado).
    ![image](https://github.com/mfriascos/Technical_test_Technihand/assets/90413990/98fff20f-0e6e-4942-9701-6164be0f7703)

  - Visualizar commits: Se muestra una lista de commits asociados a cada repositorio.
  - Acceso rápido al último commit: Botón en la vista de lista que redirige al último commit en GitHub.

  **Visualización en res.partner**
  - Pestaña adicional: En el modelo res.partner, se agrega una pestaña llamada "Code Repositories" donde se listan los repositorios asociados al cliente.

  **Reportes**
  - Informe en PDF: Generar un reporte PDF con los detalles de los commits (fecha, responsable, mensaje).

  **Seguridad**
  - Permisos diferenciados:
  - Administradores: Pueden editar y generar reportes.
  - Usuarios: Solo tienen permisos de visualización.
  

