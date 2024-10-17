from TADColD2 import *
#Criação das coleções de figurinhas
col = coleçãoD()
col2 = coleçãoD() #coleção C2 para trocas

#preenchem-se as coleções com diversas figurinhas repetidas e não repetidas
figurinhas = [23, 4, 1, 3, 4, 3, 5, 24, 23, 1, 12]
for f in figurinhas:
    col.novafigurinhaD(figurinhaD(f, 1)) #adiciona-se uma unidade por vez

figurinhas2 = [3, 5, 18, 6, 3, 12, 25, 42, 25, 42, 18]
for j in figurinhas2:
    col2.novafigurinhaD(figurinhaD(j, 1))

#Coleção C1 pós preenchimento:    
print("Figurinhas em C1:", col.string_presentes())
print("Repetidas em C1:", col.string_repetidas())
print("Figurinhas em C2:", col2.string_presentes())
print("Repetidas em C2:", col2.string_repetidas())

print("--------Removendo figurinhas de C1---------")
col.removeD(12) #figurinha única
col.removeD(45) #figurinha não presente na coleção
col.removeD(23) #figurinha repetida, remove-se uma cópia

print("C1 pós remoção:", col.string_presentes())
print("Repetidas em C1:", col.string_repetidas())

print("-----------Troca de figurinhas-------------")
col.trocaD(col2)
print("C1 pós troca:", col.string_presentes())
print("C2 pós troca:", col2.string_presentes())