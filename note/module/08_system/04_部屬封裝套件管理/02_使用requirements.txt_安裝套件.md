# 使用 requirements.txt 安裝套件

## 導出python所安裝的套件 為 requirements.txt


python -m pip freeze > requirements.txt



## 依照 requirements.txt 為你的python安裝相同的套件

python -m pip install -r requirements.txt