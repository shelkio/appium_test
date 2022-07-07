import yaml


class YamlUsage:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_yaml_url(self):
        # 读取文件操作
        fo = open(self.file_path, 'r', encoding='utf-8')
        res = yaml.load(fo, Loader=yaml.FullLoader)
        fo.close()
        del res[1:]
        return res

    def get_yaml_data(self):
        # 读取文件操作
        fo = open(self.file_path, 'r', encoding='utf-8')
        res = yaml.load(fo, Loader=yaml.FullLoader)
        fo.close()
        del res[0]
        return res

    def get_yaml_conf(self):
        # 读取文件操作
        fo = open(self.file_path, 'r', encoding='utf-8')
        res = yaml.load(fo, Loader=yaml.FullLoader)
        fo.close()
        return res

if __name__ == '__main__':
    read_yaml = YamlUsage('../datebase/rqe.yaml')
    results = read_yaml.get_yaml_url()
    for one in results:
        print(one)