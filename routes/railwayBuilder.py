import json
import logging

from flask import request

# from routes import app

logger = logging.getLogger(__name__)

def count(arr, target): 
    if target == 0: 
        return 1

    if target < 0 or len(arr) == 0: 
        return 0
    
    curr = arr[0]
    remain = arr[1:]
    num_curr = count(arr, target-curr)
    num = count(remain, target)
    return num + num_curr 

def railwayBuilder(): 
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    input = data.get("input")
    # input = ["5,3,2,1,4", "3,3,4,1,2", "11,1,2", "71,7,1,2,3,4,5,6,7"]
    result = []
    # case where target sum or diff types is 0 
    for i in range(len(input)): 
        temp = input[i].split(",")
        for j in range(len(temp)):
            temp[j] = int(temp[j])
        if temp[0] <= 0 or temp[1] <= 0:
            result.append(0)
            continue 
        else: 
            target = temp[0]
            temp = temp[2:]
            res = count(temp, target)
            result.append(res)
        
    return json.dumps(result)

if __name__ == "__main__":
    railwayBuilder()
