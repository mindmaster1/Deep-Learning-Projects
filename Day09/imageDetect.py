import json
import base64
import requests
import cv2
import numpy
from PIL import Image,ImageDraw,ImageFont


#服务详情中的接口配置
MODEL_API_URL = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/detection/uptech_bistu"
API_KEY = "vuWhKDvxmWc9SoFnr2p52taN"
SECRET_KEY = "0ZYogahXiyWxYnFB9wR5dzGssDwCdQXj"

def chinese_plot_box(image,label,x,sizes,fontcolor=(255,255,255),line_thickness=None):
    cv2img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    pilimg = Image.fromarray(cv2img)
    draw = ImageDraw.Draw(pilimg)
    font = ImageFont.truetype("./5c78c0705c579.ttf",sizes,encoding = "GB2312")
    t1 = line_thickness or round(0.002 * (image.shape[0] + image.shape[1]) / 2) + 1
    if label:
        print(label)
        tf = max(t1 - 1,1)
        draw.text((int(x[0]),int(x[1])-23),label,fontcolor,font=font)
        image = cv2.cvtColor(numpy.array(pilimg),cv2.COLOR_RGB2BGR)
    return image

def get_token():
    auth_url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}".format(API_KEY,SECRET_KEY)
    auth_resp = requests.get(auth_url)
    auth_resp_json = auth_resp.json()
    print(auth_resp_json)
    ACCESS_TOKEN = auth_resp_json["access_token"]
    return ACCESS_TOKEN

# def detect():
#     request_url = "{}?access_token={}".format(MODEL_API_URL,get_token())
#     PARAMS = {"threshold": 0.8}
#     PARAMS["image"] = get_image(IMAGE_FILEPATH)
#     headers = {'content-type': 'application/x-www-form-urlencoded'}
#     response = requests.post(url = request_url,json=PARAMS,headers=headers)
#     response_json = response.json()
#     response_str = json.dumps(response_json,indent=4,ensure_ascii=False)
#     print(response_json)
#     result = response_json['results']
#     if result != None:
#          img = cv2.imread(IMAGE_FILEPATH)
#          for locationinfo in result:
#              print(locationinfo)
#              location = locationinfo['location']
#              width = int(location['width'])
#              top = int(location['top'])
#              height = int(location['height'])
#              left = int(location['left'])
#              name = locationinfo['name']
#              if name == '螺丝':
#                   colors = (0,255,0)
#              else:
#                   colors = (0,0,255)
#              cv2.rectangle(img,(left,top),(left+width,top+height),colors,3)
#              img = chinese_plot_box(img,label=name,x=[left+20,top+20,height,width],sizes=20,fontcolor=colors)
#     cv2.imshow('img',img)
#     if cv2.waitKey(0    ) == ord('q'):
#             cv2.destroyAllWindows()


if __name__ == "__main__":

        # request_url = "{}?access_token={}".format(MODEL_API_URL, get_token())
        # PARAMS = {"threshold": 0.8}
        # PARAMS["image"] = img
        # headers = {'content-type': 'application/x-www-form-urlencoded'}
        # response = requests.post(url=request_url, json=PARAMS, headers=headers)
        # response_json = response.json()
        # response_str = json.dumps(response_json, indent=4, ensure_ascii=False)
        # print(response_json)
        # result = response_json['results']
        # if result != None:
        #     img = cv2.imread(img)
        #     for locationinfo in result:
        #         print(locationinfo)
        #         location = locationinfo['location']
        #         width = int(location['width'])
        #         top = int(location['top'])
        #         height = int(location['height'])
        #         left = int(location['left'])
        #         name = locationinfo['name']
        #         if name == '螺丝':
        #             colors = (0, 255, 0)
        #         else:
        #             colors = (0, 0, 255)
        #         cv2.rectangle(img, (left, top), (left + width, top + height), colors, 3)
        #         img = chinese_plot_box(img, label=name, x=[left + 20, top + 20, height, width], sizes=20,
        #                                fontcolor=colors)
        # cv2.imshow('img', img)
        # if cv2.waitKey(0) == ord('q'):
        #     cv2.destroyAllWindows()