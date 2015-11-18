
import csv
import os

template = """
          <html>
            <head>
              <title>Paper overview</title>
              <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">
            </head>
            <body>
              <div class="container">
                  <h1>Paper overview</h1>
                  <table class="table">
                  <tr>
                    <th>message</th>
                    <th>PDF</th>
                  </tr>
                  {}
                  </table>
              </div>
            </body>
          </html>
       """

contents = []

with open('./entries.csv') as f:
    for hsh, msg, link in list(csv.reader(f))[::-1]:
        item = '<tr><td class="col-md-5">{}</td><td><a href="./{}">pdf</a></td></tr>'.format(msg, link)
        contents.append(item)

page = template.format("\n".join(contents))

with open('index.html', 'w') as f:
    f.write(page)

