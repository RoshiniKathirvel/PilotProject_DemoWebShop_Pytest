from configparser import ConfigParser
def get_config(category,key):
    config=ConfigParser()
    config.read("E:\\EXPLEO\PilotProject_DemoWebShop_Pytest-1\\DemoWebShop\\Configurations\\config.ini")
    return config.get(category,key) 