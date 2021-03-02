from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from backend import settings
import pyodbc

# Create your views here.
#User
@csrf_exempt
def objectCaller(request, id=0):
    conn = pyodbc.connect(settings.CONN_STR)
    cursor = conn.cursor()  
    cursor.execute("usp_tbl_User 'user'")
    row = cursor.fetchall()
    if request.method == 'GET':
        return JsonResponse(str(row), safe=False)

    