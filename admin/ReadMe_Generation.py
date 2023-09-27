import numpy as np

out = open('ReadMe.md', 'w', encoding = 'utf-8')

def walk(a, t):
    for c in a.kid:
        out.write('  ' * t + '* [' + c.concept + '](note/' + c.file + ')\n')
        walk(c, t+1)

walk(root, 0)

out.close()
