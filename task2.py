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
    print("Loaded JSON :", data)
except Exception as e:
    print("Failed to load JSON from file:", e)
