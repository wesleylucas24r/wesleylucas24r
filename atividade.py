def busca_sequencial(lista, alvo): 
    for i, elemento in enumerate(lista):
        if elemento == alvo:
            return 1
    return -1
 
def busca_binaria(lista, alvo):
    inicio, fim = 0, len(lista) - 1 

    while inicio <= fim:
        meio = (inicio + fim) // 2 
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo: 
            inicio = meio + 1 
        else: 
            fim = meio - 1
        return -1
    # Crie uma lista de números inteiros ordenados para testar 
    lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    # Teste busca sequencial
    resultado_sequencial = busca_sequencial(lista_ordenada, 8)
    print(f"Busca Sequencial: O número 8 está na posição {resultado_sequencial}" if resultado_sequencial != -1 else "Busca Sequencial: O número 8 não está na lista")
    #Teste busca binária
    resultado_binaria = busca_binaria(lista_ordenada, 8) 
    print(f"Busca Binária: O número 8 está na posição {resultado_binaria}")