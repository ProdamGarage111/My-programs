number = "12".split()
def permute_number(number):
    # Преобразуем число в строку, чтобы можно было итерироваться по его цифрам
    num_str = str(number)
    
    # Вспомогательная функция для рекурсивного нахождения всех перестановок
    def permute(s):
        if len(s) == 1:
            return [s]
        
        permutations = []
        for i in range(len(s)):
            # Берем текущий символ
            current = s[i]
            # Оставшаяся часть строки
            remaining = s[:i] + s[i+1:]
            # Рекурсивно получаем все перестановки оставшейся части
            for p in permute(remaining):
                permutations.append(current + p)
        
        return permutations
    
    # Получаем все перестановки в виде строк
    permuted_strings = permute(num_str)
    
    # Преобразуем каждую строку в целое число и удаляем дубликаты
    permuted_numbers = list(set(int(p) for p in permuted_strings))
    
    return permuted_numbers

# Пример использования
number = 787
all_permutations = permute_number(number)
print(all_permutations)


