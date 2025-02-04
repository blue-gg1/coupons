import requests
from settings import BaseUrl, BaseText

print(BaseUrl)


for i in BaseText:
    TestCuponUrl = BaseUrl+i
    PossibleRequest = requests.get(TestCuponUrl)
    print(PossibleRequest.status_code)
    print(PossibleRequest.text)