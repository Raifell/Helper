import re

text = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Short poems</title>
</head>
<body>
Hi!
<p>What goes up when
the rain comes down?</p>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
<p>What do you call a snowman in the summer?</p>
<div>Excepteur sint occaecat cupidatat non proident, sunt in</div>
<p>Two little birds
Sitting on a wall,
One called Peter,
One called Paul.</p>
</body>
</html>"""


with open('example.html', 'w') as f:
    f.write(text)

with open('example.html', 'r') as f:
    print(*(re.findall(r'(?ms)(?<=<div>).+?(?=</div>)', re.sub(r'\s+', ' ', f.read()))), sep='\n')

print(10)
