# **PLAN**

## ORDER

1. load files r
    + load config
    + load recent file list
    + load notebooks r
2. open last notebook
    + open notebook r
3. open window

---

## ___Modes___

## GUI
single window with toggleable side panel(s)
+ side panel(s)
  + choose notebook
  + 

## COMMANDLINE
commandline implementation with same features
+ new
+ choose
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

## _LIST_ system

+ instead of different pages, you get list elements, all saved in one file
+ examples include old ANNOTATEps project 

---

## Settings

+ timezone & date
+ language
  + _var (int):_ __lang__
  + english (0), german (1)
+ 