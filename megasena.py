bilhetes=[
[18,30,38,42,43,56],      # 01
[28,34,43,46,52,53],      # 02
[4,6,16,26,42,53],      # 03
[2,4,21,28,41,42],      # 04
[23,25,29,43,56,58],      # 05
[2,19,28,32,41,55],      # 06
[16,18,24,30,50,57],      # 07
[3,5,6,39,44,58],      # 08
[2,4,7,26,33,39],      # 09
[21,32,33,46,53,60]]     # 10

sorteado=[1,2,3,43,56,58]

for i in range(len(bilhetes)):
    resposta =set(bilhetes[i]) & set(sorteado)
    print("=============== xxxxxxxxxxxxxxx ========================")

    
    if len(resposta) == 6:
        print(i + 1, " = seis acerto você ganhou >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    if len(resposta) == 5:
        print(i + 1, " = cinco acerto muita sorte xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    if len(resposta) == 4:
        print(i + 1," = quatro acerto tirei ok ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
    if len(resposta) == 3:
        print(i + 1, " = três acerto")
    if len(resposta) == 2:
        print(i + 1, " = dois acerto")
    if len(resposta) == 1:
        print(i+1, " = um acerto")
    if len(resposta) == 0:
        print(i+1, " = zero acerto")

