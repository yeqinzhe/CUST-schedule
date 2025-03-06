这是一个长春理工大学课表的爬虫，它可将课表生成为日历文件（.ics），该文件可以在电脑和手机自带的日历查看。
如果您想使用该爬虫，请将该项目导入pycharm当中。
若要生成课表信息，需要修改main.py中的代码

1.首先您需要获得个人id，
请按F12按钮，找到network，点击之后教学信息一体化服务平台-》全校课表-》按学生-》选择班级，
找到GetStudentBasicInfoLessonOccupy，点击response，搜索（ctrl+f）个人姓名，找到SMXSJBXXID的值填入main.py中的PersonalId

2.点击network并排的application按钮，找到cookies，将ASP.NET_SessionId对应的值填入main.py中的SessionId

3.设置服务器编号，教学信息一体化服务平台网址是“jwgls4”开头，则服务器编号为4

4.周数range(0,21)代表开学前一周到20周

5.学年学期的第一学期为九月学的学期

请注意，个人id是固定的，SessionId则会过期