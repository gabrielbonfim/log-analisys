#! python2.7
import psycopg2

db = psycopg2.connect(database = "news")

QUERY_TOP_ARTICLES = "select a.title, t.count from articles a, articles_top_desc t where a.slug like t.slug limit 3"

c = db.cursor

c.execute(QUERY_TOP_ARTICLES)

results = c.fetchall()

print results

db.close()