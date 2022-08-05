from aip import AipOcr

APP_ID = ''
API_Key = ''
SECRET_KEY = ''

client = AipOcr(APP_ID,API_Key,SECRET_KEY)

# 读取图片
def get_file_content(filepath):
    with open(filepath,'rb') as fp:
        return fp.read()

image = get_file_content('example.png')

# 调用文字识别，图片参数为本地图片
result = client.basicGeneral(image)
print(result)
