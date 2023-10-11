animals_dict = {
    "dog":"куче",
    "cat":"котка",
    "bear":"мечка",
    "wolf":"вълк"
}

animal_in_english = input("Enter a animal in english:")
animal_in_bulgarian = input("Enter a translation:")

animals_dict[animal_in_english] = animal_in_bulgarian

print(animals_dict)