# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 15:37:23 2024

@author: Mihai
"""

# Drop tables

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
time_table_drop = "DROP TABLE IF EXISTS time;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"

# Create tables

songplay_table_create = ("""
CREATE TABLE songplays(
    songplay_id int PRIMARY KEY,
    start_time bigint REFERENCES time(start_time) ON DELETE RESTRICT,
    user_id int REFERENCES users(user_id) ON DELETE RESTRICT,
    level varchar,
    song_id varchar REFERENCES songs(song_id) ON DELETE RESTRICT,
    artist_id varchar REFERENCES artists(artist_id) ON DELETE RESTRICT,
    session_id int,
    location varchar,
    user_agent varchar
    );
""")


user_table_create = ("""
CREATE TABLE users(
    user_id int PRIMARY KEY,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar);
""")



song_table_create = ("""
CREATE TABLE songs(
    song_id varchar PRIMARY KEY,
    title varchar,
    artist_id varchar,
    duration float);
""")


time_table_create = ("""
CREATE TABLE time(
    start_time bigint PRIMARY KEY,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int);
""")


artist_table_create = ("""
CREATE TABLE artists(
    artist_id varchar PRIMARY KEY,
    name varchar,
    location varchar,
    latitude float,
    longitude float);
""")


# Insert records

songplay_table_insert = ("""
INSERT INTO songplays(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT(songplay_id)
DO NOTHING;
""")


user_table_insert = ("""
INSERT INTO users(user_id, first_name, last_name, gender, level)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT(user_id)
DO UPDATE
SET level = excluded.level;
""")


song_table_insert = ("""
INSERT INTO songs(song_id, title, artist_id, duration)
VALUES(%s, %s, %s, %s)
ON CONFLICT(song_id)
DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) 
DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) 
DO NOTHING;
""")


# Find songs

song_select = ("""
SELECT s.song_id, a.artist_id FROM songs s
JOIN artists a ON s.artist_id = a.artist_id
WHERE s.title = %s AND a.name = %s AND s.duration = %s;
""")


# Query list


create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, song_table_drop, artist_table_drop, time_table_drop, songplay_table_drop]
















