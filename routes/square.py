import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)


@app.route('/square', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    input_value = data.get("input")
    result = input_value * input_value
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def generateHashMap(classes):
    hashmap = {}
    for i in classes:
        key = list(i.keys())[0]
        hashmap[key] = i[key]
    return hashmap

@app.route('/lazy-developer', methods=['POST'])
def getNextProbableWords():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    classes = data.get("classes")
    statements = data.get("statements")
    hmap = generateHashMap(classes)
    result = {}
    for statement in statements:
        keys = statement.split('.')
        local_hmap = hmap
        # go to the right location in the hashmap
        for key in range(len(keys) - 1):
            # check if it's a valid key
            if keys[key] in local_hmap and type(local_hmap) != str and type(local_hmap) != list:
                local_hmap = local_hmap[keys[key]]
            else:
                result[statement] = [""]
                break

        if statement in result:
            continue

        if type(local_hmap) == str:
            if local_hmap not in hmap:
                result[statement] = [""]
            else:
                local_hmap = hmap[local_hmap]
        
        if type(local_hmap) == dict:
            output = list(local_hmap.keys())
            output = [i for i in output if i.startswith(keys[-1])] if keys[-1] != "" else output
      
        elif type(local_hmap) == list:
            output = local_hmap
            output = [i for i in output if i.startswith(keys[-1])] if keys[-1] != "" else output
            for i in output:
                if i in hmap:  # check if it's a polymorphic type
                    result[statement]  = [""]
                    break
            if statement in result:
                continue

        else:
            result[statement] = [""]
            continue

        if len(output) == 0:
            result[statement]  = [""]
            continue

        output.sort()
        result[statement] = output if len(output) <= 5 else output[:5]

    logging.info(result)
    return result

def count_number(arr, target, dict={}): 
    if target == 0:
        return 1

    if target < 0 or len(arr) == 0:
        return 0

    if (tuple(arr), target) in dict:
        return dict[(tuple(arr), target)]

    curr = arr[0]
    remain = arr[1:]

    num_curr = count_number(arr, target - curr, dict)
    num = count_number(remain, target, dict)

    dict[(tuple(arr), target)] = num + num_curr

    return dict[(tuple(arr), target)]

@app.route('/railway-builder', methods=['POST'])
def railwayBuilder(): 
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # input = ["5,3,2,1,4", "3,3,4,1,2", "11,1,2", "71,7,1,2,3,4,5,6,7"]
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
        
    return json.dumps(result)