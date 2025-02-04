import requests
import logging
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

for i in BaseText:
    TestCuponUrl = BaseUrl+i
    PossibleRequest = requests.get(TestCuponUrl, headers=FakeHeaders)
    print(PossibleRequest.status_code)
    print(PossibleRequest.text)
    if PossibleRequest.text == FailString:
        print("lol")
        logging.info("\r\nDud" + i + PossibleRequest.url)
    else:
        print("very good")
        logging.info("\r\nWe got one!, code is" + i + PossibleRequest.url)


ReadTxtFile("fuzzcoupons.txt")
# UseListGetCupon(TxtFileList)

