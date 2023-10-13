import random
sp_sym = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*']
rus_letters = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
M = 9
def generate(a):
    N = len(a)
    Q = N % 5

    password = ''
    for i in range(1, 2+Q):
        a = random.choice(sp_sym)
        password += a
    for i in range(3+Q, M+1):
        a = random.choice(rus_letters)
        password += a
    password += str(random.randint(0, 9)) 

    return password