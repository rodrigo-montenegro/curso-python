mensaje = "Este es un texto un poco grande en cuanto a lomgitud de caracteres se refiere"

resultado = mensaje.count("e")
encuentra = "texto" in mensaje
find = mensaje.find("texto")
parte_texto = mensaje[find: find + len("texto")]
comienzo = mensaje.startswith("Este")
final = mensaje.endswith("a")

print(resultado)
print(encuentra)
print(find)
print(parte_texto)
print(comienzo)
print(final)