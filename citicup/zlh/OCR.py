# This is a sample Python script.
import base64
import json
# import jsonpath
# import datefinder
import re
import datetime

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import \
    TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models


def img2text(f):  # ile_path):
    try:
        cred = credential.Credential(
            "AKIDXtymLdf6HCqDI7fwwf7ICqDJ8gyzjCNH",
            "e18yNYS7XgZBWaMs74k8GWZNwGK8g5D4")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)

        req = models.GeneralBasicOCRRequest()
        '''
        with open(file_path, "rb") as f:
            base64_data = base64.b64encode(f.read())
            s = base64_data.decode()
            # ImageBase64_value = 'data:image/jpeg;base64,%s' % s
            params = {"ImageBase64": s}
        '''
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        # ImageBase64_value = 'data:image/jpeg;base64,%s' % s
        params = {"ImageBase64": s}
        req.from_json_string(json.dumps(params))
        resp = client.GeneralBasicOCR(req)
        return resp.to_json_string()

    except TencentCloudSDKException as err:
        print(err)


def extract_bike_traffic(json_string):
    """
    :param json_string: string format json file
    :return: string, value of biking distance
    """
    dic = json.loads(json_string)
    word_bank = ['公里', '千米', 'km', 'Km', 'KM']
    distance = 0
    for i in range(len(dic['TextDetections'])):
        # print(dic['TextDetections'][i]['DetectedText'])
        text = dic['TextDetections'][i]['DetectedText']
        for word in word_bank:
            if text.find(word) != -1:
                distance = text.replace(word, "")
                # print(text.replace(word, ""))
                break
    return distance


def extract_no_tableware(json_string):
    """
    :param json_string: string format json file
    :return: bool, state of whether a delivery order need tableware
    """
    dic = json.loads(json_string)
    word_bank = ['无需餐具', '不要餐具', '无餐具']
    state = False
    for i in range(len(dic['TextDetections'])):
        # print(dic['TextDetections'][i]['DetectedText'])
        text = dic['TextDetections'][i]['DetectedText']
        for word in word_bank:
            if text.find(word) != -1:
                state = True
                # print(text.replace(word, ""))
                break
    return state


def extract_cloth_recycle(json_string):
    """
    :param json_string: string format json file
    :return: string, value of recycling cloth weight range
    """
    dic = json.loads(json_string)
    word_bank = ['千克', 'Kg', 'kg', 'kq', 'K9', 'k9']
    weight = 0
    for i in range(len(dic['TextDetections'])):
        # print(dic['TextDetections'][i]['DetectedText'])
        text = dic['TextDetections'][i]['DetectedText']
        for word in word_bank:
            if text.find(word) != -1:
                weight = text.replace(word, "")
                # print(text.replace(word, ""))
                break
        start = 0
    for each in weight:
        a = ord(each)
        if a in range(48, 58):
            start = weight.find(each)
            break
    weight = weight[start:]
    index = weight.find('-')
    num1 = float(weight[0:index])
    num2 = float(weight[index+1:])
    avg_weight = (num1 + num2) / 2
    return avg_weight


def extract_public_transport(json_string):
    """
    :param json_string: string format json file
    :return: string, value of extracted public transport cost
    """
    dic = json.loads(json_string)
    word_bank = ['元', '¥', '￥']
    cost = ""
    img_date = None
    cur_date = datetime.date.today().strftime("%Y-%m-%d")
    flag = 0
    print(img_date, cur_date, flag)
    for i in range(len(dic['TextDetections'])):
        # print(dic['TextDetections'][i]['DetectedText'])
        text = dic['TextDetections'][i]['DetectedText']
        # parse traffic cost
        for word in word_bank:
            if text.find(word) != -1:
                cost = re.findall('\d+\.\d+', text)[0]
                # flag += 1
                break
        # parse date in image for validation
        # if you need to validate the date, uncomment the line below

        # matches = list(datefinder.find_dates(text))
        # if len(matches) > 0:
        #     img_date = matches[0].strftime("%Y-%m-%d")
        #     flag += 1
        # if flag == 2:
        #     break
    # print(img_date, cur_date)
    # return str(cost) if img_date == cur_date else "Date expired"
    return cost


# Press the green button in the gutter to run the script.
def extract_text(file_path, type):
    """
    :param file_path: string, relative or absolute path of image
    :param type: string, type of extract behavior, \
                ['bike', 'cloth', 'food', 'pub_trans']
    :return: string, extacted value
    """
    resp = img2text(file_path)
    if type == 'bike':
        ret = extract_bike_traffic(resp)
    elif type == 'cloth':
        ret = extract_cloth_recycle(resp)
    elif type == 'food':
        ret = extract_no_tableware(resp)
    elif type == 'pub_trans':
        ret = extract_public_transport(resp)
    else:
        ret = "Invalid extraction type!"
    return ret


if __name__ == '__main__':
    ret = extract_text('./test_img/food1.jpg', 'food')
    print(ret)
    ret = extract_text('./test_img/cloth1.jpg', 'cloth')
    print(ret)
    ret = extract_text('./test_img/traffic1.jpg', 'pub_trans')
    print(ret)
    ret = extract_text('./test_img/bike1.jpg', 'bike')
    print(ret)
    ret = extract_text('./test_img/bike1.jpg', 'abcsasda')
    print(ret)
