import os
print("Task1")
a = input("Podaj nazwę pliku (Przykład: test.xml) : ")
if os.path.exists(a):
    if a == ".json" or a == ".yml" or a == ".xml":
        print("Podaj prawidłową nazwę pliku")
    elif a.lower().endswith('.xml'):
        print("Wybrałeś plik xml")
    elif a.lower().endswith('.yml'):
        print("Wybrałeś plik yml")
    elif a.lower().endswith('.json'):
        print("Wybrałeś plik json")
    else:
        print("Zły format ")
else:
    print("Ścieżka pliku nie istnieje.")
