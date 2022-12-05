import re

def test1():
    # coding_javascript = r'C:\Users\user\Documents\Rogers\for_horse\javascript'

    # path = r'C:\Users\user\Documents\Rogers\for_horse\javascript\test.js'
    # with open(path, "r", encoding='utf-8') as f:
    #     js = f.read()
    # print(js)

    js = """
    function test(){
        window.alert("hi");
    }

    function test1(){
        // test 12
        console.log('test1');
    }

    function test_api_get(){
            // let memoid = 'pump_v_1';
        let myurl = 'http://220.168.100.186:8239/backstage/api1?name=rogers';
        // console.log('myurl:'+myurl);
        let xhr = new XMLHttpRequest();
            xhr.open('get',myurl, true);
            xhr.send(null);
            xhr.onload = function(){
                if(xhr.status == 200){
                    // return JSON.parse(xhr.responseText);
                    let json_data = JSON.parse(xhr.responseText);
                    console.log('200')
                    console.log(json_data)
                    // el.innerHTML = json_data['body_'+local_value['language']];
                }
                else{
                    console.log('error! myurl:'+ myurl);
                }
            }
    }
    """

    result1 = re.findall(r'\s*function\s+(\w+)\s*\(', js)

    print(result1)



if __name__ == '__main__':
    test1()