# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import sys
import json
import tkinter as tk
import ttkbootstrap as ttk # type: ignore

GetParams = GetParams # type: ignore
SetVar = SetVar # type: ignore



"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

global InputFormLoadForm, inputs__
def InputFormLoadForm(form_):
    
    global saveData2, inputs, window_form, getFileSavePathForm, inputs__
    inputs__ = {}
    def getFileSavePathForm(inputEntry, type_file):
        global window_form
        from tkinter import filedialog
        file_path = None
        if type_file == "File":
            file_path = filedialog.askopenfilename()
        if type_file == "Folder":
            import subprocess
            if sys.platform.startswith('win'):
                scr = """
                            Dim strPath

                strPath = SelectFolder( "" )
                If strPath = vbNull Then
                    WScript.WScript.StdOut.Write("")
                Else
                    WScript.StdOut.Write(strPath)
                End If


                Function SelectFolder( myStartFolder )
                ' This function opens a "Select Folder" dialog and will
                ' return the fully qualified path of the selected folder
                '
                ' Argument:
                '     myStartFolder    [string]    the root folder where you can start browsing;
                '                                  if an empty string is used, browsing starts
                '                                  on the local computer
                '
                ' Returns:
                ' A string containing the fully qualified path of the selected folder
                '
                ' Written by Rob van der Woude
                ' http://www.robvanderwoude.com

                    ' Standard housekeeping
                    Dim objFolder, objItem, objShell

                    ' Custom error handling
                    On Error Resume Next
                    SelectFolder = vbNull

                    ' Create a dialog object
                    Set objShell  = CreateObject( "Shell.Application" )
                    Set objFolder = objShell.BrowseForFolder( 0, "Select Folder", 0, myStartFolder )

                    ' Return the path of the selected folder
                    If IsObject( objfolder ) Then SelectFolder = objFolder.Self.Path

                    ' Standard housekeeping
                    Set objFolder = Nothing
                    Set objshell  = Nothing
                    On Error Goto 0
                End Function"""
                with open("tmp.vbs", "w") as f:
                    f.write(scr)
                    f.close()
                    con = subprocess.Popen('cscript tmp.vbs //Nologo', shell=True, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
                    a = con.communicate()
                    try:
                        file_path = str(a[0].decode()).replace("\\", "/")
                    except UnicodeDecodeError:
                        file_path = str(a[0].decode("latin-1")).replace("\\", "/")
            else:
                alert_ = """osascript -e 'set aa to choose folder name'"""
                p = subprocess.Popen(alert_, stdout=subprocess.PIPE, shell=True)
                output, err = p.communicate()
                file_path = str(output).replace(str(output).split(":")[0], "").replace(":", "/").replace("\\n", "")
                if file_path.endswith("'"):
                    file_path = file_path[:-1]

        if type_file == "NewFile":
            file_path = filedialog.asksaveasfilename()
        window_form.deiconify()
        window_form.update()
        inputEntry.delete(0, tk.END)
        inputEntry.insert(0, file_path)
        return file_path
    
    def do_nothing():
        pass


    def saveData2(e):
        global window_form, inputs__
        if e == 'saveData':
            for input_ in inputs__:
                try:
                    # Check the input type before getting the value
                    if inputs__[input_]['type'] in ['checkbox', 'radio']:
                        value = inputs__[input_]['value'].get()
                    elif inputs__[input_]['type'] == 'textarea':
                        value = inputs__[input_]['el'].get('1.0', tk.END)
                    elif inputs__[input_]['type'] == 'label':
                        value = None
                    elif inputs__[input_]['type'] =='select':
                        value = inputs__[input_]['value']
                    else:
                        value = inputs__[input_]['el'].get()
                    SetVar(input_, value)
                except Exception as e:
                    pass

        window_form.withdraw()
        window_form.after(1, lambda: window_form.quit())

    width=form_['window'].get('width', 800)
    height=form_['window'].get('height', 800)

    if  'window_form' in globals():
        # clear window widgets
        try:
            for widget in window_form.winfo_children():
                widget.destroy()
        except Exception as e:
            pass
        #Show window
        window_form.deiconify()
    else:
        window_form = ttk.Window(
            themename="litera"
        )
        window_form.attributes('-topmost', 1)

    window_form.config(width=width, height=height)
    # set Title
    window_form.title(form_['window'].get('title', 'Rocketbot Form'))
    # set size
    window_form.geometry(f"{width}x{height}")
    window_form.after(1, lambda: window_form.attributes('-topmost', 0))
    # set close button action to do nothing
    window_form.protocol("WM_DELETE_WINDOW", do_nothing)
    
    window_form.place_window_center()
    if form_['window'].get('resizable', False):
        window_form.resizable(True, True)
    else:
        window_form.resizable(0, 0)

    tkWindowPanel = ttk.Frame(window_form, width=width)
    tkWindowPanel.pack(fill=tk.BOTH, expand=True)
    text_welcome = ttk.Label(tkWindowPanel, text="Welcome to")
    text_welcome.place(relx=.5, rely=.2, anchor=ttk.CENTER)

    tkWindowFooter = ttk.Frame(window_form, height=50, bootstyle="dark")
    tkWindowFooter.pack(fill='both', side='bottom')


    #button submit

    button_submit = ttk.Button(
        tkWindowFooter,bootstyle="success",
        text= form_['window'].get('submit', 'Submit'), command=lambda:saveData2("saveData")
    )
    button_submit.pack(side=ttk.RIGHT, padx=5, pady=10)

    button_cancel = ttk.Button(
        tkWindowFooter,bootstyle="danger",
        text= form_['window'].get('cancel', 'Cancel'), 
        command=lambda:saveData2("cancel")
    )
    button_cancel.pack(side=ttk.LEFT, padx=5, pady=10)


    for inputs_ in form_.get('inputs', []):
        inputs__[inputs_['id']] = {}
        side = ttk.TOP
        if 'css' in inputs_:
            if 'col-md-6' in inputs_['css']:
                side = ttk.LEFT
        frm = ttk.Frame(tkWindowPanel, padding=10)
        frm.pack(side=side,fill=ttk.BOTH, expand=True)

        if inputs_['type'] == 'label':
            ttk.Label(frm,text=inputs_['title'], wraplength = height - 20 ).pack(side=ttk.TOP)
            inputs__[inputs_['id']]['type'] = inputs_['type']

        if inputs_['type'] == 'input':
            ttk.Label(frm, text=inputs_['title']).pack(side=ttk.TOP, fill=ttk.BOTH)
            if inputs_.get('format') == 'password':
                inputs__[inputs_['id']]['el'] = ttk.Entry(frm, show="*")
            else:
                inputs__[inputs_['id']]['el'] = ttk.Entry(frm)
            inputs__[inputs_['id']]['el'].pack(side=ttk.TOP, fill=ttk.BOTH)
            inputs__[inputs_['id']]['type'] = inputs_['type']
            
        if inputs_['type'] == 'select':
            ttk.Label(frm,text=inputs_['title']).pack(side=tk.TOP,fill=ttk.BOTH)
            # Extract the option texts
            option_texts = [option['text'] for option in inputs_['options']]
            inputs__[inputs_['id']]['el'] = ttk.Combobox(frm, values=option_texts, state='readonly')
            inputs__[inputs_['id']]['el'].pack(side=ttk.TOP, fill=ttk.BOTH)
            inputs__[inputs_['id']]['type'] = inputs_['type']

            # Bind the selection event
            def on_select(event, id=inputs_['id'], options=inputs_['options']):
                # Find the value corresponding to the selected text
                selected_text = inputs__[id]['el'].get()
                for option in options:
                    if option['text'] == selected_text:
                        inputs__[id]['value'] = option['value']
                        break

            inputs__[inputs_['id']]['el'].bind('<<ComboboxSelected>>', on_select)

        if inputs_['type'] == 'checkbox':
            ttk.Label(frm,text=inputs_['title']).pack(side=tk.TOP,fill=ttk.BOTH)
            # Create a control variable
            inputs__[inputs_['id']]['value'] = tk.BooleanVar()
            # Create a Checkbutton linked to the control variable
            inputs__[inputs_['id']]['el'] = ttk.Checkbutton(frm, variable=inputs__[inputs_['id']]['value'])
            inputs__[inputs_['id']]['el'].pack(side=ttk.TOP, fill=ttk.BOTH)
            inputs__[inputs_['id']]['type'] = inputs_['type']

        if inputs_['type'] == 'textarea':
            ttk.Label(frm,text=inputs_['title']).pack(side=tk.TOP,fill=ttk.BOTH)
            inputs__[inputs_['id']]['el'] = ttk.Text(frm, height=inputs_.get('height', 5))
            inputs__[inputs_['id']]['el'].pack(side=ttk.TOP, fill=ttk.BOTH)
            inputs__[inputs_['id']]['type'] = inputs_['type']

        if inputs_['type'] == 'radio':
            ttk.Label(frm,text=inputs_['title']).pack(side=tk.TOP,fill=ttk.BOTH)
            # Create a control variable
            inputs__[inputs_['id']]['value'] = tk.StringVar()
            # For each option, create a Radiobutton linked to the control variable
            for option in inputs_['options']:
                rb = ttk.Radiobutton(frm, text=option['text'], variable=inputs__[inputs_['id']]['value'], value=option['value'])
                rb.pack(side=tk.TOP, fill=ttk.BOTH)
            inputs__[inputs_['id']]['type'] = inputs_['type']
        
        if inputs_['type'] in ['file_select', 'file_save', 'folder_select']:
            #Set height frm 
            frm.config(height=20)
            ttk.Label(frm,text=inputs_['title']).pack(side=tk.TOP,fill=ttk.BOTH)
            # Search file widget 
            frame_search = ttk.Frame(frm)
            frame_search.pack(side=ttk.TOP, fill=ttk.BOTH)

            # Input file path, entry widget width 100% 

            inputs__[inputs_['id']]['el'] = ttk.Entry(frame_search)
            inputs__[inputs_['id']]['el'].pack(side=ttk.LEFT, fill=ttk.BOTH, expand=True)
            inputs__[inputs_['id']]['type'] = inputs_['type']
            type_file = "File"
            if inputs_['type'] == 'folder_select':
                type_file = "Folder"
            if inputs_['type'] == 'file_save':
                type_file = "NewFile"
            ttk.Button(frame_search, text="Search", width=5, command=lambda inputs_= inputs_, type_file=type_file:getFileSavePathForm(inputs__[inputs_['id']]['el'], type_file)).pack(side=ttk.LEFT)
    try:
        window_form.mainloop()
    except Exception as e:
        print(e)

try:
    if module == "LoadFormFile":
        file_json = GetParams("file_json")        
        #Read json file
        with open(file_json) as f:
            form_ = json.load(f)
            InputFormLoadForm(form_)
    if module == "LoadFormData":
        form_ = GetParams("form")
        form_ = json.loads(form_)
        InputFormLoadForm(form_)

except Exception as e:
    import traceback 
    traceback.print_exc()
    raise Exception(e)
