def test1():
    lis = ['PPV1-', 'PPV2-', 'PPV3-', 'PPV4-', 'PPV5-' , '']
    lis = list(filter(None, lis))
    print(lis)

if __name__ == '__main__':
    test1()


# 使用 filter lambda 移除  另一個範例
# lis = list(filter(lambda e: data_blog_title.get(e, None) is not None, lis_all))