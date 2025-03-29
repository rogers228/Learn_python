def test2():
    lis = ['selected_016', 'selected_020', 'selected_023', 'selected_028', 'selected_032', 'selected_040', 'selected_046', 'selected_056', 'selected_065', 'selected_063', 'selected_071', 'selected_080', 'selected_092', 'selected_110', 'selected_125', 'selected_140', 'selected_180', 'selected_210', 'selected_270']
    print(lis)

    lis_new = list(map(lambda e: e.replace('selected_',''), lis))
    print(lis_new)
    
if __name__ == '__main__':
    test2()