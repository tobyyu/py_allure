import pytest,allure,requests
from common.request import runMethod
from testcase.test_address import TestAddress
@allure.feature("订单管理")
class TestOrder(object):
    @allure.story("拆分订单拆单后查询可用优惠券集合")
    def test_order_split_cardcoupon(self,login):
        host="http://app.51zheli.com"
        path ="/order/queryCardCoupons"
        headers ={
            "osType": "h5",
            "token": login['token']
        }
        params={
            "skuIds":[19834,19478],
            "count":0,
            "onekey":1, #0购物车 1 下单拆单
            "userId":login['userId']
        }
        r = runMethod().get(host+path,headers,params)
        print(r)
    @allure.story("拆分订单V2")
    def test_order_splitV2(self,login):
        host = "http://app.51zheli.com"
        path = "/order/separateV2"
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        data = {
            "count": 0,
            "onekey": 1,  # 0购物车 1 下单拆单
            "skuIds": 19834,
            "storeIds":15,
            "userId": login['userId']
        }
        r = runMethod().post(host + path, headers, data)
        print(r)
    #邮费计算未完善
    @allure.story("计算邮费")
    def test_order_postage(self,login):
        host = "http://app.51zheli.com"
        path = "/order/postageCalculate"
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        data = {
            "orderJson":"",
            "userId": login['userId']
        }
        r = runMethod().post(host + path, headers, data)
        print(r)
    @allure.story("校验地址是否符合配送")
    def test_order_isaddress(self,login):
        host = "http://app.51zheli.com"
        path = "/order/validateAddress"
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        data = {
            "productIdArray":"[[110138]]",
            "province": "深圳市",
            "userId": login['userId']
        }
        r = runMethod().post(host + path, headers, data)
        assert r['code'] == '0'
        assert r['msg'] == 'success'
        print(r)
    @allure.story("获取用户下订单序列号")
    def test_order_serial(self,login):
        host = "http://app.51zheli.com"
        path="/order/serial"
        headers= {
            "osType": "h5",
            "token": login['token']
        }
        params={
            "userId":login['userId']
        }
        r = runMethod().get(host+path,headers,params)
        assert r['code'] == '0'
        assert r['msg'] =='success'
        return r['data']
    @allure.story("创建订单--购物车")
    def test_order_add(self,login):
        host = "http://app.51zheli.com"
        path = "/order/create"
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        data = {
            "addressId":TestAddress().test_address_list(login),
            "cardCouponsId":" ",
            "overseasPurchaseInfoId":" ",
            "serial":self.test_order_serial(login),
            "skuIds":[19446,19445,19834],
            "storeIds":"3,15",
            # "taxNumber":" ",
            # "title":" ",
            "userId":login['userId'],
            # "userMessage":"我的留言"
        }
        r = runMethod().post(host + path, headers, data)
        print(r)
    @allure.story("创建订单----商品详情立即购买一键下单")
    def test_order_createOnekey(self,login):
        host = "http://app.51zheli.com"
        path = "/order/create/oneKey"
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        data = {
            "addressId": TestAddress().test_address_list(login),
            "serial": self.test_order_serial(login),
            "skuId": 19834,
            "storeId": 15,
            "videoId":" ",
            "liveRoomId":" ",
            "inviteCode":" ",
            "count":2,
            "overseasPurchaseInfoId":" ",
            "userId": login['userId']
        }
        r = runMethod().post(host+path,headers,data)
        assert r['code'] == '0'
        assert r['msg'] == 'success'
        return r['data']['orderId']
        # print(r['data']['orderId'])
    @allure.story("全部订单列表")
    def test_order_list(self,login):
        host = "http://app.51zheli.com"
        path = "/order/list"
        headers={
            "osType": "h5",
            "token": login['token']
        }
        data={
            "key":"all",
            "page":1,
            "size":100,
            "userId": login['userId']
        }
        r = runMethod().post(host + path, headers, data)
        assert r['code'] =='0'
        assert r['msg'] =='success'
        return r['data']
    @allure.story("待评价订单列表")
    def test_order_listWaitevaluate(self,login):
        host = "http://app.51zheli.com"
        path = "/order/list"
        path = "/order/list"
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        data = {
            "key": "waitevaluate",
            "page": 1,
            "size": 100,
            "userId": login['userId']
        }
        r = runMethod().post(host + path, headers, data)
        # print()
        assert r['code']== '0'
        assert r['msg'] == 'success'
        list = r['data'][0]['orderDetails']
        for i in list:
            for key, value in i.items():
                if key =='orderDetailId':
                       return value
                else:
                    print("没有待评价的商品")
    @allure.story("订单完成商品评论")
    def test_order_comment(self,login):
        host = "http://app.51zheli.com"
        path = "/orderComment/save"
        headers ={
            "osType": "h5",
            "token": login['token']
        }
        data={
            "comment":"这个是评论，我就看看",
            "imagesStr":"https://img.51zheli.com/product/admin_undefined_1588833813108.jpg",
            "orderDetailId":self.test_order_listWaitevaluate(login),
            "score":5,
            "userId":login['userId']
        }
        r = runMethod().post(host+path,headers,data)
        # assert r['code'] == '0'
        # assert r['msg'] == 'success'
        print(r)
    @allure.story("获取评论列表")
    def test_ordercomment_findlist(self,login):
        host = "http://app.51zheli.com"
        path = "/orderComment/findList"
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        parames ={
            "productId":11035,
            "imageSign":0,
            "page":1,
            "size":100
        }
        repon = runMethod().get(host + path, headers, parames)
        assert repon['code'] == '0'
        assert repon['msg'] == 'success'
        print(repon)
    @allure.story("查询订单详情")
    def test_order_info(self,login):
        host = "http://app.51zheli.com"
        path = "/order/info/{orderId}".format(orderId=self.test_order_createOnekey(login))
        headers={
            "osType": "h5",
            "token": login['token']
        }
        data = {
            "orderId":self.test_order_createOnekey(login),
            "userId":login['userId']
        }
        r = runMethod().post(host+path,headers,data)
        print(r)
    @allure.story("查询顾客订单列表")
    def test_order_myConsumerOrderList(self,login):
        host = "http://app.51zheli.com"
        path = "/order/myConsumerOrderList"
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        data = {
            "key":"all", #all所有订单，waitpay待支付， waitsend待发后， waitreceive待收货 waitevaluate待评价  invoice可开发票列表
            "keyWord":"",
            "startTime":"",
            "page":1,
            "size":100,
            "userId": login['userId']
        }
        r = runMethod().post(host + path, headers, data)
        print(r)
    def orderlist(self):
