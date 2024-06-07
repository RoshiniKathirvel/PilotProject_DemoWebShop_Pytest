from configparser import ConfigParser
def get_config(category,key):
    config=ConfigParser()
    config.read("E:\\EXPLEO\\Pytest_DemoWebShop_Jayasuriya\\PilotProject_DemoWebShop_Pytest\\DemoWebShop\\PilotProject_DemoWebShop_Pytest\\DemoWebShop\\Configurations\\config.ini")
    return config.get(category,key) 