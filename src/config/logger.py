import sys
from loguru import logger

logger.add(sys.stdout, format="{time} {level} {message}", filter="my_module", level="INFO", serialize=True)

