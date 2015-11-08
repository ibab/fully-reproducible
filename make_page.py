
import csv
import os

template = """
          <html>
            <head>
              <title>Paper overview</title>
            </head>
            <body>
              <h1>Paper overview</h1>
              <table>
              <tr>
                <th>hash</th>
                <th>message</th>
                <th>PDF</th>
              </tr>
              {}
              </table>
            </body>
          </html>
       """

contents = []

with open('./entries.csv') as f:
    for hsh, msg, link in list(csv.reader(f))[::-1]:
        item = '<tr><td>{}</td><td>{}</td><td><a href="./{}">pdf</a></td></tr>'.format(hsh, msg, link)
        contents.append(item)

page = template.format("\n".join(contents))

with open('index.html', 'w') as f:
    f.write(page)

