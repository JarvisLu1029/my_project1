from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from django.db import connection

from pd.models import Deals_Info
from datetime import datetime, timedelta


@api_view(['GET'])
def get_deal_info(request):
    data = Deals_Info.objects.all()[:5]
    print(data)
    for i in data:
        print(i.title)
    return HttpResponse('OK')

@api_view(['GET'])
def get_deal_info2(request):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM deal_img LIMIT 12")
        deals_info = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        # 將MySQL查詢結果轉換為字典
        deals_info_dict = [dict(zip(columns, deal_info)) for deal_info in deals_info]
    return JsonResponse(deals_info_dict, safe=False)

@api_view(['GET'])
def get_highest_price(request):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM deal_img ORDER BY price desc LIMIT 12")
        deals_info = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        # 將MySQL查詢結果轉換為字典
        deals_info_dict = [dict(zip(columns, deal_info)) for deal_info in deals_info]
    return JsonResponse(deals_info_dict, safe=False)

@api_view(['GET'])
def get_trading_vol(request):
    data_dict = {
        'date': [],
        'vol': []
    }
    for i in range(0, 2):
        date = datetime.now() - timedelta(days=i)
        date_str = date.strftime('%Y-%m-%d')
        data_dict['date'].append(date_str)
        a = date.strftime('%A')
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT SUM(price) FROM deal_info WHERE DATE(create_time) = '{date_str}'")
            today_sum = cursor.fetchone()
            if today_sum:
                a = today_sum[0]
                data_dict['vol'].append(int(a))
    
    print(data_dict)
    return JsonResponse(data_dict, safe=False)

