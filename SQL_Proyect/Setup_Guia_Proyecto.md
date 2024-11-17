
# Guía de Configuración del Proyecto

## Prerrequisitos

Antes de comenzar, asegúrate de tener lo siguiente:

- **Python** instalado (versión 3.6 o superior).
- **PostgreSQL** instalado (versión 9.5 o superior).
- Acceso al código del proyecto, incluyendo los scripts SQL para crear e insertar tablas y datos.
- Archivo `requirements.txt` con las dependencias necesarias.

## Pasos de Configuración

### 1. Instalación de Python

#### **Mac:**

1. Verifica si Python ya está instalado:

   ```bash
   python3 --version
   ```

2. Si no está instalado, descárgalo desde la [página oficial de Python](https://www.python.org/downloads/macos/).

#### **Windows:**

1. Verifica si Python ya está instalado:

   ```cmd
   python --version
   ```

2. Si no está instalado, descárgalo desde la [página oficial de Python](https://www.python.org/downloads/windows/).
3. Durante la instalación, marca la opción **"Add Python to PATH"**.

### 2. Instalación de PostgreSQL

#### **Mac:**

1. Descarga PostgreSQL desde la [página oficial](https://www.postgresql.org/download/macosx/).
2. Sigue las instrucciones del instalador.
3. Anota el nombre de usuario y contraseña que configures.

#### **Windows:**

1. Descarga PostgreSQL desde la [página oficial](https://www.postgresql.org/download/windows/).
2. Sigue las instrucciones del instalador.
3. Anota el nombre de usuario y contraseña que configures.

### 3. Configuración de la Base de Datos

1. Inicia el servidor de PostgreSQL.
2. Abre la consola de comandos de PostgreSQL (psql) o utiliza una herramienta como **pgAdmin**.

#### **Usando psql:**

1. Conéctate al servidor:

   ```bash
   psql -U tu_usuario
   ```

2. Crea una nueva base de datos:

   ```sql
   CREATE DATABASE sistema_de_tours_de_vinas;
   ```

3. Conéctate a la nueva base de datos:

   ```sql
   \c sistema_de_tours_de_vinas;
   ```

4. Ejecuta los scripts SQL proporcionados para crear tablas e insertar datos:

   ```bash
   \i sql/creacion_tablas.sql
   \i sql/populacion/populacion_tablas.sql
   \i sql/populacion/populacion_tablas2.sql
   ```

### 4. Creación del Entorno Virtual de Python

#### **Mac:**

1. Navega al directorio raíz de tu proyecto:

   ```bash
   cd SQL_proyect
   ```

2. Crea el entorno virtual:

   ```bash
   python3 -m venv env
   ```

3. Activa el entorno virtual:

   ```bash
   source env/bin/activate
   ```

#### **Windows:**

1. Navega al directorio raíz de tu proyecto:

   ```cmd
   cd SQL_proyect
   ```

2. Crea el entorno virtual:

   ```cmd
   python -m venv env
   ```

3. Activa el entorno virtual:

   ```cmd
   env\Scripts\activate
   ```

### 5. Instalación de Dependencias

Con el entorno virtual activado, instala las dependencias usando `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 6. Ejecución del Proyecto

Ejecuta el script principal de tu proyecto:

```bash
python main.py
```

---

## Notas Adicionales

- **Firewall y Puertos:** Asegúrate de que el puerto 5432 (o el que hayas configurado para PostgreSQL) esté abierto y accesible.
- **Comprobación de Servicios:** Verifica que el servicio de PostgreSQL esté en ejecución antes de iniciar el proyecto.
- **Entorno Virtual:** Recuerda activar el entorno virtual cada vez que inicies una nueva sesión de trabajo.

## Solución de Problemas Comunes

- **Error de Conexión a la Base de Datos:**
  - Verifica las credenciales en el archivo `/python/modules/db_connection.py`.
  - Asegúrate de que el servidor de PostgreSQL esté en ejecución.
- **Paquetes Faltantes:**
  - Ejecuta nuevamente `pip install -r requirements.txt` para instalar cualquier dependencia faltante.
