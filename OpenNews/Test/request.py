import requests
from bs4 import BeautifulSoup
import json


def fetch_news():
    # URL của trang web tin tức
    url = "https://example-news-site.com"
    # Gửi yêu cầu GET để lấy dữ liệu trang
    response = requests.get(url)

    # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Phân tích cú pháp HTML của trang
        soup = BeautifulSoup(response.text, 'html.parser')

        # Tìm các bài báo trong HTML
        news_list = []
        for article in soup.select('.news-item'):  # .news-item là lớp CSS giả định
            title = article.select_one('.title').text  # Lấy tiêu đề bài báo
            link = article.select_one('.title a')['href']  # Lấy đường dẫn bài báo
            description = article.select_one('.description').text  # Lấy mô tả bài báo
            news_list.append({
                'title': title,
                'link': link,
                'description': description
            })
        return news_list
    else:
        print("Không thể lấy dữ liệu từ trang web")
        return []


def save_to_json(data, filename='news.json'):
    # Lưu dữ liệu vào tệp JSON
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# Thu thập tin tức và lưu vào tệp JSON
news = fetch_news()
if news:
    save_to_json(news)
    print("Tin tức đã được lưu vào tệp news.json")
