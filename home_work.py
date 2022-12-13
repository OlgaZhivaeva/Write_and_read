with open('Cook_book.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip() 
        number_of_ingredients = int(f.readline().strip())
        dish = []               
        for i in range(number_of_ingredients):
            ingredient_name, quantity, measure = f.readline().strip().split(' | ')
            dish.append({'ingredient_name': ingredient_name,'quantity': int(quantity), 'measure': measure})
        f.readline()
        cook_book.setdefault(dish_name, dish)
    print(f'cook_book = {cook_book}')
