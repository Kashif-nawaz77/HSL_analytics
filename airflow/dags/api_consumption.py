from airflow import DAG 
from airflow.operators.python import PythonOperator
# from airflow.operators. import DummyOperator
from airflow.models.variable import Variable
from datetime import datetime,time
import urllib
from dotenv import load_dotenv

import requests
import json

# Load environment variables from .env file
load_dotenv()

def api_request():
        
    try:
        # url = "https://api.digitransit.fi/realtime/trip-updates/v1/hsl/"
        url = "https://api.digitransit.fi/routing-data/v2/hsl"

        hdr ={
        # Request headers
        'Cache-Control': 'no-cache',
        'digitransit-subscription-key': os.getenv('DIGITRANSIT_API_KEY', ''),
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