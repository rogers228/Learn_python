import os

def string_to_dict(input_str):
    try:
        # 拆分為鍵值對
        items = input_str.split(", ")
        # 建立字典
        result = {}
        for item in items:
            key, value = item.split(": ", 1)  # 使用 ": " 作為分隔符號
            result[key.strip()] = value.strip()
        return result
    except Exception as e:
        print(f"轉換過程中出現錯誤: {e}")
        return None

def write_ads(file_path, ads_name, content):
    with open(file_path + ":" + ads_name, "w", encoding="utf-8") as ads_file:
        ads_file.write(content)

def read_ads(file_path, ads_name):
    try:
        with open(file_path + ":" + ads_name, "r", encoding="utf-8") as ads_file:
            content_str = ads_file.read()
            return string_to_dict(content_str)

    except FileNotFoundError:
        # print(f"檔案或 ADS '{ads_name}' 不存在")
        return None

    except Exception as e:
        # print(f"發生錯誤: {e}")
        return None

def test1():
    # write ads
    file_path = os.path.join(os.path.dirname(__file__), 'image1.jpg')
    print(file_path)
    public_id = 'jnu1zysyt86hcwaavh32'
    url = 'http://res.cloudinary.com/dk97nvln0/image/upload/v1731909898/jnu1zysyt86hcwaavh32.jpg'
    version = 1731909898
    write_ads(file_path, "cloudinary_metadata",
        f"public_id: {public_id}, url: {url}, version: {version}")

def test2():
    print('ok')
    file_path = os.path.join(os.path.dirname(__file__), 'image1.jpg')
    # file_path = os.path.join(os.path.dirname(__file__), 'image2.png')
    ads = read_ads(file_path, "cloudinary_metadata")
    print(ads)
    print(type(ads))

if __name__ == '__main__':
    # test1()
    test2()