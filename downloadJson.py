import base64
import json

import urllib.parse

import requests


def download_jsons(weekRange,id,SessionId,server,year_semester):
    url = f"https://jwgls{server}.cust.edu.cn/api/ClientStudent/QueryService/OccupyQueryApi/QueryScheduleData"  # 请替换为实际的 API 端点
    cookies = {
        "ASP.NET_SessionId": SessionId,
    }

    #  可选：根据 API 的要求添加请求头，例如 Content-Type
    headers = {
        "Content-Type": "application/json;charset=utf-8",  # 或者 "application/json"，视情况而定
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 YaBrowser/25.2.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Accept": "application/json, text/plain, */*",
    }
    for i in weekRange:

        param = {
            "KBLX": "2",  # 课表类型
            "CXLX": "1",  # 查询类型
            "XNXQ": year_semester,  # 学年学期
            "CXID": id,  # 查询ID
            "CXZC": str(i),  # 查询周次
            "JXBLXs": [
                "正常",
                "实验",
                "实践",
                "重修",
                "通选",
                "辅修"
            ],  # 解析表类型
            "IsOnLine": "-1"
        }
        # 准备 POST 请求的数据 (根据实际 API 的要求)
        data = {
            "param": base64.b64encode(urllib.parse.quote(str(param)).encode('utf-8')).decode('utf-8'),
            "__permission": {
                "MenuID": "9B419D97-3440-422C-8230-A83292B62FA4",
                "Operate": "select",
                "Operation": 0
            },
            "__log": {
                "MenuID": "9B419D97-3440-422C-8230-A83292B62FA4",
                "Logtype": 6,
                "Context": "查询"
            }
        }
        try:
            response = requests.post(url, cookies=cookies, headers=headers, json=data) # 使用 data 发送表单数据

            response.raise_for_status()  # 如果响应状态码不是 200，则抛出 HTTPError 异常

            print(f"第{i}周数据请求成功！")
            data = str(json.dumps(response.json(), indent=4, ensure_ascii=False))

            with open(f"json/{i}.json", "w", encoding="utf-8") as f:
                f.writelines(data)
        except requests.exceptions.RequestException as e:
            print("请求失败:", e)

