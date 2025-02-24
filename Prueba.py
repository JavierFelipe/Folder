import csv


paises = [
    ["Pais", "Compras realizadas"],
    ["Noruega", 120],
    ["Islandia", 300],
    ["Italia", 50],
    ["Alemania", 720],
    ["Francia", 935],
    ["India", 600],
    ["Suiza", 180],
    ["Grecia", 500],
    ["Porugal", 490],
    ["Inglaterra", 130],
]

with open("Files/paises.csv", "w", newline ="") as file:
    writer = csv.writer(file, delimiter =",")
    writer.writerows(paises)



with open("Files/paises.csv", newline = '') as f:
    reader = csv.DictReader(f)

    c = input("Ingrese un pais (primera letra en mayúscula): ")

    for row in reader:
        if row["Pais"] == c:
            print(c,"tiene", row["Compras realizadas"], "compras realizadas")
        






  




