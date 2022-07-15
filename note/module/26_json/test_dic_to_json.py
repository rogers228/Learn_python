def test4():
    dic ={ 
          "id": "04", 
          "name": "sunil", 
          "department": "HR"}
    print(dic)
    # {'id': '04', 'name': 'sunil', 'department': 'HR'}

    json_s = json.dumps(dic, indent = 4) 
	# json_s = json.dumps(dic, indent=4, ensure_ascii=False) 中文
    print(json_s)
    # {
    #     "id": "04",
    #     "name": "sunil",
    #     "department": "HR"
    # }

if __name__ == '__main__':
    test4()