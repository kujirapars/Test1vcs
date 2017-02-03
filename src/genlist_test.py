import sys
import os
cwd = os.getcwd()

sys.path.append(cwd)

i = 0
for i in range(1000):
    if i >= 0:
        continue
from generate_list import printIt
printIt()
