import os
import time

print(1)
time.sleep(10)
print('Привет, Dockre Compose')
password = os.environ.get('POSTGRES_PASSWORD')
print(2)
time.sleep(10)
print(f'Ваш пароль {password}')
print(3)
time.sleep(1000)

