import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
# re.match() checks for a match only at the beginning of the string. Since "quick" is not at the start of the text, it will not find a match.