from os import listdir, curdir
from re import sub
from win32api import MessageBox


for file in listdir(curdir):
    if "GT-MP-" in file and ".log" in file:
        with open(file) as log:
            with open("CHATLOG-" + file.strip(".log") + ".txt", 'w+') as chatlog:
                chatlog.write("GT-MP Chatlog Extractor Tool v1.0 (via github user charlw & mt-gaming user Trippy)\n")
                for line in log:
                    if "[ClassicChat]" in line[:37]:
                        line = line[37:]
                        if "~" in line:
                            if "~#" in line[:2]:
                                line = line[11:]
                            else:
                                line = sub('~[A-Za-z]~', '', line)
                        chatlog.write(line)



if not any ( "CHATLOG" in filename for filename in listdir(curdir) ):
    MessageBox(0, "Ensure GT-MP Chatlog Extractor.exe is placed in folder containing logs you want to convert to chatlogs!", "GT-MP Chatlog Extractor Tool")

