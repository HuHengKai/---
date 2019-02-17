from matplotlib import pyplot as plt
import random
from matplotlib import font_manager
my_font=font_manager
# font={'family':'MiscroSoft YaHei',
#       'weight':'bold',
#       'size':'larger'
# }
# matplotlib.rc("font",**font)
# matplotlib.rc("font",family='MiscroSoft YaHei',weight="bold")
x=range(0,120)
y=[random.randint(20,35) for i in range(120)]
plt.plot(x,y)
#调整x的刻度
_xtick_lables=["10点{}分".format(i) for i in range(60)]
_xtick_lables+=["11点{}分".format(i) for i in range(60)]
#取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(list(x)[::3],_xtick_lables[::3],rotation=45)
plt.show()
#调整刻度值
# _x=x
# _xtick_lables=["hello,{}".format(i) for i in _x]
# plt.xticks(_x,_xtick_lables)
# 数和字符串对应
# _x=list(x)[:: 10]
# _xtick_lables=["hello,{}".format(i) for i in _x]
# plt.xticks(_x,_xtick_lables)