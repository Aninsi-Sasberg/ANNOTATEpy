# Table of Contents

<style>
  
  *{
    font-family: IBM Plex Mono;
  }

</style>

- [Table of Contents](#table-of-contents)
- [ToDo](#todo)
- [PLAN](#plan)
  - [**ORDER**](#order)
  - [**Modes**](#modes)
    - [GUI](#gui)
    - [~~TERMINAL~~](#terminal)
  - [**Systems**](#systems)
    - [*NOTEBOOK* system](#notebook-system)
    - [*LIST* system](#list-system)
  - [**Globals**](#globals)
    - [Settings (read while loading)](#settings-read-while-loading)
  - [**Functions**](#functions)
    - [DATE](#date)
  - [**Modularisation**](#modularisation)
    - [Python](#python)
    - [XML](#xml)
  - [**References**](#references)
  - [Quotes](#quotes)

# ToDo

- XML
  - Notebook
  - loading settings etc.
- gui checking if text in QTextEdit has changed, and then implement CurrentTextContent, and thus communication between gui and files
- loading loaded file into QTextEdit (problem with self.file.read())
- think about binding a window to a file\
  &rarr; means that I can't just -\
  no. doesn't work, thought about it.
  if i open the program that would then mean i have to choose a file that's already saved somewhere.
  so i need so have a way to tell the gui you're operating in this path... oh wow that was easy, just needed the path. the rest is handled by currentTextContent. eZ.
- style of gui, fonts loading im terminal ist noch unschön
- make nice exceptions
- clean up print statements
- refactor variables

# PLAN

## **ORDER**

<mark>
OVERTHINK THIS :))))))
</mark>

1. load files r
    - load config
    - load recent file list (recentFiles, located in [data.xml](../filesystem/data.xml "open the file 'data.xml'"))
    - load notebooks/lists r (read so preview can be shown)
2. open last notebook/list
    - open notebook rw
3. open window

---

## **Modes**

### GUI

single window with toggleable side panel(s)

- ~~side panel(s)~~
  - choose notebook
- Top Ribbon Menu / Menubar
  - File
    - Save
    - Save As
    - ---
    - New File
    - ---
    - Open File
    - Open Recent
      - 10 Files: #Number fullname (= filepath + filename + extension)
  - Edit
    - Undo
    - Redo
    - ---
    - KillWhitespace
    - Insert Current Date
  - View
    - New Window
  - Help
    - Opens this Repository on Github
- Keyboard Shortcuts
  - EVERYTHING


### ~~TERMINAL~~

<mark>on hold</mark>

commandline implementation with same features

- new
  - input file..
    - name
    - type
    - path
      - can either type in relative path, whole path, or choose via explorer (&rarr; choosing path + filename + extension (via dropdown))
      - also possible whole/relative path + filename with extension via typing
- choose (like ANNOTATEps with 4 letter definition)
- write

---

## **Systems**

### *NOTEBOOK* system

- **savefile** (Saves locations of all the pages, as well as a copy of all pages in itself)
  - path
  - name
  - date (created, last edited, for each page)
- **pages**
  - title (e.g. date (possibly regex), custom, page number, regex)
  - number
- **filesystem** (lets people create fs based on page structure, folders are named by page title, and some regex)
- **attributes**
  - *title:*
  - *4chartitle:* for easy Notebook choosing in Terminal
  - *style:* can do CSS formatting
  - *length:* length of Notebook in Pages

  -

### *LIST* system

- instead of different pages, you get list elements, all saved in one file
- examples include old ANNOTATEps project

---

## **Globals**

- mode = gui(0) or terminal mode (1)

### Settings (read while loading)

- timezone & date
- language
  - *var (int):* **lang**
  - english (0), german (1)
- dialog = which file creation dialog

---

## **Functions**

### DATE

- user can add Date via a keyboard shortcut or button in windowmenu (Strg+.)

<mark>
ADD STUFF.
</mark>

---

## **Modularisation**

### Python

- [main](../../bin/annotate/main.py "open the file 'main.py'")
  - run all methods and so on in [the correct order](#order "read about the order of processes")
- load
  - loads all Notebooks, and opens them as rw
- [date](../../bin/annotate/date.py "open the file 'date.py'")
  - handles all [date formatting](#date "read about date formatting")
- [gui](../../bin/annotate/gui.py)
  - handles all the [gui](#gui "read about the GUI")
  - needs to communicate with files
- files
  - handles all file loading and saving
- terminal
  - handles [terminal execution](#terminal "read about the terminal execution")

### XML

- [settings](../../bin/annotate/filesystem/settings.xml "open the file 'settings.xml'")
  - language = lang
  - timezone = time
  - dialogue = dial
- [data](../../bin/annotate/filesystem/data.xml "open the file 'data.xml'")
  - recent files = recent
- [notebooks](../../bin/annotate/filesystem/notebooks.xml "open the file 'notebooks.xml'")
  - notebook
    - path
    - title
    - style &rarr; css
    - length in 'pages' = len
    - formatting rules (date at beginning?)
- [lists](../../bin/annotate/filesystem/lists.xml "open the file 'lists.xml'")
  - list
    - entries = ent

---

## **References**

- date
  - [python datetime module](https://docs.python.org/3/library/datetime.html "link to the datetime reference")
- list comprehensions
  +

## Quotes

- "Ist white space so the schwarze Materie of the notizprogramme" -Emma Dübner
- "bc in life u cant erase things and cant go back it just goes on and on" -Emma Dübner
