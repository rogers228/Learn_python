import sys, time, os
import multiprocessing as mp
sys.path.append(r'U:\dsprog\py_excel\tools')
import tool_check_bom

def job(pdno):
    ckq = tool_check_bom.CKB_query()
    return ckq.find_asm(pdno)

def test2():
    lis_pdnos =[]
    lis_pdnos.append('6AA03AB001E31B02')
    lis_pdnos.append('6AA03AA008AE1B01')
    lis_pdnos.append('6AA03CA048AM1B02')
    lis_pdnos.append('6AA03AB001E31B02')
    lis_pdnos.append('6AA03AA008AE1B01')
    lis_pdnos.append('6AA03CA048AM1B02')
    lis_pdnos.append('6AA03AB001E31B02')
    lis_pdnos.append('6AA03AA008AE1B01')
    lis_pdnos.append('6AA03CA048AM1B02')
    lis_pdnos.append('6AA03AB001E31B02')
    lis_pdnos.append('6AA03AB001E31B02')
    lis_pdnos.append('6AA03AA008AE1B01')
    lis_pdnos.append('6AA03CA048AM1B02')
    lis_pdnos.append('6AA03AB001E31B02')
    lis_pdnos.append('6AA03AA008AE1B01')
    lis_pdnos.append('6AA03CA048AM1B02')
    lis_pdnos.append('6AA03AB001E31B02')
    lis_pdnos.append('6AA03AA008AE1B01')
    lis_pdnos.append('6AA03CA048AM1B02')
    lis_pdnos.append('6AA03AB001E31B02')
    lis_pdnos.append('6AA03AA008AE1B01')    
    print(len(lis_pdnos))
    pool = mp.Pool(3)
    result = pool.map(job, lis_pdnos)
    print(result)

def test1():
    lis_pdnos =[]
    lis_pdnos.append('6AA03AB001E31B02')
    lis_pdnos.append('6AA03AA008AE1B01')
    lis_pdnos.append('6AA03CA048AM1B02')
    lis_pdnos.append('6AA03AB001E31B02')
    lis_pdnos.append('6AA03AA008AE1B01')
    lis_pdnos.append('6AA03CA048AM1B02')
    lis_pdnos.append('6AA03AB001E31B02')
    lis_pdnos.append('6AA03AA008AE1B01')
    lis_pdnos.append('6AA03CA048AM1B02')
    lis_pdnos.append('6AA03AB001E31B02')
    lis_pdnos.append('6AA03AB001E31B02')
    lis_pdnos.append('6AA03AA008AE1B01')
    lis_pdnos.append('6AA03CA048AM1B02')
    lis_pdnos.append('6AA03AB001E31B02')
    lis_pdnos.append('6AA03AA008AE1B01')
    lis_pdnos.append('6AA03CA048AM1B02')
    lis_pdnos.append('6AA03AB001E31B02')
    lis_pdnos.append('6AA03AA008AE1B01')
    lis_pdnos.append('6AA03CA048AM1B02')
    lis_pdnos.append('6AA03AB001E31B02')    
    print(len(lis_pdnos))

    ckq = tool_check_bom.CKB_query()
    lis_dic = []
    for pdno in lis_pdnos:
        lis_dic.append(ckq.find_asm(pdno)) #該品號的深層組件
    print(lis_dic)

if __name__ == '__main__':
    test2()
