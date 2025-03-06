from downloadJson import download_jsons
from filter import data_filter
from toICS import to_ics

# 个人id F12 GetStudentBasicInfoLessonOccupy SMXSJBXXID
PersonalId = "d85695ed-799c-418f-85ea-6e02d50a7b9b"
# PersonalId = "cb94f4b2-3bb6-4424-834d-930c00e940b4" # 姜炫

# cookie ASP.NET_SessionId
SessionId = "f2i2isiycjtaub4oz1uuum2z"

# 服务器编号
server = 3

# 周数
weekRange = range(0,21)

download_jsons(weekRange,PersonalId,SessionId, server)
data_filter(weekRange)
to_ics("all_lessons")