import sys
from loguru import logger

# 移除默认控制台输出，重新配置
logger.remove()
# 控制台打印（带颜色）
logger.add(sys.stdout, level="INFO", format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | <cyan>{message}</cyan>")
# 文件记录（按天切割，保留7天）
logger.add("reports/run_{time:YYYY-MM-DD}.log", rotation="1 day", retention="7 days", level="DEBUG", encoding="utf-8")

def get_logger():
    return logger