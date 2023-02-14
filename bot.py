import random
import subprocess
with open("changes.txt","a+") as f :
    for i in range(1,365) :
        if random.randint(0,9) > 8 :
            f.write(f'Commited Dat Number : {i}')
            commit_message = f"Day {i}"
            subprocess.call(['git', 'add', '.'])
            subprocess.call(['git', 'commit', '--date',f"{i} days ago",'-m', commit_message])
            subprocess.call(['git', 'push'])

    #s



