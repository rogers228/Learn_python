def test16():
    cf_DB_PATH = r'C:\Users\user\Dropbox\yshr\instance' #測試用 正式使用時拿掉
    file = f'{cf_DB_PATH}\\prodect_model\\specification.json'
    with open(file, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    print(data)
    print(type(data))  # <class 'dict'>
