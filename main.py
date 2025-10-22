import os
from ciscoconfparse2 import CiscoConfParse
from infonet_baseline import *

directory_path = "/workspaces/ATM_RouterConfig/INFONET"  # Replace with your directory path

try:
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):  # Check if it's actually a file
            parse = CiscoConfParse(file_path)
            # print(filename)
            # print(user_password(parse))
            print(disable_unused_port(parse))

except Exception as e:
    print(f"An error occurred: {e}")