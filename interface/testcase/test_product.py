import pytest,requests,allure
from common.request import runMethod
# 商品信息
@allure.feature("商品信息")
class TestProduct(object):
    # 搜索获取商品列表
    # rule 0/不传：综合，1：销量，2价格desc，3价格asc
    @allure.story("商品搜索")
    def test_product_seach(self,login):
        host = "http://app.51zheli.com"
        path = "/product/searchPlus"
        parames = {
            "name":"小童车",
            "rule":0,
            "page":	1,
            "size":20,
            "userId":login['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['token']
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

    @allure.story("查询商品信息")
    def test_product_info(self,login):
        host = "http://app.51zheli.com"
        # host = hosts['host']['ip']
        path = "/product/info/{productId}".format(productId= self.test_product_seach(login))
        parames = {
            "userId": login['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        repon = runMethod().get(host + path,headers,parames)
        assert repon['code'] == '0'
        assert repon['msg'] == 'success'

    @allure.story("商品详情")
    def test_product_description(self, login):
        host = "http://app.51zheli.com"
        path = "/product/description/{productId}".format(productId=self.test_product_seach(login))
        parames = {
            "userId": login['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        repon = runMethod().get(host + path, headers, parames)
        assert repon['msg'] == 'success'
        assert repon['code'] == '0'
        print(repon)

    @allure.story("商品二级分类信息")
    def test_product_classify(self, login):
        host = "http://app.51zheli.com"
        path = "/product/findCategory"
        parames = {
            "productCategoryId": 292,
            "page": 1,
            "size": 10,
            "userId": login['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        repon = runMethod().get(host + path, headers, parames)
        assert repon['msg'] == 'success'
        assert repon['code'] == '0'
        return repon['data'][0]['storeId']

    @allure.story("商品一级分类信息")
    def test_product_index(self,login):
        host= "http://app.51zheli.com"
        path = "/product/index"
        parames = {
            "productCategoryId": 2,
            "userId": login['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        reon = runMethod().get(host+path,headers,parames)
        assert reon['code'] == '0'
        assert reon['msg'] == 'success'
    @allure.story("商品推荐（购物车页推荐cartHot，商品搜索推荐searchHot，商品首页推荐indexHot，cpc任务详情推荐CPCTaskDetail，"
                  "订单详情推荐orderDetailRecommend,我的页面 my,我的订单页面 myOrder,顾客订单页面consumer,我的优惠券页面myCardCoupons）")
    def test_product_recommend(self,login):
        host = "http://app.51zheli.com"
        path = "/productRecommend/find"
        parames = {
            "recommendKey":"cartHot"
            # "userId": login['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        repon = runMethod().get(host + path, headers, parames)
        assert repon['msg'] == 'success'
        assert repon['code'] == '0'
    @allure.story("商品服务文案")
    def test_product_serverinfo(self,login):
        host = "http://app.51zheli.com"
        path = "/product/getProductServiceWriterConfig"
        parames = {
            "userId": login['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        repon = runMethod().get(host + path, headers, parames)
        assert repon['msg'] == 'success'
        assert repon['code'] == '0'
    @allure.story("获取推荐的视频商品")
    def  test_product_video(self,login):
        host = "http://app.51zheli.com"
        path = "/videoProd/searchPlus"
        parames = {
            "page":1,
            "size":100
        }
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        repon = runMethod().get(host + path, headers, parames)
        assert repon['msg'] == 'success'
        assert repon['code'] == '0'
        print(repon)
    @allure.story("商品加入纷店")
    def test_product_addfun(self,login):
        host = "http://app.51zheli.com"
        path = "/productCollection/save"
        data = {
            "productIds":"110348,110060",
            "userId":login['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        repon = runMethod().post(host+path,headers,data)
        assert repon['msg'] == 'success'
        assert repon['code'] == '0'
        print(repon)
    @allure.story('商品移出纷店')
    def test_product_deletefun(self,login):
        host="http://app.51zheli.com"
        path="/productCollection/delete"
        data = {
            "productIds": [110348,110060],
            "userId":login['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        repon = runMethod().post(host + path, headers, data)
        assert repon['code'] == '0'
        assert repon['msg'] == 'success'
        print(repon)
    @allure.story("商品种草相关")
    def test_goods_tings(self,login):
        host = "http://app.51zheli.com"
        path = "/goodThings/productAboutGoodThingsRecommend"
        parames = {
            "productId":110355
        }
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        repon = runMethod().get(host + path, headers, parames)
        assert repon['code'] == '0'
        assert repon['msg'] == 'success'
        print(repon)
    @allure.story("商品优惠券聚合页优惠券")
    def test_userCoupon_info(self,login):
        host = "http://app.51zheli.com"
        path = "/userCardCoupons/info"
        parames = {
            "couponId": "2c928ae97106c49b0171077d975d018c",
            "status":0  #0未领 1 领取
        }
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        repon = runMethod().get(host + path, headers, parames)
        assert repon['code'] == '0'
        assert repon['msg'] == 'success'
        print(repon)
    def test_userCoupon_polymerization(self,login):
        host = "http://app.51zheli.com"
        path = "/product/coupons/polymerization"
        parames = {
            "code":"2c928ae97106c49b0171078343d5018d",
            "page": 1,
            "size":100,
            "userId":login['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        repon = runMethod().get(host + path, headers, parames)
        assert repon['code'] == '0'
        assert repon['msg'] == 'success'
        print(repon)
    @allure.story('推荐商品列表')
    def test_product_getByIds(self,login):
        host = "http://app.51zheli.com"
        path = "/productCollection/delete"
        data = {
            "productIds": 292,
            "page":1,
            "size":100,
            "userId": login['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        repon = runMethod().post(host + path, headers, data)
        assert repon['code'] == '0'
        assert repon['msg'] == 'success'
        print(repon)

    @allure.story("提醒通知")
    def test_agentRule(self,login):
        host = "http://app.51zheli.com"
        path = "/agentRule/rePurchaseRemind "
        headers ={
            "osType": "h5",
            "token": login['token']
        }
        data ={
            "orderDetailId":"2c928ae9720824d201720c16a6b60021",
            "productIds":"110112",
            "rePurchaseType":3, #1:相同商品复购提示 2：相同二级品类复购提示 3：相同品类商品提示(一键推荐商品)
            "tagetUserIds":"2c928ae9720824d201720c0e4ff3001a",
            "userId":login['userId']
        }
        r = runMethod().post(host+path,headers,data)
        print(r)

    @allure.story("获取商品优惠券")
    @pytest.mark.skip("程序猿小哥哥刚才摔倒啦！请等他爬起来,商品详情没有优惠券")
    def test_cardCoupon(self, login):
        host = "http://app.51zheli.com"
        path = "/cardCoupons/show/coupon/entry"
        parames = {
            "productId": self.test_product_seach(login),
            "storeId": self.test_product_classify(login),
            "userId": login['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        repon = runMethod().get(host + path, headers, parames)
        assert repon['msg'] == 'success'
        assert repon['code'] == '0'
    @allure.story("商品详情弹框优惠券列表")
    @pytest.mark.xfail("商品详情接口的没有找到优惠券")
    def test_product_couponList(self,login):
        host = "http://app.51zheli.com"
        path = "/cardCoupons/coupon/list"
        params = {
            "productId": self.test_product_seach(login),
            "userId": login['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        r = runMethod().get(host+path,headers,params)
        print(r)
    @allure.story("商品详情 商家解答")
    def test_productFAQ(self,login):
        host = "http://app.51zheli.com"
        path = "/productFAQ/findList"
        params = {
            "productId": self.test_product_seach(login),
            "page":1,
            "size":100,
            "userId": login['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        r = runMethod().get(host + path, headers, params)
        assert r['code'] == '0'
        assert r['msg'] == 'success'
        print(r)
    @allure.story("商品详情-商品推荐")
    def test_store_listRandom(self,login):
        host = "http://app.51zheli.com"
        path = "/store/storeProductListRandom"
        params = {
            "name":" ",
            "status":1,
            "storeId":self.test_product_classify(login),
            "page":1,
            "size":100,
            "userId": login['userId']
        }
        headers = {
            "osType": "h5",
            "token": login['token']
        }
        r = runMethod().get(host + path, headers, params)
        assert r['code'] == '0'
        assert r['msg'] == 'success'
        print(r)
