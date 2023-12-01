# Input Form
  
Creates a form for the end user to enter information to the robot  

*Read this in other languages: [English](Manual_InputForm.md), [Português](Manual_InputForm.pr.md), [Español](Manual_InputForm.es.md)*
  
![banner](imgs/Banner_InputForm.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

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




## Description of the commands

### Load Form File
  
Load json file and show in a form
|Parameters|Description|example|
| --- | --- | --- |
|Path to JSON|Path to JSON file to load|form.json|

### Load Form Data
  
Load json data and show in a form
|Parameters|Description|example|
| --- | --- | --- |
|JSON Form|JSON Form to load|{json_data}|
