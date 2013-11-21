#/usr/bin/python
from alignment.sequence import Sequence
from alignment.vocabulary import Vocabulary
from alignment.sequencealigner import SimpleScoring, GlobalSequenceAligner

import re 
import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="password1",
                     db="rapscheme")

cur = db.cursor()

parsedLyricList = ["parsedLyrics", "parsedVowels", "parsedConsonants", "parsedVowelsNoStress", "parsedVowelConsonantBinary", "parsedVowelStressOnly"]

track1 = "Juicy"

selectParsedVowels = "SELECT parsedVowels from lyrics where track='%s';" % (track1)
selectLyrics = "SELECT lyrics from lyrics where track='%s';" % (track1)
selectVowelStressOnly = "SELECT parsedVowelStressOnly from lyrics where track='%s';" % (track1)

cur.execute(selectParsedVowels)
lyricsBars = cur.fetchone()[0].split("\n\n")


cur.execute(selectLyrics)
realLyricsBars = cur.fetchone()[0].split("\n\n")

cur.execute(selectVowelStressOnly)
stressBars = cur.fetchone()[0].split("\n\n")

scoring = SimpleScoring(2, -1)
aligner = GlobalSequenceAligner(scoring, -2)

v = Vocabulary()

alignments = []
"""
for i in range(0, len(lyricsBars)):
    barLines = lyricsBars[i].split("\n")
    realBarLines = realLyricsBars[i].split("\n")

    for x in range(0, len(barLines)):
        for y in range(x+1, len(barLines)):
            if barLines[x] == "\n" or barLines[y] == "\n":
                break

            wordsX = barLines[x].split(" ")
            del wordsX[-1]
            wordsX.append("\n")
            
            wordsY = barLines[y].split(" ")
            del wordsY[-1]
            wordsY.append("\n")
            
            seq1 = v.encodeSequence(Sequence(wordsX))
            seq2 = v.encodeSequence(Sequence(wordsY))

            score, encodeds = aligner.align(seq1, seq2, backtrace=True)

            alignment = v.decodeSequenceAlignment(encodeds[0])

            
            if len(alignment) > 1  and alignment.score > 2:
                print "--------------------------------------------"
                print 'Alignment score: ', alignment.score
                print 'Percent identity: ', alignment.percentIdentity()
                print 'Original lines: '
                print alignment
                print realBarLines[x]
                print realBarLines[y]
"""
"""
v = Vocabulary()
for i in range(0, len(stressBars)):
    for j in range(i+1, len(stressBars)):
        wordsX = stressBars[i].split(" ")
        del wordsX[-1]
        wordsX.append("\n")

        wordsY = stressBars[j].split(" ")
        del wordsY[-1]
        wordsY.append("\n")

        seq1 = v.encodeSequence(Sequence(wordsX))
        seq2 = v.encodeSequence(Sequence(wordsY))

        score, encodeds = aligner.align(seq1, seq2, backtrace=True)

        alignment = v.decodeSequenceAlignment(encodeds[0])
            
        if len(alignment) > 1 and alignment.score > 2:
            print "--------------------------------------------"
            print 'Alignment score: ', alignment.score
            print 'Percent identity: ', alignment.percentIdentity()
            print 'Original lines: '
            print alignment
            print realLyricsBars[i]
            print realLyricsBars[j]
"""

#a = Sequence(lyrics1[0].split())

# Create a vocabulary and encode the sequences.
#v = Vocabulary()
#aEncoded = v.encodeSequence(a)
#bEncoded = v.encodeSequence(b)
#cEncoded = v.encodeSequence(c)

#print "RUN DMC KING OF ROCK RHYME SCHEME"

#Create a scoring and align sequences using the loacl aligner.
#score, encodeds = aligner.align(aEncoded, cEncoded, backtrace=True)

#Iterate over optimal alignments and print them.
#for encoded in encodeds:
#    alignment = v.decodeSequenceAlignment(encoded)
#    print alignment
#    print 'Alignment score:', alignment.score
#    print 'Percent identity:', alignment.percentIdentity()
#    print

