import requests
import re


class Mooc():
    def __init__(self, vid):
        self.vid = vid
        self.headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'content-length': '280',
            'content-type': 'text/plain',
            'cookie': 'NTESSTUDYSI=2fe9959cb6f74f9797bec36a8ae4eee6; EDUWEBDEVICE=7076478e68f049f48b5e08fd8794917e; hb_MA-A976-948FFA05E931_source=cn.bing.com; WM_NI=OVpXku1ryjOsp2xIxJkk4BJSX3JSNWg%2F8LKueemRomAm8qNNxFHUUBwCZf42AXlpCnNxS59ZeGras7KmU7pvtCefaJ0b2olBBY5booO2yI5hepOtscVS7HDv4kcxOY7IVEU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee96d24eae988f8ecd538c8a8bb6c55a829b8aafb554a38dfa8af64fab978aaed02af0fea7c3b92a8d8ac0b9ea7ff3aeb78bce79b4eeb8aafb42a9b5fca3c9599ced86b4cd5da5f1f8adca7fa7bba3b3ee6783b3f892cd46bc9a88b6d84ab59d9687b73a8388a491c2668ea89dd6bc52a799be82f23d89b39bd8f37eb89dab87e442f4befe90ef4a8287fb83ee658deeb7aab864a7b08195f269968df9a9c77ef8b5ad99ce53f5979aa6d837e2a3; WM_TID=BIL2DGiPm%2BtBAEEERRJqTOD%2Bz1ByNVdc; __yadk_uid=VudN58iDiJ7Y1mE1v9WacULPlQSDsWN7; videoVolume=0.8; hasVolume=true; NTES_YD_SESS=fK605XEFVM.81_V8C2kxat9qCDlg4QiECkxQHKErHawBeypJekSXAhVxopWbgxq3F6YOk3TH0SBF6KbATw6DOsdZzGBBnHrCjVHaPx_UR.HdvCnRFCBmxPLlHEbJlqCthlBffOEEnmrShfQFk47NRccKMQgWkoQmOf3yXU9HwZIURxPq67Pe4EbvJDLckrWYdhntSy2L4wnApEIg3l3hEgL3ahR00nhhkHCJVF53JBRTR; NTES_YD_PASSPORT=QI17ht6eV1S.2.rBKggzR8cNJw6inz4nAYqyz6EHCwWqa7s5atXR4yJWrseLZWUpBCEmtpFA.XPJiQNELsC7yjmfm_cpYx.ri0Y.d6i05r7wN47qbbOLAn74Ewn8ExokYelyixXJYTF1s58n1pZ0omzzkNGvJYXHdcJENoxE7z8Y7IOqVaQlsz50YUtyNEVuf4DQPsPqF7CRKi0EhYu8jhkZh; S_INFO=1592622893|0|3&80##|13275697209; P_INFO=13275697209|1592622893|1|imooc|00&99|null&null&null#JP&null#10#0#0|&0||13275697209; STUDY_INFO="yd.0d290de500d947f7a@163.com|8|1396690110|1592622894032"; STUDY_SESS="4CxSDfZ81kC83lw/Iekrx7he+N/cLJL9z3y7bMG2eHEf+wacxpOJu+K8OBAOYIqr+/1lXOZ2nbv09RX27NDkj2X1oar2iaN/CIvkQZZK1HYJN3pbXLSP8VtNreuSlOl2mjL/Dp8hVQpD7rOD3g6SmGZpEu7MZaQEUXFffeIn4DMLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="X8QvimUV2gSGSfE28UMSm+Ec3+HyiU39vBhd5BC8m4SKSmPSX1zZ3kLlxCWzG+gdfxmPSxQ1lmWEyimsELn1Y0AgJ4PNVhVl4ww5hnfMqJheWq4cbwDk5uxLC4YVJdHj8Y8zqxYR3mBd5Np3h7AxbfSdLHpGdsLVXeWJKqkMSo6k3CcZduygNODrsxtc0KgjKF0A1ESPwxXdgkD2nrgUim8Z9jb7zY7IttTCFxex3bDZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1396690110#|#1563697267871; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1592622340,1592635317; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1592640398',
            'origin': 'https://www.icourse163.org',
            'referer': 'https://www.icourse163.org/learn/BIT-1001873001?tid=1001966001',
            'sec-ch-ua': r'''"\Not"A;Brand";v="99", "Chromium";v="84", "Google Chrome";v="84"''',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36',
        }

    # 获取有关参数
    def get_lastid_content_id(self):
        data = {
            'callCount':'1',
            'scriptSessionId':'${scriptSessionId}190',
            'httpSessionId':'be9c85eaa33d48b39cde8eb0d1a2c59a',
            'c0-scriptName':'CourseBean',
            'c0-methodName':'getLastLearnedMocTermDto',
            'c0-id':'0',
            'c0-param0':f'number:{self.vid}',
            'batchId':'1592643816585'
        }
        
        url = 'https://www.icourse163.org/dwr/call/plaincall/CourseBean.getMocTermDto.dwr'
        response = requests.post(url, headers=self.headers, data=data)
        lines = response.text.split('\n')
        lastLearnUnitId = re.search(",lastLearnUnitId:(\d+)", response.text).group(1)

        for line in lines:
            contentId_ = re.findall("contentId=(\d+);", line, re.S)
            id_ = re.findall(";.*?id=(\d+);", line, re.S)
            if contentId_ and id_:
                if id_[0] == lastLearnUnitId:
                    contentId = contentId_[0]
                    break
        
        if contentId:
            self.get_info(lastLearnUnitId, contentId)

        else:
            return "错误"
    

    def get_info(self, lastLearnUnitId, contentId):
        url = 'https://www.icourse163.org/dwr/call/plaincall/CourseBean.getLessonUnitLearnVo.dwr'
        data = {
            'callCount':'1',
            'scriptSessionId':'${scriptSessionId}190',
            'httpSessionId':'be9c85eaa33d48b39cde8eb0d1a2c59a',
            'c0-scriptName':'CourseBean',
            'c0-methodName':'getLessonUnitLearnVo',
            'c0-id':'0',
            'c0-param0':f'number:{contentId}',
            'c0-param1':'number:1',
            'c0-param2':'number:0',
            'c0-param3':f'number:{lastLearnUnitId}',
            'batchId':'1592640397778'
        }

        response = requests.post(url, data=data)
        # mp4HdUrl = re.search('s\d+.mp4HdUrl="(.*?)"', response.text).group(1)
        # mp4SdUrl = re.search('s\d+.mp4SdUrl="(.*?)"', response.text).group(1)

        # 这个是最大尺寸
        mp4ShdUrl = re.search('s\d+.mp4ShdUrl="(.*?)"', response.text).group(1)

        # self.save(mp4ShdUrl)


    def save(self, url, title):
        pass

        