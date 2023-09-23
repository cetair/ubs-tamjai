import json
import logging

from flask import request

# from routes import app

import time

logger = logging.getLogger(__name__)


def count_number(arr, target, memo={}): 
    # if target == 0: 
    #     return 1

    # if target < 0 or len(arr) == 0: 
    #     return 0
    
    # curr = arr[0]
    # remain = arr[1:]
    # num_curr = count_number(arr, target-curr)
    # num = count_number(remain, target)
    # return num + num_curr 

    if target == 0:
        return 1

    if target < 0 or len(arr) == 0:
        return 0

    if (tuple(arr), target) in memo:
        return memo[(tuple(arr), target)]

    curr = arr[0]
    remain = arr[1:]

    num_curr = count_number(arr, target - curr, memo)
    num = count_number(remain, target, memo)

    memo[(tuple(arr), target)] = num + num_curr

    return memo[(tuple(arr), target)]

def railwayBuilder(): 
    # data = request.get_json()
    # logging.info("data sent for evaluation {}".format(data))
    # data = ["5,3,2,1,4", "3,3,4,1,2", "11,1,2", "71,7,1,2,3,4,5,6,7"]
    data = ['502, 20, 41, 3, 13, 31, 19, 38, 11, 35, 44, 25, 40, 42, 1, 32, 17, 20, 7, 29, 8, 26', '666, 19, 1, 10, 14, 13, 35, 38, 29, 12, 23, 3, 9, 40, 47, 45, 4, 50, 6, 34, 2', '1008, 6, 13, 4, 46, 16, 47, 44', '330, 16, 24, 17, 45, 9, 49, 14, 43, 11, 10, 12, 31, 48, 44, 16, 30, 36', '354, 26, 20, 46, 28, 47, 16, 11, 18, 6, 45, 44, 14, 36, 9, 21, 25, 26, 12, 39, 7, 19, 24, 27, 41, 31, 23, 32', '608, 25, 3, 25, 31, 39, 32, 9, 35, 7, 15, 23, 36, 17, 47, 29, 43, 40, 38, 42, 37, 20, 4, 5, 34, 50, 26', '481, 21, 34, 45, 46, 49, 39, 26, 50, 18, 5, 31, 3, 21, 24, 27, 28, 14, 20, 7, 38, 36, 47', '304, 25, 16, 34, 46, 45, 5, 37, 41, 29, 39, 18, 3, 43, 19, 47, 40, 20, 17, 7, 24, 21, 15, 33, 2, 6, 48', '349, 20, 25, 40, 3, 38, 16, 32, 14, 49, 33, 12, 31, 11, 23, 6, 8, 37, 39, 45, 48, 47', '644, 29, 31, 27, 9, 23, 37, 17, 32, 7, 36, 18, 15, 10, 49, 35, 16, 41, 43, 30, 39, 22, 24, 13, 3, 45, 21, 11, 33, 8, 34']
    result = []
    # case where target sum or diff types is 0 
    for i in range(len(data)): 
        temp = data[i].split(",")
        for j in range(len(temp)):
            temp[j] = int(temp[j])
        if temp[0] <= 0 or temp[1] <= 0:
            result.append(0)
            continue 
        else: 
            target = temp[0]
            temp = temp[2:]
            res = count_number(temp, target)
            result.append(res)

if __name__ == "__main__":
    start_time = time.time()
    result = railwayBuilder()
    print("result", result)
    end_time = time.time()
    running_time = end_time - start_time
    print("Running time: {:.6f} seconds".format(running_time))



