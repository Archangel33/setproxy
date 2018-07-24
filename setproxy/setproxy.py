#!/usr/bin/env/python

import sys, getpass, os
from ProxyString import ProxyString

class setproxy:
    def main(self, args):
        proxy = ProxyString(hostname="webproxy", port="9090")
        username = self.getUsername()
        proxy.setUsername(username)
        password = self.getPassword()
        proxy.setPassword(password)
        print( proxy )

        self.setProxy(proxy.getProxyString())

    def getUsername(self):
        return getpass.getuser()
    
    def getPassword(self):
        return getpass.getpass()
    
    def setProxy(self, proxyString):
        os.environ["https_proxy"] = proxyString
        os.environ["http_proxy"] = proxyString
        os.environ["ftp_proxy"] = proxyString
        print(os.environ.get("https_proxy","ERROR"))



#  setproxy ()
# {
#     echo -n "Proxy-Server:";
#     read -e proxyserver;
#     echo -n "Proxy-Port:";
#     read -e proxyport;
#     echo -n "Proxy username:";
#     read -e proxyusername;
#     if [ -z "$proxyusername" ]; then
#         proxy=http://$proxyserver:$proxyport/;
#     else
#         printf "Password: ";
#         read_secret proxypassword;
#         proxy=http://$proxyusername:$proxypassword@$proxyserver:$proxyport/;
#     fi;
#     export http_proxy=$proxy;
#     export https_proxy=$proxy;
#     export ftp_proxy=$proxy;
#     echo -e Set the Proxy environment variables for the current session. Logout to reset them to null again..
# }       


if __name__ == '__main__':
    #options = Options(sys.argv).get_options()
    setproxy = setproxy()
    setproxy.main(sys.argv)