import requests,yaml,pytest,allure
from utils.commlib import *
# def get_test_data(test_data_path):
#     case =[]
#     http =[]
#     excepted =[]
#     with open(test_data_path) as f:
#         dat = yaml.load(f.read(),Loader=yaml.SafeLoader)
#         test = dat['tests']
#         for td in test:
#             case.append(td.get('case',''))
#             http.append(td.get('http',{}))
#             excepted.append(td.get('excepted',{}))
#     parameters =zip(case,http,excepted)
#     return case,parameters
# cases,paramters =get_test_data("/py_allure/data/test_in_theaters.yaml")
# list_params = list(paramters)
@allure.feature("用户登录功能")
class TestInTheaters(Commlib):
     filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/test_in_theaters.yaml')
     cases, paramters = Commlib.get_test_data(filename)
     @pytest.mark.parametrize('case,http,excepted',list(paramters),ids=cases)
     def test_in_theaters(self,host,case,http,excepted):
         # host="http://app.51zheli.com"
         # 未参数化
         # test_in_theaters(self)
         # r = requests.request(list_params[0][1]['method'],
         #                      url=host+list_params[0][1]['path'],
         #                      params=list_params[0][1]['params'],
         #                      headers=list_params[0][1]['headers'])
         # reponse= r.json()
         # @pytest.mark.parametrize参数化test_in_theaters(self,case,http,excepted)
         r = requests.request(http['method'],
                              url=host['host']['zhili'] + http['path'],
                              params=http['params'],
                              headers=http['headers'])
         reponse = r.json()
         assert reponse['code'] == '0'
         # assert reponse['phone'] == list_params[0][2]
         assert reponse['msg'] == 'success'

if __name__ =="__main__":
    TestInTheaters.test_in_theaters()
