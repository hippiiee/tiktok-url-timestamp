import sys
from datetime import datetime

def tiktok_timestamp(urlid):
    binary = "{0:b}".format(urlid) #conversion to binary
    i=0
    bits=""
    while i < 31:
        bits += binary[i]
        i+=1
    timestamp = int(bits,2) #convert these bits to an int which is our timestamp
    dt_object = datetime.fromtimestamp(timestamp) #convert our timestamp to a datetime
    print(dt_object)

if __name__ == '__main__':
    if len(sys.argv)!=2:
        print("Usage : tiktok_timestamp.py <videoid>")
    else:
        tiktok_timestamp(int(sys.argv[1]))