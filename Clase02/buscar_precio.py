#precio naranja.py


def buscar_precio(fruta):
    with open ("../Data/precios.csv", "rt") as f:
        for line in f:
            row = line.split(',')
            if row[0] == (fruta):
                return (float(row[1]))
        print(f"{fruta} no figura en el listado de precios")
    

precio=buscar_precio("Frambuesa")
print(f'Costo: ${precio:0.2f}')