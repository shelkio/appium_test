import configparser
import os


def read_config():
    config = configparser.ConfigParser()
    file_path = os.path.join(os.getcwd()) + '/config/config.ini'
    config.read(file_path)
    host = config.get("testServer", "URL")
    return host
