import re
from ciscoconfparse import CiscoConfParse
from ciscoconfparse.ccp_util import IPv4Obj
parse = CiscoConfParse('config.conf', factory=True)
obj = parse.find_objects(r'interface\sVlan\S+')
for vlan in obj:
        print vlan.interface_number, vlan.description
