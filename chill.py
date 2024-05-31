from colorama import Fore 
import time 
import random
import sys
colors=[Fore.GREEN,Fore.BLACK,Fore.CYAN]
def create_pattern():
  while True:
        binary_chars=['1','0']
        random_column_number=random.randrange(1,50,1)
        random_row_number=random.randrange(1,50,1)
        for n in range(random_column_number):
            sys.stdout.flush()
            sys.stdout.write(f'{random.choice(colors)}{"  ".join(random.choice(binary_chars)+random.choice(binary_chars)*random_row_number)}\n')
            time.sleep(0.001)
create_pattern()