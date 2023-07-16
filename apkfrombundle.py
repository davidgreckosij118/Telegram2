import sys
from zipfile import ZipFile

def compareFiles(first, second):
 while True:
        firstBytes = first.read(4096)
