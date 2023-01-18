#!/usr/bin/env python3
PRAGMA_START = "// @@begin "
PRAGMA_END = "// @@end "
STARTS = {}
for i, line in enumerate(open('src/the-soup.js')):
    if line.startswith(PRAGMA_START):
        filename = line[len(PRAGMA_START):]
        STARTS[filename] = i
    elif line.startswith(PRAGMA_END):
        filename = line[len(PRAGMA_END):]
        start = STARTS[filename]
        print(i - start, filename.strip())
