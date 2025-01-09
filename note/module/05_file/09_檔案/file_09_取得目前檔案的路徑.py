import os

print(__file__) # fullpath
print(os.path.dirname(__file__)) #fulldir
print(os.path.dirname(os.path.dirname(__file__))) #fulldir's up


sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))) #加入上層目錄的路徑
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..'))) #加入上層目錄的路徑  windows 與 linux 通用


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) #加入上上層目錄的路徑