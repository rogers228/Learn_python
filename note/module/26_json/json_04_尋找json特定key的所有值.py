from __future__ import print_function
import json

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError as e:
        return False
    return True


def find_values(id, json_repr):
    # https://stackoverflow.com/questions/14048948/how-to-find-a-particular-json-value-by-key
    results = []
    def _decode_dict(a_dict):
        try:
            results.append(a_dict[id])
        except KeyError:
            pass
        return a_dict

    json.loads(json_repr, object_hook=_decode_dict) # Return value ignored.
    return results

def test1():
    file = 'test.json'
    with open(file, encoding='utf-8') as data_file:
        json_str = data_file.read()

    if not is_json(json_str):
        # json 格式不合法
        print('json error:')
        print(json_str)
        return

    # 找出所有id
    lis_ids = find_values('Id', json_str)
    print(lis_ids)

    # 判斷是否重複
    if len(lis_ids) != len(set(lis_ids)):
        print('id 有重複!')


if __name__ == '__main__':
    test1()