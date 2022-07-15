# json預設為字典

# 將文字讀取為json 並取值
json_string = """{'nikhil': 1,
                 'akash' : 5, 
                 'manjeet' : 10,
                 'akshat' : 15}"""
print (json_string)
print (type(json_string))

print('')
data_dic = eval(json_string) 
print (str(data_dic))
print (type(data_dic))
print(data_dic['akshat'])
print(data_dic['nikhil'])
print(data_dic['akash'])
print(data_dic['manjeet'])

