import subprocess

total_active = 0

for x in range(0, 256):
    for y in range(1, 256):
        command = "ping -n 1 131.212.%s.%s -w 50" % (x,y)
        res = subprocess.call(command)
        if res == 0:
            total_active += 1

print (total_active)