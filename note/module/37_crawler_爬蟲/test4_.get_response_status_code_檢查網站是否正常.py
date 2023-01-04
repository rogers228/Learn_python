import requests

def test1():
    # get_response_status_code
    response = requests.get("http://www.yeoshe.tw")
    print(response.status_code)

if __name__ == '__main__':
    test1()