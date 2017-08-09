from os import listdir, curdir
from re import sub
from win32api import MessageBox
import easygui as ui

def getDirectory():
    path = ui.diropenbox("select file containing logs to convert", pname)
    if path == None:
        path = '.' # used as current directory in os lib

    if listdir( path ) == None:
        return [] # blank iterable to skip for loop

    r = ui.multchoicebox( "Select the files you wish to convert:", pname, [file for file in listdir( path ) if "GT-MP-" and ".log" in file] )

    if r == None:
        return []
    
    return r

pname = "GT-MP Chatlog Extractor Tool"

filters = ui.multchoicebox( "What would you like to filter (remove) from your chatlogs?", pname, ["Timestamps", "[N]", "((/b))", "PMs", "[OOC]"] )

for file in getDirectory():
    with open(file) as log:
        with open("CHATLOG-" + file.strip(".log") + ".txt", 'w+') as chatlog:
            chatlog.write(pname + " v2.0 (via github user charlw & mt-gaming user Trippy)\n")
            for line in log:

                # Filtering:
                if "[ClassicChat]" in line[:37]:
                    timestamp = ''

                    
                    if filters:
                        if "[N]" in filters and line[48:51] == "[N]":
                            continue
                        if "((/b))" in filters and line[48:50] == "((":
                            continue
                        if "PMs" in filters and line[48:50] == "PM":
                            continue
                        if "[OOC]" in filters and line[48:53] == "[OOC]":
                            continue
                        if "Timestamps" not in filters:
                            timestamp = line[:15] # save timestamp before killed
                        
                    # Nuke Headers:
                    line = line[37:]

                    
                    # Cleaning:
                    if "~" in line:
                        if "~#" in line[:2]:
                            line = line[11:]
                        else:
                            line = sub('~[A-Za-z]~', '', line)

                    #Writing:
                    if timestamp != '':
                        chatlog.write(timestamp + line)
                    else:
                        chatlog.write(line)



if not any ( "CHATLOG" in filename for filename in listdir(curdir) ):
    MessageBox(0, "No logs converted. \n\nEnsure you have selected at least one log from a folder containing logs!", "GT-MP Chatlog Extractor Tool")

