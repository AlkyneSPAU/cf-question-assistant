# from get import getData
from window import Window
# import sys
import json  # json.dump写入中文记得加上ensure_ascii=False参数,否则默认写入unicode
import codecs

if __name__ == '__main__':
    with codecs.open('settings.json', 'r', 'utf-8') as file:
        setting = json.load(file)  # 读取设置

    form = Window(setting)  # 创建窗体

    """
    Qt解决方案(暂未完成)
    form.widget.show()  # 显示窗体
    sys.exit(form.app.exec_())  # 点菜单关闭才关闭窗口，否则运行完上述代码直接关闭窗口
    """
