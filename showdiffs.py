import os

PATH = r"C:\test" # Path to watching folder
FOLDER = os.path.join(PATH, "appended_data") # All diffs will be created in the folder "appended_data"

def start_watching(path):
    "Remembar all files and their number of letters"
    dic = {}
    os.chdir(path)
    for filename in os.listdir():
        if os.path.isfile(filename):
            with open(filename, "rt") as f:
                f.seek(0, 2)
                offset = f.tell()
                dic.update({filename:offset})
    return dic

def after(dic):
    "Writes down all the appended data to the file LOGFILE"
    os.chdir(PATH)
    if not os.path.isdir("appended_data"):
        os.mkdir("appended_data")
    for filename in os.listdir():
        if os.path.isfile(filename):
            offset = dic.get(filename, 0)
            newfile = os.path.join(FOLDER, filename)
            with open(filename, "rt") as f, open(newfile, "w") as log:
                f.seek(offset)
                data = f.read()
                if not data:
                    log.close()
                    os.remove(newfile)
                else:
                    if data[0] == "\n":
                        data = data[1:]
                    log.write(data)

snapshot = start_watching(PATH)

"""
Waiting for a logs will be created/appended
...
...
"""

after(snapshot)
