**Prettyconf** es un paquete de Python diseñado para facilitar la gestión de variables de configuración en tus proyectos. Vamos a desglosarlo paso a paso para que lo entiendas mejor.

### ¿Para qué sirve Prettyconf?

Imagina que tienes información sensible o variables de configuración en tu proyecto, como contraseñas, claves API, o configuraciones del sistema, y no quieres que esas variables queden registradas en tu control de versiones (por ejemplo, en Git). **Prettyconf** te ayuda a manejar esos valores de manera segura y flexible. Puedes guardarlos en archivos que no subas al repositorio o en las variables de entorno de tu sistema.

### **Cómo funciona**

1. **Instalación:**
   Primero, debes instalar el paquete **prettyconf** en tu proyecto. Para ello, usas el siguiente comando:

   ```bash
   pip install prettyconf
   ```

2. **Uso básico:**

   Luego, en tu archivo de configuración (como `settings.py` en Django), puedes usar **prettyconf** para cargar las variables de configuración de una manera más sencilla. Así, no tendrás que escribir manualmente valores directamente en tu código.

   **Ejemplo de uso básico:**
   ```python
   from prettyconf import config

   PASSWD = config('PASSWORD')  # Recupera el valor de 'PASSWORD' desde una variable de entorno o archivo .env
   ```

   Con la línea anterior, **prettyconf** buscará el valor de la variable `PASSWORD`. Primero mirará en las variables de entorno del sistema y, si no la encuentra allí, buscará en un archivo `.env`.

3. **Archivos `.env`:**

   En vez de escribir las variables directamente en el código, puedes crear un archivo llamado `.env` en tu proyecto. Este archivo contendrá todas las configuraciones necesarias para tu proyecto, como credenciales, configuraciones específicas del entorno, etc.

   **Ejemplo de archivo `.env`:**
   ```plaintext
   USERNAME="thisisme"
   PASSWORD="verycomplicated"
   MESSAGE="Talk is cheap, show me the code"
   ```

   El archivo `.env` contiene las variables de configuración de manera que **prettyconf** pueda leerlas de forma segura.

4. **Evitar subir el archivo `.env` a Git:**

   Es muy importante que no subas tu archivo `.env` al repositorio de Git, ya que puede contener información sensible. Para asegurarte de que no lo subes, añádelo a tu archivo `.gitignore`, que es un archivo especial que indica a Git qué archivos no deben ser versionados.

   Ejemplo de **.gitignore**:
   ```plaintext
   .env
   ```

5. **Conversiones:**

   Por defecto, **prettyconf** lee las variables de configuración como cadenas de texto (`str`). Sin embargo, puedes usar conversiones para transformar esos valores en otros tipos de datos, como booleanos, listas, tuplas, etc.

   **Ejemplos de conversiones:**

   - **Booleano:**
     Si en tu archivo `.env` tienes algo como:
     ```plaintext
     FEATURE_ENABLED="On"
     ```
     Puedes usar `config` con la conversión `config.boolean` para que ese valor se convierta en un valor booleano (`True` o `False`):

     ```python
     FEATURE_ENABLED = config('FEATURE_ENABLED', cast=config.boolean)
     ```

   - **Lista:**
     Si tienes una lista de valores separados por comas:
     ```plaintext
     ITEMS="apple,banana,orange"
     ```
     Puedes convertirlo en una lista en Python usando `config.list`:
     ```python
     ITEMS = config('ITEMS', cast=config.list)
     # Resultado: ['apple', 'banana', 'orange']
     ```

   - **Tupla:**
     Si tienes una tupla de valores separados por comas:
     ```plaintext
     COORDINATES="40.7128,-74.0060"
     ```
     Puedes convertirlo en una tupla en Python usando `config.tuple`:
     ```python
     COORDINATES = config('COORDINATES', cast=config.tuple)
     # Resultado: (40.7128, -74.0060)
     ```

   - **JSON:**
     Si tienes una cadena con formato JSON:
     ```plaintext
     CONFIG_DATA='{"setting1": "value1", "setting2": "value2"}'
     ```
     Puedes convertirla en un objeto Python usando `config.json`:
     ```python
     CONFIG_DATA = config('CONFIG_DATA', cast=config.json)
     # Resultado: {'setting1': 'value1', 'setting2': 'value2'}
     ```

6. **Conversiones personalizadas:**

   Si necesitas una conversión especial, puedes definir tu propia función de conversión. Por ejemplo, si tienes coordenadas geográficas (latitud y longitud) en un solo string y quieres convertirlas a una tupla de números flotantes, puedes hacer lo siguiente:

   ```python
   def geoloc(loc: str) -> tuple[float, float]:
       return tuple(float(v) for v in loc.split(','))
   ```

   Luego, en tu archivo de configuración (`settings.py`), puedes usar **prettyconf** con la conversión personalizada:

   ```python
   TEIDE_GPS = config('TEIDE_GPS', cast=geoloc)
   ```

   Y en tu archivo `.env`, podrías tener algo como:
   ```plaintext
   TEIDE_GPS="28.2723364,-16.6631076"
   ```

