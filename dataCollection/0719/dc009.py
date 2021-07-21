# JSON (제이슨) 사용하기
import json
# json : { "key":"value", "key":[{"key":"value"}, {"key":"value"}] }
jsonString = '{ "arrayOfNums": [{"number":0}, {"number":1}, {"number":2}],' \
             ' "arrayOfFruits": [{"fruit":"apple"}, {"fruit":"banana"}, {"fruit":"pear"}] }'
jsonObj = json.loads(jsonString)
print(jsonObj.get("arrayOfNums"))  # [{'number': 0}, {'number': 1}, {'number': 2}]
print(jsonObj.get("arrayOfFruits"))  # [{'fruit': 'apple'}, {'fruit': 'banana'}, {'fruit': 'pear'}]

print(jsonObj.get("arrayOfNums")[0])  # {'number': 0}
print(jsonObj.get("arrayOfNums")[0].get("number"))  # 0
print(jsonObj.get("arrayOfNums")[1].get("number"))  # 1
print(jsonObj.get("arrayOfNums")[2].get("number"))  # 2

print(jsonObj.get("arrayOfFruits")[0])  # {'fruit': 'apple'}
print(jsonObj.get("arrayOfFruits")[0].get("fruit"))  # apple
print(jsonObj.get("arrayOfFruits")[1].get("fruit"))  # banana
print(jsonObj.get("arrayOfFruits")[2].get("fruit"))  # pear
