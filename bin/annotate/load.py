# loads all Notebooks, and opens them as rw
import xml.etree.ElementTree as etet
import os

pathlist = [".\\bin\\annotate\\filesystem\\settings.xml", ".\\bin\\annotate\\filesystem\\notebooks.xml", ".\\bin\\annotate\\filesystem\\lists.xml", ".\\bin\\annotate\\filesystem\\data.xml"]

def checkFilesExistCreateLoad(pathlist):
    # filesExistCreate
        for path in pathlist:
            # checks if files exist, and if not creates them
            try:
                if os.path.exists(os.path.dirname(path)) == True:
                    print("path exists")
                else:
                    os.makedirs(os.path.dirname(path))
                    open(path, "x").close()
                    print("file '{}' at '{}' has been created".format(os.path.split(path)[1], os.path.dirname(path)))
            except:
                print("Could not create path/file. Failed at '{}'.".format(path))
            # # load
            # # TODO think about loading all seperately, because you can access them easier that way; or else how do i access a single one of these xml files?
            # try:

            # except:

checkFilesExistCreateLoad(pathlist)


# SETTINGS:
# settings -> root
# [n]user(id, name) -> user settings
# [n][n]preset(name) -> presets of settings
# [n][n][0]lang -> setting the language
# [n][n][1]time -> time format container
# [n][n][1][n]tformat(name, format) -> setting the time format
# [n][n][2]font(fontFamily, fontSize) -> font family + size


settings = etet.parse(".\\bin\\annotate\\filesystem\\settings.xml")
sroot = settings.getroot()
# print(sroot[0].tag)

for user in sroot:
    print("{} = {}".format(user.tag, user.attrib["name"]))
    for preset in user:
        print("{} = {}".format(preset.tag, preset.attrib["name"]))
        for presetsettings in preset:
            if presetsettings.tag == "time":
                for tformat in presetsettings:
                    print(tformat.attrib)
            # elif presetsettings.tag == "font":
            else:
                print("{}, {}".format(presetsettings.tag, presetsettings.text))


settings.write(".\\bin\\annotate\\filesystem\\settings.xml")

# load recent files from res/filesystem/data.xml
recentsPath = "lala"

# read from res/filesystem/notebooks.xml
notebooksPath = "uiiui"


# TODO think about linking recent files with Notebook/List loading
# TODO implement different settings for different users