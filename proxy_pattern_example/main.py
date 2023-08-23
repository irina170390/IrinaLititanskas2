from proxy_pattern_example.json_reader import JsonReader
from proxy_pattern_example.json_proxy_reader import JsonProxyReader

json_reader = JsonReader('users.json')
proxy_reader = JsonProxyReader(json_reader)
print(proxy_reader.read())
print(proxy_reader.read())