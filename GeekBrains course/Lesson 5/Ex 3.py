from collections import ChainMap
import argparse
defa = {'ip': 'localhost', 'port': 7777}

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip')
parser.add_argument('-p', '--port')

args = parser.parse_args()
new_d = {key: value for key, value in vars(args).items() if value}

settings = ChainMap(new_d, defa)
print(settings['ip'])
print(settings['port'])
