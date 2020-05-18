import yaml,os
class Commlib(object):
    def get_test_data(test_data_path):
        case =[]
        http =[]
        excepted =[]
        with open(test_data_path,encoding='utf-8') as f:
            datas = yaml.load(f.read(),Loader=yaml.SafeLoader)
            tests = datas['tests']
            for td in tests:
                case.append(td.get('case',''))
                http.append(td.get('http',{}))
                excepted.append(td.get('excepted',{}))
        parameters = zip(case,http,excepted)
        return case,parameters

# if __name__ =='__main__':
#     filename = os.path.join(os.path.dirname(os.path.dirname(__file__)),'data/test_in_theaters.yaml')
#     data,parames = Commlib.get_test_data(filename)
#     print(parames.http)



