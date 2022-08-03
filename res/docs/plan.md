<style>
  
  *{
    font-family: IBM Plex Mono;
  }

</style>

# Table of Contents

- [Table of Contents](#table-of-contents)
- [PLAN](#plan)
  - [**ORDER**](#order)
  - [**Modes**](#modes)
    - [GUI](#gui)
    - [TERMINAL](#terminal)
  - [**Systems**](#systems)
    - [*NOTEBOOK* system](#notebook-system)
    - [*LIST* system](#list-system)
  - [**Settings**](#settings)
  - [**Functions**](#functions)
    - [DATE](#date)
  - [**Modularisation**](#modularisation)
    - [Python](#python)
    - [XML](#xml)
  - [**References**](#references)

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

- side panel(s)
  - choose notebook

  -

### TERMINAL

commandline implementation with same features

- new
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

## **Settings**

- timezone & date
- language
  - *var (int):* **lang**
  - english (0), german (1)

---

## **Functions**

### DATE

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
- gui
  - handles all the [gui](#gui "read about the GUI")
- terminal
  - handles [terminal execution](#terminal "read about the terminal execution")

### XML

- [settings](../filesystem/settings.xml "open the file 'settings.xml'")
  - language = lang
  - timezone = time
- [data](../filesystem/data.xml "open the file 'data.xml'")
  - recent files = "recent"
- [notebooks](../filesystem/notebooks.xml "open the file 'notebooks.xml'")
  - notebook
    - path
    - title
    - style &rarr; css
    - length in 'pages' = len
- [lists](../filesystem/lists.xml "open the file 'lists.xml'")
  - list
    - entries = ent

---

## **References**

- date
  - [python datetime module](https://docs.python.org/3/library/datetime.html "link to the datetime reference")
- list comprehensions
  +
