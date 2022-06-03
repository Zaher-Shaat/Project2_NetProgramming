# Python 3.9 compatibility
import nmap

# take the range of ports to
# be scanned (input)
begin = input("Enter the beginner port number : ")
# sure the port number is an integer
if begin.isdigit():
    begin = int(begin)
else:
    print("Please enter a valid port number")
    exit()

end = input("Enter the end port number to begin scanning : ")
if end.isdigit():
    end = int(end)
else:
    print("Please enter a valid port number")
    exit()
# assign the target ip to be scanned to a variable
target = input("Enter target ip : ")

# instantiate a PortScanner object
scanner = nmap.PortScanner()

for i in range(begin, end+1):

    # scan the target port
    res = scanner.scan(target, str(i))

    # the result is a dictionary containing
    # several information we only need to
    # check if the port is opened or closed
    # so we will access only that information
    # in the dictionary
    res = res['scan'][target]['tcp'][i]['state']

    print(f'port {i} is {res}.')
