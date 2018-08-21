import yaml
import os.path
from shutil import copyfile

CONFIG_DIR = "/etc/padawanv6"
CONFIG_FILE = CONFIG_DIR + "/config.yml"

class Config:
    def __init__(self, config_file=CONFIG_FILE):
        if not os.path.exists(CONFIG_FILE):
            copyfile(CONFIG_FILE + ".dist", CONFIG_FILE)

        with open(config_file, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)

        self.DIGIT_TAG = "%DIGITS%"
        self.record_pattern = cfg['record_pattern']
        self.ipv6_subnet = cfg['ipv6_subnet']

        self.server = cfg['server']