import json
import uuid
import hashlib


class SignParms():
    def sign(datas,appid,secretKey):
        data = json.dumps(datas)  # dumps是将dict转化成str格式，loads是将str转化成dict格式。
        data = json.loads(data)
        msgkv = {}
        for k, v in data.items():
            msgkv[k] = v
        data1 = {
            "appId": appid,
            "nonce": ''.join(str(uuid.uuid4()).split('-'))
        }
        msgkv.update(data1)
        kv = sorted(msgkv.items(), key=lambda item: item[0])  # 现在是按照key首字母进行排序，如果想按照value进行排序只需要将item[0],改为item[1]
        # print u"排序之后的字典 %s" % kv
        kv2 = {}
        mg = ""
        for k, v in kv:
            kv2[k] = v
            mg = mg + k + "=" + v + '&'
        mg = mg[:-1]
        mg1 = mg+"&"+"secretKey="+secretKey
        sign = {
            "sign":hashlib.md5(mg1.encode('utf-8')).hexdigest().upper()
        }
        msgkv.update(sign)
        return msgkv


if __name__ == '__main__':
    msg = {'cgs_token': 'fbf66c79988e43608bccc68088d7d0e4', 'pageIndex': 1}
    SignParms.sign(msg,"101000001192","B2E67270B5685C8BA31C034731E13946")
