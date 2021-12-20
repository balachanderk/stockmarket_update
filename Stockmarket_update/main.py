import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
Stock_api_key = "ZWD3F3K4NF4KR3VS"
news_apikey = "0b59539f69a04b7ba3cba14133634145"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": Stock_api_key
}
stock_response = requests.get(STOCK_ENDPOINT, params=parameters)
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterdays_data = data_list[0]["4. close"]
print(yesterdays_data)

day_before_yesterdays_data = data_list[1]["4. close"]
print(day_before_yesterdays_data)

difference = abs(float(yesterdays_data) - float(day_before_yesterdays_data))
print(difference)

percentage = round((difference / float(yesterdays_data)) * 100)
print(percentage)

if abs(difference) > 1:
    news_params = {
        "qInTitle":COMPANY_NAME,
        "apiKey":news_apikey,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()["articles"]
    three_articles = news_data[:3]
    formatted_articles = [f"Headline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]
    for description in formatted_articles:
        print(description)




