import pytest,os,yaml
# 读取测试配置文件
@pytest.fixture(scope='session')
def host(request):
    config_path = os.path.join(request.config.rootdir,
                               "config","test","config.yaml"
                               )
    with open(config_path,encoding='utf-8') as f:
        host_config = yaml.load(f.read(),Loader=yaml.SafeLoader)
    return host_config
# def pytest_sessionfinish():

# if __name__ == "__main__":
#     print(host("fixture"))