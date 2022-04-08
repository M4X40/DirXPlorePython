#########################
##   StartUp Options   ##
#########################

skipModuleInstall = False
    # If "True", this skips the module install (see the required modules section)                                        | Recommended Option: False

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
    import sys

    if skipModuleInstall == False:
        print(' ')
        print('Installing TermColor')
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install', 'termcolor'])

        print(' ')
        print('Updating PiP')
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])

        print(' ')
        print('Installing Unipath')
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install', 'unipath'])

        print(' ')
        print('Installing Prompt ToolKit')
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install', 'prompt_toolkit'])

        cls()

    ####### Other Modules
    from os.path import exists
    from termcolor import colored
    from unipath import Path
    from prompt_toolkit import prompt
    import zipfile

    # Clear Console
    cls()

    ##############
    ##   Main   ##
    ##############

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

        # Prints
        print(colored(f'Current Directory: {coloredPath}'))
        print('')
        print(colored(f'{coloredZero}   >>   Move Up ({coloredPathAbove})'))
        print(colored(f'{coloredOne}   >>   View Contents'))
        print(colored(f'{coloredTwo}   >>   Type Directory'))

        #Prompt
        while True:
            text = prompt('Option # >> ')

            if text == "0":
                currentPath = pathAbove
                cls()
                Path.chdir(currentPath)
                SelectionPrompt()
            if text == "1":
                cls()
                viewContents()
            if text == "2":
                cls()
                changeDirPrompt()

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
        if itemext == ".zip" or itemext == ".gz" or itemext == ".rar" or itemext == ".7z":
            print(colored(f'[{colored2}]  >>  Un-Zip File'))
            itemiszip = True

        #Prompt
        while True:
            text = prompt('Option # >> ')

            if text == "0":
                cls()
                viewContents()
            elif text == "1":
                os.system("start " + itemname)
                viewContents(False)
            elif text == "2" and itemiszip:
                unzip(itempath, selection, list)
            else:
                if text == "2":
                    print(colored(f'ERROR: Not a Zipped File:', 'red'), colored(f'{text}', 'magenta'))
                else:
                    print(colored(f'ERROR: Unknown Index:', 'red'), colored(f'{text}', 'magenta'))

    def unzip(path, selection, list):
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(path.parent)
        cls()
        print(colored("Done!", 'yellow'))
        fileinfo(selection, list)



    ###############
    ##   Start   ##
    ###############

    SelectionPrompt()

######################
##   Script Check   ##
######################

if __name__ == '__main__':
    main()