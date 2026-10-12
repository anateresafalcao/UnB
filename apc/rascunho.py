def mediana_e_mais_proximo_media_e_pos(lista):
    tam = len(lista)
    lista_ordenada = []
    for elemento in lista:
            lista_ordenada.append(elemento)
            lista_ordenada.sort()
    if tam > 0:
        if tam % 2 == 0:
            mediana = (lista_ordenada[int(tam/2)] + lista_ordenada[int((tam/2)-1)])/2
        else:
            mediana = (lista_ordenada[int(tam/2)])
            
        media = (sum(lista_ordenada))/(len(lista_ordenada))
        
        lista2 = []
        for elemento in lista_ordenada:
            lista2.append(elemento)
        
        lista2.append(media)
        lista2.sort()
        
        tam2 = len(lista2)

        delta = lista2[tam2-1] - lista2[0]
        prox_media = lista_ordenada[0]
        
        
        
        for i in lista_ordenada:
            if abs(media-i) <= delta:
                prox_media = i
                delta = abs(media - i)
                
        index = -1       
        for i in lista:
            index += 1
            if i == prox_media:
                break
            
                
        
        resultado = [mediana, prox_media, index]
        
    else:
        prox_media = None
        mediana = None
        index = None
        resultado = [mediana, prox_media, index]
    return resultado