import json
import logging
from typing import Dict, List

from flask import request

from routes import app

logger = logging.getLogger(__name__)


def generateHashMap(classes: List[Dict]) -> Dict[str, List[str]]:
  hashmap = {}
  for i in classes:
    key = list(i.keys())[0]
    hashmap[key] = i[key]
  return hashmap

def getNextProbableWords(classes: List[Dict],
                         statements: List[str]) -> Dict[str, List[str]]:
  hmap = generateHashMap(classes)
  result = {}
  for statement in statements:
    keys = statement.split('.')
    temp_hmap = hmap
    value = []
    for index, key in enumerate(keys):
      if type(temp_hmap) == str:
        if temp_hmap in hmap:
          loc2_hmap = hmap.get(temp_hmap)
          temp_hmap = loc2_hmap
          local_hmap = []
          for i in temp_hmap:
            if i in hmap:
              value = [""]
              break
            else:
              if i.startswith(key):
                local_hmap.append(i)
          if local_hmap == []:
            local_hmap = [""]
          if index == len(keys) - 1:
            value = local_hmap
          else:
            value = [""]
            break
        else:
          value = [""]

      elif type(temp_hmap) == list and key != "":
        local_hmap = []
        for i in temp_hmap:
          if i in hmap:
            value = [""]
            break
          else:
            if i.startswith(key):
              local_hmap.append(i)
        if local_hmap == []:
          local_hmap = [""]
        if index == len(keys) - 1:
          value = local_hmap
        else:
          value = [""]
          break

      elif key == "":
        value = []
        if index == len(keys) - 1:
          if type(temp_hmap) == dict:
            for key_dict in temp_hmap.keys():
              value.append(key_dict)
          elif type(temp_hmap) == list:
            for i in temp_hmap:
              if i in hmap:
                value = [""]
                break
              else:
                if i.startswith(key):
                  value.append(i)
            if value == []:
              value = [""]

        else:
          value = [""]
          break

      elif index == len(keys) - 1 and type(temp_hmap) == dict:
        for key_dict in temp_hmap.keys():
          if key_dict.startswith(key):
            value.append(key_dict)

      elif key in temp_hmap and type(temp_hmap) is not list:
        loc_hmap = temp_hmap.get(key)
        temp_hmap = loc_hmap
        
    value.sort()
    if len(value) > 5:
      value = value[:5]
    result[statement] = value

  return result


@app.route('/lazy_developer', methods=['POST'])
def evaluateLazyDeveloper():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    input_value = data.get("classes")
    statement_value = data.get("statements")
    # input value json
    result = getNextProbableWords(input_value, statement_value)
    logging.info("My result :{}".format(result))
    return json.dumps(result)