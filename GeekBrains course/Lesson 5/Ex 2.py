from collections import OrderedDict, defaultdict, deque

N = 1000000
with open('ips.txt', 'r') as f:
    log = deque(f, N)

data = OrderedDict()
spam = defaultdict(int)


for item in log:
    ip = item[:-1]

    if not ip.startswith('192.168'):
        spam[ip]+=1
        data[ip] = 1

data.update(spam)
with open('data.txt', 'w') as f:
    for key, value in data.items():
        f.write(f'{key} - {value}\n')
