#!/usr/bin/env python

from time import sleep
from random import randint, choice, random
from glob import glob
from colorama import Fore
from os import path
from itertools import chain

optional_path = '/opt/compiler-screensaver/logs'
logs_path = optional_path if path.isdir(optional_path) else 'logs'
logs = []
for filename in glob(f'{logs_path}/*.log'):
    with open(filename) as f:
        logs.append(f.readlines())
joined_logs = list(chain.from_iterable(logs))
timeouts = {'slow': (2.75, 2.5, 2.0, 1.0, 1.5, 0.5), 'fast': (0.01, 0.04, 0.02, 0.1, 0.2, 0.25, 0.007)}
ultra_fast_mode_lines = 0

if __name__ == '__main__':
    while True:
        try:
            for line in joined_logs:
                if random() < 0.0133 and ultra_fast_mode_lines == 0:
                    ultra_fast_mode_lines = choice((150, 100, 50, 30, 15))
                if ultra_fast_mode_lines == 0:
                    sleep(choice(timeouts['slow'] if randint(1, 30) == 15 else timeouts['fast']))
                else:
                    ultra_fast_mode_lines -= 1
                    sleep(0.01)
                if randint(1, 3) == 2:
                    print(getattr(Fore, choice([*Fore.__dict__.keys()])) + line + Fore.RESET, end='')
                else:
                    print(line, end='')
        except KeyboardInterrupt:
            raise SystemExit

