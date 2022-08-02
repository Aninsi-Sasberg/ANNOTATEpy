<style>
  
  *{
    font-family: IBM Plex Mono;
  }



</style>


# **PLAN**

## ORDER

```python
"OVERTHINK THIS". :)))))))))))))))
```
1. load files r
    + load config
    + load recent file list (recentFiles, located in [data.xml](../filesystem/data.xml "open the file 'data.xml'"))
    + load notebooks/lists r (read so preview can be shown)
2. open last notebook/list
    + open notebook rw
3. open window

---

## ___Modes___

## GUI
single window with toggleable side panel(s)
+ side panel(s)
  + choose notebook
  + 

## TERMINAL
commandline implementation with same features
+ new
+ choose (like ANNOTATEps with 4 letter definition)
+ write
+ 

---

## ___Systems___

## _NOTEBOOK_ system

+ __savefile__ (Saves locations of all the pages, as well as a copy of all pages in itself)
  + path
  + name
  + date (created, last edited, for each page)
+ __pages__
  + title (e.g. date (possibly regex), custom, page number, regex)
  + number
+ __filesystem__ (lets people create fs based on page structure, folders are named by page title, and some regex)
+ __attributes__
  + _title:_
  + _4chartitle:_ for easy Notebook choosing in Terminal 
  + _style:_ can do CSS formatting
  + _length:_ length of Notebook in Pages
  + 

## _LIST_ system

+ instead of different pages, you get list elements, all saved in one file
+ examples include old ANNOTATEps project 

---

## Settings

+ timezone & date
+ language
  + _var (int):_ __lang__
  + english (0), german (1)

---

## Functions

## DATE

<mark>
ADD STUFF.
</mark>

---

## Modularisation

+ [main](../bin/annotate/main.py "open the file 'main.py'")
  + run all methods and so on in [the correct order](#order "read about the order of processes")
+ load
  + loads all Notebooks, and opens them as rw
+ [date](../bin/annotate/date.py "open the file 'date.py'")
  + handles all [date formatting](#date "read about date formatting")
+ gui
  + handles all the [gui](#gui "read about the GUI")
+ terminal
  + handles [terminal execution](#terminal "read about the terminal execution")


+ [settings](../filesystem/settings.xml "open the file 'settings.xml'")
  + language = lang
  + timezone = time
+ [data](../filesystem/data.xml "open the file 'data.xml'")
  + recent files = "recent"
+ [notebooks](../filesystem/notebooks.xml "open the file 'notebooks.xml'")
  + notebook
    + path
    + title
    + style -> css
    + length in 'pages' = len
+ [lists](../filesystem/lists.xml "open the file 'lists.xml'")
  + list
    + entries = ent

---

## References

+ date
  + [python datetime module](https://docs.python.org/3/library/datetime.html "link to the datetime reference")
+ list comprehensions
  + 