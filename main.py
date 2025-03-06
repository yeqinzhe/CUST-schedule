from downloadJson import download_jsons
from filter import data_filter
from toICS import to_ics

# 个人id F12 GetStudentBasicInfoLessonOccupy SMXSJBXXID
PersonalId = "d85695ed-799c-418f-85ea-6e02d50a7b9b"

# cookie ASP.NET_SessionId
SessionId = "f2i2isiycjtaub4oz1uuum2z"

# 服务器编号
server = 3

# 周数
weekRange = range(0,21)

# 学年学期
year_semester = "20242"

download_jsons(weekRange,PersonalId,SessionId, server, year_semester)
data_filter(weekRange)
to_ics("all_lessons")