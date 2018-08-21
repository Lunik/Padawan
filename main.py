from time import sleep

from dnslib.server import DNSServer

from lib.resolver import Resolver
from lib.config import Config

if __name__ == '__main__':
    CONFIG = Config()
    resolver = Resolver()
    servers = [
        DNSServer(resolver, port=CONFIG.server['port'], address=CONFIG.server['address'], tcp=True),
        DNSServer(resolver, port=CONFIG.server['port'], address=CONFIG.server['address'], tcp=False),
    ]

    for s in servers:
        s.start_thread()

    try:
        while 1:
            sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        for s in servers:
            s.stop()
