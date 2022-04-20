#########################
##   StartUp Options   ##
#########################

skipModuleInstall = False
    # If "True", this skips the module install (see the required modules section)                                        | Recommended Option: False

################
##   Module  ###
################

from tkinter import *

################
##   Signal   ##
################

def main():

    #################
    ##   Imports   ##
    #################

    import os

    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    cls()

    print('Importing Modules. This may take some time.')

    #######  Required Modules
    import subprocess
    from subprocess import call
    import sys
    import platform

    if skipModuleInstall == False:
        if platform.system() == 'Windows':
            print('\nInstalling TermColor')
            call('pip install termcolor', shell=False)

            print('\nUpdating PiP')
            call('pip install --upgrade pip', shell=False)

            print('\nInstalling Unipath')
            call('pip install unipath', shell=False)

            print('\nInstalling Prompt ToolKit')
            call('pip install prompt_toolkit', shell=False)
            cls()
        else:
            print('\nInstalling TermColor')
            call('pip install termcolor', shell=True)

            print('\nUpdating PiP')
            call('pip install --upgrade pip', shell=True)

            print('\nInstalling Unipath')
            call('pip install unipath', shell=True)

            print('\nInstalling Prompt ToolKit')
            call('pip install prompt_toolkit', shell=True)
            cls()

    ####### Other Modules
        from os.path import exists
        from unipath import Path
        from prompt_toolkit import prompt
        import zipfile
        from tkinter import messagebox
        from tkinter import filedialog
        from termcolor import colored

    # Clear Console
    cls()

    ##############
    ##   Main   ##
    ##############

    def pause():
        if platform.system() == 'Windows':
            os.system("pause")
        else:
            os.system('read -s -n 1 -p "Press any key to continue...\n"')
            cls()

    def SelectionPrompt(): # Main Menu

        # Important Vars
        global currentPath
        currentPath = Path(os.getcwd())
        pathAbove = currentPath.parent

        # Coloring
        coloredPath = (colored(currentPath, 'cyan'))
        coloredPathAbove = (colored(pathAbove, 'cyan'))
        coloredZero = (colored('[0]', 'magenta'))
        coloredOne = (colored('[1]', 'magenta'))
        coloredTwo = (colored('[2]', 'magenta'))
        coloredTre = (colored('[3]', 'magenta'))

        # Prints
        print(colored(f'Current Directory: {coloredPath}\n'))
        print(colored(f'{coloredZero}   >>   Move Up ({coloredPathAbove})'))
        print(colored(f'{coloredOne}   >>   View Contents'))
        print(colored(f'{coloredTwo}   >>   Type Directory'))
        print(colored(f'--=[ EXTRA OPTIONS ]=--'))
        print(colored(f'{coloredTre}   >>   Console Here\n'))

        #Prompt
        while True:
            text = prompt('Option # >> ')

            if text == "0":
                currentPath = pathAbove
                cls()
                Path.chdir(currentPath)
                SelectionPrompt()
            elif text == "1":
                cls()
                viewContents()
            elif text == "2":
                cls()
                changeDirPrompt()
            elif text == "3":
                cls()
                console(currentPath)

    def viewContents(): # Contents List

        #Important Vars
        global currentPath
        itemnum = 1

        # Permissions Check/Directory Contents List
        try:
            itemslist = os.listdir()
        except PermissionError:
            print(colored(f'ERROR: Invalid Permissions to read:', 'red'), colored(f'{Path(os.getcwd())}', 'magenta'))
            SelectionPrompt()

        # Coloring
        coloredZero = (colored('0', 'magenta'))

        #Prints
        print(colored(f'[{coloredZero}]  >>  Go Back'))
        for i in itemslist:
            cItemnum = (colored(itemnum, 'cyan'))
            cZero = (colored('0', 'cyan') + cItemnum)
            if itemnum < 10:
                print(colored(f'[{cZero}]  >>  {i}'))
            else:
                print(colored(f'[{cItemnum}]  >>  {i}'))
            itemnum = itemnum + 1

        # Prompt
        while True:
            try:
                text = prompt('Option # >> ')
                global selection
                selection = int(text) - 1
                if selection == -1:
                    cls()
                    SelectionPrompt()
                else:
                    itemname = str(itemslist[selection])
                    joinedPath = (f'{currentPath}\{itemname}')
                    if Path.isdir(joinedPath) == True:
                        try:
                            currentPath = (joinedPath)
                            cls()
                            Path.chdir(currentPath)
                            SelectionPrompt()
                        except PermissionError:
                            print(colored(f'ERROR: Invalid Permissions to read:', 'red'), colored(f'{Path(joinedPath)}', 'magenta'))
                            SelectionPrompt()
                    elif Path.isfile(joinedPath) == True:
                        cls()
                        fileinfo(selection, itemslist)
            except IndexError:
                print(colored(f'ERROR: Must be between', 'red'), colored('0', 'magenta'), colored('and', 'red'), colored(f'{len(itemslist)}', 'magenta'))

    def changeDirPrompt(): # Custom Directory Prompt

        #Coloring
        coloredZero = (colored('0', 'magenta'))

        # Prints
        print(colored(f'[{coloredZero}] Go Back'))
        print(colored(f'Example Path:', 'cyan'), colored('C:\\Users\\dirxp\\AppData\\Local\\Python', 'magenta'))

        # Change Directory Function Call
        changeDir()

    def changeDir(): # Custom Directory Prompt

        # Prompt
        text2 = prompt('Directory >> ')

        if Path.isdir(text2):
            Path.chdir(text2)
            cls()
            SelectionPrompt()
        elif text2 == '0':
            cls()
            SelectionPrompt()
        else:
            print(colored(f'ERROR: Invalid Path:', 'red'), colored(f'{text2}', 'magenta'))
            changeDir()

    def fileinfo(selection, list): # File Information Screen

        # Important Variables
        itemname = str(list[selection])
        itempath = Path(f'{Path.cwd()}\{itemname}')
        itemstem = str(itempath.stem)
        itemext = str(itempath.ext)
        itemsizekb = int(itempath.size())
        itemct = itempath.ctime()
        itemmod = itempath.atime()

        # Size Converter
        if itemsizekb >= 1024:
            itemsizemb = itemsizekb / 1024
            if itemsizemb >= 1024:
                itemsizegb = itemsizemb / 1024
                itemsize = str(f'{itemsizegb} GB')
            else:
                itemsize = str(f'{itemsizemb} MB')
        else:
            itemsize = str(f'{itemsizekb} KB')

        # Coloring
        colored0 = (colored('0', 'magenta'))
        colored1 = (colored('1', 'magenta'))
        colored2 = (colored('2', 'magenta'))
        colored3 = (colored('3', 'magenta'))

        #Prints
        print(colored(f'          File Info for:', 'cyan'), colored(f'{itemname}', 'magenta'))
        print('----------------------------------------')
        print(colored(f'Name         |       '), colored(f'{itemstem}'))
        print(colored(f'Extension    |       '), colored(f'{itemext}'))
        print(colored(f'Size         |       '), colored(f'{itemsize}'))
        print(colored(f'Created      |       '), colored(f'{itemct}'))
        print(colored(f'Modified     |       '), colored(f'{itemmod}'))
        print('----------------------------------------')
        print(colored(f'[{colored0}]  >>  Go Back'))
        print(colored(f'[{colored1}]  >>  Open File'))

        # Zip Check/Print
        formatstable = [
            ".zip",
            ".gz",
            ".rar",
            ".7z",
            ".grit"
            ".wim"
        ]
        if itemext in formatstable:
            print(colored(f'[{colored2}]  >>  Un-Zip File'))
            itemiszip = True
        else:
            itemiszip = False

        # Txt Check/Print
        formatstable = [
            ".txt",
            ".json",
            ".py",
            ".md",
            ".rtf",
            ".html",
            ".css",
            ".lua",
            ".js",
            ".c",
            ".cs",
            ".sh",
            ".bat",
            ".r",
            ".org,"
            ".doc",
            ".docx",
            ".log"
        ]
        if itemext in formatstable:
            print(colored(f'[{colored2}]  >>  Edit Text File'))
            itemistxt = True
        else:
            itemistxt = False

        # Python Check
        if itemext == ".py":
            print(colored(f'[{colored3}]  >>  Run File Here'))
            itemispy = True
        else:
            itemispy = False

        #Prompt
        while True:
            text = prompt('Option # >> ')

            if text == "0":
                cls()
                viewContents()
            elif text == "1":
                os.system("start " + itemname)
                viewContents()
            elif text == "2" and itemiszip:
                unzip(itempath, selection, list)
            elif text == "2" and itemistxt:
                editTxT(selection, list)
            elif text == "3" and itemispy:
                runpy(selection, list)
                print()
            else:
                print(colored(f'ERROR: Unknown Index:', 'red'), colored(f'{text}', 'magenta'))

    def unzip(path, selection, list):
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(path.parent)
        cls()
        print(colored("Done!", 'yellow'))
        fileinfo(selection, list)
    
    def editTxT(selection, list):
        itemname = str(list[selection])

        # Class
        class TextEditor:

            # Constructor
            def __init__(self,root):
                self.root = root
                self.root.title("DirXPlore Text Editor | V1.2.0")
                self.root.geometry("1200x700+200+150")
                self.filename = None
                self.title = StringVar()
                self.status = StringVar()

                # Titlebar
                self.titlebar = Label(self.root,textvariable=self.title,font=("Ubuntu",15,"bold"),bd=2,relief=GROOVE)
                self.titlebar.pack(side=TOP,fill=BOTH)
                self.settitle()
                self.titlebar.configure(bg='#202020')
                self.titlebar.configure(fg='#ffffff')

                # Statusbar
                self.statusbar = Label(self.root,textvariable=self.status,font=("times new roman",15),bd=2,relief=GROOVE)
                self.statusbar.pack(side=BOTTOM,fill=BOTH)
                self.status.set("DirXPlore | Made by M4X4")
                self.statusbar.configure(bg='#1f1f1f')
                self.statusbar.configure(fg='#ffffff')

                # Menubar
                self.menubar = Menu(self.root,font=("Ubuntu",15),activebackground="skyblue")
                self.menubar.configure(bg='#202020')
                self.menubar.configure(fg='#ffffff')
                self.root.config(menu=self.menubar)

                # FileMenu
                self.filemenu = Menu(self.menubar,font=("Ubuntu",12),activebackground="skyblue",tearoff=0)
                self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.savefile)
                self.filemenu.add_separator()
                self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.exit)
                self.filemenu.configure(bg='#2c2c2c')
                self.filemenu.configure(fg='#ffffff')
                self.menubar.add_cascade(label="File", menu=self.filemenu)

                # EditMenu
                self.editmenu = Menu(self.menubar,font=("Ubuntu",12),activebackground="skyblue",tearoff=0)
                self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
                self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
                self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
                self.editmenu.add_separator()
                self.editmenu.add_command(label="Undo",accelerator="Ctrl+Z",command=self.undo)
                self.editmenu.configure(bg='#2c2c2c')
                self.editmenu.configure(fg='#ffffff')
                self.menubar.add_cascade(label="Edit", menu=self.editmenu)

                # HelpMenu
                self.helpmenu = Menu(self.menubar,font=("Ubuntu",12),activebackground="skyblue",tearoff=0)
                self.helpmenu.add_command(label="About",command=self.infoabout)
                self.helpmenu.configure(bg='#2c2c2c')
                self.helpmenu.configure(fg='#ffffff')
                self.menubar.add_cascade(label="Help", menu=self.helpmenu)

                # Scrollbar
                scrol_y = Scrollbar(self.root,orient=VERTICAL)
                self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("Ubuntu",15),state="normal",relief=GROOVE)
                scrol_y.pack(side=RIGHT,fill=Y)
                scrol_y.config(command=self.txtarea.yview)
                self.txtarea.pack(fill=BOTH,expand=1)

                # Shortcuts
                self.shortcuts()

            # SetTitle
            def settitle(self):
                if self.filename:
                    self.title.set(self.filename)
                else:
                    self.title.set(f"{itemname}")

            # SaveFile
            def savefile(self,*args):
                try:
                    data = self.txtarea.get("1.0",END)
                    outfile = open(itemname,"w")
                    outfile.write(data)
                    outfile.close()
                    self.settitle()
                    self.status.set("Saved Successfully")
                except Exception as e:
                    messagebox.showerror("Exception",e)
                    print(e)

            # Exit
            def exit(self,*args):
                op = messagebox.askyesno("WARNING","Your Unsaved Data May be Lost!!")
                if op>0:
                    self.root.destroy()
                else:
                    return

            # Cut
            def cut(self,*args):
                self.txtarea.event_generate("<<Cut>>")

            # Copy
            def copy(self,*args):
                    self.txtarea.event_generate("<<Copy>>")

            # Paste
            def paste(self,*args):
                self.txtarea.event_generate("<<Paste>>")

            # Undo
            def undo(self,*args):
                try:
                    if self.filename:
                        self.txtarea.delete("1.0",END)
                        infile = open(self.filename,"r")
                        for line in infile:
                            self.txtarea.insert(END,line)
                        infile.close()
                        self.settitle()
                        self.status.set("Undone Successfully")
                    else:
                        self.txtarea.delete("1.0",END)
                        self.filename = None
                        self.settitle()
                        self.status.set("Undone Successfully")
                except Exception as e:
                    messagebox.showerror("Exception",e)

            # About
            def infoabout(self):
                messagebox.showinfo("About DirXPlore TE","A Text Editor for DirXPlore\nCreated by M4X4.")

            # Shortcuts
            def shortcuts(self):
                self.txtarea.bind("<Control-s>",self.savefile)
                self.txtarea.bind("<Control-e>",self.exit)
                self.txtarea.bind("<Control-x>",self.cut)
                self.txtarea.bind("<Control-c>",self.copy)
                self.txtarea.bind("<Control-v>",self.paste)
                self.txtarea.bind("<Control-z>",self.undo)

            # DarkMode bg
                self.txtarea.configure(bg='#2c2c2c')
                self.txtarea.configure(fg='#ffffff')

            # OpenFile
                infile = open(itemname,"r")
                self.txtarea.delete("1.0",END)
                for line in infile:
                    self.txtarea.insert(END,line)
                infile.close()
                self.settitle()

        # Tk
        root = Tk()
        # Root
        TextEditor(root)
        #Window Looping
        root.mainloop()

    def runpy(selection, list):
        cls()

        itemname = str(list[selection])

        exec(open(itemname).read())

        print(colored(f'Script {itemname} has ended,', 'cyan'))
        pause()
        cls()
        fileinfo(selection, list)

    def console(path):
        coloredExit = colored('exit', 'magenta')

        print(f"DirXPlore [Version 1.3.0]\n(R) M4X4. All rights reserved.\n\nType {coloredExit} to exit\n")
        
        while True:
            try:
                script=prompt(f"{path}> ")

                if script == "exit":
                    cls()
                    SelectionPrompt()
                else:
                    exec(script)
            except Exception as e:
                print(colored(f"\n{e}\n", 'red'))

    ###############
    ##   Start   ##
    ###############

    SelectionPrompt()

######################
##   Script Check   ##
######################

if __name__ == '__main__':
    main()
