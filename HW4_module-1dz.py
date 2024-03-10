
with open('зарплата.txt', 'w', encoding='utf-8') as file:
    file.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000')

def total_salary(path):
    total_salary = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary_str = line.strip().split(',')
                
                try:
                    salary = float(salary_str)
                    total_salary += salary
                    count += 1
                except ValueError:
                    print(f"Warning: Невірний формат зарплати для {name}")

        average_salary = total_salary / count if count > 0 else 0
        return total_salary, average_salary
    
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return None, None
    except Exception as e:
        print(f"Помилка: {e}")
        return None, None

# way to file
total, average = total_salary('зарплата.txt')

# results
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")



