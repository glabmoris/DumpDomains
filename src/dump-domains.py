import sys
import requests
import json

if len(sys.argv) != 2:
	sys.stderr.write("Usage: dump-domains.py domain-name\n")
	sys.exit(1)


domainName = sys.argv[1]

sys.stderr.write("Fetching subdomains for {}\n".format(domainName))

r = requests.get("https://crt.sh/?q={}&output=json".format(domainName))

if r.status_code == 200:
	jsonData = json.loads(r.text)

	subDomains = {}

	for cert in jsonData:
		subs = cert['name_value'].split("\\n")
		for s in subs:
			subDomains[s]=1

	for subDomain in subDomains.keys():
		print(subDomain)
else:
	sys.stderr.write("Error while fetching sub-domains")
