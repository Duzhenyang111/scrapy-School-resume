# coding=UTF8
# @Time : 2023/7/26 13:54
# @Author : cabbage
# @File : tool.py
# @Software : PyCharm
import os.path
import random
import re
import webbrowser
from urllib.parse import urlparse
import PyPDF2
import pytesseract
import requests
from PIL import Image
import hashlib
from bs4 import BeautifulSoup
import simplejson as json
from urllib.parse import urljoin
from selenium import webdriver
import time
#from googletrans import Translator
import textwrap
from pdfminer.high_level import extract_text
MAX_NUM = 999999999
options = webdriver.FirefoxOptions()

head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Connection': 'keep-alive',
}




# def get_all(link,head):
#     driver = webdriver.Firefox(executable_path=r'D:\pythonProject\geckodriver.exe', options=options)
#
#     driver.get(link)
#     time.sleep(5)
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'lxml')
#     return soup


# def get_all(link,head):
#     driver = webdriver.Firefox(executable_path=r'D:\pythonProject\geckodriver.exe',options=options)
#     try:
#         driver.get(link)
#         time.sleep(5)
#         html = driver.page_source
#         soup = BeautifulSoup(html, 'lxml')
#     finally:
#         driver.quit()
#     return soup

# def get_all(url, head, charset='utf-8'):
#     # time.sleep(1)
#     strhtml = requests.get(url, headers=head, verify=False).content
#     soup = BeautifulSoup(strhtml.decode(charset, "ignore").replace('</p>', '</p>\n').replace('</td>', '</td>\t').replace('</li>','</li>\n').replace('</tr>', '</tr>\n').replace('\t\t', '\t').replace('\n\n', '\n').replace('\n\n\n','\n'), 'html.parser')
#     return soup

def get_all(link,head=head):
    # 设置无头选项
    options = webdriver.FirefoxOptions()
    options.headless = True

    # 初始化驱动程序
    driver = webdriver.Firefox(executable_path=r'D:\pythonProject\geckodriver.exe', options=options)

    try:
        # 访问网页
        driver.get(link)
        time.sleep(5)  # 等待页面加载
        html = driver.page_source
        html = html.replace('</br>','</br>\n').replace('<br>','<br>\n')
        # print(html)
        soup = BeautifulSoup(html, 'lxml')
    finally:
        # 关闭驱动程序
        driver.quit()
    return soup



def get_all_b(link,head=head):
    # 设置无头选项
    options = webdriver.FirefoxOptions()
    options.headless = True

    # 初始化驱动程序
    driver = webdriver.Firefox(executable_path=r'D:\pythonProject\geckodriver.exe', options=options)

    try:
        # 访问网页
        driver.get(link)
        time.sleep(5)  # 等待页面加载
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
    finally:
        # 关闭驱动程序
        driver.quit()
    return soup


def is_contain_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def random_sleep(mu, sigma=2):
    # '''正态分布随机睡眠
    # :param mu: 平均值
    # :param sigma: 标准差，决定波动范围
    # '''
    secs = random.normalvariate(mu, sigma)
    if secs <= 0:
        secs = mu  # 太小则重置为平均值
    return secs


def get_degree(content):
    # 获取degree
    if content.find("博士后") != -1:
        return "博士后"
    elif content.find("博士") != -1:
        return "博士"
    elif content.find("硕士") != -1:
        return "硕士"
    elif content.find("学士") != -1:
        return "学士"
    elif content.find("院士") != -1:
        return "院士"
    elif content.find("本科") != -1:
        return "学士"
    elif content.find("大学学历") != -1:
        return "学士"
    elif content.find("研究生") != -1:
        return "硕士"
    else:
        return ""


def real_name(ename, url):
    # 获取name
    """
    注：
    该函数有一定缺陷
    """
    if ename.find('副教授') != -1:
        name = ename.replace('副教授', '')
        return name
    elif ename.find("资格教授") != -1:
        name = ename.replace('资格教授', '')
        return name
    elif ename.find("教授") != -1:
        name = ename.replace('教授', '')
        return name
    elif ename.find("导师基本情况") != -1:
        name = ename.replace('导师基本情况', '')
        return name
    elif ename.find("在读") != -1:
        name = ename.replace('在读', '')
        return name
    elif ename.find("硕导") != -1:
        name = ename.replace('硕导', '')
        return name
    elif ename.find("中共党员") != -1:
        name = ename.replace('中共党员', '')
        return name
    elif ename.find("博导") != -1:
        name = ename.replace('博导', '')
        return name
    elif ename.find("博士后") != -1:
        name = ename.replace('博士后', '')
        return name
    elif ename.find("博士") != -1:
        name = ename.replace('博士', '')
        return name
    elif ename.find("硕士生导师") != -1:
        name = ename.replace('硕士生导师', '')
        return name
    elif ename.find("导师") != -1:
        name = ename.replace('导师', '')
        return name
    elif ename.find("高级讲师") != -1:
        name = ename.replace('高级讲师', '')
        return name
    elif ename.find("讲师") != -1:
        name = ename.replace('讲师', '')
        return name
    elif ename.find("助教") != -1:
        name = ename.replace('助教', '')
        return name
    elif ename.find("外籍") != -1:
        name = ename.replace('外籍', '')
        return name
    elif ename.find("高级工程师") != -1:
        name = ename.replace('高级工程师', '')
        return name
    elif ename.find("中国工程院院士") != -1:
        name = ename.replace('中国工程院院士', '')
        return name
    elif ename.find("高级实习指导教师") != -1:
        name = ename.replace('高级实习指导教师', '')
        return name
    elif ename.find("高级实验师") != -1:
        name = ename.replace('高级实验师', '')
        return name
    elif ename.find("副主任医师") != -1:
        name = ename.replace('副主任医师', '')
        return name
    elif ename.find("副主任护师职称") != -1:
        name = ename.replace('副主任护师职称', '')
        return name
    elif ename.find("副主任护师") != -1:
        name = ename.replace('副主任护师', '')
        return name
    elif ename.find("主任护师") != -1:
        name = ename.replace('主任护师', '')
        return name
    elif ename.find("教师简介") != -1:
        name = ename.replace('教师简介', '')
        return name
    elif ename.find('（1983年生）') != -1:
        name = ename.replace('（1983年生）', '')
        return name
    elif ename.find('副研究员') != -1:
        name = ename.replace('副研究员', '')
        return name
    elif ename.find('研究员') != -1:
        name = ename.replace('研究员', '')
        return name
    elif ename.find('[图文]') != -1:
        name = ename.replace('[图文]', '')
        return name
    elif ename.find('校外') != -1:
        name = ename.replace('校外', '')
        return name
    elif ename is None:
        webbrowser.open(url)
        name = input('name:')
        return name
    else:
        return ename


def get_title(content):
    # 获取title
    """
    注：
    该函数有一定缺陷
    """
    if content.find("副教授") != -1:
        return "副教授"
    elif content.find("教授") != -1:
        return "教授"
    elif content.find("中国工程院院士") != -1:
        return "院士"
    elif content.find('副研究员') != -1:
        return '副研究员'
    elif content.find('研究员') != -1:
        return '研究员'
    elif content.find("讲师") != -1:
        return "讲师"
    elif content.find("助教") != -1:
        return "助教"
    elif content.find("实验师") != -1:
        return "实验师"
    else:
        return ""


def only_Chinese(content):
    # 只保留字符串中的中文字符
    text = re.sub('[^\u4e00-\u9fa5]+', '', content)
    return text


def clean_text(text):
    """
    清理文本，删除特殊符号，将多个空格替换为一个空格，将多个换行符替换为一个换行符。

    参数:
    text (str): 需要清理的文本

    返回:
    str: 清理后的文本
    """
    # 删除特殊符号
    # text = re.sub(r'[★]', '', text)
    #
    # 将多个空格替换为一个空格
    # text = re.sub(r'\s+', ' ', text)
    #
    # 将多个换行符替换为一个换行符
    # text = re.sub(r'\n+', '\n', text)

    text = text.replace(' ',' ').replace(' ',' ').replace('​',' ').replace('﻿',' ').replace('\u3000', ' ').replace('\xa0', ' ')

    return text.strip()


def sp_clear(content):
    # 清除各式转义符
    pattern = re.compile(r'[\n\r\t]')
    clean_text = re.sub(pattern, '', content)
    return clean_text


def sp_kongclear(content):
    # 清除空格
    return content.replace(" ", "")



def add_elements_to_strings(str_list):
    new_strings = []
    for element in str_list:
        new_strings.append(element)
        new_strings.append(f"\n {element}")
        new_strings.append(f"\n{element}")
        new_strings.append(f"{element} \n")
        new_strings.append(f"{element}\n")
        new_strings.append(f"{element}:")
        new_strings.append(f"{element}: \n")
        new_strings.append(f"{element}:\n")
        new_strings.append(f"{element}：")
        new_strings.append(f"{element}：\n")
        new_strings.append(f"{element}\n")
        new_strings.append(f"{element}为")

    new_strings = list(set(new_strings))
    return new_strings


def get_dir(content, url):
    """
    获取一段任意中文文本中 研究方向类
    : MAX_NUM = 999999999
    : dirs 为该文本下所有满足条件的 研究发现类
    : return: 返回一个dirs中满足一定条件的 研究方向类
    模式为：
    xxx前关键字 研究方向类 后关键字xxx
    """
    # 初始化direction和directions
    direction = ''
    directions = []

    # 前关键字库
    # FrontKeyWords = ["方向：", "从事专业：", "专业领域", "从事方向", "从事领域", "研究方向：", "研究方向:","研究方向",
    #                  "研究方向和服务领域：","研究方向\n","Research Areas",
    #                  "研究方向：\n","研究领域（方向）","研究方向 Research Interests",
    #                  "研究领域：","研究领域与兴趣", "Research Interest",
    #                  "现从事学科、专业、方向", "长期从事", "主要从事", "致力于", "研究兴趣", "主要研究领域",
    #                  "主要研究内容", "主要研究领域包括", "招生方向", "主要研究方向:", "主要研究方向","主要研究",
    #                  "目前从事", "主要方向", "科研方向", "学科方向", "学术方向", "科研领域",
    #                  "研究工作：","RESEARCH AREAS",
    #                  "研究工作:", "研究工作是", "研究工作为", "学术领域", "科研兴趣", "主要研究领域或方向","学科领域","研究领域、方向与兴趣："]
    FrontKeyWords = ["方向", "从事专业", "专业领域", "从事方向", "从事领域",  "研究方向",
                     "研究方向和服务领域", "Research Areas", "研究领域（方向）", "研究方向 Research Interests",
                     "研究领域", "研究领域与兴趣", "Research Interest",
                     "现从事学科、专业、方向", "长期从事", "主要从事", "致力于", "研究兴趣", "主要研究领域",
                     "主要研究内容", "主要研究领域包括", "招生方向", "主要研究方向", "主要研究方向", "主要研究",
                     "目前从事", "主要方向", "科研方向", "学科方向", "学术方向", "科研领域", "RESEARCH AREAS",
                     "研究工作:", "研究工作是", "研究工作为", "学术领域", "科研兴趣", "主要研究领域或方向", "学科领域","研究领域、方向与兴趣","专业特长"]
    # FrontKeyWords = add_elements_to_strings(FrontKeyWords)
    # FrontKeyWords = add_elements_to_strings(FrontKeyWords)
    # 后关键字库
    LastKeyWords = ["招生与培养","电子邮件","办公室","学术兼职","奖励与荣誉", "邮    箱：", "电子邮箱", "办公电话", "电话", "邮箱", "教学课程：",
                    "通讯地址", "主要","获奖成果","教育与工作经历","研究成果","代表性论文","Honors","HONORS",
                    "导师", "。", "科研成果", "主要成果", "Education", "Professional Experience:", "Awards",
                    "承担", "讲授", "论文", "科研工作", "个人", "社会兼职", "教学经历", "主讲课程",
                    "教授课程", "等","基本信息", "email", "教学", "教学方向", "代表成果", "教育背景", "教育经历",
                    "代表性论文", "开设课程", "科研项目", "主 要 论 著", "专著教材", "Email", "学术论著", "个人简介",
                    "联系方式", "代表作", "过去的主要工作", "课题项目",
                    "招收", "招生专业", "学术成果", "主讲课程", "讲授","部分主持项目",
                    "代表性", "学术代表作", "社会兼职", "学术任职", "代表性", "联系电话", "20", "19", "Email",
                    "教育背景","招生学科"]
    # 黑名单库
    BlacklistWords = ["博士", "研究生", "硕士", "简介"]
    # 获取两个库的最大长度
    LengthLibrary = max(len(FrontKeyWords), len(LastKeyWords))

    # 初始化两个库在文本中的索引位置
    IndexFront = [x * 0 + MAX_NUM for x in range(0, LengthLibrary)]
    IndexLast = [x * 0 + MAX_NUM for x in range(0, LengthLibrary)]

    # 获取前关键字在文本中的位置
    for i in range(0, len(FrontKeyWords)):
        try:
            IndexFront[i] = content.index(FrontKeyWords[i])
        except:
            IndexFront[i] = MAX_NUM
    # 对前关键字位置进行排序，并返回下标
    SubscriptListFront = paixu(IndexFront)

    # 同上
    for j in range(0, len(LastKeyWords)):
        try:
            IndexLast[j] = content.index(LastKeyWords[j])
        except:
            IndexLast[j] = MAX_NUM
    SubscriptListLast = paixu(IndexLast)

    for sp in SubscriptListFront:  # 对SubscriptListFront进行遍历
        if IndexFront[sp] != MAX_NUM:  # 找到该文本下存在的前关键字下标
            for ss in SubscriptListLast:  # 对SubscriptListLast进行遍历
                if IndexLast[ss] == MAX_NUM:  # 若未找到后关键字，则向后匹配到文本结束
                    pattern = f'{FrontKeyWords[sp]}(.*)'
                    GroupDirs = re.findall(pattern, content, re.S | re.M)
                    directions.append(GroupDirs)
                    break
                elif IndexLast[ss] != MAX_NUM:  # 若找到后关键字，则匹配模式
                    pattern = f'{FrontKeyWords[sp]}(.*?){LastKeyWords[ss]}'
                    GroupDirs = re.findall(pattern, content, re.S | re.M)
                    directions.append(GroupDirs)

    # 对directions进行清洗，去除不包含中文的元素
    directions_x = []
    for i in range(0, len(directions)):
        if len(directions[i]) != 0:
            for j in range(0, len(directions[i])):
                directions_x.append(sp_clear(directions[i][j]))

    # 得到该文本下所有满足模式的 研究方向类 并以元素长度降序排列
    # 可在此进行debugger
    dirs = sorted(directions_x, key=lambda k: len(k))
    # print(dirs)

    # 若dirs中无元素，则该文本下无 研究方向类
    if len(dirs) == 0:
        direction = ''
        return direction.strip()

    # 对dirs中的满足一定条件并长度最小的元素进行返回
    for i in range(0, len(dirs)):
        if len(dirs[i]) >= 3:
            blackflag = 1
            for blackword in BlacklistWords:
                if blackword in dirs[i]:
                    blackflag = 0
                    break
            if blackflag == 1:
                return dirs[i].strip()
    return direction.strip()


def get_achievements(content, url):
    """
    获取一段任意中文文本中 研究方向类
    : MAX_NUM = 999999999
    : dirs 为该文本下所有满足条件的 研究发现类
    : return: 返回一个dirs中满足一定条件的 研究方向类
    模式为：
    xxx前关键字 研究方向类 后关键字xxx
    """
    # 初始化direction和directions
    direction = ''
    directions = []

    # 前关键字库
    FrontKeyWords = [
        '部分论文',
        'SLECTED PUBLICATIONS',
        '代表性论文(*通讯作者，#第一作者)',
        '代表作（*为通讯作者，#为共同一作）',
        'REPRESENTATIVE PUBLICATIONS',
        'CURRENT RESEARCH PROJECTS',
        '部分主持项目',
        'SELECTED PUBLICATIONS',
        'Selected Publications',
        '论文、著作、专利：',
        '主要代表作品',
        '近期发表文章',
        '代表性著作',
        '论文发表',
        '四、科研成果',
        '发表文章\n',
        '近期主要代表论著：',
        '近5年发表的部分文章：',
        '主要代表论文',
        '主要学术发表成果包括',
        '【科研业绩】',
        '代表成果',
        '科研信息',
        '主要研究方向及成果：',
        '研究方向及成果：',
        '专利成果',
        '出版信息',
        '论文著作',
        '先后在国际',
        '科研方面：',
        '科研论文：',
        '曾参与国家',
        '近五年代表性成果',
        '主要研究项目',
        '学术研究',
        '学术成果',
        '专利论著',
        '论著专利',
        '研究课题',
        '课题项目',
        '项目成果',
        '论文论著',
        '主 要 论 著',
        '主要发表论文',
        '主要发表论文及专著：',
        '发表论文及专著',
        '主要成果',
        '主要论著',
        '代表性教学及科研成果',
        '代表性论著',
        '代表性成果',
        '代表性\n教学成果',
        '代表性研究成果',
        '代表性论文',
        '代表论文',
        '代表作：',
        '发表论文代表作',
        '主要研究成果',
        '研究成果',
        '研究情况',
        '主要科研成果',
        '主要研究课题',
        '科研成果',
        '主要论文：',
        '主持及参与',
        '近年来，以第一作者身份在',
        '近年来，先后主持或参与',
        '近年先后主持',
        '先后主持',
        '目前，主持国家级项目',
        '目前，主持省部级项目',
        '主持',
        '近年，主持国家',
        '近年，主持省部',
        '近年来，先后在《',
        '近年来，在《',
        '近年来在《',
        '先后在《',
        '在《',
        '承担和参与',
        '承担项目',
        '发表学术论文',
        '科研项目',
        '主要学术成果',
        'Representative Research Works:',
        '科研及获奖情况',
    ]
    index_list = []
    for i in FrontKeyWords:
        if content.find(i) != -1:
            index_list.append([content.find(i), i])
    if index_list == []:
        return ''
    index_list.sort(key=lambda ele: ele[0], reverse=False)
    return content[index_list[0][0]::]


def get_introduction(content, url):
    """
    获取一段任意中文文本中 研究方向类
    : MAX_NUM = 999999999
    : dirs 为该文本下所有满足条件的 研究发现类
    : return: 返回一个dirs中满足一定条件的 研究方向类
    模式为：
    xxx前关键字 研究方向类 后关键字xxx
    """
    # 初始化direction和directions
    direction = ''
    directions = []

    # 前关键字库,删除了'发表论文'
    FrontKeyWords = [
        '部分论文',
        'SLECTED PUBLICATIONS',
        '代表性论文(*通讯作者，#第一作者)',
        '代表作（*为通讯作者，#为共同一作）',
        'REPRESENTATIVE PUBLICATIONS',
        'CURRENT RESEARCH PROJECTS',
        '部分主持项目',
        'SELECTED PUBLICATIONS',
        'Selected Publications',
        '论文、著作、专利：',
        '主要代表作品',
        '近期发表文章',
        '代表性著作',
        '论文发表',
        '四、科研成果',
        '发表文章\n',
        '近期主要代表论著：',
        '近5年发表的部分文章：',
        '主要代表论文',
        '主要学术发表成果包括',
        '【科研业绩】',
        '代表成果',
        '科研信息',
        '主要研究方向及成果：',
        '研究方向及成果：',
        '专利成果',
        '出版信息',
        '论文著作',
        '先后在国际',
        '科研方面：',
        '科研论文：',
        '曾参与国家',
        '近五年代表性成果',
        '主要研究项目',
        '学术研究',
        '学术成果',
        '专利论著',
        '论著专利',
        '研究课题',
        '课题项目',
        '项目成果',
        '论文论著',
        '主 要 论 著',
        '主要发表论文',
        '主要发表论文及专著：',
        '发表论文及专著',
        '主要成果',
        '主要论著',
        '代表性教学及科研成果',
        '代表性论著',
        '代表性成果',
        '代表性\n教学成果',
        '代表性研究成果',
        '代表性论文',
        '代表论文',
        '代表作：',
        '发表论文代表作',
        '主要研究成果',
        '研究成果',
        '研究情况',
        '主要科研成果',
        '主要研究课题',
        '科研成果',
        '主要论文：',
        '主持及参与',
        '近年来，以第一作者身份在',
        '近年来，先后主持或参与',
        '近年先后主持',
        '先后主持',
        '目前，主持国家级项目',
        '目前，主持省部级项目',
        '主持',
        '近年，主持国家',
        '近年，主持省部',
        '近年来，先后在《',
        '近年来，在《',
        '近年来在《',
        '先后在《',
        '在《',
        '承担和参与',
        '承担项目',
        '发表学术论文',
        '科研项目',
        '主要学术成果',
        'Representative Research Works:',
        '科研及获奖情况',
    ]
    index_list = []
    for i in FrontKeyWords:
        if content.find(i) != -1:
            index_list.append([content.find(i), i])
    if index_list == []:
        return content
    index_list.sort(key=lambda ele: ele[0], reverse=False)
    return content[0:index_list[0][0]:]


def get_info(content, url):
    # 原理同dir
    find_words = ['奖项', '一等奖', '二等奖', '三等奖', '研究成果', '科研成果', '代表成果', '代表性论文',
                  '代表性成果', '科研项目', '代表项目', '代表性论文与专著', '代表性论文专著', '代表论著',
                  '代表性论文及专著', '论文成果', '发表论文', '学术论著']
    split_words = ['。', '\n', ':', '：']
    Max_num = max(len(find_words), len(split_words))
    suoyin = [x * 0 + MAX_NUM for x in range(0, Max_num)]
    ach = ''
    for i in range(0, len(find_words)):
        try:
            suoyin[i] = content.index(find_words[i])
        except:
            suoyin[i] = MAX_NUM
    sub_list_f = paixu(suoyin)
    if suoyin[sub_list_f[0]] == MAX_NUM:
        print('该教授未找到奖项', end=" ")
        print(url)
        print(suoyin)
        print(content)
        info = content
    else:
        text_str = content.split(find_words[sub_list_f[0]])[0]
        max_num = 0
        index_j = 0
        for j in range(0, len(split_words)):
            t = text_str.rfind(split_words[j])
            if max_num < t:
                max_num = t
                index_j = j
        a = content[max_num]
        info = content[:max_num + 1]
        ach = content[max_num + 1:]
    return info, ach


def paixu(list):  # 以降序排列
    down_list = sorted(range(len(list)), key=lambda k: list[k])
    return down_list


def get_email(content):
    try:
        if content.find("@") != -1:
            youxiang = re.search(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:\.[A-Za-z]{2,})?', content).group()
            return youxiang
        elif content.find("(at)") != -1:
            youxiang = re.search(r'[A-Za-z0-9._%+-]+\(at\)[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:\.[A-Za-z]{2,})?', content).group()
            return youxiang
        else:
            return ""
    except:
        return ""


def get_phone(content):
    phone2 = ''
    phone__ = re.findall(r'(\d{2,4})-(\d{7,8})', content)
    if len(phone__) > 0:
        phone2 = ' '+phone__[0][0] + '-' + phone__[0][1]
    phone3 = ''
    phone__3 = re.findall(r'\((\d{2,4})\)(\d{7,8})', content)
    if len(phone__3) > 0:
        phone3 = ' '+phone__3[0][0] + '-' + phone__3[0][1]
    phone5 = ''
    phone__5 = re.findall(r'（(\d{2,4})）(\d{7,8})', content)
    if len(phone__5) > 0:
        phone3 = ' '+phone__5[0][0] + '-' + phone__5[0][1]
    phone4 = ''
    phone__4 = re.findall(r'\((\d{2,4})\) , (\d{3,4})-(\d{3,4})', content)
    if len(phone__4) > 0:
        if phone__4[0][0][0] != 0:
            phone4 = ' '+'0' + phone__4[0][0] + '-' + phone__4[0][1] + phone__4[0][2]

    phone6 = ''
    phone__6 = re.findall(r'\(\+86\)(\d{3,4})\s(\d{7,8})', content)
    if len(phone__6) > 0:
        if phone__6[0][0][0] != 0:
            phone6 = ' '+'0' + phone__6[0][0] + '-' + phone__6[0][1]

    # phone7 = ''
    # phone__7 = re.findall(r'(\d{7,8})', content)
    # if len(phone__7) >0:
    #     return '010-'+phone__7[0]
    phone = []
    phone_str = ""
    pattern = r"\d+"

    # 使用re.findall()方法匹配模式
    result = re.findall(pattern, content)

    # 选择以 "1" 开头且长度为 11 位的数字字符串
    selected_numbers = [number for number in result if number.startswith("1") and len(number) == 11]
    for phone_number in selected_numbers:
        phone.append(phone_number)
    if len(phone) == 0:
        phone = "" + phone2 + phone3 + phone4 + phone5 + phone6
        return phone
    else:
        for number in phone:
            phone_str += number+" "
    phone_str = phone_str + phone2 + phone3 + phone4 + phone5 + phone6
    return phone_str.strip()


def get_address(text):
    if re.search('地址', text):
        address = re.search('地址(.*)', text).group(1)
    else:
        address = ""
    return address


def timeStampConvert(link):
    id = '-'.join(link.split("/")[1::])
    return id


def download(url, heads, dir):
    """
    简易文件下载方法
    :param url:下载链接
    :param heads: 请求头
    :param dir: 下载位置 尽量使用文件类型作为下载位置
    :return: 下载文件绝对位置
    """
    response = requests.get(url, headers=heads, verify=False)
    if not os.path.exists(dir):
        os.makedirs(dir)
    filename = os.path.join(dir, os.path.basename(urlparse(url).path))
    file_type = url.split('.')[-1]
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"{file_type} downloaded successfully to {url}")
        return os.path.abspath(filename)
    else:
        print(f"Failed to download {file_type}. Status code: {response.status_code}")
    return filename


def extract_text_from_pdf(pdf_path):
    """
    :param pdf_path: pdf 文件位置
    :return: pdf 文件解析内容
    """
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            txt = page.extract_text()
            page = re.sub(r'^\d\s', '', txt)
            text += page
            txt = extract_text(pdf_path)
            text = re.sub(r'^\d\s', '', txt)
    return text


def read_image(name):
    """
    :param name:img位置
    :return: img解析内容 可能不正确
    """
    return pytesseract.image_to_string(Image.open(name), lang='-l chi_sim+eng')


def sha256_hash(text):
    """
    sha256算法生成id
    :param text: 输入文本内容
    :return: hash码
    """
    hash_object = hashlib.sha256(text.encode())
    return hash_object.hexdigest()


def print_json(o):
    print(json.dumps(o, indent=4, ensure_ascii=False))


def get_img(soup, link, length=1, index=0):
    t = soup.find_all('img')
    print(t)
    print(len(t))
    if len(t) < length:
        return ''
    # print(t[index])
    return urljoin(link, t[1].get('src'))

def get_obj_exp(obj_exp_list):
    obj_exp = {
        "name": "",
        "title": "",
        "degree": "",
        "school": obj_exp_list.get('school'),
        "college": obj_exp_list.get('college'),
        "city": obj_exp_list.get('city'),
        "province": obj_exp_list.get('province'),
        "address": obj_exp_list.get('address'),
        "photo": "",
        "phone": "",
        "collegePhone": obj_exp_list.get('collegePhone').replace(' ',''),
        "researchPhone": obj_exp_list.get('researchPhone').replace(' ',''),
        "direction": "",
        "email": "",
        "url": "",
        "introduction": "",
        "achievements": "",
        "id": "",
    }
    return obj_exp

def get_tag_resume(url,combined_list):
    html = get_all(url, head)
    for i in combined_list:
        elements = html.find_all(i[0], attrs={i[1]: i[2]})
        if elements:
            print('使用得combined_list',i)
            return elements # 返回找到的第一个匹配元素的文本内容
    return None  # 如果没有找到任何匹配的元素，返回None


def get_son_url_name(page,source_url,vals_list,p_list,index_p,index_name):
    link_name_list = []
    name_set = ['', '更多', '上页', '下页', '首页', '尾页', '跳转', '第一页', '<<上一页', '下一页>>', '跳转到', '师资队伍',
                '[详细]', '研究方向：', '助理', '副教授', '教授', '院士', '副研究员', '研究员', '讲师', '助教', '实验师','教辅人员','党务政工人员'
                ,'人才建设','正高级专业技术人员']
    requests.packages.urllib3.disable_warnings()
    link_Set = ['javascript:;','javascript:void(0);','javacript:void(0)'
                ]
    for i in page:
        print(i)
        all_html = get_all(i, head=head)
        #all_html = BeautifulSoup(xyz, 'html.parser')
        # all_html = BeautifulSoup(i, 'html.parser')
        vals = all_html.find_all(vals_list[0], attrs={vals_list[1]:vals_list[2]})
        #vals = all_html.find_all('tbody')
        #vals = all_html.find_all('ul')
        # print(vals)
        for j in vals:
            syz = '123'
            if index_p == 0:
                p = j.find_all(p_list[0])
            elif index_p == 1:
                p = j.find_all(p_list[0], attrs={p_list[1]: p_list[2]})
            elif index_p == 2:
                link_name = j.find_all('a')
                p = j
                c = j
                syz = '321'
            # if syz == '123':
            for c in p:
                link_name = c.find_all('a')
                for nasdad in link_name:
                    if nasdad.text is not None and 'href' in nasdad.attrs:
                        link = nasdad.get('href').strip()
                        # link = link.replace('http://','https://')
                        #print(link)
                        #print(urljoin(source_url, link))
                        if index_name == 1:
                            #name1 = c.find_all('div', attrs={'class':'teacherText1'})[0].get_text()
                            name1 = c.find_all('div')[0].get_text()
                        elif index_name == 2:
                            name2 = c.find_all('div', attrs={'class': 'a_box'})
                            name1 = name2.find_all('p')[0].get_text()
                            #print(name1)
                        else:
                            print('222222222222222222',nasdad)
                            name1 = nasdad.text.strip()
                            # span_tag = nasdad.find('span')
                            # name1 = span_tag.text
                            print('222222222222222222',name1)
                            #name1 = c.find_all('span')[0].text
                            #print(name1)
                            #print('11111111111111111111111',nasdad)
                        # name1 = nasdad.get('title').strip()
                        # name1 = c.find_all('div',attrs={'class':'name_new'})[0].get_text()
                        name = name1.replace('院士','').replace('博士生','').replace('硕士生','').replace('[object Object]','').replace(' ','').replace(' ','').replace('​','').replace('*','').replace('简介','').replace('副教授','').replace('教授','').replace('讲师','').replace('博士','').replace('研究生','').replace('研究员','').replace('导师','').replace('\n','')
                        name = name.replace(' ','').split('——')[-1].split('，')[0].split('\n')[0].split('导师')[0].split('个人')[0]
                        #name = name[:-10]
                        if '病区' not in name and 2 <= len(name) and name not in name_set and link not in link_Set and urljoin(source_url, link) not in link_Set and link not in ['#'] :
                            link_Set.append(urljoin(source_url, link))
                            link_Set.append(link)
                            name_set.append(name)
                            link_name_list.append([urljoin(source_url, link), name])
                            #link_name_list.append([source_url+link.split('../')[-1], name])
                            #print(link)
                            #link_name_list.append([link, name])
    print("***********************************************\nj: {}".format(j))
    print("***********************************************\np: {}".format(p))
    print("***********************************************\nc: {}".format(c))
    return link_name_list


def get_other1(url, name, obj_exp, combined_list):
    dir = ''
    id = ''
    title = ''
    introduction = ''
    degree = ''
    text = ''
    link = url
    dir = ''
    id = ''
    title = ''
    introduction = ''
    degree = ''
    img = ''
    obj = obj_exp.copy()
    #print(link)
    #value = get_all(url, head)
    name_true = name
    t2 = get_tag_resume(url,combined_list)
    # print('55555555555555555555',t2)
    # print(t2[3])
    if not t2:
        # webbrowser.open(link)
        print(link)
        return None
    x = ''
    for i in t2:
        x += i.text.strip()
    img = get_img(t2[0], link, )
    #print(img)

    text = re.sub(r'\n+', '\n',x.replace('   ', ' ').replace('\r', '   ').replace('\t', '   ').replace(' ', '').replace('@@', '@').strip())
    # text = text.split('基本信息\n')[-1]
    # print(text)
    try:
        # print(text.split(f'{name}'))
        text = ''.join(text.split(f'{name}')[1:]).split('版权所有')[0]
        # text = text.split('引领科学前沿、面向国家需求、服务区域发展人才详细信息\n')[-1].split('Name')[-1]

        text = text
    except:
        text = text
    # print(text)
    #print(text.replace('\n', '\\n'))
    # paragraphs = textwrap.dedent(text).strip().split('\n')
    # translator = Translator()
    # # 逐段翻译并存储结果
    # translated_paragraphs = []
    # for paragraph in paragraphs:
    #     print(paragraph)
    #     translation = translator.translate(paragraph, src='auto', dest='zh-cn')
    #     print(translation.text)
    #     translated_paragraphs.append(translation.text)
    #
    # # 合并翻译结果
    # translated_text = '\n'.join(translated_paragraphs)
    # text = translated_text
    dir = get_dir(text, link)
    title = get_title(text)
    degree = get_degree(text)
    ach = get_achievements(text, link)
    introduction = get_introduction(text, link)
    email = get_email(text)
    phone = get_phone(text)
    id = timeStampConvert(link)
    dir = re.sub(r'^[^\w]+', '', dir)
    dir = re.sub(r'[^\w]+$', '', dir)
    obj['name'] = clean_text(name_true.split('/')[0])
    obj['photo'] = img
    obj['direction'] = dir
    obj['title'] = title
    obj['url'] = link
    obj['degree'] = degree
    obj['achievements'] = ach #clean_text(ach)#.replace(' ','')
    obj['introduction'] = introduction #clean_text(introduction)#.replace(' ','')
    obj['email'] = email
    obj['phone'] = phone
    obj['id'] = id
    # exit(0)
    return obj



def get_other2(url_list, name, obj_exp, combined_list):
    t2_list = []
    x = ''
    for url in url_list:
        link = url
        obj = obj_exp.copy()
        name_true = name
        t2 = get_tag_resume(url,combined_list)
        if not t2:
            # webbrowser.open(link)
            print(link)
            return None
        for i in t2:
            x += i.text.strip()
    img = get_img(t2[0], link, )
    #print(img)

    text = re.sub(r'\n+', '\n',x.replace('   ', ' ').replace('\r', '   ').replace('\t', '   ').replace(' ', '').replace('@@', '@').strip())
    # text = text.split('基本信息\n')[-1]
    try:
        text = text.split('全所PI名录\n院士风采\n杰出青年首页　　 人才队伍\n个人信息')[-1]
    except:
        text = text
    dir = get_dir(text, link)
    title = get_title(text)
    degree = get_degree(text)
    ach = get_achievements(text, link)
    introduction = get_introduction(text, link)
    email = get_email(text)
    phone = get_phone(text)
    id = timeStampConvert(link)
    dir = re.sub(r'^[^\w]+', '', dir)
    dir = re.sub(r'[^\w]+$', '', dir)
    obj['name'] = clean_text(name_true.split('/')[0])
    obj['photo'] = img
    obj['direction'] = dir
    obj['title'] = title
    obj['url'] = link
    obj['degree'] = degree
    obj['achievements'] = ach #clean_text(ach)#.replace(' ','')
    obj['introduction'] = introduction #clean_text(introduction)#.replace(' ','')
    obj['email'] = email
    obj['phone'] = phone
    obj['id'] = id
    # exit(0)
    return obj