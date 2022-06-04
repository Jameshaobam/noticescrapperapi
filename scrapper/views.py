from django.shortcuts import render
from django.http import HttpResponse
import requests
from rest_framework import status
from bs4 import BeautifulSoup
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Notice import Notice,Syllabus
from .serializers import NoticeSerializer,SyllabusSerializer

MY_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                        'Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56 '
@api_view(['GET'])
def scrape_mu(req):
    data = {
        'status': 'Working', 
    }
    try:
        URL = 'https://www.manipuruniv.ac.in/notice'
        
        headers = {"User-Agent": MY_USER_AGENT}
        html_response = requests.get(URL, headers=headers).text
        soup = BeautifulSoup(html_response, 'lxml')
        div = soup.find('div', class_='newsDetailsList')
        print(len(div.find_all('div', class_='row')))
        notices_list = []
        for row in div.find_all('div', class_='row'):
            notice = Notice(head=row.find_next('div', class_='col-sm-12').a.get_text(),
                            url=row.find_next('div', class_='col-sm-12').a['href'])
            if row.find_next('div', class_='col-sm-12').img is not None:
                notice.is_new_notice = True

            notices_list.append(notice)
        for notice_ele in notices_list:
            print(notice_ele.head)
            print(notice_ele.url)
            print(notice_ele.is_new_notice)
        #serializer fields will be used for displaying fields
        serializer = NoticeSerializer(notices_list, many=True)
        return Response({'status': 'Working', "data": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def scrape_mit_syllabus(req):
    data = {
        'status':'working',
    }
    syllabus_list = []
    all_list=[]
    try:
        URL = 'https://mitimphal.in/'
        headers = {"User-Agent": MY_USER_AGENT}
        html_response = requests.get(URL, headers=headers).text
        soup = BeautifulSoup(html_response, 'lxml')
        divs = soup.find_all('div', class_='four columns')
        x = [d for d in divs]
        # print(x[1])
        print("============================")
        t = x[1].find_all('ul')
        # print(t[2])
        print('****************************************')
        
   
        s = [ele for ele in t[2]]

        print('\n' in s)
        while '\n' in s:
            s.remove('\n')
        for i,j in enumerate(s):
            index_of_li = i+1
            if index_of_li % 2 == 0:
                continue
            all_list.append(j.a)

        # print(all_list[0])
        # print(all_list[5:10])
        head = all_list[0].get_text().strip().upper()
        url =all_list[0]['href'].strip()
        #be ordinance
        context = {
            
                'head':head,
                'url':url,
            }
        
        print(head,url,sep='||')
        for ele in all_list[5:10]:
            syllabus = Syllabus(url=ele['href'].strip(), head=ele.get_text().strip())
            print(syllabus.head,syllabus.url,sep='***')
            syllabus_list.append(syllabus) 
        syllabusserializer = SyllabusSerializer(syllabus_list, many=True)      
        return Response({'status': 'Working','be_ordinance':context, "data": syllabusserializer.data}, status=status.HTTP_200_OK)


    except Exception as e:
        print(e)
        return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)

def home(req):
    return render(req,'index.html')
