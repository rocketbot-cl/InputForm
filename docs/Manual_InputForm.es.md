# Input Form
  
Crea un formulario para que el usuario final ingrese información al robot  

*Read this in other languages: [English](Manual_InputForm.md), [Português](Manual_InputForm.pr.md), [Español](Manual_InputForm.es.md)*
  
![banner](imgs/Banner_InputForm.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


# Cómo utilizar el módulo
El módulo InputForms te permite mostrar formularios de forma sencilla y rápida en base a un diccionario de datos.


## Formato de datos
El json desde el cual se carga el formulario debe respetar cierta estructura para funcionar correctamente. Los parámetros que recibe son:
- window: Datos de la ventana del formulario. Es un diccionario con los siguientes parámetros:
    - title: Título de la ventana.
    - width: Ancho de la ventana.
    - height: Alto de la ventana.
    - resizable (opcional): Indica si la ventana es redimensionable. Por defecto es `false`.
    - submit: Texto del botón de envío.
- inputs: Lista de campos del formulario. Cada campo es un diccionario que corresponda con el tipo de dato que se desea mostrar. Para más información sobre los tipos de datos disponibles, ver la sección [Tipos de datos](#tipos-de-datos).

Ejemplo: 
```json
{
    "window": {
        "title": "Formulario de ejemplo",
        "width": 500,
        "height": 500,

        "resizable": true,
        "submit": "Enviar"
    },
    "inputs": [ 
        // Ver ejemplos de inputs debajo de esta sección 
    ]
}
```


## Tipos de datos
El módulo acepta formularios con los siguientes tipos de datos:
- label: Texto plano informativo.
- input: Campo de texto para ingresar datos.
- select: Lista desplegable para seleccionar una opción.
- checkbox: Campo de casilla de verificación que puede ser seleccionado o no.
- textarea: Campo de texto para ingresar datos de varias líneas.
- radio: Botón de selección única.
- file_select: Campo de texto con buscador para seleccionar un archivo.
- file_save: Campo de texto con buscador para crear o sobrescribir un archivo.
- folder_select: Campo de texto con buscador para seleccionar una carpeta.

### label
El tipo de dato label es un texto plano que se muestra en el formulario. Recibe los siguientes parámetros:
- title: Texto a mostrar.
- id: Identificador del campo.
- css (opcional): Clases Bootstrap a aplicar al elemento.

Ejemplo:
```json
{
    "type": "label",
    "title": "Texto de ejemplo",
    "id": "text",
    "css": "col-md-12"
}
```

### input
El tipo de dato input es un campo de texto para ingresar datos. Recibe los siguientes parámetros:
- title: Texto a mostrar.
- id: Identificador del campo. Nombre que debe tener la variable en Rocketbot que almacena el valor ingresado.
- format (opcional): Formato de validación del texto ingresado por defecto es `text`. Los formatos disponibles son:
    - text: Texto libre.
    - password: Contraseña.
- css (opcional): Clases Bootstrap a aplicar al elemento.

Ejemplo:
```json
{
    "type": "input",
    "title": "Ingrese su nombre",
    "id": "name",
    "format": "text",
    "css": "col-md-12"
},
{
    "type": "input",
    "title": "Ingrese su contraseña",
    "id": "pass",
    "format": "password",
    "css": "col-md-12"
}
```

### select
El tipo de dato select es una lista desplegable para seleccionar una opción. Recibe los siguientes parámetros:
- title: Texto a mostrar.
- id: Identificador del campo. Nombre que debe tener la variable en Rocketbot que almacena el valor seleccionado.
- options: Lista de opciones a mostrar. Cada opción es un diccionario con los siguientes parámetros:
    - value: Valor de la opción que se almacena en la variable.
    - text: Texto a mostrar.
- css (opcional): Clases Bootstrap a aplicar al elemento.

Ejemplo:
```json
{
    "type": "select",
    "title": "Seleccione una opción",
    "id": "option",
    "options": [
        {
            "value": "1",
            "text": "Opción 1"
        },
        {
            "value": "2",
            "text": "Opción 2"
        },
        {
            "value": "3",
            "text": "Opción 3"
        }
    ],
    "css": "col-md-12"
}
```

### checkbox
El tipo de dato checkbox es una casilla de verificación. Recibe los siguientes parámetros:
- title: Texto a mostrar.
- id: Identificador del campo. Nombre que debe tener la variable en Rocketbot que almacena el valor seleccionado.
- default (opcional): Valor por defecto de la casilla. Puede ser `true` o `false`. Por defecto es `false`.
- css (opcional): Clases Bootstrap a aplicar al elemento.

Ejemplo:
```json
{
    "type": "checkbox",
    "title": "Marque la casilla",
    "id": "check",
    "default": true,
    "css": "col-md-12"
}
```

### textarea
El tipo de dato textarea es un campo de texto para ingresar datos de varias líneas. Recibe los siguientes parámetros:
- title: Texto a mostrar.
- id: Identificador del campo. Nombre que debe tener la variable en Rocketbot que almacena el valor ingresado.
- height (opcional): Altura del campo en líneas. Por defecto es `5`.
- css (opcional): Clases Bootstrap a aplicar al elemento.

Ejemplo:
```json
{
    "type": "textarea",
    "title": "Ingrese su dirección",
    "id": "address",
    "height": 4,
    "css": "col-md-12"
}
```

### radio
El tipo de dato radio es un botón de selección única. Recibe los siguientes parámetros:
- title: Texto a mostrar.
- id: Identificador del campo. Nombre que debe tener la variable en Rocketbot que almacena el valor seleccionado.
- options: Lista de opciones a mostrar. Cada opción es un diccionario con los siguientes parámetros:
    - value: Valor de la opción que se almacena en la variable.
    - text: Texto a mostrar.
- css (opcional): Clases Bootstrap a aplicar al elemento.

Ejemplo:
```json
{
    "type": "radio",
    "title": "Seleccione una opción",
    "id": "option",
    "options": [
        {
            "value": "1",
            "text": "Opción 1"
        },
        {
            "value": "2",
            "text": "Opción 2"
        },
        {
            "value": "3",
            "text": "Opción 3"
        }
    ],
    "css": "col-md-12"
}
```

### file_select
El tipo de dato file_select es un campo de texto con buscador para seleccionar un archivo. Recibe los siguientes parámetros:
- title: Texto a mostrar.
- id: Identificador del campo. Nombre que debe tener la variable en Rocketbot que almacena la ruta del archivo seleccionado.
- css (opcional): Clases Bootstrap a aplicar al elemento.

Ejemplo:
```json
{
    "type": "file_select",
    "title": "Seleccione un archivo",
    "id": "file",
    "css": "col-md-12"
}
```

### file_save
El tipo de dato file_save es un campo de texto con buscador para crear o sobrescribir un archivo. Recibe los siguientes parámetros:
- title: Texto a mostrar.
- id: Identificador del campo. Nombre que debe tener la variable en Rocketbot que almacena la ruta del archivo seleccionado.
- css (opcional): Clases Bootstrap a aplicar al elemento.

Ejemplo:
```json
{
    "type": "file_save",
    "title": "Seleccione un archivo",
    "id": "file",
    "css": "col-md-12"
}
```

### folder_select
El tipo de dato folder_select es un campo de texto con buscador para seleccionar una carpeta. Recibe los siguientes parámetros:
- title: Texto a mostrar.
- id: Identificador del campo. Nombre que debe tener la variable en Rocketbot que almacena la ruta de la carpeta seleccionada.
- css (opcional): Clases Bootstrap a aplicar al elemento.

Ejemplo:
```json
{
    "type": "folder_select",
    "title": "Seleccione una carpeta",
    "id": "folder",
    "css": "col-md-12"
}
```





## Descripción de los comandos

### Cargar Formulario desde Archivo
  
Carga un archivo json y lo muestra en un formulario
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo JSON|Ruta del archivo JSON a cargar|form.json|

### Cargar Formulario desde Datos
  
Carga datos json y los muestra en un formulario
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Formulario formato JSON|Formulario formato JSON a cargar|{json_data}|
