from time import sleep
import logging

from dnslib.server import DNSServer

from .lib.resolver import Resolver
from .lib.config import Config

CONFIG = Config()

class PadawanV6:
    def __init__(self):
        self.logger = logging.getLogger('PadawanV6')
        resolver = Resolver()
        self.servers = [
            DNSServer(resolver, port=CONFIG.server['port'], address=CONFIG.server['address'], tcp=True),
            DNSServer(resolver, port=CONFIG.server['port'], address=CONFIG.server['address'], tcp=False),
        ]

    def start(self):
        for s in self.servers:
            s.start_thread()
        self.logger.info("DNS server start on " + str(CONFIG.server['address']) + ":" + str(CONFIG.server['port']))

    def stop(self):
        for s in self.servers:
            s.stop()
        self.logger.ingo("DNS server stop")
