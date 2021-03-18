import time
from events import event


@event()
def on_start(hi):
    for i in range(11):
        print('Starting up', f'{i*10}%')
        time.sleep(1)


@on_start.listener
def greet_user(hi):
    print('Listening with', hi)


@event()
def on_end():
    time.sleep(10)
    print('Ended')


on_start('greeting', block=True)
on_end(block=True)
