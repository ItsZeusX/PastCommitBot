import random
import subprocess

for i in range(1,365) :
    if random.randint(0,9) > 8 :
        commit_message = f"Day {i}"
        subprocess.call(['git', 'add', '.'])
        subprocess.call(['git', 'commit', '--date',f"{i} days ago",'-m', commit_message])
        subprocess.call(['git', 'push'])

#s



