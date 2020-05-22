import pytest,allure
from common.request import runMethod
# 购物车类
class TestShoppingCart(object):
    @allure.story("加入购物车")
    def test_add_cart(self,login):
        host = "http://app.51zheli.com"
        path = "/cart/save"
        headers = {
            "osType":"h5",
            "token":login['token']
        }
        data ={
            "count":1,
            "productId":110348,
            "skuId":19834,
            "storeId":15,
            "userId":login['userId']
        }
        r = runMethod().post(host+path,headers,data)
        print(r)

    @allure.story("用户购物车分组")
    def test_user_group_cart(self,login):
        host = "http://app.51zheli.com"
        path = "/cart/findUserShoppingCart"
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        params = {
            "userId": login['userId']
        }
        r = runMethod().get(host+path,headers,params)
        list = r['data']
        for i in list:
            print(i)
    @allure.story("获取购物车")
    def test_find_cart(self,login):
        host = "http://app.51zheli.com"
        path = "/cart/find"
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        params = {
            "page":1,
            "size":100,
            "status":0,
            "userId": login['userId']
        }
        r = runMethod().get(host+path,headers,params)
        print(r)
    @allure.story("获取购物车数量")
    def test_cart_num(self,login):
        host = "http://app.51zheli.com"
        path = "/cart/findNum"
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        params = {
            "userId": login['userId']
        }
        r = runMethod().get(host + path, headers, params)
        print(r)
    @allure.story("清除失效商品")
    def test_lost_cart(self,login):
        host = "http://app.51zheli.com"
        path = "/cart/deleteInvalid"
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        data = {
            "userId": login['userId']
        }
        r = runMethod().post(host + path, headers, data)
        print(r)
    @allure.story("修改购物车商品")
    def test_update_cart(self,login):
        host = "http://app.51zheli.com"
        path = "/cart/update"
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        data = {
            "count": 2,
            "productId": 110348,
            "skuId": 19834,
            "storeId": 15,
            "userId": login['userId']
        }
        r = runMethod().post(host + path, headers, data)
        print(r)
    @allure.story("删除购物车中的商品")
    @pytest.mark.skip("删除功能跳过")
    def test_delete_cart(self,login):
        host = "http://app.51zheli.com"
        path = "/cart/delete"
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        data = {
            "skuIds": 19834,
            "userId": login['userId']
        }
        r = runMethod().post(host + path, headers, data)
        print(r)