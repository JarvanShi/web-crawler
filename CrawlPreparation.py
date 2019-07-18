import builtwith  # python-builtwith
import whois  # python-whois

uri = "http://example.webscraping.com"
siteTech = builtwith.builtwith(uri)
belongs = whois.whois(uri)
print(siteTech)
print(belongs)
