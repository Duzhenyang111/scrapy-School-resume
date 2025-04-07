# scrapy-School-resume

## 项目简介
这是一个基于Python的教师简历信息爬取工具，主要用于自动化收集和整理高校教师的个人简历信息。该工具支持多个学校网站的数据爬取，并能够智能解析和提取教师的基本信息、研究方向、教育背景等内容。

## 功能特点
- 支持多个高校教师网站的数据爬取
- 自动提取教师姓名、职称、研究方向等信息
- 支持PDF文档中的文本提取和解析
- 智能处理不同网站的页面结构
- 数据以JSON格式保存，方便后续处理

## 环境依赖
```
python 3.x
requests
beautifulsoup4
selenium
PyPDF2
pytesseract
pdfminer.six
simplejson
```

## 主要文件说明
- `tool_dzy.py`: 工具函数库，包含以下功能：
  - PDF文本提取
  - 数据清洗
  - 信息结构化
  - URL处理
- `main_dzy1.py`: 负责获取教师列表页面URL和教师个人页面URL
- `main_dzy2.py`: 负责解析教师个人页面并提取简历信息
- `main_dzy_pdf.py`: 负责PDF文件的下载和解析
  - 支持从指定URL下载PDF文件
  - 自动提取PDF中的文本内容
  - 结构化处理教师信息
  - 生成标准化的JSON输出
- `json_change.py`: JSON数据处理工具

## 使用方法
1. 安装依赖包：
```bash
pip install -r requirements.txt
```

2. 配置目标网站信息：
在`main_dzy1.py`中设置目标学校的网站URL：
```python
page_list = [
    'http://example.edu.cn/faculty/',
    # 添加更多学校网站
]
```

3. 运行爬虫：
```bash
# 第一步：获取教师列表
python main_dzy1.py

# 第二步：提取简历信息
python main_dzy2.py
```

4. 输出结果：
程序会在当前目录生成以学院名称命名的JSON文件，包含所有教师的简历信息。

## 注意事项
- 使用前请确保已安装Firefox浏览器和geckodriver
- 遵守网站的robots协议和访问频率限制
- 建议在使用前测试小规模数据
- 不同网站可能需要调整页面解析规则
