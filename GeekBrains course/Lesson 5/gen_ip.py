import random as r
with open("ips.txt", 'a') as file:
    for i in range(1000000):
        ip = f'{str(r.randint(1,255))}.{str(r.randint(1,255))}.{str(r.randint(1,255))}.{str(r.randint(1,255))}\n'
        file.write(ip)