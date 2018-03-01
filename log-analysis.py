#!/usr/bin/env python2
#
# This program is open source.  For license terms, see the LICENSE file.
#
# Reporting tool that prints out reports in plain text based on the data in
# the database "news"
# Reports:
# 1) The most popular three articles of all time
# 2) The most popular article authors of all time
# 3) Days with more than 1% of requests that lead to errors

# Module import for PostgreSQL
import psycopg2

# Constants with database name, querys and titles
DBNAME = "news"
APP_TITLE = "\n\nLog Analysis"
TOP_ARTICLES_QUERY = "select a.title, t.count from articles a, articles_top_desc t where a.slug like t.slug limit 3"
TOP_ARTICLE_TITLE = "\n\nThe most popular three articles of all time are:\n"
TOP_AUTHORS_QUERY = "select au.name as author, sum(top.count) as count from authors au, articles ar, articles_top_desc top where au.id = ar.author and ar.slug = top.slug group by au.name order by count desc"
TOP_AUTHORS_TITLE = "\n\nThe most popular article authors of all time are:\n"
ACCESS_ERRORS_QUERY = "select to_char(d.day, 'Month DD, YYYY'), d.percentage from (select l200.day, l200.count, l404.count, round(((l404.count * 100)::numeric / (l200.count + l404.count)::numeric),1) as percentage from (select date_trunc('day', time) as day, count(*) as count from log where status like '200 OK' group by day) as l200, (select date_trunc('day', time) as day, count(*) as count from log where status like '404 NOT FOUND' group by day) as l404 where l200.day = l404.day order by percentage desc) as d where percentage > 1"
ACCESS_ERRORS_TITLE = "\n\nDays with more than 1% of requests that lead to errors:\n"
FOOTER = "\n\nGabriel Almeida - Udacity Student - v1.0\n"

# Print the app title
print APP_TITLE

# Database connection creation, and cursor
db = psycopg2.connect(database=DBNAME)
c = db.cursor()

# Execution of the query to fetch in the database the data for the elaboration
# of the report "The most popular three articles of all time"
c.execute(TOP_ARTICLES_QUERY)
results = c.fetchall()

# Print the report title "The most popular three articles of all time"
print TOP_ARTICLE_TITLE

# Loop to print the results of the report "The most popular three articles of
# all time"
for result in results:
    print "> " + result[0] + " - " + str(result[1]) + " views"

# Execution of the query to fetch in the database the data for the elaboration
# of the report "The most popular article authors of all time"
c.execute(TOP_AUTHORS_QUERY)
results = c.fetchall()

# Print the report title "The most popular article authors of all time"
print TOP_AUTHORS_TITLE

# Loop to print the results of the report "The most popular article authors of
# all time"
for result in results:
    print "> " + result[0] + " - " + str(result[1]) + " views"

# Execution of the query to fetch in the database the data for the elaboration
# of the report "Days with more than 1% of requests that lead to errors"
c.execute(ACCESS_ERRORS_QUERY)
results = c.fetchall()

# Print the report title "Days with more than 1% requests that lead to errors"
print ACCESS_ERRORS_TITLE

# Loop to print the results of the report "Days with more than 1% requests that
# lead to errors"
for result in results:
    print "> " + result[0] + " - " + str(result[1]) + "% errors"

# Close database connection
db.close()

# Print footer information
print FOOTER
