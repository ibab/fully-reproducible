
import os

lst = os.listdir('./data')

pdfs = filter(lambda x: x.endswith('.pdf'), lst)

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

for pdf in pdfs:
    item = elem.format('<a href="./data/{}">{}</a>'.format(pdf, pdf))
    contents.append(item)

page = template.format("\n".join(contents))

with open('index.html', 'w') as f:
    f.write(page)

