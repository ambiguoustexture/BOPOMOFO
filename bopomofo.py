# # -*- coding:utf-8 -*-
# Author：ambiguoustexture
# Date: 2020-01-30
from pypinyin import pinyin, lazy_pinyin, Style
import re

def chinese_characters_2_bopomofo(chinese_characters):
    """
    将汉字转换为注音符号表示
    :param chinesecharacters: 待转换的汉字字符串
    :return:                  对应的注音符号
    """
    return re.sub(r'[\[\]\'\', ]', '', str(pinyin(chinese_characters, style=Style.BOPOMOFO)))
    #通过pinyin( , style=Style.BOPOMOFO)得到每个汉字对应的注音串列表
    #通过str()将注音串列表转为字符串格式
    #通过re.sub(r'[\[\]\'\', ]', '', str)正则匹配方括号并通过替换为空字符的方式连接起来


if __name__ == "__main__":
    
    for line in open("./pinyin.txt"):
        index = line.find("=")
        bopomofo = chinese_characters_2_bopomofo(line[ : index])
        line = line[ : index + 1] + bopomofo
        print(line)
        with open("./bopomofo.txt", 'a+') as bopomofodic:
           bopomofodic.write(line + '\n')
    
