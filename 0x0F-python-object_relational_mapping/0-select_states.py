#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat April  8 09:05:11 2023
@author:Kris Adelowo
"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=data, port=3306)
    cur = db.cursor()
    num_rows = cur.execute('SELECT * FROM states ORDER BY states.id;')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
