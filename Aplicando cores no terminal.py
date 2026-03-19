print('\033[0;30;41m Olá mundo')
#Style - 0 (nada); 1 (negrito), 4 (sublinhado), 7 (negativo ou invertido)
#text - 30 branco ; 31 vermelho, 32 verde , 33 amarelo, 34 azul, 35 roxo, 36 ciano, 37 cinza
#BACK/cor de fundo : 40 branco ; 41 vermelho, 42 verde , 43 amarelo, 44 azul, 45 roxo, 46 ciano, 47 cinza
print('\033[7;30;42m Olá mundo!\033[m')
#Colocando \033[m no final ele volta para a formatação normal.