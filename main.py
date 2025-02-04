import requests
from settings import BaseUrl, BaseText,FakeHeaders, FailString

print(BaseUrl)



for i in BaseText:
    TestCuponUrl = BaseUrl+i
    PossibleRequest = requests.get(TestCuponUrl, headers=FakeHeaders)
    print(PossibleRequest.status_code)
    print(PossibleRequest.text)
    if PossibleRequest.text == FailString:
        print("lol")
    else:
        print("very good")