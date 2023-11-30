# Input Form
  
Cria um formulário para o usuário final inserir informações no robô  

*Read this in other languages: [English](Manual_InputForm.md), [Português](Manual_InputForm.pr.md), [Español](Manual_InputForm.es.md)*
  
![banner](imgs/Banner_InputForm.pngjpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


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


## Descrição do comando

### Carregar formulário do arquivo
  
Carrega um arquivo json e mostra em um formulário
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho para JSON|Caminho para o arquivo JSON a ser carregado|form.json|

### Carregar formulário de dados
  
Carrega dados json e mostra em um formulário
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Formulário JSON|Formulário JSON para carregar|{json_data}|
