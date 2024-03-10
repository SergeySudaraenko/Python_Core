with open('Зарплата.txt', 'w', encoding='utf-8') as fh:
    fh.write('Alex Korp,3000\n')
    fh.write('Nikita Borisenko,2000\n')
    fh.write('Sitarama Raju,1000\n')

# Читання з файлу
with open('Зарплата.txt', 'r', encoding='utf-8') as fh:
    all_file = fh.read()
    print(all_file)












































































