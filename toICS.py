import datetime
import json
import uuid

from icalendar import Calendar, Event


def calculate_date_from_week_day(week_number, day_of_week):
  """
  计算给定周数和星期几的日期。

  Args:
    week_number:  周数 (从1开始，第一周从2025年2月24日开始)
    day_of_week:  星期几 (1: 星期一, 2: 星期二, ..., 7: 星期日)

  Returns:
    一个datetime.date对象表示计算出的日期，如果输入无效则返回None。
  """

  # 验证输入
  if not (1 <= week_number <= 53) or not (1 <= day_of_week <= 7):
    print("无效的输入。周数必须在1到53之间，星期几必须在1到7之间。")
    return None

  # 定义起始日期 (2025年2月24日是星期一)
  start_date = datetime.date(2025, 2, 24)

  # 计算目标日期
  # 第一周的起始日期就是start_date
  # 对于其他周，先计算相对于start_date的周数差。
  #  然后计算相对于星期一的偏移量，因为start_date是星期一。
  delta_days = (week_number - 1) * 7 + (day_of_week - 1)
  target_date = start_date + datetime.timedelta(days=delta_days)

  return target_date

def to_ics(name):
    # 从 output.json 文件读取数据
    try:
        with open('output.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("错误：找不到 output.json 文件。")
        exit()
    except json.JSONDecodeError:
        print("错误：output.json 文件格式不正确，无法解析 JSON。")
        exit()

    # 创建日历对象
    cal = Calendar()
    cal.add('prodid', '-//My Python ICS Generator//NONSGML v1.0//EN')
    cal.add('version', '2.0')

    # 循环处理每个课程
    for lesson_data in data:
        date = calculate_date_from_week_day(lesson_data["week"], lesson_data["WIndex"])

        start_time = datetime.datetime.strptime(f'{date} {lesson_data["StartTime"]} +0000', "%Y-%m-%d %H:%M %z", )
        end_time = datetime.datetime.strptime(f'{date} {lesson_data["EndTime"]} +0000', "%Y-%m-%d %H:%M %z", )

        start_time -= datetime.timedelta(hours=8)

        end_time -= datetime.timedelta(hours=8)

        now = datetime.datetime.now(datetime.UTC)

        event = Event()
        event.add('summary', lesson_data['Lesson'])
        event.add('location', lesson_data['Room'])
        event.add('description', f"教师：{lesson_data['Teacher']}")  # 使用 f-string 格式化字符串
        event.add('dtstart', start_time)  # 使用 UTC 时间的 datetime 对象
        event.add('dtend', end_time)  # 使用 UTC 时间的 datetime 对象
        event.add('dtstamp', now)  # 添加 DTSTAMP 属性

        # 生成一个唯一的 UID
        event.add('uid', str(uuid.uuid4()) + "@yqz")  # 使用 UUID

        cal.add_component(event)  # 将事件添加到日历对象

    # 将日历对象写入文件 (在循环结束后)
    filename = f"{name}.ics"  # 指定输出文件名
    with open(filename, 'wb') as f:  # 使用 'wb' 以二进制写入
        f.write(cal.to_ical())

    print(f"所有课程的 ICS 文件已生成: {filename}")

