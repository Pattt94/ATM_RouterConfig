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
    port_status = port.re_list_iter_typed("port\S* ([on|off]+)")
    count_on = port_status.count("on")
    count_off = port_status.count("off")
    port_on = [p.text for p in port.children if re.search("(\S+ port\S*) on", p.text)]
    port_off = [p.text for p in port.children if re.search("(\S+ port\S*) off", p.text)]
    if len(port_status) > 1 and count_on == 1 and count_off > 1:
        return port_on ,port_off
    else:
        return port_status, count_on ,count_off