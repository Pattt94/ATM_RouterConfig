from ciscoconfparse2 import CiscoConfParse
import re

def user_password(parse):
    username = parse.re_match_iter_typed(r'^hostname\s+(\S+)', default='')
    password = parse.re_match_iter_typed(r'^password\s+(\S+)', default='')
    if "SCB" in username and re.search(r'\*+', password):
        return username, password
    else:
        return "Something went wrong"
    
def collect_log(parse):
    radius = parse.find_objects(r"service radius")[0]
    radius_ip = radius.re_match_iter_typed(r'((\d+\.){3}\d+)', default='')
    if radius_ip == "203.33.240.49":
        return radius_ip
    else:
        return "Something went wrong"
    
def disable_unused_port(parse):
    port = parse.find_objects(r"service port")[0]
    port_status = port.re_list_iter_typed(r"port\S* ([on|off]+)")
    count_on = port_status.count("on")
    count_off = port_status.count("off")
    port_on = [p.text for p in port.children if re.search(r"(\S+ port\S*) on", p.text)]
    port_off = [p.text for p in port.children if re.search(r"(\S+ port\S*) off", p.text)]

    if len(port_status) > 1 and count_on == 1 and count_off > 1:
        return port_on[0]
    else:
        return port_on, port_off
    
def access_control(parse):
    acl_list = parse.find_objects(r"^access-list mac")
    mac_address_format = "(([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}))|(([0-9A-Fa-f]{4}[.]){2}[0-9A-Fa-f]{4})"
    mac_address = [i.re_list_iter_typed(mac_address_format)[0] for i in acl_list if i.re_list_iter_typed(mac_address_format) != []]
    mac_input = [i.re_list_iter_typed(r"input (\S+.+)")[0] for i in acl_list if i.re_list_iter_typed(r"input (\S+.+)") != []]
    mac_forward = [i.re_list_iter_typed(r"forward (\S+.+)")[0] for i in acl_list if i.re_list_iter_typed(r"forward (\S+.+)") != []]

    if all(x == mac_address[0] for x in mac_address) and "deny any" in mac_input and "deny any" in mac_forward:
        return f"{mac_address[0]} is permitted."
    else:
        return mac_address, f"{mac_address[0]} is NOT permitted."

def session_timeout(parse):
    retry = parse.find_child_objects(['line vty', r'fail-timeout 3'])
    if retry != []:
        return retry[0]
    else:
        return "No session-timeout"
    
def snmp_shutdown(parse):
    snmp = parse.find_child_objects(["service snmp", "shutdown"])
    if snmp != []:
        return snmp[0]
    else:
        return "SNMP is not shutdown"
    
def syslog_shutdown(parse):
    syslog = parse.find_child_objects(["service syslog", "shutdown"])
    if syslog != []:
        return syslog[0]
    else:
        return "syslog is not shutdown"
    
def dhcp_shutdown(parse):
    dhcp = parse.find_child_objects(["service dhcp", "shutdown"])
    if dhcp != []:
        return dhcp[0]
    else:
        return "DHCP is not shutdown"
    
def sync_time(parse):
    ntp = parse.find_child_objects(["service ntp", "time zone bangkok"])
    if ntp != []:
        return ntp[0]
    else:
        return "Time is not BKK timezone"