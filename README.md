# Esteganografia

Trabalho Final da disciplina "DCOM3105 - Processamento Digital de Imagens"

## Description

Este projeto demonstra o uso de uma técnica básica para ocultar uma imagem dentro de outra através de uma manipulação a nível de bit.

Concatena-se quatro bits da parte alta da imagem de prevalência com os quatro bits da parte alta da imagem a ser ocultada. A parte mais significativa dos bits da imagem resultante serão da imagem de prevalência e os menos significativos serão da imagem ocultada.

```
Pixel da imagem de prevalência [1011 1101]
Pixel da imagem a ser ocultada [0011 1100] 
                            
                            [1011 XXXX] + [0011 XXXX]

Pixel resultante        ==>       [1011 + 0011] 
```

Para descobrir a imagem ocultada, basta criar uma imagem com os 4 bits menos significativos da imagem com algo escondido como bits mais significativos e para os bits menos significativos podemos adicionar valores de ruído (valores aleatórios).

```
Imagem com algo Oculto [1011 0011]

Resultado     ==>           [0011 + 4 bits de valores aleatórios]
```

## Observation
Esse processo é feito para cada canal de cor de um pixel de uma imagem RGB (Colorida).
