import requests
class runMethod(object):
    def get(self,url,headers,parames=None):
        if url:
            r = requests.get(url=url,headers=headers,params=parames)
            ren =r.json()
            return ren
        else:
            try:
                print("接口错误")
            except Exception as e:
                print("错误原因 %s " % e)
    def post(self,url,headers,data):
        if url:
           r = requests.post(url=url,headers=headers,data=data)
           res = r.json()
           return res
        else:
            try:
                print("请求接口错误")
            except Exception as e:
                print("请求错误%s" %e)

