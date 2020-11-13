import os;
import sys;
filePathSrc="E:\\Dev\\MasterThesis_Rep\\UE_Project\\Source\\ThesisProject\\"
for root, dirs, files in os.walk(filePathSrc):
    for fn in files:
      if fn[-4:] == '.txt' or fn[-4:] == '.csv' or fn[-4:] == '.cpp' or fn[-2:] == '.h':
        notepad.open(root + "\\" + fn)
        console.write(root + "\\" + fn + "\r\n")
        notepad.runMenuCommand("Encoding", "Convert to UTF-8")
        notepad.save()
        notepad.close()