# 导入模块
import argparse 
# 创建一个解析对象
parser = argparse.ArgumentParser() 
# --help时显示的的开始文字
parser.description = '叫我出来干嘛？' 
# 向该对象中添加你要关注的命令行参数和选项
parser.add_argument('-a', '--A', help = '我是A', type = int)
parser.add_argument('-b', '--B', help = '我是B', type = int)
# 进行解析
args = parser.parse_args()
if args.A:
    print('得到了A，它是：', args.A)
if args.B:
    print('得到了B，它是：', args.B)
if args.A and args.B:
    print('得到了A和B，它们的乘积是：', args.A * args.B)
