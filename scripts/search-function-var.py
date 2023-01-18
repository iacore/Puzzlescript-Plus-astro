import re, glob, os
r_var = re.compile(r"var ([_\w0-9]+)( =)?.*")
r_let = re.compile(r"let ([_\w0-9]+)( =)?.*")
r_const = re.compile(r"const ([_\w0-9]+)( =)?.*")
r_func = re.compile(r"(?:async )?function ([_\w0-9]+).*")

for jsfile in glob.glob('src/js/*'):
    with open(jsfile) as f:
        filename = os.path.basename(jsfile)
        
        for i, line in enumerate(f):
            match = None
            reason = None
            def try_match(r, what):
                global match, reason
                if not match:
                    match = r.match(line)
                    reason = what
            try_match(r_var, "var")
            try_match(r_let, "let")
            try_match(r_const, "const")
            try_match(r_func, "function")
            if match:
                print(filename, match[1], i, reason, match[0], sep='\t')
    # print(
# for line in open('undef.txt'):
#     match = r.match(line)
#     if match:
#         print(match[1], match[2], sep='\t')
