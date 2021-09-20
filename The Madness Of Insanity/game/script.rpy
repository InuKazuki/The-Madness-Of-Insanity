define j = Character("Jenny")
define y = Character("Yuri")
define a = Character("Julia")

#image fundocozinha = "images/Screenshot_8.png"

label start:

    #scene Screenshot_8
    #zoom 0.5
    show yurinormal

    y "{font=Timeless.ttf}O que tem pra hoje?{/font}"

    hide yurinormal
    show julianormal

    a "Pão com ovo frito, o café tá na pia"

    hide julianormal
    show yurinormal

    y "Valeu pela comida, não sei o que eu faria sem você"

    hide yurinormal
    show julianormal

    a "Mesmo sem você fazendo quase nada, ainda te mimo. Só que há uma condição, há algo chamado caminhão do lixo, que só passa segunda, quarta e sexta, então TRATE DE LEVAR O LIXO HOJE! TÁ UM FEDOR!"

    hide julianormal
    show yurinormal

    y "Eu tava ocupado! Não podia levar ontem!"

    hide yurinormal
    show julianormal

    a "Anime, né?"

    hide julianormal
    show yurinormal

    y "N-Não..."

    hide yurinormal
    show juliarage

    a "..."

    hide juliarage
    show julianormal

    y "...Mas enfim, hoje tu tem prova né?"

    hide julianormal
    show yurinormal

    y "Tenho"

    hide yurinormal
    show julianormal


    # This ends the game.

    return
