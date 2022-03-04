import sys
import os
import crypt
import argparse

def testPass(cryptPass: str, dictFile: str):
    salt = cryptPass[0:11]
    with open(dictFile, 'r') as dictionary:
        for word in dictionary.readlines():
            dictWord = word.strip('\n')
            wordHash = crypt.crypt(dictWord, salt)
            if wordHash == cryptPass:
                print("Found Password: {0}.".format(dictWord))
                return 

    print("Password Not Found.")
    return

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("passwordFile", help="An encrypted password file text. Each line contains the username and hashed password.")
    parser.add_argument("dictionaryFile", help="A word dictionary")
    args = parser.parse_args()

    passFile = args.passwordFile
    dictFile = args.dictionaryFile

    if not (os.path.isfile(passFile) and os.path.isfile(dictFile)):
        print("Error. File(s) doesn't exists.")
        exit(0)

    if not (os.access(passFile,os.R_OK) and os.access(dictFile, os.R_OK)):
        print("Error. File(s) have improper access permissions for user.")
        exit(0)

    with open(passFile) as file:
        for line in file.readlines():
            entry = line.split(':')
            cryptPassword = entry[1].strip(" ")
            print("Cracking Password For: {0}".format(entry[0]))
            testPass(cryptPass=cryptPassword, dictFile=dictFile)

if __name__ == "__main__":
    main()