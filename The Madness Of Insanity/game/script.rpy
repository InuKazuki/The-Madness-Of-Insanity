define je = Character("Jenny")
define ydialogo = Character("Yuri", image="ydialogo", who_color="#145DA0")
define alguem = Character("?", image="vazio", who_color="#603F8B")
define vmonica = Character("Monica", image="vazio2", who_color="#603F8B")
define vjenny = Character("Jenny", image="vazio3", who_color="#603F8B")
define vjulia = Character("Julia", image="vazio", who_color="#603F8B")
define jydialogo = Character("Jenny", image="jydialogo", who_color="#A16AE8")
define yu = Character("Yuri", who_color="#0302ff")
define ju = Character("Julia", who_color="#8aefe8")
define n = Character(" ")
image rua = "images/fundorua.png"
image side ydialogo = "images/icones/yuritela.png"
#image side alguem = "vazio.png"
image side jdialogo = "images/icones/juliatela.png"
image side jydialogo = "images/icones/jennytela.png"
image bg carro = "images/carro.png"
image chapter1 = "images/chapter1.png"
image chapter2 = "images/chapter2.png"

label start:

    show chapter1
    n ""
    hide chapter1

    scene black
    n "Tudo está escuro"

    n "Nada pode ser escutado, ou sentido, como se tudo não existisse mais"

    n "E mesmo assim, é confortante a presença do vácuo"

    n "Poderia até dizer que passaria a eternidade neste estado dormente"

    n "Então que ouço, dos confins do universo, um som alto e irritante, pulsando incessantemente"

    n "A cada toque da sirene, reganho meus sentidos, as coisas voltam a existir e começo a reconhecer meus arredores"

    n "*BEEP* *BEEP* *BEEP* *BEEP* *BEEP*"

    n "E eu acordo, com este maldito som ensurdecente do despertador"

    n "Aaaaaaaaargh, cala a boca…"

    n "Dou um soco nele para silenciá-lo, e funciona, talvez até demais"

    n "Com uma expressão amarga, me levanto da cama e abro as cortinas"

    n "Ah! Que brilho enorme!"

    n "Talvez devesse ter aberto com mais cuidado"

    scene quartoyuri
    ydialogo "No fundo, pode-se ver meu quarto, estreito mas comprido, minha cama estando em um canto com uma escrivaninha no outro, em cima dela, um pouco de papel hi-"

    alguem "*TOC* *TOC* *TOC*"

    alguem "O café tá pronto, vem logo"

    ydialogo "Oooook!"

    scene cozinha
    n "Logo depois, abro a porta e me dirijo a cozinha, onde vejo uma mesa redonda de tamanho mediano, sentada em uma das cadeiras, está a minha irmã, Júlia"

    ydialogo "O que tem pra hoje?"

    show julianormal
    vjulia "Pão com ovo frito, o café tá na pia"

    ydialogo "Valeu pela comida, não sei o que eu faria sem você"

    vjulia "Mesmo você não fazendo quase nada, ainda te mimo"

    vjulia "Se me lembro bem, em troca, pedi apenas uma coisa de você"

    ydialogo "Sério? O que isso seria?"

    show juliarage
    vjulia "Que você levasse a DESGRAÇA DO LIXO PRA FORA NO DIA QUE O CAMINHÃO PASSA! E JÁ FAZ 1 SEMANA QUE NÃO ESVAZIOU A LIXEIRA!"

    ydialogo "Fique sabendo que estava muito ocupado ontem, ok?"

    hide juliarage
    show juliasuspeito
    vjulia "Vendo anime o dia todo?!"

    ydialogo "N-não..."

    vjulia "..."

    hide juliasuspeito

    vjulia "De qualquer forma, você não tem uma prova hoje?"

    ydialogo "Tenho, por que?"

    vjulia "E estudasse?"

    ydialogo "Nem um pouco"

    show juliarage
    vjulia "COMO ASSIM VOCÊ NÃ-"

    ydialogo "Vou pegar o café, tchau!"

    scene black
    n "Eu pego o café e volto rapidamente para meu quarto, assim ela não me alcançará!"

    n "Depois de comer, começo a trocar as minhas roupas, um moletom do meu time de basquete favorito e uma calça do mesmo material"

    n "Não é o conjunto mais bonito, mas dá pro gasto"

    n "Após escovar os dentes, pego a minha mochila e vou para a porta da frente, onde minha irmã me espera"

    n "Nós corremos em direção ao ponto de ônibus, quando chegamos, o mesmo estava prestes a sair"

    n "Felizmente, conseguimos o adentrar a tempo, e estava lotado como sempre"

    n "Alguns minutos se passaram e finalmente chegamos à escola"

    n "Eu juro que a cada semana que passa eles tentam adicionar ainda mais salas na construção"

    scene escola
    n "A grande placa da frente apresenta o nome e slogan da escola"

    n "Seria um pouco mais motivador se não estivesse tão suja"

    scene black
    n "Saímos do ônibus e entramos na grande estrutura, nos separando em um dos corredores"

    scene corredor
    n "A porta da minha sala fica no meio de um corredor, com um par de banheiros à direita"

    n "Sinto como se cada vez que eu andasse, mais longe estou do-"

    scene caiu
    n "Meu monólogo interno é rapidamente interrompido por uma menina que saia do banheiro feminino"

    n "Ela usa um moletom preto, com seu capuz cobrindo parte de seu cabelo, possuindo duas mechas de seu cabelo rosa expostas"

    ydialogo "Me desculpa, você tá bem?"

    vjenny "Ah, sim, obrigada…"

    scene black
    n "Ela então sai correndo em direção oposta a minha"

    n "Um pouco confuso, decidi continuar a ir até minha sala"

    scene sala
    n "É a sala do 2º ano, razoavelmente espaçosa, com mais ou menos 20 alunos, mas apenas 2 estão presentes"

    n "A aula ainda não começou, mas como a primeira aula é a prova de portugues, os papéis já estão em cima de cada carteira"

    scene black
    n "Sei que estou pronto, mas mesmo assim, estou nervoso"

    n "Sinto cada vez mais ansiedade, nervosismo e medo, será que isso é normal? É apenas uma prova"

    n "Meu coração começa a acelerar cada vez mais, como se fosse pular do meu peito a qualquer momento"

    n "Até que então, ouço um alto e profundo batimento"

    n "*TUM-TUM*"

    n "O tempo ao meu redor para, tudo ficar gradualmente cinza, até que culmina na escuridão"

    n "Não vejo nada"

    n "Antes que possa processar o que vi, sinto uma forte briza em meu corpo"

    n "Abro lentamente os meus olhos e-"

    scene ceu1
    n "AAAAAAAAAAAAAAAAAAAAAAHHHHHHHH!!!"

    n "Estou… caindo?! Como?! Eu estava na minha sala de aula a poucos segundos atrás!"

    n "Em meio ao pânico, avisto uma vasta cidade abaixo de mim"

    scene ceu4
    n "Então é isso, irei morrer? Assim do nada?"

    n "Cada segundo que passa, me aproximo mais do meu fim, tenho mais 10 segundos no máximo"

    n "Não há mais nada que posso fazer, não há nada perto para amortecer a queda"

    scene ceu6
    n "5 segundos, acho que é isso, vivi uma vida medíocre e sem graça, antes que pudesse aproveitar o resto"

    scene black
    n "Fecho meus olhos e-"

    n "Pareço ter batido em várias coisas antes de atingir o chão"

    scene death1
    with fade
    n "Minha respiração está pesada e está difícil ficar acordado"

    n "A cor vermelha está por toda minha volta. Sangue. Meu sangue"

    n "Provavelmente veio do grande corte que possuo na minha barriga. Destruiu minhas roupas também"

    n "Sinto minhas forças drenando ao montes, a qualquer momento, irei fechar os olhos pela última vez"

    scene death2
    with fade
    n "Logo antes disso, percebi uma silhueta familiar vindo em minha direção"

    scene ceu6
    n "..."

    show chapter2
    n ""
    hide chapter1

    scene black
    n "Tudo está escuro"

    n "Nada pode ser escutado, ou sentido, como se-"

    n "Pera, isso já aconteceu antes"

    n "Estou apenas dormindo"

    n "Mas… e o que aconteceu antes? Foi tudo apenas um sonho?"

    n "Isso não faz sentido, não posso ter um sonho dentro de outro sonho"

    n "Pensando bem, se estou dormindo, não era pro despertador ter tocado a esse ponto?"

    n "Vou me atrasar pra aula!"

    n "Tento ao máximo me forçar a abrir os olhos e acordar"

    scene yuriacordando
    n "Hah!"

    n "Acordei"

    n "Mas, espera, onde estou?"

    n "Esta não é minha casa"

    n "De fato, parece um lugar muito mais velho e rústico"

    n "E esta também não é minha cama, eu não tinha um cobertor de lã grossa assim"

    n "Argh!"

    n "Tento me levantar mas dores rápidas e angustiantes se espalham pelo meu corpo"

    n "Levanto minha camisa para checar de onde toda essa dor veio"

    n "Q-Que…"

    n "Uma enorme lesão se encontra em minha barriga, quase igual àquele sonho horroroso"

    n "Será que…? Não, não pode ser…"

    scene black
    n "QUE PO##A É ESSA?!"

    n "FOI REAL?! TUDO AQUILO REALMENTE ACONTECEU?!"

    n "MAS ENTÃO, COMO SOBREVIVI AQUELA QUEDA ENORME?!"

    n "E ONDE C###LHOS EU ESTOU SE ESTA NÃO É MINHA CASA?!"

    n "NADA DISSO FAZ SENTIDO!!!"

    n "Justo quando estava prestes a enlouquecer, ouço a porta do quarto se abrindo"

    alguem "Ei garoto, está tudo bem?"

    scene black
    show monicanormal

    n "Uma moça simpática, que aparenta estar entre os 30 e 40 anos, atravessa a porta"

    n "Essa moça, ela… eu já vi ela antes"

    n "Mas… mas como isso é possível...?"

    n "Não consigo conter minhas emoções, e começo a chorar de leve"

    vmonica "Porque você está chorando?"

    scene yuriacordando

    n "N-Não é nada…"

    show monicanormal

    vmonica "Como assim nada? Vimos o que aconteceu com você, afinal, minha filha o encontrou"

    scene black

    n "Filha? Mas, como isso..."

    scene yuriacordando

    n "Sua filha? Espera, então, o que eu sou de você?"

    show monicanormal

    vmonica "Hã? A gente se conhece?"

    scene yuriacordando

    n "Ah, não, acho que não, afinal, isso tudo é apenas um sonho"

    show monicanormal

    vmonica "Sonho? Para mim você parece bem real, e sei que estou acordada"

    scene yuriacordando

    n "Sim, claro que sim… De qualquer forma, vou conseguir andar ainda?"

    show monicanormal

    vmonica "Com certeza! Apenas espere um pouco, o feitiço de cura ainda não te recuperou por completo"

    scene yuriacordando

    n "Sim enten-, pera, feitiço?"

    show monicanormal

    vmonica "Exato. Quando minha filha o encontrou no meio da cidade, você estava em um estado horrível, ela então aplicou o feitiço de cura imediatamente, caso contrário, você já estaria morto"

    scene yuriacordando

    n "Então foi assim que eu sobrevivi a queda. Gostaria de agradecer a minha salvadora"

    show monicanormal

    vmonica "Ah, ela não está em casa no momento"

    vmonica "Pode esperar um pouco? Irei buscar a comida pra você"

    scene black

    n "Ela então prontamente sai do quarto"

    n "Durante nossa conversa inteira, não olhei nos olhos dela em nenhum momento"

    n "Acho melhor descansar mais, afinal, hoje eu caí do céu e quase virei panqueca"

    n "Mas ainda não entendo, como eu vim parar aqui? Eu não estava prestes a fazer uma prova de português na escola?"

    n "Além do mais, quem é aquela mulher? Eu reconheço seu rosto, mas não pode ser ela"

    n "Se não é ela, quem é? E porque seus rostos são tão parecidos?"

    n "Ah! Que droga! Não posso apenas ficar aqui deitado sem fazer nada, preciso saber o que está acontecendo, esteja machucado ou não!"

    n "Me levanto rápido da cama, ignorando a dor que está por vir em meu corpo"



    scene rua

    play sound "euquero.mp3"
    ydialogo "Aquele carro, eu quero ele!"

    call screen rua

    if _return == "carro":
        jump carro

label carro:
    hide bg rua
    scene bg carro:
    with dissolve

    show yurinormal

    play sound "baitacarro.mp3"
    yu "Baita carro"

    hide yurinormal
    show julianormal

    play sound "batata.mp3"
    ju "batata"

    hide julianormal
    return

screen rua:
    imagemap:
        ground "images/ground.png"
        hover "images/hover.png"

        hotspot(756, 294, 49, 69) action Return("carro")
