import argparse
parser = argparse.ArgumentParser()
# parser.add_argument('echo',help='echo the string you use here')     # add_argument()指定程序可以接受的命令行选项
# args = parser.parse_args()      # parse_args()从指定的选项中返回一些数据
parser.add_argument('square',help='display a square of a given number',type=int)
args = parser.parse_args()
print(args)
# print(args.echo)
print(args.square**2)