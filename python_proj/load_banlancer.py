
import math
import os
import random
import re
import sys
import requests
import json


def getServerIndex(n, arrival, burstTime):
    # Write your code here
    m = len(arrival)
    server_working = [0]*n
    ret = [-1]*m
    # debug statements log:
    # print(n, m, arrival, burstTime)
    # current_time = 0
    arrival2 = sorted([[i, a]
                      for i, a in enumerate(arrival)], key=lambda x: x[1])
    # debug statements log:
    # print("sorted arrival:", arrival2)
    for req_idx, current_time in arrival2:
        avail_node = -1
        for i, w in enumerate(server_working):
            if current_time >= w:
                # debug statements log:
                # print("find one node:", req_idx, i, w)
                avail_node = i
                break

        if avail_node >= 0:
            ret[req_idx] = avail_node+1
            server_working[avail_node] = current_time+burstTime[req_idx]
            # debug statements log:
            # print("server_working:", server_working, "bust time =", burstTime[req_idx])

    return ret


#
# Complete the 'getCapitalCity' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING country as parameter.
# API URL: https://jsonmock.hackerrank.com/api/countries?name=<country>
#

def getCapitalCity(country):
    # Write your code here
    URL = 'https://jsonmock.hackerrank.com/api/countries?name='
    req = requests.get(URL+country)
    print("statuss code:", req.status_code)
    req_json = json.loads(req.content)
    print(req.content, req_json)


getCapitalCity('Italy')
