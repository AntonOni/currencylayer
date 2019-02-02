import requests


class UsdCheker():

    def __init__(self):
        self.url = "http://www.apilayer.net/api/live?access_key=cee025a5d2ae5127fc4c7924cc8afc5a"
        self.json = {"post_request": 1001001}

    def get_cheker(self):
        response = requests.get(self.url)
        print("Headers",response.headers)
        print("Status_code", response.status_code)
        print("URL", response.url)
        print("History", response.history)
        print("Encoding", response.encoding)
        print("Reason", response.reason)
        print("Cookies", response.cookies)
        print("Elapsed", response.elapsed)
        print("Request", response.request)

    def post_cheker(self):
        response = requests.post(self.url, json=self.json)
        print(response.headers)

    def delete_cheker(self):
        response = requests.delete(self.url)
        print(response.status_code)

    def head_cheker(self):
        response = requests.head(self.url)
        print(response.url)

    def put_cheker(self):
        response = requests.put(self.url, json=self.json)
        print(response.text)



a = UsdCheker()
a.get_cheker()