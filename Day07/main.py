import pathlib
file_name = "./e.txt"
# 取得脚本所在目录
current_path = pathlib.PurePath(__file__).parent

#和脚本同目录下的文件绝对路径
file = current_path.joinpath(file_name)

# 打开文件
with open(file,encoding='utf-8') as f:
    # 读取文件
    content = f.read()
    words = content.rstrip()
    number = len(words)
    print(number)