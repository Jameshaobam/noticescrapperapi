from django.test import TestCase
import requests


def main():
    try:
        URL = 'http://127.0.0.1:8000/api/v1/MU'
        MY_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                        'Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56 '
        headers = {"User-Agent": MY_USER_AGENT}
        response = requests.get(URL, headers=headers)

        datas = response.json()
        for data in datas:
            print(f"New notice: {data['is_new_notice']}")
            print(data['head'])
            print(data['url'])
    except Exception as e:
        print(e)

def syllabus():
    try:
        URL="http://127.0.0.1:8000/api/v1/mit-syllabus"
        MY_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                        'Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56 '
        headers = {"User-Agent": MY_USER_AGENT}
        response = requests.get(URL, headers=headers)

        datas = response.json()
        print(datas)
        print(datas.get('status'))
        print(datas['be_ordinance']['head'],datas['be_ordinance']['url'])
        for data in datas['data']:
            print(data['head'],data['url'])

    except Exception as e:
        print(e)

if __name__ == "__main__":
    syllabus()
