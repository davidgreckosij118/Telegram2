import sys
from zipfile import ZipFile

def compareFiles(first, second):
 while True:
        firstBytes = first.read(4096)
if firstBytes != secondBytes:
            return False

        if firstBytes == b"" and secondBytes == b"":
            break

    return True

def remove_prefix(text, prefix):
  if text.startswith(prefix):
   return text[len(prefix):]
    return text
