#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('firstTest.db')
	
with con:
	cur = con.cursor()
	cur.execute("DROP TABLE Cars")
	cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
	cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
	cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',52642)")
	cur.execute("INSERT INTO Cars VALUES(3,'Audi',52642)")
	cur.execute("INSERT INTO Cars VALUES(4,'Audi',52642)")
	cur.execute("INSERT INTO Cars VALUES(5,'Audi',52642)")
	cur.execute("INSERT INTO Cars VALUES(6,'Audi',52642)")
	cur.execute("INSERT INTO Cars VALUES(7,'Audi',52642)")
	cur.execute("INSERT INTO Cars VALUES(8,'Audi',52642)")
	cur.execute("INSERT INTO Cars VALUES(9,'Audi',52642)")
	