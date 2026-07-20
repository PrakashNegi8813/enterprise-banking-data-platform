import os

ENV = os.getenv("ENV", "dev")

if ENV == "prod":
    from configs.prod_config import *
else:
    from configs.dev_config import *