#!/usr/bin/env python2
#
# Displays various statistics about website usage

import psycopg2
import sys

try:
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()
except:
    print("Error: Unable to connect to the database")
    sys.exit(1)

# display the three most popular articles of all time and their views
request = """
select title, views from (
select path, count(*) as views from log group by path
order by views desc limit 3 offset 1)
as toparticles, articles where
concat('/article/', slug) = path order by views desc;
"""
cursor.execute(request)
results = cursor.fetchall()
print('The most viewed articles are:')
for row in results:
    print('    ' + str(row[0]) + ' Views: ' + str(row[1]))


# display authors and view counts in descending order
request = """
select authors.name, sum(views) from (
select path, count(*) as views from log group by path
order by views desc offset 1)
as toparticles join articles on concat('/article/', slug) = path
join authors on author = authors.id
group by authors.name order by count(views) desc;
"""
cursor.execute(request)
results = cursor.fetchall()
print('\nAuthors and current view counts are: ')
for row in results:
    print('    ' + '{0: <32}'.format(str(row[0])) + ' Views: ' + str(row[1]))

# display dates on which error rate exceeded one percent and the error rate
request = """
select traffic.date, (errors * 100.0 / total) as error from
(select date_trunc('day', time) as date, count(*) as total
from log group by date) as traffic,
(select date_trunc('day',time) as date, count(*) as errors from log
where not status like '%200%' group by date) as errortable
where errortable.date = traffic.date and (errors * 100.0 / total) >= 1;
"""
cursor.execute(request)
print("\nDates on which the error rate exceeded 1%:")
results = cursor.fetchall()
for row in results:
    print('    Date: ' + str(row[0])[:10] +
          '           Error Rate: ' + str(row[1])[:4] + '%')
conn.close()
print('\n')
