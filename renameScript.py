from pathlib import Path
import shutil
import glob

def findFiles(path) : return glob.glob(path)

labels = [
    "Apple" , 
    "Banana" , 
    "Mango" , 
    "Papaya" , 
    "Pear" , 
    "Watermelon"
]

for label in labels:
    path = Path(label)
    jpgFiles = findFiles(f"{path}/*.jpg")
    jpegFiles = findFiles(f"{path}/*.jpeg")
    mergedFiles = jpgFiles + jpegFiles
    for i in range(len(mergedFiles)):
        extension = mergedFiles[i].split("/")[1].split('.')[-1]
        shutil.copy(mergedFiles[i] , f"{path}/{label}-{i}.{extension}")