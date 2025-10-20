import sys  # 导入系统模块，用于获取命令行参数
def echo():
    # 判断命令行是否传入了 -s 选项
    shout = "-s" in sys.argv
    message = input("Enter something: ")
    # 如果有 -s 选项，输出大写；否则正常输出
    print(message.upper() if shout else message)
if __name__ == "__main__":
    echo()