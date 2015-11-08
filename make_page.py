
import csv
import os

template = """
          <html>
            <head>
              <title>Paper overview</title>
            </head>
            <body>
              <h1>Paper overview</h1>
              <ul>
              {}
              </ul>
            </body>
          </html>
       """

elem = "<li>{}</li>"

contents = []

with open('./entries.csv') as f:
    for hsh, msg, link in csv.reader(f):
        item = elem.format('{} {} <a href="./data/{}">pdf</a>'.format(hsh, msg, link))
        contents.append(item)

page = template.format("\n".join(contents))

with open('index.html', 'w') as f:
    f.write(page)

