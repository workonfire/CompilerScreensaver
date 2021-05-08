#!/usr/bin/env python

from typing import List, Dict, Tuple
from time import sleep
from random import randint, choice
from glob import glob
from colorama import Fore

final_logs: List[List[str]] = [open(filename).readlines() for filename in glob('logs/*.log')]
joined_logs: List[str] = [line for sublist in final_logs for line in sublist]
timeouts: Dict[str, Tuple[float, ...]] = {'slow': (1, 1.5, 2, 0.5),
                                          'fast': (0.01, 0.04, 0.02, 0.1, 0.2, 0.007)}
ultra_fast_mode_lines: int = 0

if __name__ == '__main__':
    while True:
        for line in joined_logs:
            if randint(1, 75) == 25 and ultra_fast_mode_lines == 0:
                ultra_fast_mode_lines = 150
            if ultra_fast_mode_lines == 0:
                sleep(choice(timeouts['slow'] if randint(1, 30) == 15 else timeouts['fast']))
            else:
                ultra_fast_mode_lines -= 1
                sleep(0.01)
            if randint(1, 3) == 2:
                print(getattr(Fore, choice([*Fore.__dict__.keys()])) + line + Fore.RESET, end='')
            else:
                print(line, end='')

