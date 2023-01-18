#!/usr/bin/env python3
PRAGMA_START = "// @@begin "
PRAGMA_END = "// @@end "
STARTS = {}
accumulated_lines = []

for i, line in enumerate(open('src/the-soup.js')):
    if line.startswith(PRAGMA_START):
        filename = line[len(PRAGMA_START):].strip()
        STARTS[filename] = i
        accumulated_lines = []
    elif line.startswith(PRAGMA_END):
        filename = line[len(PRAGMA_END):].strip()
        start = STARTS[filename]
        print(i - start, filename)
        with open(filename, 'w') as f:
            f.writelines(accumulated_lines)
        accumulated_lines = []
    else:
        accumulated_lines.append(line)
