from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Notice import Notice
from .serializers import NoticeSerializer


@api_view(['GET'])
def scrape_mu(req):
    data = {
        'status': 'Working',
    }

    URL = 'https://www.manipuruniv.ac.in/notice'
    MY_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                    'Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56 '
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

    serializer = NoticeSerializer(notices_list, many=True)
    return Response(serializer.data)


def home(req):
    return render(req,'index.html')
