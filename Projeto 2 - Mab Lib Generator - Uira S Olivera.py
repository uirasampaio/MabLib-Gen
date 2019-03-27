# coding=utf-8

niveis = ['fácil', 'médio', 'difícil']
frase_facil = "Mais __0__ um __1__ na __2__ do que dois __3__."
frase_medio = "De __0__ e de __1__ todo __2__ tem um __3__."
frase_dificil = "Água __0__, __1__ dura, tanto __2__ até que __3__."
respostas_facil = ['vale', 'pássaro', 'mão', 'voando']
respostas_medio = ['medico', 'louco', 'mundo', 'pouco']
respostas_dificil = ['mole', 'pedra', 'bate', 'fura']
frases = [frase_facil, frase_medio, frase_dificil]
answers = [respostas_facil, respostas_medio, respostas_dificil]

def nivel_selector():
    # Utilizada para selecionar o nivel do jogo a função toma um input do usuario, caso o nivel seja selecionado
    # corretamente a função inicia a "level_procedure"
    while True:
        nivel = raw_input("Bem vindo ao Mab libs."
                           " Escolha um nível para o jogo: ( Fácil | Médio | Difícil ) ").strip().lower()
        if nivel in niveis:
            break
        print "Nível incorreto! Por favor tente novamente."
    print level_procedure(nivel)

def level_procedure(nivel):
    # Com base no nível escolhido na função "Nivel_Selector", essa função vai identificar o index
    # do nível selecionado e usar isso como parâmetro para identificar as 3 variáveis que vão ser
    # utilizadas como input na função "jogar_level". Fora isso a função confirma o nível selecionado, deseja boa
    # sorte para o jogador e solicita como input a quantidade de tentativas.
    print ("Voce escolheu o nivel " + nivel + ". Boa sorte!")
    game_index = niveis.index(nivel)
    frase = frases[game_index]
    respostas = answers[game_index]
    tentativas = raw_input("Quantas tentativas voce precisa para terminar o jogo?")
    print jogar_level(frase, respostas, tentativas)



def jogar_level(frase, respostas, tentativas):
    # A função executa o jogo, toma tres parametros como input e por meio de um loop while conta
    # a quantidade de tentativas do usuario, substitui as palavras certas e encerra o jogo quando
    # todas as palavras forem definidas.
    print ("Você tem {} chances de para concluir o mab libs!".format(tentativas))
    indice = 0
    print(frase)
    while tentativas > 0 and indice < len(respostas):
        palavra = raw_input("A palavra do campo __{}__ é? ".format(indice)).lower().strip()
        if palavra in respostas:
            frase = frase.replace("__{}__".format(indice), palavra)
            print "Resposta certa! Veja como esta ficando a frase:"
            print(frase)
            indice = indice + 1
        else:
            tentativas = tentativas - 1
            print "Resposta errada! Voce tem mais {} chance(s).".format(tentativas)
    return "Game over. Vamos jogar outra vez?"


print nivel_selector()
