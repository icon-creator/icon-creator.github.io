from PIL import Image

# Define constants
ROW_COUNT = 6
COL_COUNT = 4
TEMPLATE_HTML = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <title>&#65279;</title>

    <link rel="stylesheet" href="assets/styles/main.css" />
    <link rel="apple-touch-icon" href="../images/{}x{}.png">
  </head>
  <body>
    <script src="assets/scripts/main.js"></script>
  </body>
</html>
"""

# Generate the html files
for i in range(1, ROW_COUNT + 1):
    for j in range(1, COL_COUNT + 1):
        file_name = 'icon-site/' + str(i) + 'x' + str(j) + '.html'
        f = open(file_name, 'w')

        built_string = str.format(TEMPLATE_HTML, str(i), str(j))
        f.write(built_string)
        f.close()

# Generate the html files
for i in range(1, ROW_COUNT + 1):
    print('<tr>')
    for j in range(1, COL_COUNT + 1):
        file = 'icon-site/' + str(i) + 'x' + str(j) + '.html'
        table_tag = '    <td><a href=\"' + file + '\">' + file + '</a></td>'
        print(table_tag)
    print('</tr>')

exit(1)

# Format the images
im = Image.open("Wallpaper.png")
(left, upper, right, lower) = (20, 20, 100, 100)
im_crop = im.crop((left, upper, right, lower))

# Generate the images
for i in range(0, ROW_COUNT):
    for j in range(0, COL_COUNT):
        left = 54 * (j + 1) + j * 120
        right = left + 120
        upper = 60 + (56 * i) + (i * 120)
        lower = upper + 120

        im_crop = im.crop((left, upper, right, lower))
        print('image ' + str(i + 1) + 'x' + str(j + 1))
        print((left, upper, right, lower))
        file_name = 'images/' + str(i + 1) + 'x' + str(j + 1) + '.png'
        im_crop.save(file_name)
