from ciscoconfparse import CiscoConfParse
parse = CiscoConfParse('config.conf')
vlans = parse.find_objects('^interface')
for vlan in vlans:
	print vlan.text
