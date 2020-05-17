import keyboard
import time
from random import*



def sorteia_palavra():

    palavras = open('palavras.txt', 'r') #abre o arquivo contendo as palavras que podem ser sorteadas
    lista = []
    

    for palavra in palavras.readlines():
        nova_palavra = palavra.rstrip('\n') #rstrip retira a quebra de linha da palavra definida por \n
        lista.append(nova_palavra)
        
    chave_aleatoria = randint(0, len(lista)-1) 
    print(chave_aleatoria)
    palavra_sorteada = (lista [chave_aleatoria])
    print(palavra_sorteada)
    return palavra_sorteada.lower()



def monta_jogo_da_forca (palavra_sorteada):

    vetor_palavra_sorteada = []
    vetor_forca = []
    tentativas = 0
    letras_ja_tentadas = [] 
  
        
    
    for letra in palavra_sorteada:
        vetor_forca.append ("_")
        vetor_palavra_sorteada.append(letra) #transforma a palavra sorteada em um vetor com as letras


    print(vetor_palavra_sorteada)
   
    

    time.sleep(1)
        
    while (tentativas < 10):
       print (vetor_forca) 
       if ("_") not in vetor_forca: 
           print ("PARABÉNS VOCE VENCEU O JOGO!")
       
       entrada_usuario = input("Digite uma letra : ") #recebe a entrada de letra do usuarios
       
       if entrada_usuario in letras_ja_tentadas: #checa se o usuario ja tentou a letra antes e exibe uma mensagem de erro caso sim
           print("Você já inseriu essa letra antes! Tente outra letra.")
       
       elif entrada_usuario in vetor_palavra_sorteada: #se  for uma letra nova que ainda nao tentou, exibe mensagem de confirmação
           letras_ja_tentadas.append(entrada_usuario)    
           entrada = entrada_usuario
           print ("Parabens! Você acertou a letra! ",entrada_usuario)
           print("\n"*3)
           index_palavra = vetor_palavra_sorteada.index(entrada)
           vetor_forca [index_palavra] = entrada
               #vetor_forca[index_vetor] = entrada_usuario

          
           
               
       else:
           letras_ja_tentadas.append(entrada_usuario)
           print ("Voce não acertou a letra.")
           
       print (letras_ja_tentadas)
       tentativas += 1
    
    print('\n'*10)
    print ("VOCE PERDEU O JOGO!!!") 
    time.sleep(10)

            
       





palavra_sorteada = sorteia_palavra()
vetor_palavra_sorteada = monta_jogo_da_forca(palavra_sorteada)
jogo(vetor_palavra_sorteada)


