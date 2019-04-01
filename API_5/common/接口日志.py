import logging
from API_5.common.read_config import ReadConfig
from API_5.common import project_path
class Mylog:
    def __init__(self):
        #日志收集器的名字
        self.logger_name =ReadConfig(project_path.conf_path).get_str("My_log","logger_name")
        #日志收集器的等级
        self.logger_level =ReadConfig(project_path.conf_path).get_data("My_log","logger_level")
        #输出到输出台日志等级
        self.logger_console = ReadConfig(project_path.conf_path).get_data("My_log", "console")
        #输出到输出泰德日志等级
        self.logger_formatters = ReadConfig(project_path.conf_path).get_data("My_log", "formatter")
        #创建的日志文件名
        self.file_name = ReadConfig(project_path.conf_path).get_data("My_log", "file_name")
        #创建的日志文件等级
        self.file_level = ReadConfig(project_path.conf_path).get_data("My_log", "file_level")
    def mylog(self,lavel,msg):
        logger = logging.getLogger(self.logger_name)  # 定义日志收集器的名字
        logger.setLevel(self.logger_level)  # 设置级别
        formatter = logging.Formatter(self.logger_formatters)

        ch = logging.StreamHandler()  #输出到console的log等级开关
        ch.setLevel(self.logger_console)  # 设置级别
        ch.setFormatter(formatter)  # 设置格式

        fh = logging.FileHandler(self.file_name, encoding="utf-8")  #写入的日志文件
        fh.setLevel("INFO")  # 设置级别
        fh.setFormatter(formatter)  # 设置格式

        logger.addHandler(ch)
        logger.addHandler(fh)
        if lavel == "DEBUG":
            logger.debug(msg)
        elif lavel == "INFO":
            logger.info(msg)
        elif lavel == "WARNING":
            logger.warning(msg)
        elif lavel == "ERROR":
            logger.error(msg)
        else:
            logger.critical(msg)

        logger.removeHandler(fh)
        logger.removeHandler(ch) #移除日志

    def debuf(self,msg):
        self.mylog("DEBUG",msg)
    def info(self,msg):
        self.mylog("INFO",msg)
    def warning(self, msg):
        self.mylog("WARNING", msg)
    def error(self,msg):
        self.mylog("ERROR",msg)
    def critcal(self,msg):
        self.mylog("CRITCAL",msg)

if __name__ == '__main__':
    logger = Mylog()
    logger.mylog("ERROR","!!!")