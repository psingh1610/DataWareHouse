import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE users"
song_table_drop = "DROP TABLE songs"
artist_table_drop = "DROP TABLE artists"
time_table_drop = "DROP TABLE time"

# CREATE TABLES

staging_events_table_create= ("""CREATE TABLE IF NOT EXISTS staging_events
(artist text,auth text,firstName text,gender text,itemInSession integer,lastName text,length float,level text,location text,method text,page text,registration float,sessionId integer,song text,status integer,ts bigint,userAgent text,userId integer
""")

staging_songs_table_create = ("""CREATE TABLE IF NOT EXISTS staging_songs
(num_songs integer,artist_id text,artist_latitude float,artist_longitude float,artist_location text,artist_name text,song_id text,title text,duration float,year integer
""")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays
(songplay_id serial PRIMARY KEY, start_time bigint NOT NULL, user_id integer NOT NULL, level text, song_id text, artist_id text, session_id integer, location text, user_agent text
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
user_id integer PRIMARY KEY NOT NULL , first_name text, last_name text, gender text, level text)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
song_id text NOT NULL PRIMARY KEY , title text, artist_id text, year integer, duration float)
""")

artist_table_create = ("""CREATE TABLE  IF NOT EXISTS artists (
artist_id varchar(255) PRIMARY KEY NOT NULL , name text, location text, latitude float, longitude float)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
start_time bigint NOT NULL PRIMARY KEY, hour integer, day integer, week integer, month integer, year integer, weekday integer)
""")

# STAGING TABLES

staging_events_copy = ("""COPY staging_events
FROM <s3://udacity-dend/log_data>
CREDENTIALS 'aws_iam_role=arn:aws:iam::158827665655:role/myRedshiftRole'
REGION 'us-east-1'
""")

staging_songs_copy = ("""COPY staging_songs
FROM <s3://udacity-dend/song_data>
CREDENTIALS 'aws_iam_role=<arn:aws:iam::158827665655:role/myRedshiftRole>'
REGION 'us-east-1'
""")

# FINAL TABLES

songplay_table_insert = ("""insert into songplays(start_time,user_id,level,song_id, artist_id, session_id,location,user_agent)
values(%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""insert into users(user_id,first_name,last_name,gender,level)
values(%s,%s,%s,%s,%s)
ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""insert into songs(song_id,title,artist_id,duration,year)
values(%s,%s,%s,%s,%s) 
ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""insert into artists(artist_id,name,location,latitude,longitude)
values(%s,%s,%s,%s,%s)
ON CONFLICT (artist_id) DO NOTHING
""")

time_table_insert = ("""insert into time(start_time,hour,day,week,month,year,weekday)
values(%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (start_time) DO NOTHING
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
