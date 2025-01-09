@click.option('-qsno', help='qsno', required=True, type=int) # required 必要的

# type=int 驗證參數類型
# 有以下
# str
# int
# float
# bool
# click.uuid
# click.File
# click.Path
# click.Choice
# click.IntRange
# click.FloatRange
# click.DateTime