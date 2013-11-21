#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user='root',
                     passwd='password1',
                     db='rapscheme')

cur = db.cursor()

with open('../cmuPronunciation/cmudict.0.7a') as f:
    content = f.readlines()

    count = 0
    for line in content:
        if (line[0].isalpha()):
            line = line.split("  ");
            word = line[0].replace("'", "''");
            # Strip newline at the end.
            pronunciation = line[1].split("\n")[0].replace("'", "''");

            insertString = "INSERT INTO pronunciations(word, pronunciation) VALUES ('%s', '%s');" % (word, pronunciation)

            if count % 1000 == 0:
                print insertString

            cur.execute(insertString)
            db.commit()

            count += 1
    db.close()
