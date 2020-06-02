# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS times"

# CREATE TABLES

# songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
songplay_table_create = ("""
CREATE TABLE songplays (songplay_id serial primary key, start_time timestamp, user_id int, level varchar(20), song_id varchar (255), artist_id varchar (255), session_id varchar(255), location varchar(255), user_agent varchar(255));
""")

# user_id, first_name, last_name, gender, level
user_table_create = ("""
CREATE TABLE users ( user_id int, first_name varchar (255), last_name varchar (255), gender char(1), level varchar(10));
""")

# song_id, title, artist_id, year, duration
song_table_create = ("""
CREATE TABLE songs (song_id varchar(255), title varchar (255), artist_id varchar (255), year int, duration int)
""")

# artist_id, name, location, latitude, longitude
artist_table_create = ("""
CREATE TABLE artists (artist_id varchar (255), name varchar(255), location varchar(255), latitude int null , longitude int null )
""")

# start_time, hour, day, week, month, year, weekday
time_table_create = ("""
CREATE TABLE times (start_time timestamp , hour int, day int, week int, month int, year int, weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""
INSERT INTO times (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
    SELECT s.song_id, s.artist_id FROM artists a JOIN songs s ON s.artist_id = a.artist_id WHERE s.title = %s AND a.name = %s AND s.duration = %s
""")

# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
