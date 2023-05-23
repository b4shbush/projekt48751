import sys
import json
import yaml
import xml.etree.ElementTree as ET
#TU JEST UI ALE TROCHE DZIWNIE JEST
#TASK8
def load_json():
    file_path = input("Enter the path to the JSON file: ")
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        print("Loaded JSON:", data)
    except Exception as e:
        print("Failed to load JSON from file:", e)

def save_json():
    json_data = input("Enter the JSON data to save: ")
    file_path = input("Enter the path to save the JSON file: ")
    try:
        with open(file_path, "w") as file:
            json.dump(json_data, file, indent=4)
        print("JSON data saved to", file_path)
    except Exception as e:
        print("Failed to save JSON data:", e)

def load_yaml():
    file_path = input("Enter the path to the YAML file: ")
    try:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
        print("Loaded YAML:", data)
    except Exception as e:
        print("Failed to load YAML from file:", e)

def save_yaml():
    yaml_data = input("Enter the YAML data to save: ")
    file_path = input("Enter the path to save the YAML file: ")
    try:
        with open(file_path, "w") as file:
            yaml.dump(yaml_data, file)
        print("YAML data saved to", file_path)
    except Exception as e:
        print("Failed to save YAML:", e)

def load_xml():
    file_path = input("Enter the path to the XML file: ")
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        print("Loaded XML:")
        for child in root:
            print(child.tag, child.text)
    except Exception as e:
        print("Failed to load XML from file:", e)

def save_xml():
    xml_data = input("Enter the XML data to save: ")
    file_path = input("Enter the path to save the XML file: ")
    try:
        with open(file_path, "w") as file:
            file.write(xml_data)
        print("XML data saved to", file_path)
    except Exception as e:
        print("Failed to save XML:", e)
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
#ZAPIS DANYCH DO PLIKU .XML ZGODNIE ZE SKŁADNIA
#TASK7

output_file = "output.xml"
try:
    with open(output_file, "w") as file:
        tree.write(file)
    print("XML data saved to", output_file)
except Exception as e:
    print("Failed to save XML:", e)
