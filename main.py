import csv

resultado = {}

with open("data\weather_stations.csv", "r", encoding="utf-8") as arquivo:
    leitor_csv = csv.reader(arquivo, delimiter=";")
    for linha in leitor_csv:
        print(linha)


    print(type(leitor_csv))