import discord
from discord.ext import commands, tasks
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import re, os
from io import BytesIO
import datetime
import sys
from crud import insert_img_info, insert_deal_info

load_dotenv()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
url = "https://www.8591.com.tw/mallList-list.html?searchGame=859&searchServer=&buyStatus=1&searchType=&searchKey=&uid="
headers = {
    'User-Agent': 'Mozilla/5.0',  # 自定義 User-Agent 標頭
    'Content-Type': 'application/json'  # 自定義 Content-Type 標頭
}


def get_8591data():
    # 讀取檔案
    with open('data.txt', 'r') as f:
        lines = f.readlines()
        # 檢查行數是否超過30行
        if len(lines) > 30:
            # 保留後30行，刪除剩餘行數
            lines = lines[-30:]
        
    with open('data.txt', 'w') as f:    
        f.writelines(lines)
    # 移除每一行的換行符
    existing_data = [line.strip() for line in lines]

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    commodity_links = soup.select("a.detail_link")
    commodity_links = re.findall(r'href=\"(.+.html)"' , f'{commodity_links}')
    commodity_titles = soup.select("span.ml-item-title")
    commodity_prices = soup.select("div.other b") 

    # <span class="ft-left">08-12 16:30</span>
    # <span class="ft-left iscomplete">交易完成</span>
    # 排除標籤有 '交易完成' 的資料 
    deal_time_data = soup.select("span.ft-left:not(:-soup-contains('交易完成'))")
    data_list = []
    for i in range(len(commodity_titles)):
        commodity_title = commodity_titles[i].get_text()
        commodity_price = commodity_prices[i].get_text()
        deal_time = deal_time_data[i].get_text()
        sql_price = re.sub(r'\D', '', commodity_price)
        full_commodity_link = commodity_links[i].replace('./', 'https://www.8591.com.tw/')
        
        if i >= 20:
            break
        # 跳過標題包含某些字的資料
        # exclusions = ['世界', '莉莉絲', '金幣'] 
        # if any(exclusion in commodity_title for exclusion in exclusions):
        #     continue
        else: 
            if full_commodity_link not in existing_data:
                # 寫入資料
                with open('data.txt', 'a') as f:
                    f.write(full_commodity_link + "\n")
            else:
                continue
            insert_deal_info(commodity_title, int(sql_price), full_commodity_link, f'2023-{deal_time}')
            response = requests.get(full_commodity_link, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")
            try:
                # 如果沒有圖片
                if soup.select_one("div.user-content img") != None:
                    image_url = soup.select_one("div.user-content img")['src']
                    data_list.append(f'{commodity_title}\n價格: {commodity_price}\n網址:{full_commodity_link}\n{image_url}\n==================================================================\n')
                    insert_img_info(commodity_title, int(sql_price), full_commodity_link, image_url)
            except Exception as e:
                print('An error occurred:', str(e))
                continue
    return data_list

@bot.event
async def on_ready():
    global channel_to_post
    print(f'We have logged in as {bot.user}')
    # 從指定的id取得頻道對象並設定給 channel_to_post (數字不能用字串)
    channel_to_post = bot.get_channel(int(os.getenv('DISCORD_CHANNEL')))
    scrape_and_post.start()

@tasks.loop(minutes=5)
async def scrape_and_post():
    message_content = get_8591data()
    data_time = data_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
    str = f'=============================\n{data_time} 近期成交資訊\n=============================\n'
    print(data_time)
    sys.stdout.flush()
    if message_content != []:
        await channel_to_post.send(content=str)
        for i in message_content:
            image_url = re.findall(r'\n(https:.+)\n', i)[0]
            content = '==================================================================\n' + i.replace(image_url+'\n', "")
            # 先下載圖片的二進制數據
            image_response = requests.get(image_url)
            # 創建一個二進制數據的對象
            image_bytes = BytesIO(image_response.content)
            # 建立一個 File 物件
            image_file = discord.File(image_bytes, 'image.jpg')
            await channel_to_post.send(content=content, file=image_file)

bot.run(os.getenv('DISCORD_TOKEN'))