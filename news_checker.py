import requests
import xmltodict


class NewsChecker:

    def __init__(self):
        lenta = "http://lenta.ru/rss/top7"
        yandex = "https://news.yandex.ru/games.rss"
        self.urls = [lenta, yandex]

    def work(self):
        massive_responses = []
        for url in self.urls:
            response = self.__get_response(url)
            if response is not None:
                converted_response = self.__convert_response(response)
                if converted_response is not None:
                    print("Novosti saita {}".format(url))
                    parsed_response = self.__parser(converted_response)
                    massive_responses.append(parsed_response)
        return massive_responses


    def __get_response(self, url):
        try:
            response = requests.get(url)
            return response
        except:
            print("Can't reach link")
            return None

    def __convert_response(self, response):
        try:
            converted_response = xmltodict.parse(response.content)
            return converted_response
        except:
            print("Can't covert from xml to dict")
            return None

    def __parser(self, converted_response):
        news_list = []
        rss = converted_response["rss"]
        channel = rss["channel"]
        description = channel["description"]
        print(description)
        list_into_item = channel.get("item", [])
        for i in list_into_item:
            for _ in i:
                news = {}
                news["title"] = i["title"]
                news["description"] = i["description"]
                news["pubDate"] = i["pubDate"]
                news_list.append(news)
        return news_list





    # def checker(self):
    #     try:
    #         for url in self.urls:
    #             response = requests.get(url)
    #             json_news = response.content
    #             json_news = xmltodict.parse(json_news)
    #             # p = json.loads(json.dumps(json_news))
    #             rss = json_news["rss"]
    #             channel = rss["channel"]
    #             print("Novosti saita {}".format(url))
    #             description = channel["description"]
    #             print(description)
    #             list_into_item = channel.get("item", [])
    #             for i in list_into_item:
    #                 for _ in i:
    #                     if _ == "title":
    #                         print("Zagolovok: {}".format(i["title"]))
    #                     if _ == "description":
    #                         print("Novost:")
    #                         print(i["description"])
    #                     if _ == "pubDate":
    #                         print("Data: {}".format(i["pubDate"]))
    #     except:
    #         print("Something go wrong")











"""
Отправляем запрос на сервер
Получаем ответ
Ковертируем xml в OrderedDict
OrderedDict ковертируем в нормальный диск через json dump/load
Парсим дикт и вынимаем то что нам надо
"""