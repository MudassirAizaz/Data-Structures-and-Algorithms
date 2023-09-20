spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    for i in spicy_foods: return i["name"]


def get_spiciest_foods(spicy_foods):
    list1 = []
    for i in spicy_foods:
        if i['heat_level'] > 5:
            list1.append(i)
    return list1

def print_spicy_foods(spicy_foods):
    for i in spicy_foods:
        print(i['name'],'('+ i['cuisine'],') | Heat Level:',i['heat_level']*'�')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for i in spicy_foods:
        if i['cuisine'].lower() == cuisine.lower():
            print(i)

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))
    
def get_average_heat_level(spicy_foods):
    total = 0
    j = 0
    for i in spicy_foods:
        total += i['heat_level']
        j += 1
    return total/j

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    print(spicy_foods)

def main():
    print("Calling all the functions in main")
    print(get_names(spicy_foods))
    print(get_spiciest_foods(spicy_foods))
    print_spicy_foods(spicy_foods)
    print_spiciest_foods(spicy_foods)
    print(get_average_heat_level(spicy_foods))


if __name__=="__main__":
    main()
