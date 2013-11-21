#/usr/bin/python
from alignment.sequence import Sequence
from alignment.vocabulary import Vocabulary
from alignment.sequencealigner import SimpleScoring, LocalSequenceAligner

import re 
import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="password1",
                     db="rapscheme")

cur = db.cursor()

parsedLyricList = ["parsedLyrics", "parsedVowels", "parsedConsonants", "parsedVowelNoStress", "parsedVowelConsonantBinary", "parsedVowelStressOnly"]

track1 = "King of Rock"
track2 = "Tricky"
track3 = "Juicy"

selectStatement1 = "SELECT parsedVowels from lyrics where track='%s';" % (track1)
selectStatement2 = "SELECT parsedVowels from lyrics where track='%s';" % (track2)
selectStatement3 = "SELECT parsedVowels from lyrics where track='%s';" % (track3)

cur.execute(selectStatement1)
lyrics1 = cur.fetchone()

cur.execute(selectStatement2)
lyrics2 = cur.fetchone()

cur.execute(selectStatement3)
lyrics3 = cur.fetchone()

scoring = SimpleScoring(2, -2)
aligner = LocalSequenceAligner(scoring, -2)

a = Sequence(lyrics1[0].split(" "))
b = Sequence(lyrics2[0].split(" "))
c = Sequence(lyrics3[0].split(" "))

# Create a vocabulary and encode the sequences.
v = Vocabulary()
aEncoded = v.encodeSequence(a)
bEncoded = v.encodeSequence(b)
cEncoded = v.encodeSequence(c)

print "RUN DMC VS BIGGIE SMALLS"

#Create a scoring and align sequences using the loacl aligner.
score, encodeds = aligner.align(aEncoded, cEncoded, backtrace=True)

#Iterate over optimal alignments and print them.
if
    alignment = v.decodeSequenceAlignment(encodeds[0])
    print alignment
    print 'Alignment score:', alignment.score
    print 'Percent identity:', alignment.percentIdentity()
    print

print "RUN DMC VS RUN DMC"

#Create a scoring and align sequences using the loacl aligner.
score, encodeds = aligner.align(aEncoded, bEncoded, backtrace=True)

#Iterate over optimal alignments and print them.
for encoded in encodeds:
    alignment = v.decodeSequenceAlignment(encoded)
    print alignment
    print 'Alignment score:', alignment.score
    print 'Percent identity:', alignment.percentIdentity()
    print


#Create a scoring and align sequences with the global aligner.

