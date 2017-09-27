import time
import subprocess
import multiprocessing.dummy
import multiprocessing
from multiprocessing.pool import Pool

def ping(ip):
    success = subprocess.call(['ping', '-n', '1', '-w', '15', ip], stdout=subprocess.PIPE)
    if success == 0:
        print("{} responded".format(ip))
        file = open("pingReply.txt", "a")
        file.write("1")
        file.close()
    else:
        print("{} did not respond".format(ip))

def ping_range():
    totalActive = 0
    num_threads = 3 * multiprocessing.cpu_count()
    p = multiprocessing.dummy.Pool(num_threads)
    for i in range(0, 256):
        p.map(ping, ["131.212.%s.%s" % (i,x) for x in range(0, 256)])

def countActive(latency):
    chars = 0
    with open('pingReply.txt', 'r') as in_file:
        for line in in_file:
            chars += len(line)
    open('pingReply.txt', 'w').write('Total Active: ' + str(chars) + "\nLatency: " + str(latency))


def main():
    open('pingReply.txt', 'w').close()
    start = time.time()
    ping_range()
    end = time.time()
    latency = (end - start) / 60 / 60
    countActive(latency)

main()