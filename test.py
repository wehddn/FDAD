import json
from multiprocessing import Pool
import time

N = 40

def load(i):
    start = i*1000
    return json.load(open("data/mpd.slice." + str(start) + "-" + str(start+999) + ".json"))["playlists"]


# first way, using multiprocessing
start_time = time.perf_counter()
with Pool() as pool:
    result = pool.map(load, range(0,N))
finish_time = time.perf_counter()
print("Program finished in {} seconds - using multiprocessing".format(finish_time-start_time))
print("---")
# second way, serial computation
start_time = time.perf_counter()
result = []

for x in range(0,N):
    result.append(load(x))

finish_time = time.perf_counter()
print("Program finished in {} seconds".format(finish_time-start_time))
