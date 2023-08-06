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
  secondList = list(filter(lambda secondInfo: secondInfo.filename not in FILES_TO_IGNORE, bundleZip.infolist()))
  
    for apkInfo in firstList:
        if (apkInfo.filename.startswith("META-INF/")):
     continue
        if (apkInfo.filename.startswith("res/")):
 continue
        if (apkInfo.filename.startswith("AndroidManifest.xml")):
   continue

        found = False
   for bundleInfo in secondList:
 fileName = bundleInfo.filename
 fileName = remove_prefix(fileName, "base/root/")
            fileName = remove_prefix(fileName, "base/dex/")
 fileName = remove_prefix(fileName, "base/manifest/")
            fileName = remove_prefix(fileName, "base/")
if (fileName.startswith("BUNDLE-METADATA")):
                fileName = "META-INF" + remove_prefix(fileName, "BUNDLE-METADATA/")
 if fileName == apkInfo.filename:
 found = True
                firstFile = apkZip.open(apkInfo, 'r')
 secondFile = bundleZip.open(bundleInfo, 'r')
                if compareFiles(firstFile, secondFile) != True:
