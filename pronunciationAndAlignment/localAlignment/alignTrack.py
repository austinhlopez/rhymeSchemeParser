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

selectStatement1 = "SELECT parsedLyrics, parsedVowels, parsedConsonants, parsedVowelsNoStress, parsedVowelConsonantBinary, parsedVowelStressOnly from lyrics where track='%s';" % (track1)
selectStatement2 = "SELECT parsedLyrics, parsedVowels, parsedConsonants, parsedVowelsNoStress, parsedVowelConsonantBinary, parsedVowelStressOnly from lyrics where track='%s';" % (track2)
selectStatement3 = "SELECT parsedLyrics, parsedVowels, parsedConsonants, parsedVowelsNoStress, parsedVowelConsonantBinary, parsedVowelStressOnly from lyrics where track='%s';" % (track3)

cur.execute(selectStatement)

lyricResult = cur.fetchone()

vocabularies = []

for x in range(0, len(parsedLyricList)):
    vocabularies.append(Vocabulary())

    lyricType = parsedLyricList[x]
    lyrics = lyricResult[x]

    splitByBar = lyrics.split("\n\n")
    splitByLine = lyrics.split("\n")

    #Create sequences to be aligned and encode them via the vocabulary.
    '''for bar in splitByBar:
        words = re.findall("[A-Za-z0-2']+", bar)

        if len(words) > 0:
            encodedBarSequence.append(vocabularies[x].encodeSequence(Sequence(words)))

    for line in splitByLine:
        words = re.findall("[A-Za-z0-2']+", line)
        
        if len(words) > 0:
            encodedLineSequence.append(vocabularies[x].encodeSequence(Sequence(words)))'''

    # Create a scoring and align the sequences using global aligner.
    scoring = SimpleScoring(2, -1)
    aligner = LocalSequenceAligner(scoring, -2)

    alignFunctionString = "aligner.align("

    print "----------------------------------------------"
    print lyricType
    print "BAR SEQUENCE ALIGNMENT"

    for y in range(0, len(encodedBarSequence)):
        alignFunctionString += "encodedBarSequence[%d], " % (y)
        
    alignFunctionString += "backtrace=True)"

    score, encodeds = evala(lignFunctionString)

    for encoded in encodeds:
        alignment = vocabularies[x].decodeSequenceAlignment(encoded)
        print alignment
        print 'Alignment score:', alignment.score
        print 'Percent identity:', alignment.percentIdentity
        print

    #Iterate over optimal alignments and print them.

    alignFunctionString = "aligner.align("

    print "--------------------------------------------"
    print lyricType
    print "LINE SEQUENCE ALIGNMENT"

    for y in range(0, len(encodedLineSequence)):
        alignFunctionString += "encodedLineSequence[%d], " % (y)
    alignFunctionString += "backtrace=True)"
    print alignFunctionString

    score, encodeds = eval(alignFunctionString)


    for encoded in encodeds:
        alignment = vocabularies[x].decodeSequenceAlignment(encoded)
        print alignment
        print 'Alignment score:', alignment.score
        print 'Percent identity:', alignment.percentIdentity
        print


    print "###########################################"

    #score, encodeds = exec alignFunctionString
