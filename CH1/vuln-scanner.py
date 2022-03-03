import socket
import sys
import os

def retBanner(ip: str, port: int) -> str:
    banner = "connection Failed"
    try: 
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024).decode('utf-8')
        return banner
    except OSError as err:
        print("OS error: {0}". format(err))
        return "OS error: " + str(err)

def checkVulns(banner: str, file: str) -> bool:
    with open(file, 'r') as f:
        for line in f.readlines():
            vulnBanner = line.strip('\n')
            if vulnBanner in banner.strip('\n'):
                return True
    return False

def main():
    if len(sys.argv) == 2:
        if os.path.exists(sys.argv[1]):
            vulnbannerFile = sys.argv[1]
            if not os.access(vulnbannerFile, os.R_OK):
                print("{0} cannot be read.".format(vulnbannerFile))
                exit(0)

            services = {'ftp': 21, 'ssh': 22, 'smtp': 25, 'http': 80}
            ip = "192.168.228."
            for x in range(1, 255):
                ipx = ip + str(x)
                for protocol in services:
                    print("Trying {0} protocol at {1} address".format(protocol, ipx))
                    banner = retBanner(ipx, services[protocol])
                    if "No route to host" in banner:
                        break

                    if not "OS error" in banner:
                        print("Connection to {0}:{1} successful.".format(ipx, services[protocol]))
                        if checkVulns(banner,vulnbannerFile):
                            print("{0} Server is vulnerable at {1}".format(protocol, ipx))
                        else:
                            print("{0} Server is not vulnerable at {1}".format(protocol, ipx))

        else:
            print("File doesn't exist or file path cannot be determined.")
    else:
        print("VulnScanner.py requires 1 parameter.")

main()