# import random

# for i in range(1,365) :
#     if random.randint(0,9) > 8 :
#         print(i)

import subprocess

commit_message = "My commit message"
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', commit_message])
subprocess.call(['git', 'push'])
