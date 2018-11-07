import re

from .config import Config

CONFIG = Config()

# Get only the last digits of the device
# 2001:1234:5678:9101:1121:3141:5161:7181 --> 1121314151617181
def ipv6_ip_to_id(ip):
  pattern = r'([0-9a-f].)*0.8.e.f.ip6.arpa.'
  print(ip)
  if (re.match(pattern, ip)):
    return "local-" + str(ip).replace(CONFIG.ipv6_linklocal, '').replace('.', '')[::-1]
  else:
    return str(ip).replace(CONFIG.ipv6_subnet, '').replace('.', '')[::-1]

# Apply the pattern
# pattern = %DIGITS%.ipv6.exemple.com
 # 1121314151617181 --> 1121314151617181.ipv6.exemple.com
def ipv6_id_to_ptr_record(ip_id):
	return CONFIG.record_pattern.replace(CONFIG.DIGIT_TAG, ip_id)

def ipv6_ptr_record_to_id(record):
	return str(record).replace(CONFIG.pattern['prefix'], '').replace(CONFIG.pattern['sufix'], '')

def ipv6_is_ptr_match_pattern(record):
  pattern = r'' + CONFIG.pattern['prefix'] + '(local-)?[0-9a-f]*' + CONFIG.pattern['sufix']
  return bool(re.match(pattern, record))

def ipv6_arpa_to_id(arpa_ip):
	return ''.join(arpa_ip.replace('.ip6.arpa.', '').split('.'))[::-1]

def ipv6_id_to_ip(ip_id):
	return re.sub(r'([0-9a-f]{4})', r'\1:', ip_id)[:-1]
