#!/usr/bin/python
import MySQLdb
import sys, os.path
import re

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="password1",
                     db="rapscheme")

cur = db.cursor()

artist = sys.argv[1].replace("'", "''")
track = sys.argv[2].replace("'", "''")
lyricFile = sys.argv[3]

if (len(sys.argv) == 5):
    year = sys.argv[4]
else:
    year = 0

with open(lyricFile) as f:
    lyrics =  f.read().replace("'", "''")
    f.seek(0)
    lyricsByLine = f.readlines()
    parsedLyrics = ""
    parsedVowels = ""
    parsedConsonants = ""
    parsedVowelsNoStress = ""
    parsedVowelConsonantBinary = ""
    parsedVowelStressOnly = ""

    for line in lyricsByLine:
        words = re.findall("[a-zA-Z'-]+", line)
        for word in words:
            word = word.upper().replace("'", "''")
            
            selectStatement = "SELECT pronunciation from pronunciations WHERE word='%s';" % (word)
            cur.execute(selectStatement)

            pronunciationResult = cur.fetchone()
            
            if pronunciationResult is not None:
                pronunciationList = pronunciationResult[0]
                parsedLyrics += pronunciationList + " "

                # Go through the list of phonemes for the word, split lyrics into
                # consonants/vowels.
                pronunciationList = pronunciationList.split(" ")
                for pronunciation in pronunciationList:
                    alphaNumericPronunciation =  re.findall("[A-Z0-2]+", pronunciation)[0]
                    stressNumber = re.findall("[0-2]+", pronunciation)
                    
                    alphaOnly = re.findall("[A-Z]+", alphaNumericPronunciation)[0];

                    selectStatement = "SELECT type from phonemes WHERE phoneme='%s';"  % (alphaOnly)
                    cur.execute(selectStatement)

                    typeResult = cur.fetchone()[0]

                    vowelList = ["vowel", "semivowel"]
                    if typeResult in vowelList:
                        parsedVowels += alphaNumericPronunciation + " "
                        parsedVowelsNoStress += alphaOnly + " "
                        parsedVowelConsonantBinary += "V "
                        
                        if len(stressNumber) == 1:
                            parsedVowelStressOnly += stressNumber[0] + " "
                        else:
                            parsedVowelStressOnly += "3 "
                            
                    else:
                        parsedConsonants += alphaNumericPronunciation + " "
                        parsedVowelConsonantBinary += "C "

        parsedLyrics += "\n"
        parsedVowels += "\n"
        parsedConsonants += "\n"
        parsedVowelsNoStress += "\n"
        parsedVowelConsonantBinary += "\n"
        parsedVowelStressOnly += "\n"

    insertString = "INSERT INTO lyrics (artist, track, year, lyrics, parsedLyrics, parsedVowels, parsedVowelsNoStress, parsedConsonants, parsedVowelConsonantBinary, parsedVowelStressOnly) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (artist, track, year, lyrics, parsedLyrics, parsedVowels, parsedVowelsNoStress, parsedConsonants, parsedVowelConsonantBinary, parsedVowelStressOnly)

    cur.execute(insertString)
    db.commit()

db.close()
