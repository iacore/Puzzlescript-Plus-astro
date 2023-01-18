import re
r = re.compile(r".*?/js/(.*?\.js):.*:.* '(.*)' is not defined.")
for line in open('undef.txt'):
    match = r.match(line)
    if match:
        print(match[1], match[2], sep='\t')