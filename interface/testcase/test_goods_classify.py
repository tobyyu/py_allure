import pytest,requests,allure
from common.request import runMethod
# 商品信息
@allure.feature("商品信息")
class TestGoods(object):
    # 搜索获取商品列表
    @allure.story("商品搜索")
    def test_seach_goods(self,login):
        host = "http://app.51zheli.com"
        path = "/product/searchPlus"
        parames = {
            "name":"小童车",
            "rule":0,
            "page":	1,
            "size":20,
            "userId":login['data']['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['data']['token']
        }
        repon = runMethod().get(host + path,headers,parames)
        assert repon['msg'] == 'success'
        assert repon['code'] == '0'
        list = repon['data']['searchList']
        # res = [item[key] for item in list for key in item]
        # print(res)
        for item in list:
            for k,v in item.items():
                if k == 'productId':
                    return v
                    # print("/product/info/{productId}".format(productId=v))
    #  商品信息
    @allure.story("商品信息")
    def test_goods_info(self,login):
        host = "http://app.51zheli.com"
        # host = hosts['host']['ip']
        path = "/product/info/{productId}".format(productId= self.test_seach_goods(login))
        parames = {
            "userId": login['data']['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['data']['token']
        }
        repon = runMethod().get(host + path,headers,parames)
        assert repon['code'] == '0'
        assert repon['msg'] == 'success'
    # 商品详情
    @allure.story("商品详情")
    def test_goods_tings(self, login):
        host = "http://app.51zheli.com"
        path = "/goodThings/productAboutGoodThingsRecommend"
        parames = {
            "productId":self.test_seach_goods(login),
            "userId": login['data']['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['data']['token']
        }
        repon = runMethod().get(host + path, headers, parames)
        return repon['data']['goodThingsRecommends']['product']['categoryId']
        # print(repon['data']['goodThingsRecommends']['product']['categoryId'])
    # 商品描述
    @allure.story("商品描述")
    def test_product_description(self,login):
        host = "http://app.51zheli.com"
        path = "/product/description/{productId}".format(productId= self.test_seach_goods(login))
        parames = {
            "userId": login['data']['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['data']['token']
        }
        repon = runMethod().get(host + path, headers, parames)
        assert repon['msg'] == 'success'
        assert repon['code'] == '0'
        # print(repon)
    # 商品分类信息
    @allure.story("商品分类信息")
    def test_goods(self,login):
        host = "http://app.51zheli.com"
        path = "/product/findCategory"
        parames = {
            "productCategoryId":self.test_goods_tings(login),
             "page": 1,
             "size":10,
             "userId":login['data']['userId']
         }
        headers = {
             "osType": "h5",
             "token":login['data']['token']
         }
        repon = runMethod().get(host + path, headers, parames)
        assert repon['msg'] == 'success'
        assert repon['code'] == '0'
        return repon['data'][0]['storeId']
        # print(repon['data'][0]['storeId'])
    # 商品店铺信息
    @allure.story("商品店铺信息")
    def test_store(self,login):
        host = "http://app.51zheli.com"
        path = "/store/findStoreByUserId"
        parames = {
            "storeId":self.test_goods(login),
            "userId": login['data']['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['data']['token']
        }
        repon = runMethod().get(host + path, headers, parames)
        assert repon['msg'] == 'success'
        assert repon['code'] == '0'
        # print(repon)
    # 产品服务说明
    @allure.story("产品服务说明")
    def test_product_serverinfo(self,login):
        host = "http://app.51zheli.com"
        path = "/product/getProductServiceWriterConfig"
        parames = {
            "userId": login['data']['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['data']['token']
        }
        repon = runMethod().get(host + path, headers, parames)
        assert repon['msg'] == 'success'
        assert repon['code'] == '0'
    # 对应商品视频列表
    @allure.story("对应商品视频列表")
    def test_product_videolist(self,login):
        host = "http://app.51zheli.com"
        path = "/videoRec/productRecommendVideoList"
        parames = {
            "productId":self.test_seach_goods(login),
            "page": 1,
            "size": 20,
            "userId": login['data']['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['data']['token']
        }
        repon = runMethod().get(host + path, headers, parames)
        assert repon['msg'] == 'success'
        assert repon['code'] == '0'
        print(repon)
    # 获取商品优惠券
    @allure.story("获取商品优惠券")
    @pytest.mark.skip("程序猿小哥哥刚才摔倒啦！请等他爬起来")
    def test_cardCoupon(self,login):
        host = "http://app.51zheli.com"
        path = "/cardCoupons/show/coupon/entry"
        parames = {
            "productId": self.test_seach_goods(login),
            "storeId":self.test_goods(login),
            "userId": login['data']['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['data']['token']
        }
        repon = runMethod().get(host + path, headers, parames)
        assert repon['msg'] == 'success'
        assert repon['code'] == '0'

