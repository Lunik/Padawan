import yaml
import os.path
from shutil import copyfile

CONFIG_DIR = "/etc/padawan"
CONFIG_FILE = CONFIG_DIR + "/config.yml"

class Config:
    def __init__(self, config_file=CONFIG_FILE):
        if not os.path.exists(CONFIG_FILE):
            copyfile(CONFIG_FILE + ".dist", CONFIG_FILE)

        with open(config_file, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)

        self.DIGIT_TAG = "%DIGITS%"
        self.record_pattern = cfg['record_pattern']
        patterns = self.record_pattern.split(self.DIGIT_TAG)
        self.pattern = {
        	'prefix': patterns[0],
        	'sufix': patterns[1]
        }

        self.ipv6_subnet = cfg['ipv6_subnet']
        self.ipv6_linklocal = "0.8.e.f.ip6.arpa."

        self.server = cfg['server']

        self.myip_domain = cfg['myip_domain']
