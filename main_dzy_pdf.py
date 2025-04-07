# -*- coding:utf-8 -*-
import os
import random
import re
import time
from bs4 import BeautifulSoup  # 网页解析，获取数据
import requests
import webbrowser
import simplejson as json
from urllib.parse import urljoin, urlparse
from tool_dzy import *




#father_url
page = [
    'https://cdwyxy.ccu.edu.cn/szdw/zyyyyx.htm',
]
page = [
    #'https://chuban.bigc.edu.cn/xygk/szdw/szcbzy/index.htm',
    #'https://chuban.bigc.edu.cn/xygk/szdw/bjcbxzy/index.htm',
    'https://kouqiang.dmu.edu.cn/info/1046/1954.htm',

]



#jsonmoban
obj_exp_list = {'college': '口腔医学院', 'collegePhone': "0411-86110394", "researchPhone": "0411-86110023",
                 "school": "大连医科大学", "province": "辽宁", 'city': '大连', "address": "辽宁省大连市旅顺南路西段9号"}

#father_and_son
vals_list = ['div', 'class', 'v_news_content']
p_list = ['p', 'class', 'team_list']
index_p = 0  # 0为基本模式 1为特殊模式 2为跳过
index_name = 0  # 0为基本模式 1为特殊模式
#teacher_resume_url
tag1_list = ['div', 'ul', 'from']
tag2_list = ['class', 'id', 'name']
tag3_list = ['subscribe','col-lg-8 col-md-8 col-sm-9','Section0','v_news_content','szShow','article','subArticle','ins_research','art_news f14px art','dft-main clearfix','mainpages','vsb_content_2','vsb_content_4','left','_newscontent_fromname',
             'v_news_content', 'textLayer', 'main', 'page', 'jieli', 'Lp', 'cn-content', 'content', 'vsb_content',
             'rightContent', 'rightBox', 'w770 grid', 'sy-middle-id fl', 'TabbedPanels1', 'mainCont', 'per-infor', 'baseinfoBar clearfix']
tag3_list = list(set(tag3_list))
original_list = [(t1, t2, t3) for t1 in tag1_list for t2 in tag2_list for t3 in tag3_list]
combined_list = set(original_list)


obj_exp = get_obj_exp(obj_exp_list)
source_url = page[0].split('cn/')[0]+'cn/'+'info/'
print(source_url)
#source_url = 'https://pac.bistu.edu.cn/yjspy/dsfc/'
#print(source_url)
name_set = ['', '更多', '上页', '下页', '首页', '尾页', '跳转', '第一页', '<<上一页', '下一页>>', '跳转到',
                '[详细]', '研究方向：', '助理', '副教授', '教授', '院士', '副研究员', '研究员', '讲师', '助教', '实验师','打印']

if __name__ == "__main__":
    res_fin = []
    # link_List_Value=[]
    #print('22222222222222222222222222222222222')
    link_List_Value = get_son_url_name(page, source_url, vals_list, p_list, index_p, index_name)
    print('1111111111111111111111', get_son_url_name(page, source_url, vals_list, p_list, index_p, index_name))
    print('**************************', len(link_List_Value), '**********************************')
    for i in link_List_Value:
        o = None
        while 1:
                try:
                    #o = get_other1(url=i[0], name=i[1], obj_exp=obj_exp, combined_list=combined_list)
                    # all_html = get_all(i[0],head)
                    # vals = all_html.find_all(vals_list[0], attrs={vals_list[1]: vals_list[2]})
                    # res1 = str(vals).split('showVsbpdfIframe("')[-1].split('","100%"')[0]
                    # soup = get_all(i[0], head)
                    # ss = soup.find_all('script')[-6]
                    # print(ss)
                    # link = str(ss).split('showVsbpdfIframe("')[-1].split('","100%"')[0]
                    link = i[0]
                    url = urljoin(source_url, link)
                    if 'pdf' in url:
                        asd123 = download(url, head, 'D:/pythonProject/python_job/pdf')
                        text = extract_text_from_pdf(asd123)
                        obj = obj_exp.copy()
                        dir = get_dir(text, link)
                        title = get_title(text)
                        degree = get_degree(text)
                        ach = get_achievements(text, link)
                        introduction = get_introduction(text, link)
                        email = get_email(text)
                        phone = get_phone(text)
                        id = timeStampConvert(link)
                        name_true = clean_text(i[1].replace(' ','').strip())

                        obj['name'] = name_true
                        #obj['photo'] = img
                        obj['direction'] = dir
                        obj['title'] = title
                        obj['url'] = link
                        obj['degree'] = degree
                        obj['achievements'] = clean_text(ach)  # .replace(' ','')
                        obj['introduction'] = clean_text(introduction)  # .replace(' ',''))
                        obj['email'] = email
                        obj['phone'] = phone
                        obj['id'] = id
                        o = obj
                    else:
                        print(1)
                except Exception as e:
                    print(e)
                    continue
                break
        if o is not None and name_true not in name_set:
            name_set.append(name_true)
            print(json.dumps(o, indent=4, ensure_ascii=False))
            res_fin.append(o)
    #print(o)
    with open("123-{}.json".format(obj_exp['college']), "w", encoding='utf-8') as f:
        json_loads = json.dumps(res_fin, ensure_ascii=False, indent=2)
        f.write(json_loads)
        f.flush()