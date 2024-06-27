from airflow import DAG 
from airflow.operators.python import PythonOperator
# from airflow.operators. import DummyOperator
from airflow.models.variable import Variable
from datetime import datetime,time
import urllib

import requests
import json


def api_request():
    
    # url = "https://api.digitransit.fi/timetables/v1/hsl/"

    # hdr ={
    # # Request headers
    # 'Cache-Control': 'no-cache',
    # 'digitransit-subscription-key': '6a3f029fde0f430c8c468dc2c715f095',
    # }

    # req = urllib.request.Request(url, headers=hdr)
    
    # req.get_method = lambda: 'GET'
    # response = urllib.request.urlopen(req)
    # print(response.getcode())
    # print(response.read())
    
    
    # headers = {"content-type": "application/json"}
    # payload = json.dumps({ "name": "Apple AirPods", "data": { "color": "white", "generation": "3rd", "price": 135}})
    # requestUrl = "https://api.digitransit.fi/timetables/v1/hsl"
    # r = requests.get(requestUrl, headers=headers)
    # print(r.content)
    
    
    try:
        # url = "https://api.digitransit.fi/realtime/trip-updates/v1/hsl/"
        url = "https://api.digitransit.fi/routing-data/v2/hsl"

        hdr ={
        # Request headers
        'Cache-Control': 'no-cache',
        'digitransit-subscription-key': '6a3f029fde0f430c8c468dc2c715f095',
        }

        req = urllib.request.Request(url, headers=hdr)

        req.get_method = lambda: 'GET'
        response = urllib.request.urlopen(req)
        # print(response.getcode())
        print(response.read())
        # pdf_content = response.read()
        # pdf_content = b"%PDF-1.4\n1 0 obj\n<<\n/Type /Catalog\n/Pages 2 0 R\n>>\nendobj\n2 0 obj\n<<\n/Type /Pages\n/Kids [3 0 R]\n/Count 1\n>>\nendobj\n3 0 obj\n<<\n/Type /Page\n/Parent 2 0 R\n/Resources <<\n>>\n/MediaBox [0 0 200 200]\n>>\nendobj\ntrailer\n<<\n/Root 1 0 R\n>>\n%%EOF"

        # with open('output.pdf', 'wb') as f:
        #     f.write(pdf_content)
        # print("PDF file has been saved as 'output.pdf'")
    except Exception as e:
        print(e)
    
api_request()