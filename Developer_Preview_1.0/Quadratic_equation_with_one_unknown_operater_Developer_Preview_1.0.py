#一元二次方程求解器
while True:
  print("欢迎使用一元二次方程求解器 ©2022 Lynn\nDeveloper Preview 2.0\n下面是输入示例：\n如方程为5x²+2x+6=0（方程右边必须化为0！）\n把二次项系数，一次项系数，常数项分别输入，即可得到结果")
  a=int(input("二次项系数？"))
  b=int(input("一次项系数？"))
  c=int(input("常数？"))
  import math
  try:
    derta=math.sqrt(b*b-4*a*c)
    answer1=((0-b)+derta)/2*a
    answer2=((0-b)-derta)/2*a
    if answer1==answer2:
      print("该方程的两个相等的实数根是",answer1)
    else:
      print("第一个答案是：",answer1,"第二个答案是：",answer2)
  except:
    print("该方程无解！")
    