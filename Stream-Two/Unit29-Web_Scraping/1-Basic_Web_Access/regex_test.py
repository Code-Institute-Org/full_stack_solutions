import re

# Using * asterisk - multiple occurrences of the character preceding it
print re.findall("ab*c", "ac")                  # ['ac']
print re.findall("ab*c", "abcd")                # ['abc']
print re.findall("ab*c", "acc")                 # ['ac']
print re.findall("ab*c", "abcac")               # ['abc', 'ac']
print re.findall("ab*c", "abdc")                # []
print re.findall("ab*c", "ABC")                 # [] case sensitive

# Using re.IGNORECASE
print re.findall("ab*c", "ABC", re.IGNORECASE)  # ['ABC']

# Using . period - any single occurrence
print re.findall("a.c", "abc")                  # ['abc']
print re.findall("a.c", "abbc")                 # []
print re.findall("a.c", "ac")                   # []
print re.findall("a.c", "acc")                  # ['acc']

# Combining . with *
print re.findall("a.*c", "abc")                 # ['abc']
print re.findall("a.*c", "abbc")                # ['abbc']
print re.findall("a.*c", "ac")                  # ['ac']

# Using re.search()
results = re.search("ab*c", "ABC", re.IGNORECASE)
print results.group()

a_string = "Everything we do is <replaced> if it is indeed inside <tags>."

# Substitute the tags with 'coming up roses' using the re.sub() method
a_string = re.sub("<.*>", "coming up roses", a_string)
print a_string

another_string = "Everything we do is <replaced> if it is indeed inside <tags>."

# Make sure that both tags are replaced by using the ? too tell
# re.sub() to stop after first match of '>'
another_string = re.sub("<.*?>", "coming up roses", another_string)
print another_string
