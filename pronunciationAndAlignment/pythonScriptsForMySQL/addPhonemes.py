#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user='root',
                     passwd='password1',
                     db='rapscheme')

cur = db.cursor()

with open('../cmuPronunciation/cmudict.0.7a.phones') as f:
    content = f.readlines()

    for line in content:
        line = line.split("\t");
        phoneme = line[0].replace("'", "''")
        # Strip newline at the end
        phonemeType = line[1].split("\n")[0].replace("'", "''")
        
        insertString = "INSERT INTO phonemes (phoneme, type) VALUES ('%s', '%s');" % (phoneme, phonemeType)
        print insertString
        cur.execute(insertString)
        db.commit()

db.close()
