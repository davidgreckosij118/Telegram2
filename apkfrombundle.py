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

def compareApkFromBundle(bundle, apk):
    FILES_TO_IGNORE = ["resources.arsc", "stamp-cert-sha256"]

    apkZip = ZipFile(apk, 'r')
    bundleZip = ZipFile(bundle, 'r')

    firstList = list(filter(lambda info: info.filename not in FILES_TO_IGNORE, apkZip.infolist()))
