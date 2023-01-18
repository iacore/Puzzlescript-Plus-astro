import re, glob, os
r_var = re.compile(r"var (\w+) =.*")
r_let = re.compile(r"let (\w+) =.*")
r_const = re.compile(r"const (\w+) =.*")
r_func = re.compile(r"function (\w+).*")


for jsfile in glob.glob('src/js/*'):
    with open(jsfile) as f:
        filename = os.path.basename(jsfile)
        for i, line in enumerate(f):
            match = r_var.match(line) or r_let.match(line) or r_const.match(line) or r_func.match(line)
            if match:
                print(filename, match[1], i, match[0], sep='\t')
    # print(
# for line in open('undef.txt'):
#     match = r.match(line)
#     if match:
#         print(match[1], match[2], sep='\t')
