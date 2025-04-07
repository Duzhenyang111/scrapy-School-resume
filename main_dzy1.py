from tool_dzy import *
import pickle

#father_url
page = 'https://faculty.cqupt.edu.cn/xyjslb.jsp?urltype=tsites.CollegeTeacherList&wbtreeid=1004&st=0&id=1051&lang=zh_CN#collegeteacher'
page_list = [
    'http://www.iscas.ac.cn/yjsjy2016/dsxx/',

]
#father_and_son
vals_list = ['div', 'class', 'TRS_Editor']
p_list = ['tr', 'class', 'sub_content_item clearfix']
next_list= ['ul', 'class', 'nav clearfix']
index_p = 0  # 0为基本模式 1为特殊模式 2为跳过
index_name = 0  # 0为基本模式 1为特殊模式
source_url = page_list[0].split('cn/')[0]+'cn/'# + 'gwxy/info/123/'#+'jjx/jsfc/'
#source_url = page[0].split('index')[0]
source_url = page_list[0] + '/'
print(source_url)
head = '1'
def get_next_page_url(url):
    all_html = get_all_b(url,head)
    vals = all_html.find_all(next_list[0], attrs={next_list[1]: next_list[2]})
    # print(vals)
    soup = BeautifulSoup(str(vals), 'html.parser')
    # next_page_link = soup.find('a', class_='temp02-page temp02-page-inactive', text='下一页')
    next_page_link = soup.find_all('h3')
    if next_page_link:
        return next_page_link#['href']
    return None

def get_list_page_url(url):
    all_html = get_all_b(url,head)
    vals = all_html.find_all('div', attrs={'class': 'page'})
    print(vals)
    soup = BeautifulSoup(str(vals), 'html.parser')
    next_page_link = soup.find('a', class_='page_btn', text='下一页')
    # next_page_link = soup.find_all('li')
    if next_page_link:
        return next_page_link['href']

# page = 'https://faculty.cqupt.edu.cn/jsjs.jsp?urltype=tree.TreeTempUrl&wbtreeid=1003'
# page_list = []
# page_list.append(page)
# yema = 1
# next_page_url = get_list_page_url(page)
# for i in next_page_url:
#     print('22222222',urljoin('https://faculty.cqupt.edu.cn/',i.find('a')['href']))
# i_list = []
# for i in next_page_url:
#     print('11111111111',i)
#     i_list.append(i['href'])
# print(i_list)
# while True:
#     print(page)
#     next_page_url = get_list_page_url(page)
#     print(next_page_url)
#     if not next_page_url:
#         break
#     all_url = urljoin('http://www.cemps.cas.cn/rcdw/pi/',next_page_url)
#     page_list.append(all_url)
#     page = all_url
#     yema += 1
#     print(yema,page)
#     print(page_list)
# print(f"成功翻页并提取到{len(page_list)}个url")
#
if __name__ == "__main__":
    link_List_Value = get_son_url_name(page_list, source_url, vals_list, p_list, index_p, index_name)
    print('1111111111111111111111', link_List_Value)
    print('**************************',len(link_List_Value),'**********************************')

    # 保存 link_list_value 到文件
    with open('D:/pythonProject/python_job/暂存/link_list_value.pkl', 'wb') as f:
        pickle.dump(link_List_Value, f)
        print("成功将link_list_value保存到link_list_value.pkl文件中。")

