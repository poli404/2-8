from TADColE import *

#Cria-se a coleção (total do álbum)
col = colecaoE(60)
col2 = colecaoE(60) #segunda coleção (para troca)

#inserem-se as figurinhas obtidas pelo colecionador
col.inserefigurinhaE(figurinhaE(1, 2))
col.inserefigurinhaE(figurinhaE(1, 1))
col.inserefigurinhaE(figurinhaE(6, 2))
col.inserefigurinhaE(figurinhaE(23, 1))
col.inserefigurinhaE(figurinhaE(19, 2))
col.inserefigurinhaE(figurinhaE(2, 3))

col2.inserefigurinhaE(figurinhaE(43, 3))
col2.inserefigurinhaE(figurinhaE(23, 4))
col2.inserefigurinhaE(figurinhaE(18, 2))
col2.inserefigurinhaE(figurinhaE(2, 3))

#resultado do preenchimento das coleções
print("Figurinhas em C1:", col.string_presentesE())
print("Repetidas em C1:", col.string_repetidasE())

print("Figurinhas em C2:", col2.string_presentesE())
print("Repetidas em C2:", col2.string_repetidasE())

#experimentando remoções
print("---------- Removendo figurinhas de C1 ----------")
col.removeE(2) #uma figurinha repetida
col.removeE(3) #uma figurinha que não está na coleção
col.removeE(23) #uma figurinha não repetida (única)

#resultado pós-remoções em C1:
print("C1 pós remoção:", col.string_presentesE()) #não é alterada na remoção
print("C1 repetidas:", col.string_repetidasE()) #é alterada na remoção

#Efetuando a troca entre coleções:
print("------------ Troca de figurinhas ------------")
col.trocaE(col2)
print("C1 pós troca:", col.string_presentesE())
print("C2 pós troca:", col2.string_presentesE())