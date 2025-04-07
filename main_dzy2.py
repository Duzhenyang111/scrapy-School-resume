from tool_dzy import *
import pickle
import itertools

obj_exp_list = {'college': '地理科学与资源研究所', 'collegePhone': "010-64889276",
                "researchPhone": "010-64889276", "school": "地理科学与资源研究所",
                "province": "北京", 'city': '北京', "address": "北京海淀区中关村南四街4号中国科学院软件园"}

#teacher_resume_url
tag1_list = ['div', 'ul','form','p']
tag2_list = ['class','name', 'id']
tag3_list = ['container','col-md-9 col-sm-8','container','TRS_PreAppend','col-md-9 col-sm-8','wrap_w wrap_content2 fr','xlmain','el-tabs__content','wrapper','ny-right','MsoNormal','mainco','info-box','container','teamShow','secondarydetailbox bgbai1','secondarydetailbox','contMain','ContentBox','w1170 mat70 padt20','v_news_content','_newscontent_fromname','carea','teadtl','news-content','Section1','container p-0','subscribe','col-lg-8 col-md-8 col-sm-9','Section0','v_news_content','szShow','article','subArticle','ins_research',
             'art_news f14px art','dft-main clearfix','mainpages','vsb_content_2','vsb_content_4','left','_newscontent_fromname','v_news_content', 'textLayer',
             'main','juzhong', 'page', 'jieli', 'Lp', 'cn-content', 'content', 'vsb_content','rightContent', 'rightBox', 'w770 grid', 'sy-middle-id fl', 'TabbedPanels1',
             'mainCont', 'per-infor', 'baseinfoBar clearfix','w1400']
tag1_list = ['body']
tag2_list = ['id']
tag3_list = ['myzone3','myzone2','myzone1','myzone4']
# tag3_list = list(set(tag3_list))
# original_list = [(t1, t2, t3) for t1 in tag1_list for t2 in tag2_list for t3 in tag3_list]
# combined_list = set(original_list)
combined_list = list(itertools.product(tag1_list, tag2_list, tag3_list))
print(combined_list)
obj_exp = get_obj_exp(obj_exp_list)
if __name__ == "__main__":
    res_fin = []
    none_url = []
    # 从文件中读取 link_list_value
    with open('D:/pythonProject/python_job/暂存/link_list_value.pkl', 'rb') as f:
        link_list_value = pickle.load(f)
    # link_list_value = link_list_value[:10]
    # 打印调试信息
    for i in link_list_value:
        i[0] = i[0].replace('http://','https://')
    print('1111111111111111111111', link_list_value)
    print('**************************', len(link_list_value), '**********************************')
    index = 0
    index_1 = 0
    length = len(link_list_value)
    # 处理 link_list_value
    for i in link_list_value:
        index += 1
        o = None
        while True:
            try:
                o = get_other1(url=i[0], name=i[1], obj_exp=obj_exp, combined_list=combined_list)
                # print(o)
            except Exception as e:
                print(e)
                continue
            break
        if o is not None and o.get("introductions") != "":
            index_1 += 1
            print(json.dumps(o, indent=4, ensure_ascii=False))
            print('****************有效数量:{} | 爬取数量:{} | 总数量:{}****************'.format(index_1,index,length))
            res_fin.append(o)
        else:
            none_url.append(i[0])
    #print(o)
    print(none_url)
    # with open("{}-{}.json".format(obj_exp['school'],obj_exp['college']), "w", encoding='utf-8') as f:
    with open("{}.json".format(obj_exp['college']), "w", encoding='utf-8') as f:
        json_loads = json.dumps(res_fin, ensure_ascii=False, indent=2)
        f.write(json_loads)
        f.flush()