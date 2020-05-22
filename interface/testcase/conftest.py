import pytest,requests,os,yaml
from common.request import runMethod
# 获取IP地址
@pytest.fixture(scope='session')
def hosts():
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'config','config.yaml')
    with open(config_path,encoding='utf-8') as f:
        host_config =yaml.load(f.read(),Loader=yaml.SafeLoader)
    return host_config
@pytest.fixture(scope='session')
def login():
    host = "http://app.51zheli.com"
    path = "/user/login"
    params= {
        "phone":17700000002,
        "code":1254
    }
    headers = {"osType":"h5"}
    r = requests.request("POST",url=host+path,params=params,headers=headers)
    repon = r.json()
    return repon['data']
    # print(repon['data']['token'])
