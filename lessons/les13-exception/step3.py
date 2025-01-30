def func_c():
    return 1 / 0  # Ошибка: деление на ноль

def func_b():
    func_c()

def func_a():
    func_b()

func_a()