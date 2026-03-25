import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"                           # r ka matlab raw string hota hai (regex me special characters ke liye useful).S

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
