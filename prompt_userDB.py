#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 16:53:12 2025

@author: madisonskinner
"""

import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="school_reviews",
    user="postgres",
    password="password",
    host="localhost"
)
cur = conn.cursor()

# Get user input
user_id = int(input("Enter user ID: "))
professor_id = int(input("Enter professor ID: "))

# Insert user input into the table
try:
    cur.execute(
        """
        INSERT INTO user_professors (user_id, professor_id, is_valid)
        VALUES (%s, %s, TRUE)
        ON CONFLICT (user_id, professor_id) DO UPDATE 
        SET is_valid = EXCLUDED.is_valid;
        """,
        (user_id, professor_id)
    )
    conn.commit()
    print("Data inserted successfully!")
except Exception as e:
    print("Error:", e)
    conn.rollback()

# Verify the data
cur.execute("SELECT * FROM user_professors WHERE user_id = %s;", (user_id,))
rows = cur.fetchall()

print("\nUpdated Table Data:")
for row in rows:
    print(row)

# Close connection
cur.close()
conn.close()
