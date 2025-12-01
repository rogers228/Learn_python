import sys, os
import requests
import json
import time

# 添加 GRST_PATH 路徑，匯入 global_config
sys.path.append(os.getenv('GRST_PATH'))
from global_config import OPTION
ANON_KEY = OPTION.get("spwr_api_anon_key")

def fun_hello_world(payload=None):
    function_url = 'https://amqxaxsygazhotsrzmox.supabase.co/functions/v1/hello-world'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {ANON_KEY}'
    }
    try:
        response = requests.post(function_url, headers=headers, json=payload)
        print(f"HTTP Status Code (狀態碼): {response.status_code}")

        try:
            response_json = response.json()
            print(type(response_json))
            print(json.dumps(response_json, indent=4, ensure_ascii=False))

        except requests.exceptions.JSONDecodeError:
            print("Response Body (原始文本):")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"請求發生錯誤: {e}")

def test1():
    print('test requests...')
    payload = {"name": "Rogers"}
    fun_hello_world(payload)

if __name__ == '__main__':
    test1()