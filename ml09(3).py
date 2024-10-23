rivers = { "Дніпро": 2201, "Дністер": 1362, "Південний Буг": 806, "Сіверський Донець": 1053,
           "Тиса": 966, "Прип'ять": 775, "Дунай": 2857, "Інгулець": 549 }
def add(name, length):
  rivers[name] = length
  print("Додана нова річка")
def delete(name):
  if name in rivers:
    del rivers[name]
    print("Видалено")
  else:
    print("Не знайдено")
def print_out():
  for name , length in rivers.items():
    print(f"-{name}: {length} ;")
while True:
    choice = input("\nВиберіть дію:\n1 - Додати річку\n2 - Видалити річку\n3 - Вивести всі річки\n4-Вихід\nВаш вибір: ")

    if choice == '1':
        add(input("Введіть назву річки: "), int(input("Введіть довжину річки: ")))
    elif choice == '2':
        delete(input("Введіть назву річки: "))
    elif choice == '3':
        print_out()
    elif choice == '4':
       break
    else:
        print("Хибний вибір")
