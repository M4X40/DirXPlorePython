DirXPlore
%%%%%%%%%

Python Directory and File managment at your keystrokes.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Script Version:    1.1.0
:Python Version:    3.10.2
:Main Page:         https://github.com/M4X40/DirXPlore
:Documentation:     https://github.com/M4X40/DirXPlore#readme
:Author:            Max S. <maxst.marie11@gmail.com>
:License:           GPL https://opensource.org/licenses/gpl-license

**DirXPlore** is a Python script that will (eventually) be capable of replacing the modern File Explorer on windows, and someday, MacOS's Finder.

This currently is **WINDOWS ONLY**, with some plans for a MacOS version later.

.. contents::

Installation
============

Installation is very simple, just download the script from ``Releases``, and run the script.
All required modules will automagically install themselves, as well as updating pip. (For the nerds, this is done using subprocess)
 - The modules that are downloaded include:
    - TermColor
    - Unipath
    - Prompt_Toolkit

If you want to disable the module download for whatever reason, Line **5** is your friend.

Main Menu
=========

This is the initial page you are sent to after the installation process. It should look a little something like::

    Current Directory: C:\Users\dirxp
    
    [0]   >>   Move Up (C:\Users)
    [1]   >>   View Contents
    [2]   >>   Type Directory

Lets go over what each of these does, shall we?

[0] Move Up
-----------

This is used to move up in the directory you are currently in (e.g. C:/Users/DirXP > C:/Users).

[1] View Contents
-----------------

This lets you view the Files/Subfolders of the Current Directory. These are indexed in order by name, descending. More information is in ``Content Viewing``

[2] Type Directory
------------------

Type Directory allows you to change to a specific directory, without having to navigate much. As of now, you are required to input the full path, and not the local path, of the directory.

Content Viewing
===============

All files and subfolders will be shown, including hidden/system folders/files. Examples of this are shown with ``desktop.ini`` and ``$Recycle-Bin``.
There is one exception to this however, data streams. These will not show, no matter what. You will have to use separate tools to find those.

Indexing
--------

All items have a ``Index Number``, which looks like this:
``[01]``

You can select an item by typing its Index Number. If the item is a folder, it will switch your directory to said folder, otherwise, the file selected will be open with the default program on your machine.

``Note: typing an index outside of the given range will result in an error, but not cause any harm to the script or the directory. The script handles IndexErrors itself so there is no hassle.``

File Information System
-----------------------

This is a new feature in release 1.1.0. The File Information System (F.I.S) is a system in which you are given information about a user-selected file.
This information can include File Name, Size, Extension, Creation Date, and Modification Date.

The F.I.S will look something like this::

          File Info for: DirXPlore.py
    ________________________________________
    Name         |        DirXPlore
    Extension    |        .py
    Size         |        6.970703125 MB
    Created      |        1647743941.8419933
    Modified     |        1647836592.4208443
    ________________________________________

``Note: The Created and Modified numbers will have offical date/time info soon.``

Future Plans
============

These future plans are in my reach, just need the motivation to get there:
 - [X] MacOS version, complete with all features that the Windows version has.
 - [X] Ubuntu version, with more advanced (less user-friendly) capabilities.
 - [X] Built-In text editor, similar to VIM for linux.
 - [-] Compressed Folder extractor, will work with .zip, .rar, .7z, .gz, and other formats.
 - [] Quick Access, like Windows
 - [] Tabs, or as close as i can get
 - [] Built-In console/IPY Window
 - [] File Similarity View, check if 2 or more files are similar or check if a string is in other files.
 ``[X] > Not Working On It``
 ``[-] > Being Worked On``
 ``[+] > Done and Implemented``

