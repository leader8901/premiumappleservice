import re

count = 0

text = '13 pro max 512 silver - 100000₽🇪🇺'

def replFind(m):
    global count
    count += 1
    return f"<value> '{count}' {m.group(1)}<value\n "


list = re.sub(r"\s*(\w*)\s*", text)
print(list)
