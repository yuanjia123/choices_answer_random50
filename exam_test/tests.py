import requests
import json


def send_single_sms(apikey,code,mobile):
    url = "https://sms.yunpian.com/v2/sms/single_send.json"

    text = "【袁佳佳】您的验证码是{}".format(code)

    res = requests.post(url,data={
        "apikey":apikey,
        "mobile":mobile,
        "text":text
    })
    re_json = json.loads(res.text)
    return re_json

if __name__ == '__main__':
    res = send_single_sms("92201394a24e2e320e7922eeaa76e498","456789","17795906752")
    # print(res.text)


    res_json = json.loads(res.text)
    code = res_json["code"]
    msg = res_json['msg']
    if code == 0:
        print("发送成功")
    else:
        print("发送失败: {}".format(msg))
    print(res.text)