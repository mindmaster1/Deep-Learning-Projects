import pytesseract
from PIL import Image

# 打开图片
image = Image.open('example.png')

# 转为灰度图片
imgry = image.convert('L')
# 二值化，采用阈值分割算法，threhold为分割点，根据图片质量调节
threhold = 150
table = []
for j in range(256):
    if j<threhold:
        table.append(0)
    else:
        table.append(1)

temp = imgry.point(table,'1')

temp = imgry.point(table,'1')

# OCR识别，调用pytesseract库，lang指定中文，--psm 6表示按行识别，有助于提升准确率
text = pytesseract.image_to_string(temp,lang="chi_sim+eng",config='--psm 6')

# 打印识别结果
print(text)