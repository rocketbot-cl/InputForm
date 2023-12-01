# How to use the module
The InputForms module allows you to display forms quickly and easily based on a data dictionary.

## Data format
The json from which the form is loaded must respect a certain structure to work correctly. The parameters it receives are:
- window: Form window data. It is a dictionary with the following parameters:
    - title: Window title.
    - width: Window width.
    - height: Window height.
    - resizable (optional): Indicates whether the window is resizable. By default it is `false`.
    - submit: Submit button text.
- inputs: List of form fields. Each field is a dictionary that corresponds to the type of data you want to display. For more information on the available data types, see the [Data types](#data-types) section.

Example: 
```json
{
    "window": {
        "title": "Example form",
        "width": 500,
        "height": 500,
        "resizable": true,
        "submit": "Submit"
    },
    "inputs": [ 
        // See input examples below this section 
    ]
}
```

## Data types
The module accepts forms with the following data types:
- label: Informative plain text.
- input: Text field for entering data.
- select: Dropdown list to select an option.
- checkbox: Check box field that can be selected or not.
- textarea: Text field for entering multiline data.
- radio: Single selection button.
- file_select: Text field with search engine to select a file.
- file_save: Text field with search engine to create or overwrite a file.
- folder_select: Text field with search engine to select a folder.

### label
The label data type is plain text that is displayed in the form. It receives the following parameters:
- title: Text to display.
- id: Field identifier.
- css (optional): Bootstrap classes to apply to the element.

Example:
```json
{
    "type": "label",
    "title": "Example text",
    "id": "text",
    "css": "col-md-12"
}
```

### input
The input data type is a text field for entering data. It receives the following parameters:
- title: Text to display.
- id: Field identifier. Name that the variable in Rocketbot that stores the entered value must have.
- format (optional): Text validation format by default is `text`. The available formats are:
    - text: Free text.
    - password: Password.
- css (optional): Bootstrap classes to apply to the element.

Example:
```json
{
    "type": "input",
    "title": "Enter your name",
    "id": "name",
    "format": "text",
    "css": "col-md-12"
},
{
    "type": "input",
    "title": "Enter your password",
    "id": "pass",
    "format": "password",
    "css": "col-md-12"
}
```

### select
The select data type is a dropdown list to select an option. It receives the following parameters:
- title: Text to display.
- id: Field identifier. Name that the variable in Rocketbot that stores the selected value must have.
- options: List of options to display. Each option is a dictionary with the following parameters:
    - value: Option value that is stored in the variable.
    - text: Text to display.
- css (optional): Bootstrap classes to apply to the element.

Example:
```json
{
    "type": "select",
    "title": "Select an option",
    "id": "option",
    "options": [
        {
            "value": "1",
            "text": "Option 1"
        },
        {
            "value": "2",
            "text": "Option 2"
        },
        {
            "value": "3",
            "text": "Option 3"
        }
    ],
    "css": "col-md-12"
}
```

### checkbox
The checkbox data type is a check box. It receives the following parameters:
- title: Text to display.
- id: Field identifier. Name that the variable in Rocketbot that stores the selected value must have.
- default (optional): Default value of the box. It can be `true` or `false`. By default it is `false`.
- css (optional): Bootstrap classes to apply to the element.

Example:
```json
{
    "type": "checkbox",
    "title": "Check the box",
    "id": "check",
    "default": true,
    "css": "col-md-12"
}
```

### textarea
The textarea data type is a text field for entering multiline data. It receives the following parameters:
- title: Text to display.
- id: Field identifier. Name that the variable in Rocketbot that stores the entered value must have.
- height (optional): Field height in lines. By default it is `5`.
- css (optional): Bootstrap classes to apply to the element.

Example:
```json
{
    "type": "textarea",
    "title": "Enter your address",
    "id": "address",
    "height": 4,
    "css": "col-md-12"
}
```

### radio
The radio data type is a single selection button. It receives the following parameters:
- title: Text to display.
- id: Field identifier. Name that the variable in Rocketbot that stores the selected value must have.
- options: List of options to display. Each option is a dictionary with the following parameters:
    - value: Option value that is stored in the variable.
    - text: Text to display.
- css (optional): Bootstrap classes to apply to the element.

Example:
```json
{
    "type": "radio",
    "title": "Select an option",
    "id": "option",
    "options": [
        {
            "value": "1",
            "text": "Option 1"
        },
        {
            "value": "2",
            "text": "Option 2"
        },
        {
            "value": "3",
            "text": "Option 3"
        }
    ],
    "css": "col-md-12"
}
```

### file_select
The file_select data type is a text field with a search engine to select a file. It receives the following parameters:
- title: Text to display.
- id: Field identifier. Name that the variable in Rocketbot that stores the selected file path must have.
- css (optional): Bootstrap classes to apply to the element.

Example:
```json
{
    "type": "file_select",
    "title": "Select a file",
    "id": "file",
    "css": "col-md-12"
}
```

### file_save
The file_save data type is a text field with a search engine to create or overwrite a file. It receives the following parameters:
- title: Text to display.
- id: Field identifier. Name that the variable in Rocketbot that stores the selected file path must have.
- css (optional): Bootstrap classes to apply to the element.

Example:
```json
{
    "type": "file_save",
    "title": "Select a file",
    "id": "file",
    "css": "col-md-12"
}
```

### folder_select
The folder_select data type is a text field with a search engine to select a folder. It receives the following parameters:
- title: Text to display.
- id: Field identifier. Name that the variable in Rocketbot that stores the selected folder path must have.
- css (optional): Bootstrap classes to apply to the element.

Example:
```json
{
    "type": "folder_select",
    "title": "Select a folder",
    "id": "folder",
    "css": "col-md-12"
}
```



---
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




---
# Como usar o módulo
O módulo InputForms permite exibir formulários de forma rápida e fácil com base em um dicionário de dados.

## Formato de dados
O json do qual o formulário é carregado deve respeitar uma certa estrutura para funcionar corretamente. Os parâmetros que ele recebe são:
- window: Dados da janela do formulário. É um dicionário com os seguintes parâmetros:
    - title: Título da janela.
    - width: Largura da janela.
    - height: Altura da janela.
    - resizable (opcional): Indica se a janela é redimensionável. Por padrão é `false`.
    - submit: Texto do botão de envio.
- inputs: Lista de campos do formulário. Cada campo é um dicionário que corresponde ao tipo de dados que você deseja exibir. Para obter mais informações sobre os tipos de dados disponíveis, consulte a seção [Tipos de dados](#tipos-de-dados).

Exemplo: 
```json
{
    "window": {
        "title": "Formulário de exemplo",
        "width": 500,
        "height": 500,
        "resizable": true,
        "submit": "Enviar"
    },
    "inputs": [ 
        // Ver exemplos de entrada abaixo desta seção 
    ]
}
```

## Tipos de dados
O módulo aceita formulários com os seguintes tipos de dados:
- label: Texto informativo simples.
- input: Campo de texto para inserir dados.
- select: Lista suspensa para selecionar uma opção.
- checkbox: Campo de caixa de seleção que pode ser selecionado ou não.
- textarea: Campo de texto para inserir dados de várias linhas.
- radio: Botão de seleção única.
- file_select: Campo de texto com mecanismo de pesquisa para selecionar um arquivo.
- file_save: Campo de texto com mecanismo de pesquisa para criar ou substituir um arquivo.
- folder_select: Campo de texto com mecanismo de pesquisa para selecionar uma pasta.

### label
O tipo de dados label é texto simples que é exibido no formulário. Ele recebe os seguintes parâmetros:
- title: Texto para exibir.
- id: Identificador do campo.
- css (opcional): Classes de inicialização para aplicar ao elemento.

Exemplo:
```json
{
    "type": "label",
    "title": "Texto de exemplo",
    "id": "text",
    "css": "col-md-12"
}
```

### input
O tipo de dados input é um campo de texto para inserir dados. Ele recebe os seguintes parâmetros:
- title: Texto para exibir.
- id: Identificador do campo. Nome que a variável no Rocketbot que armazena o valor inserido deve ter.
- format (opcional): Formato de validação de texto por padrão é `text`. Os formatos disponíveis são:
    - text: Texto livre.
    - password: Senha.
- css (opcional): Classes de inicialização para aplicar ao elemento.

Exemplo:
```json
{
    "type": "input",
    "title": "Insira seu nome",
    "id": "name",
    "format": "text",
    "css": "col-md-12"
},
{
    "type": "input",
    "title": "Insira sua senha",
    "id": "pass",
    "format": "password",
    "css": "col-md-12"
}
```

### select
O tipo de dados select é uma lista suspensa para selecionar uma opção. Ele recebe os seguintes parâmetros:
- title: Texto para exibir.
- id: Identificador do campo. Nome que a variável no Rocketbot que armazena o valor selecionado deve ter.
- options: Lista de opções para exibir. Cada opção é um dicionário com os seguintes parâmetros:
    - value: Valor da opção que é armazenado na variável.
    - text: Texto para exibir.
- css (opcional): Classes de inicialização para aplicar ao elemento.

Exemplo:
```json
{
    "type": "select",
    "title": "Selecione uma opção",
    "id": "option",
    "options": [
        {
            "value": "1",
            "text": "Opção 1"
        },
        {
            "value": "2",
            "text": "Opção 2"
        },
        {
            "value": "3",
            "text": "Opção 3"
        }
    ],
    "css": "col-md-12"
}
```

### checkbox
O tipo de dados checkbox é uma caixa de seleção. Ele recebe os seguintes parâmetros:
- title: Texto para exibir.
- id: Identificador do campo. Nome que a variável no Rocketbot que armazena o valor selecionado deve ter.
- default (opcional): Valor padrão da caixa. Pode ser `true` ou `false`. Por padrão é `false`.
- css (opcional): Classes de inicialização para aplicar ao elemento.

Exemplo:
```json
{
    "type": "checkbox",
    "title": "Marque a caixa",
    "id": "check",
    "default": true,
    "css": "col-md-12"
}
```

### textarea
O tipo de dados textarea é um campo de texto para inserir dados de várias linhas. Ele recebe os seguintes parâmetros:
- title: Texto para exibir.
- id: Identificador do campo. Nome que a variável no Rocketbot que armazena o valor inserido deve ter.
- height (opcional): Altura do campo em linhas. Por padrão é `5`.
- css (opcional): Classes de inicialização para aplicar ao elemento.

Exemplo:
```json
{
    "type": "textarea",
    "title": "Insira seu endereço",
    "id": "address",
    "height": 4,
    "css": "col-md-12"
}
```

### radio
O tipo de dados radio é um botão de seleção única. Ele recebe os seguintes parâmetros:
- title: Texto para exibir.
- id: Identificador do campo. Nome que a variável no Rocketbot que armazena o valor selecionado deve ter.
- options: Lista de opções para exibir. Cada opção é um dicionário com os seguintes parâmetros:
    - value: Valor da opção que é armazenado na variável.
    - text: Texto para exibir.
- css (opcional): Classes de inicialização para aplicar ao elemento.

Exemplo:
```json
{
    "type": "radio",
    "title": "Selecione uma opção",
    "id": "option",
    "options": [
        {
            "value": "1",
            "text": "Opção 1"
        },
        {
            "value": "2",
            "text": "Opção 2"
        },
        {
            "value": "3",
            "text": "Opção 3"
        }
    ],
    "css": "col-md-12"
}
```

### file_select
O tipo de dados file_select é um campo de texto com mecanismo de pesquisa para selecionar um arquivo. Ele recebe os seguintes parâmetros:
- title: Texto para exibir.
- id: Identificador do campo. Nome que a variável no Rocketbot que armazena o caminho do arquivo selecionado deve ter.
- css (opcional): Classes de inicialização para aplicar ao elemento.

Exemplo:
```json
{
    "type": "file_select",
    "title": "Selecione um arquivo",
    "id": "file",
    "css": "col-md-12"
}
```

### file_save
O tipo de dados file_save é um campo de texto com mecanismo de pesquisa para criar ou substituir um arquivo. Ele recebe os seguintes parâmetros:
- title: Texto para exibir.
- id: Identificador do campo. Nome que a variável no Rocketbot que armazena o caminho do arquivo selecionado deve ter.
- css (opcional): Classes de inicialização para aplicar ao elemento.

Exemplo:
```json
{
    "type": "file_save",
    "title": "Selecione um arquivo",
    "id": "file",
    "css": "col-md-12"
}
```

### folder_select
O tipo de dados folder_select é um campo de texto com mecanismo de pesquisa para selecionar uma pasta. Ele recebe os seguintes parâmetros:
- title: Texto para exibir.
- id: Identificador do campo. Nome que a variável no Rocketbot que armazena o caminho da pasta selecionada deve ter.
- css (opcional): Classes de inicialização para aplicar ao elemento.

Exemplo:
```json
{
    "type": "folder_select",
    "title": "Selecione uma pasta",
    "id": "folder",
    "css": "col-md-12"
}
```

---