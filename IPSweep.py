from pythonping import ping

number_of_IPs = int(input("Number of IP addresses: "))
number_of_pings = int(input("Number of pings: "))
ip_addresses = []

for i in range(number_of_IPs):
    ip_address = input("Enter IP address: ")
    ip_addresses.append(ip_address)
    
    print("")
    
    for x in ip_addresses:
        print(f"Result for: {x}")
        ping(x, verbose=True, count=number_of_pings)
        print("")