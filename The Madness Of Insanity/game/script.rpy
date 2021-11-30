define ydialogo = Character("Yuri", image="ydialogo", who_color="#145DA0")
define jydialogo = Character("Jenny", image="jydialogo", who_color="#A16AE8")
define mdialogo = Character("Monica", image="mdialogo", who_color="#FFAEBC")
define jyalterdialogo = Character("Jenny", image="jyalterdialogo", who_color="#A16AE8")
define jyalterragedialogo = Character("Jenny", image="jyalterragedialogo", who_color="#A16AE8")
define vjulia = Character("Julia", image="vazio", who_color="#FBE7C6")
define vmonica = Character("Monica", image="vazio", who_color="#FFAEBC")
define vjenny = Character("Jenny", image="vazio", who_color="#A16AE8")
define vjennyalter = Character("Jenny", image="vazio", who_color="#A16AE8")
define vyuri = Character("Yuri", image="vazio", who_color="#145DA0")
define alguem = Character("?", image="vazio", who_color="#B5E5CF")
define n = Character(" ")
image chapter1 = "images/chapter/capitulo1.png"
image chapter2 = "images/chapter/capitulo2.png"
image side mdialogo = "images/icones/monicatela.png"
image side ydialogo = "images/icones/yuritela.png"
image side jdialogo = "images/icones/juliatela.png"
image side jyalterdialogo = "images/icones/jennyaltertela.png"
image side jyalterragedialogo = "images/icones/jennyalterragetela.png"
image bg carro = "images/carro.png"
image rua = "images/fundorua.png"

label start:

    show capitulo1
    n ""
    hide capitulo1

    scene black
    with dissolve

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
    with dissolve

    ydialogo "No fundo, pode-se ver meu quarto, estreito mas comprido, minha cama estando em um canto com uma escrivaninha no outro, em cima dela, um pouco de papel hi-"

    alguem "*TOC* *TOC* *TOC*"

    alguem "O café tá pronto, vem logo"

    ydialogo "Oooook!"

    scene cozinha
    with fade

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
    with dissolve

    n "Eu pego o café e volto rapidamente para meu quarto, assim ela não me alcançará!"

    n "Depois de comer, começo a trocar as minhas roupas, um moletom do meu time de basquete favorito e uma calça do mesmo material"

    n "Não é o conjunto mais bonito, mas dá pro gasto"

    n "Após escovar os dentes, pego a minha mochila e vou para a porta da frente, onde minha irmã me espera"

    n "Nós corremos em direção ao ponto de ônibus, quando chegamos, o mesmo estava prestes a sair"

    n "Felizmente, conseguimos o adentrar a tempo, e estava lotado como sempre"

    n "Alguns minutos se passaram e finalmente chegamos à escola"

    n "Eu juro que a cada semana que passa eles tentam adicionar ainda mais salas na construção"

    scene escola
    with dissolve

    n "A grande placa da frente apresenta o nome e slogan da escola"

    n "Seria um pouco mais motivador se não estivesse tão suja"

    scene black
    with dissolve

    n "Saímos do ônibus e entramos na grande estrutura, nos separando em um dos corredores"

    scene corredor
    with dissolve

    n "A porta da minha sala fica no meio de um corredor, com um par de banheiros à direita"

    n "Sinto como se cada vez que eu andasse, mais longe estou do-"

    scene caiu
    with fade

    n "Meu monólogo interno é rapidamente interrompido por uma menina que saia do banheiro feminino"

    n "Ela usa um moletom preto, com seu capuz cobrindo parte de seu cabelo, possuindo duas mechas de seu cabelo rosa expostas"

    ydialogo "Me desculpa, você tá bem?"

    vjenny "Ah, sim, obrigada…"

    scene black
    with dissolve

    n "Ela então sai correndo em direção oposta a minha"

    n "Um pouco confuso, decidi continuar a ir até minha sala"

    scene sala
    with dissolve

    n "É a sala do 2º ano, razoavelmente espaçosa, com mais ou menos 20 alunos, mas apenas 2 estão presentes"

    n "A aula ainda não começou, mas como a primeira aula é a prova de portugues, os papéis já estão em cima de cada carteira"

    scene black
    with dissolve

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
    with fade

    n "AAAAAAAAAAAAAAAAAAAAAAHHHHHHHH!!!"

    scene ceu2
    with dissolve

    n "Estou… caindo?! Como?! Eu estava na minha sala de aula a poucos segundos atrás!"

    scene ceu3
    with dissolve

    n "Em meio ao pânico, avisto uma vasta cidade abaixo de mim"

    scene ceu4
    with dissolve

    n "Então é isso, irei morrer? Assim do nada?"

    n "Cada segundo que passa, me aproximo mais do meu fim, tenho mais 10 segundos no máximo"

    scene ceu5
    with dissolve

    n "Não há mais nada que posso fazer, não há nada perto para amortecer a queda"

    scene ceu6
    with dissolve
    n "5 segundos, acho que é isso, vivi uma vida medíocre e sem graça, antes que pudesse aproveitar o resto"

    scene black
    with dissolve

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

    scene black
    with dissolve

    n "..."

    show capitulo2
    n ""
    hide capitulo2

    scene black
    with dissolve

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
    with dissolve

    vyuri "Hah!"

    vyuri "Acordei"

    vyuri "Mas, espera, onde estou?"

    vyuri "Esta não é minha casa"

    vyuri "De fato, parece um lugar muito mais velho e rústico"

    vyuri "E esta também não é minha cama, eu não tinha um cobertor de lã grossa assim"

    vyuri "Argh!"

    vyuri "Tento me levantar mas dores rápidas e angustiantes se espalham pelo meu corpo"

    vyuri "Levanto minha camisa para checar de onde toda essa dor veio"

    vyuri "Q-Que…"

    vyuri "Uma enorme lesão se encontra em minha barriga, quase igual àquele sonho horroroso"

    vyuri "Será que…? Não, não pode ser…"

    scene black
    with dissolve

    n "QUE PO##A É ESSA?!"

    n "FOI REAL?! TUDO AQUILO REALMENTE ACONTECEU?!"

    n "MAS ENTÃO, COMO SOBREVIVI AQUELA QUEDA ENORME?!"

    n "E ONDE C###LHOS EU ESTOU SE ESTA NÃO É MINHA CASA?!"

    n "NADA DISSO FAZ SENTIDO!!!"

    n "Justo quando estava prestes a enlouquecer, ouço a porta do quarto se abrindo"

    alguem "Ei garoto, está tudo bem?"

    scene black
    with dissolve

    n "Uma moça simpática, que aparenta estar entre os 30 e 40 anos, atravessa a porta"

    n "Essa moça, ela… eu já vi ela antes"

    n "Mas… mas como isso é possível...?"

    n "Não consigo conter minhas emoções, e começo a chorar de leve"

    show monicanormal
    vmonica "Porque você está chorando?"
    hide monicanormal

    scene yuriacordando
    with dissolve

    vyuri "N-Não é nada…"

    mdialogo "Como assim nada? Vimos o que aconteceu com você, afinal, minha filha o encontrou"

    scene black
    with dissolve

    n "Filha? Mas, como isso..."

    scene yuriacordando
    with dissolve

    vyuri "Sua filha? Espera, então, o que eu sou de você?"

    mdialogo "Hã? A gente se conhece?"

    vyuri "Ah, não, acho que não, afinal, isso tudo é apenas um sonho"

    mdialogo "Sonho? Para mim você parece bem real, e sei que estou acordada"

    vyuri "Sim, claro que sim… De qualquer forma, vou conseguir andar ainda?"

    mdialogo "Com certeza! Apenas espere um pouco, o feitiço de cura ainda não te recuperou por completo"

    vyuri "Sim enten-, pera, feitiço?"

    mdialogo "Exato. Quando minha filha o encontrou no meio da cidade, você estava em um estado horrível, ela então aplicou o feitiço de cura imediatamente, caso contrário, você já estaria morto"

    vyuri "Então foi assim que eu sobrevivi a queda. Gostaria de agradecer a minha salvadora"

    mdialogo "Ah, ela não está em casa no momento"

    mdialogo "Pode esperar um pouco? Irei buscar a comida pra você"

    scene black
    with dissolve

    n "Ela então prontamente sai do quarto"

    n "Durante nossa conversa inteira, não olhei nos olhos dela em nenhum momento"

    n "Acho melhor descansar mais, afinal, hoje eu caí do céu e quase virei panqueca"

    n "Mas ainda não entendo, como eu vim parar aqui? Eu não estava prestes a fazer uma prova de português na escola?"

    n "Além do mais, quem é aquela mulher? Eu reconheço seu rosto, mas não pode ser ela"

    n "Se não é ela, quem é? E porque seus rostos são tão parecidos?"

    n "Ah! Que droga! Não posso apenas ficar aqui deitado sem fazer nada, preciso saber o que está acontecendo, esteja machucado ou não!"

    n "Me levanto rápido da cama, ignorando a dor que está por vir em meu corpo"

    n "Ué? Não está doendo?"

    n "Será que o feitiço de cura já fez efeito? Por quanto tempo fiquei dormindo desde que vim pra cá?"

    n "Nossa, está escuro aqui dentro, não dá pra ver quase nada"

    n "A pouca luz no quarto vem da fresta da porta entreaberta"

    n "Bom, quanto mais cedo eu sair daqui, melhor"

    n "Atravesso a porta do quarto, me deparo com a visão de um corredor"

    n "Numa de suas extremidades, avistou uma garota, com vestimentas que parecem ter saído direto da seção medieval de uma loja de fantasias"

    n "Junto da armadura, há uma espada presa em suas costas por uma bainha de couro"

    n "Além do cosplay do Rei Arthur, outro aspecto notável é seu cabelo rosa choque, com uma franja e cabelos soltos na frente de seu rosto"

    n "Pensando bem, já vi este exato cabelo e o jeito que ele cobre o rosto antes"

    n "É a garota que esbarrei na escola logo antes de entrar na sala de aula"

    scene caiumemoria
    with dissolve

    scene black
    with fade

    n "Mas ela parece meio diferente aqui, antes, parecia tímida e frágil"

    n "Contudo, aqui ela está encostada na parede de braços cruzados"

    n "A julgar pela sua postura e face, consigo deduzir que ela conseguiria (e provavelmente não hesitaria) em me descer a porrada"

    n "E acho que meus olhares não foram muito bem escondidos"

    n "Ela olha pra mim com um rosto mal humorado e começa a falar"

    show jennyalternormal

    vjennyalter "Dá pra parar de me olhar assim? Vai me transformar em pedra"

    scene black
    with fade

    n "Pelo visto minhas análises não estavam exatamente erradas"

    show jennyalternormal

    vjennyalter "E antes que pergunte, ela tá lá embaixo na cozinha"

    ydialogo "Ela quem?"

    vjennyalter "Eu que não sou"

    ydialogo "Ah, sim, é claro"

    vjennyalter "..."

    ydialogo "..."

    ydialogo "Então… qual o seu nome?"

    scene black
    with fade

    n "Ela solta um longo suspiro"

    show jennyalternormal

    vjennyalter "Sou Jenny, me chame de outra coisa e corto em dois"

    ydialogo "Ahn… que?"

    vjennyalter "Isso mesmo que você ouviu, ou quer que eu repita pro bebê aqui?"

    ydialogo "N-não vai ser necessário"

    scene black
    with fade

    n "Nossa, é realmente um 180° da menina que vi na escola"

    show jennyalternormal

    vjennyalter "Ah sim, esqueci de mencionar, a mulher que te tratou no quarto, o nome dela é Mônica"

    ydialogo "Mônica?"

    vjennyalter "Sim, por quê?"

    ydialogo "Não é nada não, só me lembrei de alguém especial com esse nome"

    scene black
    with fade

    n "No fundo do corredor, está as escadas para baixo, delas, é possível ouvir uma voz"

    hide jennyalternormal
    show monicanormal

    vmonica "Jenny, pode checar o garoto no quarto?!"

    jyalterdialogo "Ele já está de pé, Dona Mônica!"

    vmonica "Então chame-o para comer alguns biscoitos"

    hide monicanormal
    show jennyalternormal

    vjennyalter "E aí? Vai querer os cookies ou vai ficar parado vendo tinta secar?"

    ydialogo "Não sou de recusar biscoitos fresquinhos"

    scene black
    with fade

    n "acompanho a Jenny até as escadas, ao descer, consigo ter visão da cozinha"

    n "É relativamente grande, com uma mesa de madeira redonda no centro, um forno de pedra no canto, junto de alguns armários na parede, além de uma janela no lado da mesa"

    show monicanormal

    vmonica "Vamos, sente-se, ninguém gosta de comer em pé"

    scene black
    with fade

    n "Ao me sentar, reparo nos biscoitos, estão frescos e quentes"

    show monicanormal

    ydialogo "São de manteiga?"

    vmonica "Sim! Você gosta desse sabor?"

    ydialogo "Bom, faz muito tempo desde a última vez que comi um, minha mãe os fazia pra mim"

    vmonica "Nossa, adoraria conhecê-la então, fariamos ótimos biscoitos!"

    ydialogo "Ah, isso… não é bem possível, ela…"

    ydialogo "Esquece, não gosto de tocar no assunto"

    vmonica "Oh, bem, me desculpe, não queria ser mal educada"

    vmonica "..."

    ydialogo "Então… o que é este lugar?"

    vmonica "Eu… não entendi, o que você quis dizer?"

    jyalterdialogo "Argh, eu não te disse que ele é estranho? Olhe só as roupas dele, claramente não é dessas redondezas"

    vmonica "Jenny, não se trata os convidados dessa maneira!"

    vmonica "Me desculpe pelo comportamento dela, as vezes pode ficar meio irritada"

    ydialogo "Sem problemas, já estou acostumado com meninas facilmente aborrecidas"

    scene black
    with fade

    n "Solto uma pequena risada enquanto falo isso"

    show monicanormal

    jyalterdialogo "Como que eu vou ser educada com um estranho que fica me provocando desse jeito?!"

    scene black
    with fade

    n "Espero que a gente não comece uma discussão agora, provavelmente duraria muito tempo"

    show monicanormal

    vmonica "Isso me lembrou que você ainda não nos disse o seu nome"

    ydialogo "Ah, me desculpe, eu ainda não me apresentei"

    scene black
    with fade

    n "Com uma referência obscura, eu faço uma pose apontando para o teto"

    show monicanormal

    ydialogo "Eu me chamo Yuri Santos, tenho 15 anos e além de não ter nenhuma noção deste lugar, também estou totalmente quebrado!"

    scene black
    with fade

    n "A Jenny olha pra mim com uma expressão tão confusa quanto irritada"

    n "Obviamente, ninguém entendeu a referência"

    show monicanormal

    vmonica "Ah… bem, eu me chamo Mônica, e a irritadinha se chama Jenny"

    scene black
    with fade

    n "Jenny não diz nada, mas dá pra ver que a qualquer momento ela vai explodir"

    show monicanormal

    vmonica "E ela também tem 15 anos, que coincidência!"

    ydialogo "Ah sim, uma ÓTIMA coincidência"

    scene black
    with fade

    n "Falo isso com um tom obviamente sarcástico"

    show monicanormal

    vmonica "Hoje eu irei fazer ensopado de peixe, tem algumas coisas faltando como batata e tomate, vocês dois poderiam ir comprar enquanto faço outras coisas?"

    scene black
    with fade

    n "Considerando minha posição, seria ideal não desperdiçar tempo fazendo tarefas domésticas desse tipo"

    n "Mas considerando minha atual situação, não tenho nenhuma pista para onde ir, então talvez algo simples me ajude"

    show monicanormal

    ydialogo "Por mim, tudo bem!"

    jyalterragedialogo "Mas nem fu###do que eu vou com ele"

    vmonica "Jenny, por favor, faz isso por mim?! Além do mais, ele não parece uma má pessoa"

    scene black
    with fade

    n "Ela solta um enorme suspiro"

    show monicanormal

    jyalterdialogo "...Tá, eu vou, é na barraca do Seu Jorge né?"

    vmonica "Lá mesmo! Não demore muito, ok?"

    hide monicanormal

    scene black
    with fade

    show capitulo3
    n ""
    hide capitulo3

    scene black
    with fade

    n "Saímos então da casa da Dona Mônica"

    n "Nossa caminhada até a loja é bem quieta, nenhum de nós dois falou algo"

    n "Talvez seja uma boa tentar quebrar o gelo"

    show yurinormal

    vyuri "Por um momento, achei que você ia explodir de raiva do meu lado depois de termos saído"

    jyalterragedialogo "..."

    scene black
    with fade

    n "Tá, não parece ter dado certo. Talvez uma estratégia diferente funcione?"

    show yurinormal

    vyuri "Então, qual é a dessa sua armadura? Parece pesada, ainda mais com essa espada, por que você precisa dela de qualquer forma?"

    jyalterragedialogo "..."

    scene black
    with fade

    n "Isso já está me irritando, por que ela não diz nada?"

    n "Eu sei que não sou o melhor pra falar com garotas, mas isso já é exagero"

    show yurinormal

    vyuri "Pode pelo menos falar alguma coisa pra eu saber que você está no mínimo reconhecendo minha existência?!"

    scene black
    with fade

    n "Ela solta um enorme suspiro, um touro respiraria menos que ela"

    show yurinormal

    jyalterragedialogo "Olha... eu não te conheço, simplesmente te achei quase morto no meio da rua e, como a ótima pessoa que sou, decidi te ajudar"

    jyalterragedialogo "Mas isso não quer dizer que somos amigos ou algo do tipo"

    vyuri "Bom, se a gente não conversar, aí mesmo que não vamos ser amigos"

    jyalterdialogo "Você tem várias perguntas, certo? Eu também tenho várias sobre você, então que tal, eu respondo a suas e vice versa, trato?"

    vyuri "Ok, você primeiro então"

    jyalterdialogo "Tá, primeiramente, de você veio? Não reconheço essas suas roupas de nenhum lugar, e confia em mim, eu conheço os arredores"

    vyuri "De forma geral, sou do Brasil"

    jyalterdialogo "'Basil?' Mas que tipo de cidade baseia seu nome em um condimento?"

    vyuri "Não! BRASIL, com um R no meio"

    jyalterdialogo "Nunca ouvi falar, você deve ser de muito longe então"

    vyuri "É, acho que pode-se dizer isso"

    jyalterdialogo "Mas, se você é de tão longe, como veio parar aqui? E por que você tava quase morto na praça?"

    vyuri "Isso… eu não consigo responder"

    jyalterdialogo "Como assim não consegue?! Que tipo de pessoa vai pra outro lado do mundo e nem sabe como foi?!"

    vyuri "N-não é isso! É que, é muito complicado de explicar…"

    jyalterdialogo "Desembucha, o que quer que seja, é melhor do que não saber"

    vyuri "Tá bom *respira*"

    scene black
    with fade

    n "Dou uma sugada gigante de ar"

    show yurinormal

    vyuri "Tudo começou num dia normal da minha vida"

    vyuri "Minha irmã estava me enchendo o saco porque não tinha levado lixo fora"

    vyuri "A gente foi de ônibus até a escola que nem todos os outros dias"

    vyuri "A primeira aula era de portugues e tinha uma prova"

    vyuri "Eu fiquei muito nervoso, mas aí comecei a passar mal no meio da sala"

    vyuri "Meu coração e cabeça começaram a doer muito, depois tudo ficou cinza"

    vyuri "Quanto me dei por vir, estava caindo do céu, e logo depois eu caí no chão quase morto"

    vyuri "Ai você apareceu e salvou a minha vida por um triz, e depois disso só lembro acordando na sua casa"

    vyuri "*Arf arf arf*"

    scene black
    with fade

    n "Estou quase sem ar depois dessa explicação toda, espero que ela tenha entendido tudo"

    show yurinormal

    jyalterdialogo "Eu não entendi po##a nenhuma do que você me disse"

    scene black
    with fade

    n "Saco"

    show yurinormal

    vyuri "Pois é… eu disse que era complicado, ainda estou tentando entender como isso aconteceu"

    jyalterdialogo "Bom, aproveitando a deixa, eu imagino que você queria que eu te respondesse agora, certo?"

    vyuri "Esse era o trato"

    jyalterdialogo "Ok, e não se preocupe, minha explicação é muito menos confusa que a sua"

    jyalterdialogo "Aquela casa onde moro, pertence a Dona Mônica, pode-se dizer que ela é minha atual mãe"

    vyuri "Atual? O que aconteceu com sua mãe original?"

    jyalterdialogo "Posso acabar de falar?!"

    scene black
    with fade

    n "Eu fico em silêncio!"

    show yurinormal

    jyalterdialogo "Enfim, a Dona Mônica cuida de mim agora, em troca, eu protejo ela e a casa de quaisquer ameaças que apareçam"

    vyuri "Eu presumo que você tenha habilidade em combate então?"

    jyalterdialogo "Meu pai me treinava quando era pequena, ele era um cavaleiro afinal de contas"

    jyalterdialogo "Sobre a minha mãe, ela nos abandonou logo depois de eu nascer, não queria aceitar a responsabilidade de ter uma criança pelo visto"

    vyuri "E seu pai? Por que ele não cuida de você?"

    jyalterdialogo "..."

    vyuri "Ah…, desculpe, não queria-"

    jyalterdialogo "Não, não precisa, não tinha como você saber mesmo"

    scene black
    with fade

    n "Uma questão fica na minha cabeça, seria meio insensato perguntar isso, mas a curiosidade vai me devorar enquanto não tenho uma resposta"

    show yurinormal

    vyuri "Ãhn… se não for muito incomodo, como o seu pai morreu?"

    jyalterdialogo "Me desculpe?"

    vyuri "Só fiquei curioso, mas entendo se você não quiser-"

    jyalterdialogo "Em combate tá? Ele morreu durante uma batalha…"

    jyalterdialogo "Uma batalha totalmente inútil! Eu disse pra ele não ir, mas ele nunca me escutou!!!"

    scene black
    with fade

    n "Ela começa a chutar violentamente o barro e as pedras no chão. Acho que cutuquei um ninho de vespas"

    show yurinormal

    jyalterdialogo "Se ele apenas tivesse me ouvido, nada daquilo teria acontecido!"

    jyalterdialogo "Argh!!!"

    scene black
    with fade

    n "Ela dá um soco enorme numa inocente árvore por perto"

    show yurinormal

    vyuri "Você… você ta bem?"

    jyalterdialogo "Ah… ah… sim, tô bem"

    jyalterdialogo "Só… precisava liberar a minha raiva um pouco"

    vyuri "Desculpa, eu não deveria ter perguntado aquilo"

    jyalterdialogo "Não, não tem problema, a culpa não é sua"

    vyuri "Vamos continuar então?"

    jyalterdialogo "Hmm? Ah sim, a gente ia fazer compras certo? Vamos então"

    scene black
    with fade

    n "A gente volta a caminhar em silêncio por alguns minutos"

    show yurinormal

    vyuri "Ah, verdade, a Mônica mencionou ter uma filha, foi ela que me salvou certo?"

    jyalterdialogo "Sim, do contrário, você já teria virado adubo"

    vyuri "Enfim, eu gostaria de agradecer ela por salvar minha vida"

    jyalterdialogo "Isso seria meio difícil"

    vyuri "Mas por que?"

    jyalterdialogo "A Juji não é bem uma pessoa fácil de lidar… Raramente a vejo, ela passa a maior parte do tempo na cidade, chegando sempre tarde parecendo cansada…"

    vyuri "Entendi…"

    jyalterdialogo "Seria compreensível se ela fosse uma adulta, mas ela tem apenas 13 anos, e eu que tenho 15 não faço nem metade do que ela deve fazer..."

    vyuri "Nossa, 13 anos?!"

    jyalterdialogo "Eu nem sei como ela aguenta…"

    jyalterdialogo "Talvez a gente encontre ela pelo caminho"

    scene black
    with fade

    n "Continuamos caminhando pela cidade, a arquitetura parece arcaica, as estradas e casas parecem ser feitas do mesmo material. Jenny para em frente a um beco"

    show yurinormal

    vyuri "Um beco?! Não parece um lugar tranquilo para passar"

    jyalterdialogo "Se a gente seguir por aqui é bem mais rápido"

    vyuri "Mas é perigoso!"

    jyalterdialogo "Relaxa, é seguro… Se você ficar quieto"

    vyuri "Por quê?"

    jyalterdialogo "Apenas cale a boca e me siga, tá bom?"

    vyuri "Tá…"

    scene black
    with fade

    n "Seguindo pelo beco, não dá para ver nada pela maior parte do caminho, apenas janelas cobertas por cortinas. De repente, é possível ver a luz no final, mas a caminhada é interrompida por um som"

    alguem "Maria… Maria…Maria…"

    scene black
    with fade

    n "No meio das sombras, sentado no chão, um homem apoiado no muro, suas pernas esticadas, suas vestes eram longas e em seu rosto uma barba rala. Parecia murmurar algo"

    show yurinormal

    vyuri "O senhor está bem?"

    scene black
    with fade

    n "Simplesmente abria a boca de forma despreocupada, ignorando o que Jenny havia dito"

    n "O homem então olha em meus olhos, fazendo com que eu entenda o porquê do aviso de Jenny. Seu olhar era desesperado e aterrorizado, esse homem deveria ter passado por coisas que nem se pode imaginar"

    alguem "Maria?… Maria.… MARIA!!… FALSA MARIA, MARIA, MARIA!! Maria Maria!!!MariaMariaMariaMariaMariaMaria!!! AAAHHHH!!"

    n "Jenny me puxa pelo braço para fora do beco. Levantando a cabeça, vejo-a irritada"

    show yurinormal

    vyuri "MAS QUE MERDA FOI ESSA?"

    jyalterdialogo "Eu falei para você calar a boca!"

    vyuri "Quem é aquele velho e por que ele começou a gritar ‘Maria’?"

    jyalterdialogo "Eu sei lá! Só sei que Maria era o nome da esposa dele!"

    vyuri "Esposa?"

    jyalterdialogo "Esse cara não sai do beco, e está sempre com aquele olhar assustador falando o nome de sua amada…"

    vyuri "Mas por quê?"

    jyalterdialogo "Não faço idéia, só sei que é o nome da esposa dele por causa de rumores de velhos sem assunto…"

    alguem "Jenny?"

    show capitulo4
    n ""
    hide capitulo4




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
    vyuri "Baita carro"

    hide yurinormal
    show julianormal

    play sound "batata.mp3"
    vjulia "batata"

    hide julianormal
    return

screen rua:
    imagemap:
        ground "images/ground.png"
        hover "images/hover.png"

        hotspot(756, 294, 49, 69) action Return("carro")
