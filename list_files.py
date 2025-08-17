
import os

root_dir = "/home/milad/techland/authz"

for dirpath, dirnames, filenames in os.walk(root_dir):
    print(f"Directory: {dirpath}")
    for file in filenames:
        print(f"  - {file}")
