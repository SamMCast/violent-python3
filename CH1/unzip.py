import zipfile
import argparse
import os

def extractFile(zFile: zipfile.ZipFile, dictFile: str, verbose: bool = False):
    with open(dictFile, 'r') as dictionaryFile:
        trial = 0
        for line in dictionaryFile.readlines():
            password = line.strip("\n")
            try:
                if verbose:
                    print("Trial: {0} Attempting zip file crack with password {1}".format(trial +1, password))
                zFile.extractall(pwd=password.encode())
                print("Success. Password =", password)
                exit(0)
            except RuntimeError:
                 pass
            trial = trial +1
        if verbose:
            print("Unable to determine password upon performing {0} different passwords.".format(trial+1))
        else:
            print("Unable to find password after exhaustive search. ")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("zipFile", help="Password encrypted zipfile")
    parser.add_argument("dictionary", help="A wordlist file")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    zipFile = args.zipFile
    dictFile = args.dictionary
    verbose = args.verbose

    if not (os.path.isfile(zipFile) and zipfile.is_zipfile(zipFile.encode())):
        print("Error. First argument {0} is either not a regular zip file.".format(zipFile))
        exit(0)
    if not (os.path.isfile(dictFile) and os.access(dictFile, os.R_OK)):
        print("Error. Second argument {0} is either not a regular txt file")
        exit(0)
    

    zFile = zipfile.ZipFile(zipFile)
    extractFile(zFile, dictFile, verbose)


if __name__ == "__main__":
    main()