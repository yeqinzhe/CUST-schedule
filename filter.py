import json


def convert_to_output(week):
    try:
        with open(f'json/{week}.json', 'r', encoding='utf-8') as f:  # 推荐指定编码 utf-8
            data = json.load(f)  # 将 JSON 文件解析为 Python 对象
    except FileNotFoundError:
        print("文件未找到")
        data = None  # 或采取其他适当的措施
    except json.JSONDecodeError:
        print("JSON 格式错误")
        data = None  # 或采取其他适当的措施

    Lessons=[]
    for i in data["data"]["AdjustDays"]:
        for j in i["MN__TimePieces"]+i["AM__TimePieces"]+i["AF__TimePieces"]+i["PM__TimePieces"]+i["EV__TimePieces"]:
            for k in j["Dtos"]:
                lecture = {
                    "Lesson":"",
                    "Teacher":"",
                    "Room":"",
                    "Time":"",
                    "WIndex":"",
                    "StartTime":"",
                    "EndTime":"",
                    "week": week,
                }
                for l in k["Content"]:
                    lecture[l["Key"]] = l["Name"]
                lecture["WIndex"]=i["WIndex"]
                lecture["StartTime"] = j["StartTime"]
                lecture["EndTime"] = j["EndTime"]
                Lessons.append(lecture)
    return Lessons

def data_filter(weekRange):
    data = []
    for i in weekRange:
        data += convert_to_output(i)
    print(f"一共{len(data)}节课")
    try:
        with open('output.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("数据已成功写入到 output.json 文件")

    except Exception as e:
        print(f"写入 JSON 文件时发生错误: {e}")