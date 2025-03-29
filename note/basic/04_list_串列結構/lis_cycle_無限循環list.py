from itertools import cycle

    colors = cycle(['red', 'yellow', 'green'])  # 使用 itertools.cycle 创建颜色迭代器
    for i in range(len(x) - 1):
        color = next(colors) 