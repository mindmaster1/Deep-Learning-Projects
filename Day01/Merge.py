import xlrd
import xlwt
from pathlib import Path, PurePath

# 导入Excel和文件操作库

# 指定要合并excel的路径
src_path = 'D:/Python自动化办公/Day01/调查问卷'
# 指定合并完成的路径
dst_file = 'D:/Python自动化办公/Day01/result/结果.xls'

# 取得给目录下所有的xlsx格式文件
p = Path(src_path)
files = [x for x in p.iterdir() if PurePath(x).match('*.xls')]
print(files)

# 准备列表存放读取结果
content = []


# 对每一个文件进行重复处理
for file in files:
    # 用文件作为每个用户的标识
    username = file.stem
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]

    # 取得每一项的结果
    answer1 = table.cell_value(rowx=4, colx=4)
    answer2 = table.cell_value(rowx=10, colx=4)
    temp = f'{username},{answer1},{answer2}'

    # 合并为一行存储
    content.append(temp.split(','))
    print("你好")
    print(temp)

# 准备写入文件的表头
table_header = ['员工姓名', '第一题', '第二题']

workbook = xlwt.Workbook(encoding='utf-8')
x1sheet = workbook.add_sheet("统计结果")

# 写入表头
row = 0
col = 0
for cell_header in table_header:
    x1sheet.write(row, col, cell_header)
    col += 1

# 向下移动一行
row += 1
# 取出每一行的内容
for line in content:
    col = 0
    # 取出每个单元格内容
    for cell in line:
        # 写入内容
        x1sheet.write(row, col, cell)
        # 向右移动一个单元格
        col += 1
    # 向下移动一行
    row += 1

# 保存最终结果
workbook.save(dst_file)
