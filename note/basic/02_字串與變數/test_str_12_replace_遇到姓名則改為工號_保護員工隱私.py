import pyodbc

def nogetName(myno): #依人員列表，人員編號取得姓名
    for x in range(len(psList)):
        if psList[x][1] == myno:
            return psList[x][2]

def NamegetNo(myName): #依人員列表，人員編號取得姓名
    for x in range(len(psList)):
        if psList[x][2] == myName:
            return psList[x][1]

def reName2No(Str): #依人員列表，人員編號取得姓名
    tmp = Str
    for x in range(len(psList)):
        tmp = tmp.replace(psList[x][2], psList[x][1])
    return tmp
        
global DBSTR
DBSTR='''DRIVER={SQL Server};
        SERVER=220.168.100.250;
        DATABASE=YEOSHE_HR;UID=sa;
        PWD=dsc80057052'''

cnxn = pyodbc.connect(DBSTR)
cursor = cnxn.cursor()

#取得人員列表
SQL = "SELECT ps01,ps02,ps03,ps31 FROM rec_ps ORDER BY ps01"
cursor.execute(SQL)
rows=cursor.fetchall()
global psList
psList=[] #人員列表
for row in rows:
    psList.append([row.ps01,row.ps02,row.ps03])

a = "adfad陸上名dfaasdf陳穩安fdaas265641"
print(a)
b = reName2No(a)
print(b)


