text = input("Введіть рядок : ").lower()
golosni = {'а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я'}
prigolosni = {'б', 'в', 'г', 'ґ', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'}
golosni_count = 0
prigolosni_count = 0
unique = set()
for i in text:
    if i in golosni:
        golosni_count += 1
        unique.add(i)
    elif i in prigolosni:
        prigolosni_count += 1
        unique.add(i)
        print(f"Кількість гласних звуків: {golosni_count}")
print(f"Кількість приголосних звуків: {prigolosni_count}")
print(f"Кількість унікальних звуків: {len(unique)}")
