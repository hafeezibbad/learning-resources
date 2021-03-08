import random
from datetime import datetime
from time import sleep

import pybreaker


def failing_method():
    if random.random() < 0.25:
        print(' / Operation successful')
    else:
        print(' / Failure', end=' ')
        raise Exception('Just some error')


def main(breaker):
    while True:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), end=' ')

        try:
            print(f'Failure Counter: {breaker.fail_counter}', end=' ')
            breaker.call(failing_method)
        except Exception as e:
            print(f'{type(e)}: {e}')

        finally:
            sleep(5)


breaker = pybreaker.CircuitBreaker(fail_max=2, reset_timeout=30)
main(breaker)
