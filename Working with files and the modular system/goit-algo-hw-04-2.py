def get_cats_info(path):
    cats_list = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            cat_data = line.strip().split(",")
            cat_info = {"id": cat_data[0], "name": cat_data[1], "age": int(cat_data[2])}
            cats_list.append(cat_info)

    return cats_list


# Приклад використання:
file_path = "Коты.txt"
cats_info = get_cats_info(file_path)

# Виведення інформації про котів
for cat in cats_info:
    print(f"ID: {cat['id']}, Ім'я: {cat['name']}, Вік: {cat['age']} років")
