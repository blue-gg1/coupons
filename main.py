import requests
from settings import BaseUrl, BaseText,FakeHeaders, FailString


def ReadTxtFile(FileName):
    global TxtFileList
    TxtFile = open(FileName, "r")
    TxtFileData = TxtFile.read()
    TxtFileList = TxtFileData.split("\n")
    TxtFile.close()



# def UseListGetCupon(CouponList):
#     for i in CouponList:
#         TestCuponUrl = BaseUrl+i
#         PossibleRequest = requests.get(TestCuponUrl, headers=FakeHeaders)
#         if PossibleRequest.text == FailString:
#             print("lol")
#         else:
#             print("very good")
#     pass

# for i in BaseText:
#     TestCuponUrl = BaseUrl+i
#     PossibleRequest = requests.get(TestCuponUrl, headers=FakeHeaders)
#     print(PossibleRequest.status_code)
#     print(PossibleRequest.text)
#     if PossibleRequest.text == FailString:
#         print("lol")
#     else:
#         print("very good")


ReadTxtFile("fuzzcoupons.txt")
UseListGetCupon(TxtFileList)

