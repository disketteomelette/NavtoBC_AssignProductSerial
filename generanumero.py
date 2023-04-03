def asignar_codigos(nombre_archivo):
    codigo = 1
    familia = input('Insertar tal cual está la familia:')
    numserie = input("- Insertar el prefijo del número de serie:")
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo_entrada, open('resultados.csv', 'w', encoding='utf-8') as archivo_salida:
        for linea in archivo_entrada:
            datos = linea.strip().split(';')
            print(datos[18])
            if familia in datos[18]:
                print("-----COINCIDENCIA-----")
                codigo_str = str(codigo).zfill(5)
                datos.insert(20, numserie+codigo_str)
                codigo += 1
            archivo_salida.write(';'.join(datos) + '\n')
asignar_codigos("ANTERIOR.csv")
print("- Se ha guardado como 'resultados.csv' el mismo archivo pero con los códigos de la familia elegida en la columna final.")