from ciscoconfparse2 import CiscoConfParse

def user_password(parse):
    default_passwords = ["admin", "1234", "password", "cisco"]
    username = parse.re_match_iter_typed(r'^hostname\s+(\S+)', default='')
    password = parse.re_match_iter_typed(r'^password\s+(\S+)', default='')
    # lst =  username.re_list_iter_typed("hostname (\S+)\npassword (\S+)", default='')
    return username, password