from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from django.db import connection

from pd.models import DealsInfo
from datetime import datetime, timedelta

import pandas as pd

@api_view(['GET'])
def get_deal_info(request):
    data = DealsInfo.objects.all()[:5]
    print(data)
    for i in data:
        print(i.title)
    return HttpResponse('OK')

@api_view(['GET'])
def get_deal_info2(request):
    with connection.cursor() as cursor:
        cursor.execute(f'''
                    SELECT img.title, img.price, img.img_url, img.deal_url, info.deal_time FROM deal_img AS img
                    JOIN deal_info AS info on img.deal_url = info.deal_url
                    LIMIT 30;
                       ''')
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
        # 找到過去幾天日期的資料
        # date = datetime.now() - timedelta(days=i)
        date = datetime(2023, 7, 13, 1, 29, 30, 105172) - timedelta(days=i)
        date_str = date.strftime('%Y-%m-%d')
        day_of_week = date.strftime('%A')
        day_of_week = switch_day_of_week(day_of_week)
        data_dict['date'].append(f'{date_str} ({day_of_week})')
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT SUM(price) FROM deal_info WHERE DATE(create_time) = '{date_str}'")
            today_sum = cursor.fetchone()
            if today_sum:
                a = today_sum[0]
                data_dict['vol'].append(int(a))
    
    print(data_dict)
    return JsonResponse(data_dict, safe=False)

def switch_day_of_week(day_of_week):
    match day_of_week:
        case 'Monday':
            return '一'
        case 'Tuesday':
            return '二'
        case 'Wednesday':
            return '三'
        case 'Thursday':
            return '四'
        case 'Friday':
            return '五'
        case 'Saturday':
            return '六'
        case 'Sunday':
            return '日'

@api_view(['POST'])
@csrf_exempt
def get_upload_excel(request):
    excel_file = request.FILES['excelFile']
    df = pd.read_excel(excel_file)
    df_ids = df['學號或職員編號']
    for df_id in df_ids:
        print(df_id)
    
    return JsonResponse('OK', safe=False)