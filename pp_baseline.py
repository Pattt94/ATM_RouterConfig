from ciscoconfparse2 import CiscoConfParse

def user_password(parse):
    default_passwords = ["admin", "1234", "password", "cisco"]
    username = parse.find_objects("^hostname HOSTNAME=")[0]
    # lst =  username.re_list_iter_typed("hostname (\S+)\npassword (\S+)", default='')
    return username