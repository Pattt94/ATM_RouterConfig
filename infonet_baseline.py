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
    
    return port.children[0]