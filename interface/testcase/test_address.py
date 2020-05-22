import pytest,allure,requests
from common.request import runMethod
@allure.feature("地址信息")
class TestAddress():
    @allure.story("添加地址")
    def test_address_add(self,login):
        host = "http://app.51zheli.com"
        path = "/address/save"
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        data = {
            "area":"宝安区",
            "city":"深圳市",
            "defaul":0,
            "detail":"详细地址",
            "name":"张旭",
            "phone":14734567567,
            "province":"广东省",
            "userId": login['userId']
        }
        r = runMethod().post(host+path, headers, data)
        print(r)
    @allure.story("地址列表")
    def test_address_list(self,login):
        host = "http://app.51zheli.com"
        path = "/address/find"
        url = host+path
        headers ={
            "osType":"h5",
            "token":login['token']
        }
        params = {
            "page": 1,
            "size": 10,
            "keyWord": " ",
            "userId": login['userId']
        }
        r = runMethod().get(url,headers,params)
        assert r['code'] == '0'
        assert r['msg'] == 'success'
        return r['data'][-1]['addressId']
        # print(r['data'][-1]['addressId'])
    @allure.story("获取EDI地址列表")
    def test_address_EDI(self,login):
        host = "http://app.51zheli.com"
        path = "/address/find2"
        url = host + path
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        params = {
            "page": 1,
            "size": 10,
            "userId": login['userId']
        }
        r = runMethod().get(url, headers, params)
        print(r)
    @allure.story("删除地址")
    @pytest.mark.skip("删除功能跳过")
    def test_address_add(self,login):
        host = "http://app.51zheli.com"
        path = "/address/delete"
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        data = {
            "addressId":self.test_address_list(login),
            "userId": login['userId']
        }
        r = runMethod().post(host+path, headers, data)
        assert r['code'] == '0'
        assert r['msg'] == 'success'
    @allure.story("搜索地址")
    def test_address_seach(self,login):
        host = "http://app.51zheli.com"
        path = "/address/find"
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        params = {
            "page":1,
            "size":100,
            "keyWord":"",
            "userId": login['userId']
        }
        r = runMethod().get(host + path, headers, params)
        assert r['code'] == '0'
        assert r['msg'] == 'success'
        print(r)