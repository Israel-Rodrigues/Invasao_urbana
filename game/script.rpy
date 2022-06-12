
define d = Character("David")
define t = Character("Theo")

image banheiro = "images/banheiro.png"
image casarao = "images/casa_frente.jpg"
image casa_lado = "images/casa_lado.jpg"
image corredor_escolha = "images/corredor_escolha.png"
image corredor = "images/corredor.png"
image continua = "images/continua.png"
image david = "images/david.png"
image david_normal = "images/david_normal.png"
image david_cel_normal = "images/david_cel_normal.png"
image david_teste = "images/david-teste.png"
image david_frustado = im.Flip("images/atores/david/frustado.png", horizontal="True")
image david_bravo = im.Flip("images/atores/david/bravo.png", horizontal="True")
image david_surpreso = im.Flip("images/atores/david/surpreso.png", horizontal="True")
image david_surpresao = im.Flip("images/atores/david/surpresao.png", horizontal="True")
image david_feliz = im.Flip("images/atores/david/feliz.png", horizontal="True")
image despensa = "images/despensa.jpg"
image escritorio = "images/escritorio.jpg"
image fundo = "images/room.png"
image garage = "images/garage.jpg"
image janela_direita = "images/janela_direita.jpg"
image janela_esquerda = "images/janela_esquerda.jpg"
image office_closed_door = "images/office_closed-door.png"
image office_open_door = "images/office_open-door.png"
image office_cadeado = "images/office_cadeado.png"
image quartoCasal = "images/quarto_casal.png"
image quarto_visitaD = "images/quarto_visita_direito.jpg"
image quarto_visitaE = "images/quarto_visita_esquerdo.jpg"
image quarto_infantil = "images/quarto_infantil.png"
image sala_reuniao = "images/sala_reuniao.jpg"
image rouxinol = "images/rouxinol.jpg"
image theo = "images/theo.png"
image theo_normal = "images/theo_normal.png"
image theo_camera_normal = "images/theo_camera_normal.png"
image theo_camera_surpreso = "images/theo_camera_surpreso.png"
image theo_confuso = "images/theo_confuso.png"
image theo_careta = "images/atores/theo/careta.png"
image theo_feliz = "images/atores/theo/feliz.png"
image theo_triste3 = "images/atores/theo/triste.png"
image theo_tristao = "images/atores/theo/tristao.png"

label start:

    # ATO UM
    scene fundo:
        zoom 0.70

    play music "audio/quarto_david.mp3"

    show theo_normal at right:

    t "Era uma manhã de quarta-feira quando eu fui para casa de David."
    t "O dia havia amanhecido limpo mas o céu estava começando a fechar, fazendo com que o azul claro fosse substituído pouco a pouco por um nublado cinzento e empoeirado."
    t "Eu não gostava desse clima, pois indicava chuva, pequenos engarrafamentos e poças de lama pela cidade."
    t "No entanto, ainda assim, eu me encontrava sentado na janela do quarto do meu amigo, olhando distraidamente para o horizonte."
    t "Ele, sempre animado, tagarelava sobre os vídeos que poderíamos produzir."
    t "David e eu temos um canal de vídeos há uns três anos."
    t "Ele — um cara extrovertido, popular e que ama aparecer — ficou fascinado pela ideia."
    t "Enquanto eu — um cara introvertido, nerd, que manja minimamente sobre algumas coisas, mas que é bom com tecnologia — achei que seria bom juntar o útil ao agradável."
    t "Assim criamos o “Nada de Ócio”."
    t "É, eu sei."
    t "O nome não é grande coisa, mas, dá um desconto!"
    t "É melhor que muitos nomes por aí."
    t "O que nós fazemos?"
    t "Bom, vários tipos de vídeos: reações, vlogs das nossas vidas pessoais, vídeos jogando coisas legais…"
    t "Nosso conteúdo é bem amplo, pois sempre tentamos fazer o que gostamos."
    show david_normal at left:
    with dissolve
    d "{cps=15}“Ei, Theo!”{/cps}"
    d "{cps=15}“Você ta me escutando, cara?”{/cps}"
    show david_frustado at left:
    with dissolve
    t "Quando virei o rosto para o David, ele parecia bem frustrado."
    d "{cps=15}“Cara, preciso da sua ajuda!”{/cps}"
    d "{cps=15}“Não consigo pensar em nada!”{/cps}"
    show theo_careta at right:
    with dissolve
    t "Fiz uma careta."
    t "Isso era ruim pois David era quem sempre vinha com ideias do que podíamos gravar."
    hide theo_careta
    with dissolve
    t "{cps=15}“Você sabe que eu não costumo ter boas ideias, cara.”{/cps}"
    t "{cps=15}“Não quer dar uma olhada na gringa?”{/cps}"
    d "{cps=15}“Não sei.”{/cps}"
    hide david_frustado
    with dissolve
    d "{cps=15}“Quero fazer algo mais original mas....”{/cps}"
    t "David começou a murmurar baixinho."
    d "{cps=15}“pensa, pensa...”{/cps}"
    hide david_normal
    with dissolve
    t "Suspirei novamente e tirei meu celular do bolso."
    t "Comecei a rolar a página que hospedava vários vídeos (inclusive os nossos) em busca de ideias e acabei me distraindo com um vídeo noticiário, que informava sobre crimes na região. "
    t "Meu pai é detetive e eu sabia que ele estava encarregado de um caso sério, por isso fico um pouco preocupado..."
    t "Meus dedos rolaram a tela em direção aos comentários, mas a aba de vídeos relacionados me chamou a atenção."
    t "E lá estava."
    t "Um vídeo gringo de um grupo invadindo e explorando uma instalação abandonada."
    t "Ajeitei a postura e me concentrei no conteúdo."
    t "{cps=15}“Cara...”{/cps}"
    show david_normal at left:
    with dissolve
    t "Imediatamente David apareceu ao meu lado."
    t "{cps=15}“Se liga nisso.”{/cps}"
    hide david_normal
    show david_cel_normal at left:
    with dissolve
    t "Ele pegou o celular da minha mão e começou a assistir."
    d "{cps=15}“Na rua Rouxinol tem uma casa abandonada muito sinistra...”{/cps}"
    t "Comentou David, com os olhos ainda na tela."
    t "{cps=15}“Sim, e eu me lembro de não ter visto sequer uma pichação no lugar.”{/cps}"
    t "{cps=15}“O que será que rola por lá?”{/cps}"
    t "David deu um sorriso largo ao me entregar o celular."
    hide david_cel_normal
    show david_normal at left:
    with dissolve
    d "{cps=15}“Só tem uma maneira de descobrir.”{/cps}"
    d "{cps=15}“Vamos à garagem nos preparar.” {/cps}"

    jump garagem
    # ATO DOIS

label garagem:
    scene garage:
        zoom 0.70

    with pixellate
    play music "audio/quarto_david.mp3"
    show theo_normal at right:
    show david_normal at left:

    d "{cps=15}“Cara, a gente não vai acampar...”{/cps}"
    t "Comentou David, olhando para a minha mochila por cima dos meus ombros, onde eu guardava o material que levaríamos para nossa empreitada."
    t "{cps=15}“Eu sei.”{/cps}"
    t "Respondi, balançando os ombros."
    d "{cps=15}“Então pra quê tudo isso?”{/cps}"
    t "Olhei para a mochila. "
    t "Além do essencial — garrafas de água, barrinhas de cereal, uma lanterna e um sinalizador por acionamento — havia apenas o equipamento de gravação — câmera, flash, microfone, bateria…"
    t "{cps=15}“Estamos  indo para um local abandonado que fica ao lado de uma floresta enorme.”{/cps}"
    t "{cps=15}“Eu só tô me preparando...”{/cps}"
    d "{cps=15}“Você é muito surtado...”{/cps}"
    show theo_feliz at right:
    t "Comentou rindo, antes de voltar a atenção para sua mochila quase vazia."
    t "Eu revirei os olhos."
    t "Quando terminei de guardar os equipamentos, me virei para o David e o encontrei se arrumando no espelho, fazendo caras e bocas."
    t "{cps=15}“Cara, você sabe que a gente não vai se encontrar com a Poliana, né?”{/cps}"
    d "{cps=15}“Você sabe mesmo como se vingar, hein?”{/cps}"
    t "Disse, virando-se para mim, sorrindo e revirando os olhos. "
    d "{cps=15}“Tudo pronto para a gente ir?”{/cps}"
    t "{cps=15}“Sim, senhor.”{/cps}"
    t "David colocou sua mochila nas costas e passou o braço pelos meus ombros, me conduzindo até a saída da garagem."
    d "{cps=15}“Então, vamos nessa.”{/cps}"
    hide theo_feliz

    jump rouxinol

label rouxinol:
    scene rouxinol:
        zoom 0.80
        yalign 1.0
    with pixellate
    play music "audio/upside down grin2.ogg"
    show theo_normal at right:
    show david_normal at left:

    t "Já era no meio da tarde quando chegamos na rua — um lugar deserto e sujo."
    t "Uma cerca de arame farpado enferrujado separava um longo trecho do matagal do outro lado."
    t "O caminho de barro seco seguia em uma subida que não era íngreme, mas era extensa."
    t "Eu já estava ofegante por causa do peso da mochila — e pelo meu sedentarismo — e estava com dificuldade para acompanhar David que seguia um pouco mais a frente, falando distraidamente, sem perceber que eu estava ficando para trás."
    d "{cps=15}“Não, mas se liga. Que tal a gente colocar no título, tipo, “Casa mal assombrada”…?”{/cps}"
    d "{cps=15}“Ou “Casa assombrada, encontramos algo?”.”{/cps}"
    d "{cps=15}“Um título com algo sobrenatural vai chamar a atenção..”{/cps}"
    t "{cps=15}“Podemos parar um pouco?”{/cps}"
    t "{cps=15}“Os equipamentos estão pesando.”{/cps}"
    d "{cps=15}“Oh, certo.”{/cps}"
    t "Contemplamos matagal alto e extenso e do céu cheio de nuvens."
    t "Já não estava mais nublado como de manhã e o sol aparecia timidamente, iluminando o topo da vegetação."
    t "Peguei minha garrafa e bebi um pouco de água."
    t "David aceitou um gole alegremente."
    t "Até ele estava um pouco cansado."
    t "{cps=15}“Ok.”{/cps}"
    t "Disse ajeitando a mochila nas minhas costas."
    t "{cps=15}“Bora lá, estamos quase chegando.”{/cps}"
    t "Caminhamos mais algum tempo até avistar o casarão."

    jump casarao

label casarao:
    scene casarao at center:
        zoom 0.70
        yalign 0.30
    with pixellate
    play music "audio/upside down grin2.ogg"
    show theo_normal at right:
    show david_normal at left:

    t "A arquitetura da casa lembrava a estética gótica vitoriana, com telhados pontudos, colunas com entalhes outrora repleto de detalhes e uma escada dupla que se unificava na porta de entrada."
    t "A vegetação que já havia tomado conta de boa parte da casa, invadia algumas janelas quebradas, enquanto outras, fechadas com tábuas de madeira, pareciam oferecer um espaço perfeito para pequenos animais selvagens construírem suas tocas."
    t "As paredes acinzentadas e a sujeira alojada entre as madeiras do assoalho, junto com a vegetação densa, davam um aspecto assustador para o lugar."
    t "E realmente: nada de pichações."
    d "{cps=15}“Ah, é aqui.”{/cps}"
    t "Comecei a tirar o equipamento da mochila, começando pela a câmera com o aparelho de luz flash em cima, enquanto David ajustava o celular para servir de microfone."
    hide theo_normal
    show theo_camera_normal at right:
    show david_cel_normal at left:
    with dissolve
    t "{cps=15}“Ok, tudo certo aqui.”{/cps}"
    t "Olhei para meu amigo e ele fez um sinal de positivo para mim."
    t "Apertei o rec e comecei a gravar."
    d "{cps=15}“Fala galera do mal, aqui é o David e hoje eu vim trazer para vocês um vídeo arrepiante”{/cps}"
    t "Disse, diminuindo o tom de voz e se aproximando da câmera."
    t "Quase sussurrava, como se alguém estivesse à espreita ou como se a casa não pudesse saber que estávamos ali."
    d "{cps=15}“Essa casa aqui atrás da gente, pertenceu a uma família muito rica durante a década de 90, porém dizem que depois de acontecer alguns casos SINISTROS aqui, agora é mal assombrada.”{/cps}"
    t "Apontei a câmera para a casa."
    t "O lugar era realmente sinistro, eu sequer precisava me esforçar para conseguir alguns takes assustadores."
    d "{cps=15}“Então...”{/cps}"
    t "David retomou. Voltei a enquadrá-lo."
    d "{cps=15}“Viemos aqui para investigar e saber se é real!”{/cps}"
    d "{cps=15}“E aí? Vamos juntos?”{/cps}"
    t "David se virou em direção à casa e começou a caminhar."
    t "Eu o segui com a câmera."
    d "{cps=15}“Vamos investigar se há alguma maneira de entrar aqui.”{/cps}"
    t "Começamos a inspecionar o local."
    t "{cps=15}“Cara, parece que tá tudo fechado...”{/cps}"
    t "Aponto a câmera para as janelas do primeiro andar a fim de conseguir uma visão melhor com o zoom e noto que a janela do lado direito está um pouco aberta."
    t "Talvez com um pouco de força conseguíssemos abrir, mas a escalada até lá seria difícil."
    t "Segui rodeando a casa pela esquerda enquanto o David continuava examinando as janelas da frente."
    t "Encontro outra janela, esta com poucas tábuas de madeira."
    t "Seria fácil invadir se conseguíssemos, por exemplo, um pé de cabra, mas era provável que isso fizesse um barulhão e, apesar do aspecto abandonado, não sabíamos se realmente não havia ninguém ali."
    hide david_normal
    hide theo_camera_normal
    hide david_cel_normal

    t "O que eu faço?"

    menu:
        "Janela da esquerda":
            jump esquerda
        "Janela da direita":
            jump direita

label esquerda:
    play music "audio/upside down grin2.ogg"
    show theo_normal at right:

    t "{cps=15}“David, vem cá.”{/cps} Chamei um pouco mais alto."
    show david_normal at left:
    with dissolve
    t "Em alguns segundos David aparece de pé ao meu lado."
    t "{cps=15}“Olha lá em cima.”{/cps}"
    t "Aponto para a janela com poucas tábuas."
    t "{cps=15}“As tábuas parecem frágeis e é fácil de escalar.”{/cps}"
    t "{cps=15}“O que acha?”{/cps}"
    t "Ele analisou para onde meu dedo apontava e em seguida começou a procurar algo no chão."
    d "{cps=15}“Deve ter pelo menos uma pedrona aqui...”{/cps}"
    t "Comecei a procurar com ele qualquer coisa que ajudasse com as tábuas."
    t "{cps=15}“Aí, tenta isso.”{/cps}"
    t "Entreguei para ele um pedaço de ferro que encontrei, cujo formato lembrava um pé de cabra."
    t "David segurou a ferramenta improvisada e começou a escalar a parede até a janela."
    t "Eu o segui."
    t "Quando o alcancei, ele já havia conseguido abrir o lugar."
    d "{cps=15}“Demorou hein?”{/cps}"
    t "Ele me provocou."
    t "Deixou o pedaço de ferro ao lado da janela e entrou no lugar."
    t "Eu o segui alguns passos atrás."

    jump quarto_casal

label quarto_casal:
    scene quartoCasal:
        zoom 0.70
        yalign 1.0
    with pixellate
    play music "audio/Amb Corredor.ogg"
    show theo_normal at right:
    show david_normal at left:

    t "O cômodo era um quarto de casal."
    t "E assim como o lado de fora, o local estava deplorável."
    t "Fedia a mofo por causa da cama."
    hide theo_normal
    hide david_normal
    show theo_camera_normal at right:
    show david_cel_normal at left:
    with dissolve
    t "Peguei novamente minha câmera e comecei a gravar, ao mesmo tempo que David ligava o microfone."
    d "{cps=15}“Conseguimos entrar na casa pelo primeiro andar.”{/cps}"
    d "{cps=15}“Aqui parece ser o quarto do casal que vivia neste lugar.”{/cps}"
    d "{cps=15}“Vamos dar uma olhada no que podemos encontrar mais.”{/cps}"
    t "Com o flash da câmera ligado segui filmando cada canto do cômodo até chegar na penteadeira ao lado da cama, onde entre os vários produtos de beleza e bem-estar um papel dobrado se destacava."
    t "{cps=15}“David, encontrei algo.”{/cps}"
    t "Ele veio até mim e desdobrou o papel, revelando o mapa do primeiro andar da casa."
    d "{cps=15}“Isso vai ser bom pra gente se orientar.”{/cps}"
    t "Comenta, analisando o papel."
    d "{cps=15}“Olha, aqui na frente tem um quarto infantil.”{/cps}"
    d "{cps=15}“Vamos lá investigar.”{/cps}"
    t "Meu amigo saiu em disparada até a porta do quarto."
    t "Eu o segui imediatamente."

    jump quarto_infantil

label quarto_infantil:
    scene quarto_infantil:
        zoom 0.70
        yalign 0.8
    with pixellate
    play music "audio/Amb Corredor.ogg"
    show theo_normal at right:
    show david_normal at left:

    t "A frente do quarto que saímos tinha outro, então decidimos entrar neste primeiro."
    t "O quarto que entramos tinha um aspecto infantil."
    t "As paredes, que outrora pareciam ter ostentado um azul bebê, agora estavam sujas pelo tempo e com manchas de infiltração."
    t "Os brinquedos empoeirados no chão e nas prateleiras, junto com a cama infantil quebrada e o pequeno colchão rasgado completavam o quadro peculiar."
    hide theo_normal
    hide david_normal
    show theo_camera_normal at right:
    show david_cel_normal at left:
    with dissolve
    t "Peguei a câmera e comecei a gravar."
    d "{cps=15}“Cara...”{/cps}"
    t "Arfou David."
    d "{cps=15}“Aqui tá muito sinistro.”{/cps}"
    t "Ele se voltou para a câmera, já com o microfone preparado."
    d "{cps=15}“Conseguimos entrar no primeiro andar.”{/cps}"
    d "{cps=15}“Aqui parece ser  um quarto infantil.”{/cps}"
    t " Desvio a câmera para gravar os brinquedos."
    d "{cps=15}“Vamos continuar explorando.”{/cps}"
    t "Sigo filmando o local."
    t "Além dos brinquedos, enquadro a janela pela qual entramos e alguns desenhos na parede provavelmente feitos por uma criança, que se destacaram mesmo em baixo da sujeira."

    jump corredor

label direita:
    play music "audio/upside down grin2.ogg"
    show theo_camera_normal at right:

    t "{cps=15}“Ei, David.”{/cps}"
    t "Chamei, indo em direção ao meu amigo."
    show david_normal at left:
    with dissolve
    t "{cps=15}“O que acha daquela janela?”{/cps}"
    t "Aponto para a janela logo acima de nós."
    t "{cps=15}“Parece fácil de abrir.”{/cps}"
    t "David observa o caminho por alguns segundos, procurando uma forma de escalar até lá."
    d "{cps=15}“Vai ser difícil chegar lá, mas realmente é uma entrada boa.”{/cps}"
    d "{cps=15}“Vou tentar subir.”{/cps}"
    d "{cps=15}“Se prepare para escalar também.”{/cps}"
    hide theo_camera_normal
    show theo_normal at right:
    with dissolve
    t "Parei de gravar e guardei a câmera na mochila, seguindo David alguns passos atrás."
    t "Escorreguei algumas vezes, mas nada que comprometesse a escalada."
    t "Parei do lado dele ao chegar na janela."
    d "{cps=15}“Certo.”{/cps}"
    t "Disse ele, um pouco ofegante."
    d "{cps=15}“Segura desse lado que eu vou segurar deste.”{/cps}"
    d "{cps=15}“ No três, vamos empurrar juntos para cima.”{/cps}"
    t "Posicionei meu braço direito."
    d "{cps=15}“Um... dois... três!”{/cps}"
    t "Começamos a fazer força juntos."
    t "A janela estava muito dura, mas depois de algum tempo conseguimos abri-la completamente."
    t "{cps=15}“Ufa.”{/cps}"
    t "Suspirei aliviado."
    d "{cps=15}“Já cansou, cara?”{/cps}"
    t "David soltou uma risadinha."
    d "{cps=15}“Bora, vamos entrar.”{/cps}"

    jump quarto_infantil_

label quarto_infantil_:
    scene quarto_infantil:
        zoom 0.70
        yalign 0.8
    with pixellate
    play music "audio/Amb Corredor.ogg"
    show theo_normal at right:
    show david_normal at left:

    t "O quarto que entramos tinha um aspecto infantil."
    t "As paredes, que outrora pareciam ter ostentado um azul bebê, agora estavam sujas pelo tempo e com manchas de infiltração."
    t "Os brinquedos empoeirados no chão e nas prateleiras, junto com a cama infantil quebrada e o pequeno colchão rasgado completavam o quadro peculiar."
    hide theo_normal
    show theo_camera_normal at right:
    with dissolve
    t "Peguei a câmera e comecei a gravar."
    d "{cps=15}“Cara...”{/cps}"
    t "Arfou David."
    d "{cps=15}“Aqui tá muito sinistro.”{/cps}"
    t "le se voltou para a câmera, já com o microfone preparado."
    d "{cps=15}“Conseguimos entrar no primeiro andar.”{/cps}"
    d "{cps=15}“Aqui parece ser  um quarto infantil.”{/cps}"
    t "Desvio a câmera para gravar os brinquedos."
    d "{cps=15}“Vamos continuar explorando.”{/cps}"
    t "Sigo filmando o local."
    t "Além dos brinquedos, enquadro a janela pela qual entramos e alguns desenhos na parede provavelmente feitos por uma criança, que se destacaram mesmo em baixo da sujeira."
    d "{cps=15}“Ei cara, tem um quarto aqui na frente com a porta aberta.”{/cps}"
    d "{cps=15}“Acho que é um quarto de casal.”{/cps}"
    d "{cps=15}“Entrei lá e encontrei esse mapa em cima da penteadeira.”{/cps}"
    d "{cps=15}“Agora não vamos ficar mais perdidos.”{/cps}"

    jump quarto_casal_

label quarto_casal_:
    scene quartoCasal:
        zoom 0.70
        yalign 1.0
    with pixellate
    play music "audio/Amb Corredor.ogg"
    show theo_normal at right:
    show david_normal at left:

    t "A frente do quarto que saímos tinha outro, então decidimos entrar neste primeiro."
    t "O cômodo era um quarto de casal."
    t "E assim como o lado de fora, o local estava deplorável."
    t "Fedia a mofo por causa da cama."
    hide theo_normal
    show theo_camera_normal at right:
    with dissolve
    t "Peguei novamente minha câmera e comecei a gravar, ao mesmo tempo que David ligava o microfone."
    d "{cps=15}“Foi aqui neste quarto que achamos um mapa.”{/cps}"
    t "Ele mostra o papel pra câmera."
    d "{cps=15}“Aqui parece ser o quarto do casal que vivia aqui, então vamos continuar explorando.”{/cps}"

    jump corredor

label corredor:
    scene corredor:
        zoom 0.70
        yalign 1.0
    with pixellate
    play music "audio/Amb Corredor.ogg"
    show theo_camera_surpreso at right:
    show david_cel_normal at left:

    t "O corredor daquele andar estava tão precário e sujo como o resto da casa."
    t "Além dos dois quartos explorados, haviam mais três de cada lado."
    t "Como estava escuro, ajustei a luz acima da câmera."
    t "Foco o equipamento no David. Ele volta a falar para o público, quase sussurrando."
    d "{cps=15}“Galera, estamos no corredor do primeiro andar agora.”{/cps}"
    d "{cps=15}“Como podem ver, a casa está toda esbagaçada e suja por causa do tempo.”{/cps}"
    t "Gravei as paredes e o chão, cujo aspecto estava horrível."
    t "Voltei a enquadrar Davi."
    d "{cps=15}“Ainda têm vários quartos que vamos explorar.”{/cps}"
    d "{cps=15}“Tô bem curioso para saber o que tem em cada um deles.”{/cps}"
    t "Disse, e então ele se virou e seguiu para uma das portas."

    jump quartoVisitaEsquerdo

label quartoVisitaEsquerdo:
    scene quarto_visitaE:
        zoom 0.7
        yalign 1.0
    with pixellate
    play music "audio/Amb quarto visita esquerdo.ogg"
    show theo_camera_normal at right:
    show david_cel_normal at left:

    t "Ao entrarmos pela porta, encontramos um quarto igualmente sujo e deplorável."
    t "A cama de solteiro, sem colchão e com aspecto enferrujado e o pequeno armário de madeira tomavam a maior parte do ambiente."
    t "As paredes, que um dia foram brancas, haviam sido consumidas por infiltração e sujeira."
    t "As tábuas na janela, mesmo bem pregadas, permitiam que alguns raios de luz passassem pelas frestas, iluminando o cômodo com uma luz amarelada."
    t "Quando dei uma olhada o David, e ele estava distraído observando algo perto do abajur de parede."

    jump quartoVisitaDireito

label quartoVisitaDireito:
    scene quarto_visitaD:
        zoom 0.7
        yalign 1.0
    with pixellate
    play music "audio/Amb quarto visita direito.ogg"
    show theo_camera_normal at right:
    show david_cel_normal at left:

    t "O quarto tinha uma cama de casal mais simples que a do aposento anterior e, assim como provavelmente o resto da casa, estava sujo e destruído."
    t "A janela estava totalmente tampada por tábuas."
    t "O assoalho exibia rachaduras grotescas e eu tinha a sensação de que poderia desabar junto com o chão se pisasse ali."
    d "{cps=15}“Cara..”{/cps}"
    t "Virei a câmera para David."
    d "{cps=15}“Esse quarto aqui tá MUITO mal acabado.”{/cps}"
    d "{cps=15}“E nem pensar em pisar nesse chão aí.”{/cps}"
    t "Filmei melhor o chão, aproximando a imagem com o zoom."
    t "{cps=15}“Melhor evitar de andar nesse lugar.”{/cps}"

    jump despensa

label despensa:
    scene despensa:
        zoom 0.7
        yalign 1.0
    with pixellate
    play music "audio/Amb dispensa.ogg"
    show theo_camera_normal at right:
    show david_cel_normal at left:

    t "Entramos em um local um pouco apertado, repleto de prateleiras com garrafas de vidro de vários tamanhos, rótulos e tipos, organizadas de maneira impecável.."
    d "{cps=15}“Pelo mapa, aqui é a adega...”{/cps}"
    t "David olhou para o papel que estava em mãos."
    d "{cps=15}“Estranho ter uma aqui em cima.”  {/cps}"
    t "{cps=15}“Só bebida alcoólica aqui.” {/cps}"
    t "Comento, aproximando a câmera de um dos produtos."
    t "{cps=15}“Todos vencidos, é claro.”{/cps}"
    t "Segui filmando a adega."

    jump banheiro

label banheiro:
    scene banheiro:
        zoom 0.70
        yalign 1.0
    with pixellate
    play music "audio/Amb banheiro.ogg"
    show theo_camera_surpreso at right:
    show david_cel_normal at left:

    t "Ao abrir a próxima porta, um cheiro forte de esgoto invadiu nossos narizes."
    t "Demos alguns passos para trás para fugir do mal cheiro."
    d "{cps=15}“Caralho...”{/cps}"
    t "David colocou a mão no nariz."
    t "{cps=15}“É, a gente devia ter esperado por isso.”{/cps}"
    d "{cps=15}“Eu não vou entrar aí não.”{/cps}"
    t "Ele se virou."
    d "{cps=15}“Grava um pouquinho aí e vamos pra próxima.”{/cps}"
    t "Apontei a câmera para a porta e comecei a gravar o que, sem dúvidas, era o pior lugar da casa."
    t "O chão, que outrora havia sido branco, estava completamente encardido."
    t "A pia, ainda mais encardida que o azulejo. A privada também estava deplorável — dentro dela, podia-se ver uma água turva e densa."
    t "Aproximo a câmera da banheira, que felizmente não tinha água dentro."
    t "{cps=15}“Ok, terminei aqui.”{/cps}"
    d "{cps=15}“Ótimo, vamos indo.”{/cps}"
    t "David seguiu para a próxima porta."
    d "{cps=15}“E deixa isso aí aberto, para o ar circular um pouco.”{/cps}"

    jump salaReuniao

label salaReuniao:
    scene sala_reuniao:
        zoom 0.7
        yalign 1.0
    with pixellate
    play music "audio/Amb Sala de reunioes.ogg"
    show theo_camera_normal at right:
    show david_cel_normal at left:

    t "O próximo cômodo estava bem preservado em comparação com as outras partes da casa, apesar da sujeira."
    t "Apresentava um sofá e algumas poltronas, além de uma mesa circular com duas cadeiras."
    t "As janelas estavam fechadas com tábuas assim como as dos outros cômodos."
    d "{cps=15}“Fala no mapa que estamos na sala de reunião.”{/cps}"
    t "David olhou em volta."
    d "{cps=15}“É a melhorzinha que visitamos até agora.”{/cps}"
    t "Me aproximo do sofá e filmo um pouco."
    t "O cheiro não era exatamente agradável, mas em geral o móvel estava em bom estado."
    t "Viro a câmera para o David."
    d "{cps=15}“Galera, esse é o espaço que está bem mais preservado.”{/cps}"
    t "Ele caminhou até uma poltrona e sentou de maneira tensa, tomando cuidado para não sujar as roupas."
    d "{cps=15}“Parece que alguém vivia aqui recentemente.”{/cps}"
    d "{cps=15}“O que será que rolava aqui?”{/cps}"

    jump escritorio

label escritorio:
    scene office_closed_door:
        zoom 0.7
        yalign 0.1
    with pixellate
    play music "audio/Amb Escritorio.ogg"
    show theo_camera_surpreso at right:
    show david_cel_normal at left:

    t "Chegamos em uma porta fechada com um cadeado."
    d "{cps=15}“Epa.”{/cps}"
    t "David se aproximou e examinou o cadeado."
    d "{cps=15}“Parece um cadeado novo.”{/cps}"

    hide theo_camera_surpreso
    hide david_normal

    jump escritorio_fechado

label escritorio_fechado:
    scene office_cadeado:
        zoom 0.70

    t "Aproximei a câmera para mostrar melhor o ferrolho."
    t "{cps=15}“É daqueles que você precisa colocar a senha girando os números.”{/cps}"

    # Senha da logica da senha da porta
    python:
        senha_cadeado = renpy.input("Digite a senha de 4 números para abrir o cadeado", "", allow="0123456789", length=4)

    if str(senha_cadeado) == '4913':
        jump escritorio_aberto
    else:
        scene office_closed_door:
            zoom 0.70
        play music "audio/door-close.ogg" noloop
        show theo_normal at right:
        show david_bravo at left:


    d "{cps=15}“Cara, não é possível.”{/cps}"
    d "{cps=15}“A senha tem que estar por aqui, em algum papel, escrita na parede…”{/cps}"
    t "David olhou em volta."
    t "{cps=15}“Vamos ter que investigar melhor então.”{/cps}"

    jump corredor_escolha

    return

label quartoVisitaDireito_puzzle:
    scene quarto_visitaD:
        zoom 0.7
    with pixellate
    play music "audio/Amb quarto visita direito.ogg"
    play music "audio/upside down grin2.ogg"
    show theo_normal at right:
    show david_normal at left:

    t "{cps=15}“Vamos procurar alguma coisa que indique a senha do cadeado.”{/cps}"
    d "{cps=15}“Espera.”{/cps}"
    t "David avançou até o abajur na parede."
    d "{cps=15}“Esse abajur me chamou atenção mais cedo e vi sobre esses números. Ta escrito 1-4.”{/cps}"

    jump corredor_escolha

    return

label quarto_infantil_puzzle:
    scene quarto_infantil:
        zoom 0.70
        yalign 0.8
    with pixellate
    play music "audio/upside down grin2.ogg"
    show theo_normal at right:
    show david_normal at left:

    t "Vamos procurar alguma coisa que indique a senha do cadeado."
    t "Onde devo procurar?"

    jump quarto_infantil_puzzle_menu

    return

label quarto_infantil_puzzle_menu:
    scene quarto_infantil:
        zoom 0.70
        yalign 0.8
    play music "audio/upside down grin2.ogg"
    show theo_normal at right:
    show david_normal at left:
    menu:
        "Cama":
            t "Me aproximo da cama e tento ver se há algo que me chama atenção, mas não tem nada."
            jump quarto_infantil_puzzle_menu
        "Armário":
            t "Me aproximo do armário e abro ele, não há nada dentro."
            jump quarto_infantil_puzzle_menu
        "Brinquedos":
            t "Me aproximo dos brinquedos que estão no chão espalhados com um aspecto bem triste e destruído."
            t "Afastei algumas pelúcias para encontrar uma boneca que me chamou a atenção."
            t "Ela vestia uma roupinha amarela com os números 2-9. Acho que é isso."

    jump corredor_escolha

    return

label banheiro_puzzle:
    scene banheiro:
        zoom 0.67
    with pixellate
    play music "audio/upside down grin2.ogg"
    show theo_normal at right:
    show david_normal at left:

    d "{cps=15}“Cara, não vou entrar aí de jeito nenhum.”{/cps}"
    t "David me encarou seriamente."
    t "Suspirei. Alguém precisa fazer o trabalho sujo."
    t "Onde devo procurar?"

    jump banheiro_puzzle_menu

    return

label banheiro_puzzle_menu:
    scene banheiro:
        zoom 0.67
    play music "audio/upside down grin2.ogg"
    show theo_normal at right:
    show david_normal at left:
    menu:
        "Pia":
            t "Me aproximei da pia. Não percebi nada em particular além de muito musgo e sujeira. Estava nojento."
            jump banheiro_puzzle_menu
        "Banheira":
            t "Me aproximei da banheira. Parecia que nada me chamou a atenção, mas então notei uma placa pequena de ferro parafusada perto da torneira que contém os números 3-1."
        "Privada":
            t "Me aproximei da privada mas parece que foi uma péssima ideia. Ver de perto a água completamente suja e preta quase me fez golfar."
            jump banheiro_puzzle_menu

    jump corredor_escolha

    return

label quartoVisitaEsquerdo_puzzle:
    scene quarto_visitaE:
        zoom 0.7
        yalign 1.0
    with pixellate
    play music "audio/upside down grin2.ogg"
    show theo_normal at right:
    show david_normal at left:

    d "{cps=15}“Já dei uma olhada aqui e não achei nada que me chamou atenção.”{/cps}"
    d "{cps=15}“Bem, então vamos para o próximo.”{/cps}"

    jump corredor_escolha

    return

label despensa_puzzle:
    scene despensa:
        zoom 0.7
        yalign 1.0
    with pixellate
    play music "audio/upside down grin2.ogg"
    show theo_normal at right:
    show david_normal at left:

    d "{cps=15}“Já dei uma olhada aqui e não achei nada que me chamou atenção.”{/cps}"
    d "{cps=15}“Bem, então vamos para o próximo.”{/cps}"

    jump corredor_escolha

    return

label salaReuniao_puzzle:
    scene sala_reuniao:
        zoom 0.7
        yalign 1.0
    with pixellate
    play music "audio/upside down grin2.ogg"
    show theo_normal at right:
    show david_normal at left:

    d "{cps=15}“Já dei uma olhada aqui e não achei nada que me chamou atenção.”{/cps}"
    d "{cps=15}“Bem, então vamos para o próximo.”{/cps}"

    jump corredor_escolha

    return

label escritorio_puzzle:
    scene escritorio:
        zoom 0.7
        yalign 0.1
    with pixellate
    play music "audio/upside down grin2.ogg"
    show theo_normal at right:
    show david_normal at left:

    d "{cps=15}“Já dei uma olhada aqui e não achei nada que me chamou atenção.”{/cps}"
    d "{cps=15}“Bem, então vamos para o próximo.”{/cps}"

    jump corredor_escolha

    return

label escritorio_fechado_puzzle:
    scene office_cadeado:
        zoom 0.70

    # Senha da logica da senha da porta
    python:
        senha_cadeado = renpy.input("Digite a senha de 4 números para abrir o cadeado", "", allow="0123456789", length=4)

    if str(senha_cadeado) == '4913':
        scene office_closed_door:
            zoom 0.70
        show theo_feliz at right:
        show david_feliz at left:
        t "{cps=15}“Consegui!”{/cps}"
        d "{cps=15}“Eita, como?”{/cps}"
        t "David olhou por cima do meu ombro."
        d "{cps=15}“Pois aparentemente nós só tínhamos três números.”{/cps}"
        t "{cps=15}“Eu chutei o último.”{/cps}"
        t "Tirei o cadeado e o joguei ao lado da porta."
        t "{cps=15}“E aí, bora entrar?”{/cps}"
        d "{cps=15}“Só se for agora.”{/cps}"
        hide theo_normal
        show theo_camera_normal at right:
        with dissolve
        t "Troquei de lugar com o David e comecei a gravar."
        d "{cps=15}“Pessoal, essa porta estava fechada com cadeado mas conseguimos tirar.”{/cps}"
        t "David se prepara para abrir a porta."
        d "{cps=15}“Vamos ver o que tem lá dentro que precisou ser trancado assim.”{/cps}"

        jump escritorio_aberto_puzle
    else:
        scene office_closed_door:
            zoom 0.70
        play music "audio/door-close.ogg" noloop
        show theo_normal at right:
        show david_normal at left:

    d "{cps=15}“Cara, não é possível.”{/cps}"
    d "{cps=15}“A senha tem que estar por aqui, em algum papel, escrita na parede…”{/cps}"
    t "David olhou em volta."
    t "{cps=15}“Vamos ter que investigar melhor então.”{/cps}"

    jump corredor_escolha

    return

label escritorio_aberto:
    scene office_open_door:
        zoom 0.70
        yalign 1.0
    play music "audio/door-open.ogg" noloop
    t "Você acertou a senha, vamos entrar"

    jump escritorio_

label escritorio_aberto_puzle:
    scene office_open_door:
        zoom 0.70
    
    hide theo_camera_normal
    hide theo_camera_surpreso

    play music "audio/door-open.ogg" noloop
    
    t "E então, ele abriu a porta e entrou, eu o segui logo depois."

    jump escritorio_

label escritorio_:
    scene escritorio:
        zoom 0.7
        yalign 1.0
    with pixellate

    show theo_normal at right:
    show david_normal at left:

    t "Ao entrarmos, nos deparamos com um lugar muito escuro, imediatamente liguei o flash da câmera para iluminar."
    t "Dessa vez, as janelas não estavam apenas fechadas com tábuas, mas mas cada uma estava encoberta por cortinas grossas."
    t "Conforme o mapa, aquele era o escritório."
    t "A mesa gigante, com uma cadeira enorme e chique parecia confirmar a informação."
    t "David pegou a lanterna da minha mochila e iluminou as paredes."
    t "Nelas, encontramos vários papéis pregados sobre um mapa da cidade."
    t "{cps=15}“Que sinistro.”{/cps}"

    show theo_triste3 at right:
    with dissolve

    t "Com cautela, me aproximei da mesa, gravando cada canto que parecia interessante."
    t "Empurrei a cadeira, que rangeu bem alto, para acessar as gavetas do móvel."
    t "Abri uma por uma em busca de material para o nosso vídeo, até perceber que a última estava emperrada."
    t "Forcei o puxador, mas a gaveta não abriu."
    play music "audio/medo.ogg" volume 0.10
    t "Certo. Estava trancada. Comecei a procurar a chave na mesa."
    d "{cps=15}“Theo…”{/cps}"
    queue sound "audio/medo.ogg" volume 0.11
    t "David chamou, voltei minha atenção para ele."
    t "{cps=15}“Encontrou alguma coisa?”{/cps}"
    queue sound "audio/medo.ogg" volume 0.12
    t "Perguntei, me aproximando."
    queue sound "audio/medo.ogg" volume 0.13
    t "Ele apenas apontou a lanterna para o chão, onde havia um rastro vermelho, como se algo tivesse sido arrastado."
    d "{cps=15}“Isso é o que eu tô pensando?”{/cps}"
    queue sound "audio/medo.ogg" volume 0.14
    t "David seguiu o rastro com a lanterna até uma porta."
    t "Engoli seco."
    queue sound "audio/medo.ogg" volume 0.15
    t "{cps=15}“Vou ir abrir.”{/cps}"
    t "Disse, tomando coragem."
    queue sound "audio/medo.ogg" volume 0.16

    show david_surpreso at left:
    with dissolve

    queue sound "audio/medo.ogg" volume 0.17
    t "Adrenalina e medo moviam o meu corpo."
    t "Avancei até a porta e girei a maceta mais devagar do que gostaria."
    t "O que havia do outro lado da porta tirou completamente meu fôlego."
    t "Uma menina, pendurada pelo pescoço por uma corda, cuja a outra extremidade estava presa em uma haste de um equipamento que servia para pendurar roupas."
    t "O corpo, completamente dilacerado na barriga — um corte grotesco, pelo qual as tripas escapavam e uma poça de sangue enorme estava embaixo dela."
    t "Ainda escorriam algumas gotas de onde havia o corte."
    d "{cps=15}“Meu deus…..”{/cps}"
    t "David ofegou, em choque."
    t "Em seguida, escutei ele dando alguns passos para trás e vomitando."
    t "Precisei reunir uma coragem sobre-humana para olhar o rosto."
    t "Parece uma jovem da minha idade."
    t "Seus cabelos escuros e lisos estavam presos em uma trança que se desfazia perto das pontas."
    t "Tudo nela estava pálido, e seu olhar…"
    d "{cps=15}“A gente precisa…”{/cps}"
    t "David não conseguiu concluir a frase antes de golfar novamente."
    t "Foi então que algo me veio à mente."
    t "A parede cheia de papéis."

    show david_surpresao at left:
    with dissolve

    t "Corri para verificar e me deparei com diversas notícias de desaparecimento."
    t "Fotos de pessoas cujos rostos eu não conhecia, cartazes de procurados e manchetes de jornal de um serial killer à solta…"
    t "Espera…"
    t "Seria aquele serial killer que eu vi na notícia hoje cedo?!"
    t "{cps=15}“A gente precisa sair daqui…”{/cps}"
    t "Olhei para o David esperando uma resposta de fuga, mas ele parecia em choque."
    t "Segurei seu braço e comecei a puxar em direção à porta, desesperado."
    t "{cps=15}“Cara, vamos logo, a gente precisa ir embora.”{/cps}"
    show theo_tristao at right:
    with dissolve
    t "De repente um barulho de porta rangendo e logo em seguida um baque ecoou por toda a casa."
    t "Parei de caminhar."
    t "Minha boca estava completamente seca."
    t "Uma sensação de pânico tomou conta do meu corpo."
    hide david_surpresao
    with dissolve
    t "Apertei o braço de David e olhei para ele."
    t "Passos começaram a ecoar em toda a casa, pesados e lentos."
    t "Nós temos tempo ainda."
    t "PRECISAMOS NOS ESCONDER!"

    stop sound
    stop music fadeout 1.0

    jump continua

label continua:
    scene continua:
    with pixellate
    play music "audio/upside down grin2.ogg"

    t "{cps=15}“Continua...”{/cps}"

return

label corredor_escolha:
    call screen corredor
    if _return == "quartoVisitaDireito_puzzle":
        jump quartoVisitaDireito_puzzle
    elif _return == "quartoVisitaEsquerdo_puzzle":
        jump quartoVisitaEsquerdo_puzzle
    elif _return == "quarto_infantil_puzzle":
        jump quarto_infantil_puzzle
    elif _return == "despensa_puzzle":
        jump despensa_puzzle
    elif _return == "banheiro_puzzle":
        jump banheiro_puzzle
    elif _return == "escritorio_fechado_puzzle":
        jump escritorio_fechado_puzzle
    elif _return == "escritorio_puzzle":
        jump escritorio_puzzle

screen corredor:
    imagemap:
        ground "images/corredor_escolha.png"
        hotspot(335, 169, 84, 80) action Return("quartoVisitaEsquerdo_puzzle")
        hotspot(501, 268, 64, 55) action Return("despensa_puzzle")
        hotspot(568, 336, 57, 55) action Return("quarto_infantil_puzzle")
        hotspot(851, 171, 83, 76) action Return("quartoVisitaDireito_puzzle")
        hotspot(722, 273, 71, 57) action Return("banheiro_puzzle")
        hotspot(675, 342, 55, 43) action Return("escritorio_fechado_puzzle")
