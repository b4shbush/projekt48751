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
