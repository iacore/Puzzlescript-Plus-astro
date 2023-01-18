import re
r = re.compile(r"/home/user/computing/gui/Puzzlescript-plus-astro/js/(.*?):.*:.* '(.*)' is not defined.")
for line in open('undef.txt'):
    match = r.match(line)
    if match:
        print(match[1], match[2], sep='\t')