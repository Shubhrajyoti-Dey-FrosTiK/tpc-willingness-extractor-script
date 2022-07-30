import os
import csv

def getFiles(directory):
    files = [f for f in os.listdir(directory)]
    return files

def checkFile(fileTag,extension,fileArray):
    files = []
    for f in fileArray:
        if(fileTag and fileTag.lower() not in f.lower()):
            continue
        if(f.endswith(extension)):
            if((fileTag != "RESUMES" and f != "RESUMES.zip") or (fileTag == "RESUMES" and f == "RESUMES.zip")):
                files.append(f);
    return files;


files = getFiles(".")
print(files)

willingnessFile = checkFile("","csv",files)

if(len(willingnessFile) > 0):
    willingnessFile = willingnessFile[0]
    print("Found the file: " + willingnessFile)
else:
    print("No file .csv found")
    exit()

updatedWillingness = checkFile("Willingness_"+willingnessFile,"csv",files)
print(updatedWillingness)

if(len(updatedWillingness) > 0):
    os.remove(updatedWillingness[0])

with open(willingnessFile, "r") as source:
    reader = csv.reader(source)
      
    with open("Willingness_"+willingnessFile, "w") as result:
        writer = csv.writer(result)
        for r in reader:
            writer.writerow((r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[16],r[17],r[18],r[19],r[20],r[22],r[23],r[24],r[25],r[26],r[27],r[28],r[29],r[30],r[32],r[33],r[34],r[36],r[37],r[38],r[39],r[40],r[41],r[42],r[43],r[44],r[45],r[46],r[47],r[48],r[49],r[50],r[51],r[52],r[53],r[54],r[55],r[56],r[57],r[58],r[59],r[60],r[61],r[62],r[63],r[64],r[65],r[66],r[67]))


print("Updated willingness file created")