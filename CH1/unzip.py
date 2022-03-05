import zipfile
import argparse
import os
from threading import Thread, Lock

def extractFile(zFile: zipfile.ZipFile, password: str):
    try:
        zFile.extractall(pwd=password.encode())
        print("Success. Password =", password)
        exit(0)
    except RuntimeError:
            pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("zipFile", help="Password encrypted zipfile")
    parser.add_argument("dictionary", help="A wordlist file")
    args = parser.parse_args()

    zipFile = args.zipFile
    dictFile = args.dictionary

    if not (os.path.isfile(zipFile) and zipfile.is_zipfile(zipFile.encode())):
        print("Error. First argument {0} is either not a regular zip file.".format(zipFile))
        exit(0)
    if not (os.path.isfile(dictFile) and os.access(dictFile, os.R_OK)):
        print("Error. Second argument {0} is either not a regular txt file")
        exit(0)
    

    zFile = zipfile.ZipFile(zipFile)
    lock = Lock()
    with open(dictFile, 'r') as dictFile:
        for line in dictFile.readlines():
            password = line.strip('\n')
            t = Thread(target=extractFile, kwargs={"zFile": zFile, "password": password})
            t.start()
    


if __name__ == "__main__":
    main()