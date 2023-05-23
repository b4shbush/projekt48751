import sys
import json
import yaml
#PARSOWANKO ARGUMENTÓW
#TASK 1

arguments = sys.argv[1:]
print("Podane argumenty:", arguments)
#WCZYTYWANIE DO OBIEKTU PLIKU (JSON)
#TASK2
json_file = "file.json"
try:
    with open(json_file, "r") as file:
        data = json.load(file)
    print("Loaded JSON:", data)
except Exception as e:
    print("Failed to load JSON from file:", e)
#Zapis danych z do pliku w formacie i zgodnie ze składnią .json
#TASK3 
output_file = "output.json"
try:
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)
    print("JSON data saved to", output_file)
except Exception as e:
    print("Failed to save JSON data:", e)
#WCZYTANIE Z PLIKU .yml I SPRAWDZENIE SKŁADNI
#TASK4
yml_file = "file.yml"
try:
    with open(yml_file, "r") as file:
        data = yaml.safe_load(file)
    print("Loaded YAML :", data)
except Exception as e:
    print("Failed to load YAML from file:", e)
#ZAPIS DANYCH DO PLIKU .yml ZGODNIE ZE SKLADNIA
#TASK5
output_file = "output.yml"
try:
    with open(output_file, "w") as file:
        yaml.dump(data, file)
    print("YAML saved to", output_file)
except Exception as e:
    print("Failed to save YAML:", e)

#WCZYTANIE Z PLIKU .XML I SPRAWDZENIE SKLADNI
#TASK6

xml_file = "file.xml"
try:
    tree = xml_file.parse(xml_file)
    root = tree.getroot()
    print("Loaded XML :")
    for child in root:
        print(child.tag, child.text)
except Exception as e:
    print("Failed to loaded XML from file:", e)
