

IP = "172.16.254.1"
IP = list(IP.split('.'))
IPv4 = [i for i in IP if (int(i) in range(0,256) and not i.startswith('0'))  ]
if (len(IPv4) == 4):
    print ("IPv4")
else:
    print ("not IPv4")
        

