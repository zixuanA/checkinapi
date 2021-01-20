# -*- coding: utf-8 -*-
import requests
import base64
import json
import time
from os import environ as env
from logging import warning


def sign():
    # 反编译出的词典
    dict1 = ["s9ZS", "jQkB", "RuQM", "O0_L", "Buxf", "LepV", "Ec6w", "zPLD", "eZry", "QjBF", "XPB0", "zlTr", "YDr2",
             "Mfdu", "HSoi", "frhT", "GOdB", "AEN0", "zX0T", "wJg1", "fCmn", "SM3z", "2U5I", "LI3u", "3rAY", "aoa4",
             "Jf9u", "M69T", "XCea", "63gc", "6_Kf"]
    dict2 = ["89KC", "pzTS", "wgte", "29_3", "GpdG", "FDYl", "vsE9", "SPJk", "_buC", "GPHN", "OKax", "_Kk4", "hYxa",
             "1BC5", "oBk_", "JgUW", "0CPR", "jlEh", "gBGg", "frS6", "4ads", "Iwfk", "TCgR", "wbjP"]
    # 获取用于标记词典索引的日期
    date = time.localtime(time.time())
    return dict1[date.tm_mday - 1] + dict2[date.tm_hour - 1]


headers = {
    'Connection': 'keep-alive',
    'Host': 'we.cqu.pt',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 '
                  'Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat ',
    'content-type': 'application/json',
    'Referer': 'https://servicewechat.com/wx8227f55dc4490f45/76/page-frame.html'
}

key = {
    "name": env.get('name', "肖家愚"),
    "xh": env.get('sid', " "),
    "xb": env.get('sex', "男"),
    "openid": env.get('openid', " "),
    "locationBig": env.get('addr1', "重庆市,重庆市,南岸区"),
    "locationSmall": env.get('addr2', "重庆邮电大学"),
    "latitude": float(env.get('latitude', '29.52168')),
    "longitude": float(env.get('longitude', '106.56256')),
    "szdq": env.get('addr1', "重庆市,重庆市,南岸区"),
    "xxdz": env.get('addr2', "重庆邮电大学"),
    "ywjcqzbl": "低风险",
    "ywjchblj": "无",
    "xjzdywqzbl": "无",
    "twsfzc": "是",
    "ywytdzz": "无",
    "beizhu": "无",
    "mrdkkey": sign(),
    "timestamp": int(time.time())
}


def checkin():
    if key.get("xh") == " " or key.get("openid") == " ":
        warning("请配置环境变量")
        exit()
    key_base64 = base64.b64encode(json.dumps(key).encode('utf-8'))
    post_data = {'key': key_base64.decode('utf-8')}
    result = requests.post('https://we.cqu.pt/api/mrdk/post_mrdk_info.php', data=json.dumps(post_data), headers=headers)
    print(result.content)


if __name__ == "__main__":
    checkin()
