from dnslib import QTYPE, RCODE
from dnslib import PTR, AAAA, TXT

from .record import Record
from .config import Config
from .ipv6utils import *

CONFIG = Config()

class Resolver:
    def __init__(self):
        self.zones = {}

    def resolve(self, request, handler):
        reply = request.reply()

        if request.q.qtype == QTYPE.PTR and (CONFIG.ipv6_subnet in str(request.q.qname) or CONFIG.ipv6_linklocal in str(request.q.qname)):
            self.resolve_ipv6_ptr(request, reply)

        elif request.q.qtype == QTYPE.AAAA and ipv6_is_ptr_match_pattern(str(request.q.qname)):
            self.resolve_ipv6_aaaa(request, reply)

        elif request.q.qtype == QTYPE.TXT and str(request.q.qname) == CONFIG.myip_domain:
            self.resolve_myip_txt(request, reply, handler)

        else:
            reply.header.rcode = getattr(RCODE, 'NXDOMAIN')

        # Reply to the client
        return reply

    def append_reply(self, reply, record):
        try:
            reply.add_answer(record)
        except Exception as err:
            print(err)
            reply.header.rcode = getattr(RCODE, 'NXDOMAIN')

    def resolve_ipv6_ptr (self, request, reply):
        ipv6_digits = ipv6_ip_to_id(str(request.q.qname))
        code = ipv6_id_to_ptr_record(ipv6_digits)

        dns_record = Record(PTR, code).as_rr(request.q.qname)
        self.append_reply(reply, dns_record)

    def resolve_ipv6_aaaa (self, request, reply):
        ipv6_digits = ipv6_ptr_record_to_id(str(request.q.qname))

        ipv6_subnet = ipv6_arpa_to_id(CONFIG.ipv6_subnet)

        pattern = r'local-[0-9a-f]*'
        if (re.match(pattern, ipv6_digits)):
            ipv6_subnet = 'fe80'
            ipv6_digits = ipv6_digits.replace('local-', '')

        ip = ipv6_id_to_ip(ipv6_subnet + ipv6_digits)


        dns_record = Record(AAAA, ip).as_rr(request.q.qname)
        self.append_reply(reply, dns_record)

    def resolve_myip_txt (self, request, reply, handler):
        dns_record = Record(TXT, str(handler.client_address[0])).as_rr(request.q.qname)
        self.append_reply(reply, dns_record)