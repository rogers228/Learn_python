# csv to dataframe
df_t = pd.read_csv(csvfile, sep = ',',encoding='utf-8')

# dataframe  to  json
json_str = '{"data":' + df.to_json(orient="records") + '}' 


#檢視用
dic_data = json.loads(json_str)  # string-json variable to dict
json_s = json.dumps(dic_data, indent=4, ensure_ascii=False) # dict to format json
print(json_s)


    json_s_min = json.loads(jsmin(json_s)) #to min json
    print(json_s_min)