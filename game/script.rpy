init python:
    import compression

define d = Character("David")
define t = Character("Theo")

image theo = "images/theo.png"
image david = "images/david.png"
image fundo = "images/room.png"
image garage = "images/garagem.jpg"
image rouxinol = "images/rouxinol.jpg"
image janela_direita = "images/janela_direita.jpg"
image janela_esquerda = "images/janela_esquerda.jpg"

label start:
    python:
        compression.compression('projects\\invasao_urbana\\game\\images')
        
    # ATO UM
    scene fundo

    play music "audio/upside down grin2.ogg"

    show theo at right:
        zoom 0.3

    t "É manhã de quarta-feira quando nos reunimos no quarto do David. O dia começou limpo mas começou a fechar em um nublado esbranquiçado."
    t "Não gostava desse clima, pois é sinal de uma provável chuva acontecer. Mas por mais que o tempo estivesse feio (para mim), estava sentado olhando distraidamente pela janela do quarto do meu amigo."
    t "Este mesmo que estava tagarelando sobre uma ideias de vídeo que vamos produzir."
    t "Temos um canal de vídeos para a internet há uns três anos. O David ficou fascinado pela ideia e bem, eu sou bom com tecnologia."
    t "Juntou o útil ao agradável (um extrovertido popular que gosta de falar e se expor com um introvertido nerd que manja minimamente de algumas coisas) e assim criamos o canal Nada de Ócio."
    t "Eu sei, o nome não é tão bom mas, dá um desconto! É melhor que muitos por aí. Fazemos vários tipos de vídeos: reações, vlogs da vida pessoal, jogando algo legal. É bem amplo nosso conteúdo, pois tentamos fazer o que gostamos sempre."

    show david at left:
        zoom 0.3
    with dissolve

    d "{cps=15}“Hey, Theo! Ah cara, você ta me escutando??”{/cps}"
    t "Virei o rosto para o David e ele parecia bem indignado."
    d "{cps=15}“Cara, preciso da sua ajuda! Não consigo mais pensar em nada!”{/cps}"
    t "Suspirei. Isso era um pouco ruim pois David sempre vinha com uma lista de coisas que podemos gravar."
    t "{cps=15}“Você sabe que eu não tenho ideias boas cara, não quer dar uma olhada na gringa?”{/cps}"
    d "{cps=15}“Não sei.”{/cps}"
    d "{cps=15}“Quero fazer algo mais original mas....”{/cps}"
    d "{cps=15}“pensa, pensa...”"
    t "Suspirei novamente e tirei meu celular do bolso. Comecei a rolar a página da internet que hospedava várias vídeos (inclusive os nossos) em busca de alguma ideia."
    t "Acabei me distraindo um pouco com um vídeo noticiário, informando sobre crimes que estão rolando na região."
    t "Fico um pouco preocupado, pois meu pai é detetive e soube que ele está encarregado de um caso sério. Arrastei para baixo para ler os comentários mas me deparei com vídeos relacionados."
    t "E estava lá. Um vídeo gringo de um grupo invadindo e explorando uma instalação abandonada."
    t "Ajeitei minha postura na cadeira e comecei a ver o vídeo concentrado."
    t "{cps=15}“Cara..”{/cps}"
    t "chamei e imediatamente David estava do meu lado."
    t "{cps=15}“Se liga nisso.”{/cps}"
    t "Ele pegou o celular das minhas mãos e começou a assistir. Logo levantou o olhar até mim."
    d "{cps=15}“Na rua Rouxinol tem uma casa abandonada muito sinistra...”{/cps}"
    t "{cps=15}“Sim, e lembro de não ter visto nem pichações na casa. O que será que rola por lá?”{/cps}"
    t "David deu um grande sorriso ao entregar o celular para mim."
    d "{cps=15}“Só tem uma maneira de descobrir.”{/cps}"
    d "{cps=15}“Vamos para garagem nos preparar.” {/cps}"

    jump garagem
    # ATO DOIS

    label garagem:
        hide fundo
        scene garage:
            zoom 2.0
        play music "audio/upside down grin2.ogg"
        show theo at right:
            zoom 0.3
        show david at left:
            zoom 0.3
        t "Estávamos na garagem da casa do David para nos prepararmos."
        t "Estava colocando o essencial na minha mochila: garrafas d’água, lanterna, algumas barrinhas de cereal e um sinalizador por acionamento."
        d "{cps=15}“Cara, a gente não vai acampar...”{/cps}"
        t "Me virei rapidamente para ver o David olhando por cima dos meus ombros as coisas que guardei na mochila."
        t "{cps=15}“Eu sei.”{/cps}"
        d "{cps=15}“Então pra quê tudo isso?”{/cps}"
        t "Comecei a verificar os equipamentos de gravação: câmera, microfone, bateria..."
        t "{cps=15}“A gente ta indo pra um local abandonado e do lado de uma floresta enorme, eu só to me preparando...”{/cps}"
        d "{cps=15}“Você é muito surtado...”{/cps}"
        t "Ele riu e voltou a atenção na sua mochila."
        t "Revirei os olhos. Quando terminei de verificar e guardar os equipamentos, me virei pro David. Ele estava se arrumando no espelho, fazendo caras e bocas."
        t "{cps=15}“Cara, a gente não vai se encontrar com a Poliana, você sabe né?”{/cps}"
        t "Ele se virou pra mim, sorrindo."
        d "{cps=15}“Sabe mesmo como se vingar. Tudo pronto?”{/cps}"
        t "{cps=15}“Sim, senhor.”{/cps}"
        t "David coloca a mochila nas costas e passa um braço por cima dos meus ombros, me conduzindo a caminhar."
        d "{cps=15}“Então, vamos.”{/cps}"

        jump rouxinol

        label rouxinol:
            hide garage
            scene rouxinol:
                zoom 2.0
            play music "audio/upside down grin2.ogg"
            show theo at right:
                zoom 0.3
            show david at left:
                zoom 0.3

            t "Já estava no meio da tarde quando caminhávamos pela rua. Ela se encontrava muito deserta, e bem suja. A vegetação era alta e tinha arame farpado entre o matagal intenso. "
            t "O caminho de barro seco seguia em uma subida que não era íngreme mas era extensa. "
            t "Já estava ofegante por causa de tudo que estava carregando (e pelo meu sedentarismo também). David estava um pouco mais a frente, fala distraidamente e seguiu sem perceber que estava ficando para trás."
            d "{cps=15}“Não, se liga: que tal, tipo, ‘casa mal assombrada’ ou ‘casa assombrada, encontramos algo?’. Um título com algo sobrenatural vai chamar a atenção..”{/cps}"
            t "{cps=15}“Podemos parar um pouco? Os equipamentos estão pesando.”{/cps}"
            d "{cps=15}“Oh, certo.”{/cps}"
            t "Comtemplamos a extensa visão do matagal alto e do céu cheio de nuvens. Já não estava mais tão nublado e o sol aparecia timidamente para iluminar."
            t "Peguei minha garrafa d’água e bebi um gole. Ofereci pro David, que aceitou alegremente. Até ele estava ficando cansado."
            t "{cps=15}“Ok.”{/cps}"
            t "Disse enquanto ajeitava a mochila nas minhas costas."
            t "{cps=15}“Bora lá, estamos quase chegando.”{/cps}"
            t "Caminhamos mais algum tempo até avistar o casarão. A aparência da casa lembrava da estética gótica medieval, uma escada que começava dividida e se juntava para levar a porta de entrada."
            t "A vegetação já tinha tomado conta de boa parte da casa, tinha algumas janelas quebradas, outras fechadas com tábuas de madeira por dentro."
            t "O lugar estava bem sujo e as arvores ao redor dava uma vibe assustadora. E realmente: nada de pichações."
            d "{cps=15}“Ah, é aqui.”{/cps}"
            t "Suspirou, David."
            t "Comecei a pegar o equipamento de gravação - a camera com uma light ring em cima dela - e o David já estava com o celular ajustado para ser o microfone."
            t "{cps=15}“Ok, tudo certo aqui.”{/cps}"
            t "Falei. Olhei para meu amigo e ele acenou para mim. Comecei a gravar."
            d "{cps=15}“Fala galera do mal, aqui é o David e vim trazer um vídeo interessantíssimo pra vocês!”{/cps}"
            d "{cps=15}“Essa casa aqui atrás da gente, pertenceu a uma família muito rica na região durante a década de 90, porém aconteceu uns casos SINISTROS aqui e falam agora que ela é mal assombrada.”{/cps}"
            d "{cps=15}“Então... Viemos aqui para investigar e saber se é real! E aí? Vamos juntos?”{/cps}"
            t "David se virou em direção a casa e começou a caminhar até ela."
            d "{cps=15}“Vamos investigar se há alguma maneira de entrar aqui.”{/cps}"
            d "{cps=15}“Cara, parece que ta tudo fechado...”{/cps}"
            t "Aponto a camera para as janelas do primeiro andar para conseguir uma visão melhor com o zoom e vejo que a janela do lado esquerdo está um pouco aberta. Talvez com um pouco de força possa abrir mas parece difícil de escalar até lá."
            t "Segui rodeando a casa para a direita enquanto o David ainda examinava as janelas do térreo."
            t "Percebi outra janela que tinha poucas tábuas de madeira e seria fácil tirar se conseguíssemos um pé de cabra por exemplo, porém pode fazer um barulhão e não sabemos se há realmente ninguém ai."
            t "O que eu faço?"

            menu:
                "Janela da esquerda":
                    jump esquerda
                "Janela da direita":
                    jump direita

            label esquerda:
                hide rouxinol
                scene janela_esquerda:
                    zoom 2.0
                play music "audio/upside down grin2.ogg"
                show theo at right:
                    zoom 0.3
                show david at left:
                    zoom 0.3

                t "{cps=15}“David, vem cá.”{/cps}"
                t "Falei um pouco mais alto, em alguns segundos ele chega."
                d "{cps=15}“Fala comigo, Theo.”{/cps}"
                t "{cps=15}“Olha lá em cima.”{/cps}"
                t "Apontei pra janela com poucas tábuas."
                t "{cps=15}“É fácil de escalar e as tábuas parecem frágeis, o que acha?”{/cps}"
                t "Ele analisa onde apontei e logo em seguida procura algo no chão."
                d "{cps=15}“Deve ter pelo menos uma pedrona aqui...”{/cps}"
                t "Me juntei a ele para procurar qualquer coisa que ajude a quebrar as tábuas. Acabei achando um pedaço de ferro parecido com um pé de cabra."
                t "{cps=15}“Aí, tenta isso.”{/cps}"
                t "Entreguei o objeto e David começou a escalar até a janela. Quando cheguei perto, já estava aberta."
                d "{cps=15}“Demorou hein?”{/cps}"
                t "David entrou e deixou o pedaço de ferro perto da janela, segui ele."
                t "Ele foi primeiro e o segui. Ao entrar, nos deparamos com um quarto de casal."
                t "Igualmente como o lado de fora, o estado do quarto estava deplorável e fedia a mofo por causa da cama."
                t "Peguei novamente minha câmera e comecei a gravar com o David já com o microfone pronto."
                d "{cps=15}“Conseguimos entrar na casa pelo primeiro andar. Aqui parece ser um quarto do casal que vivia aqui, então vamos continuar explorando.”{/cps}"
                t "Liguei o flash da câmera e segui filmando cada canto que podia até chegar na penteadeira ao lado da cama: havia vários produtos de beleza e cuidados porém um papel dobrado se destacava."
                t "{cps=15}“David, encontrei algo.”{/cps}"
                t "Ele parou ao meu lado e abriu o papel, revelando o mapa do segundo andar da casa."
                d "{cps=15}“Isso vai ser bom pra gente se orientar.”{/cps}"
                t "David continua a analisar o papel."
                d "{cps=15}“Olha, estamos aqui, lado esquerdo e na frente tem um quarto infantil. Vamos lá investigar.”{/cps}"
                t "O David saiu em disparada até a saída do quarto. Fui seguindo ele."

                jump corredor

            label direita:
                hide janela_esquerda
                scene janela_direita:
                    zoom 2.0
                play music "audio/upside down grin2.ogg"
                show theo at right:
                    zoom 0.3
                show david at left:
                    zoom 0.3

                t "{cps=15}“Hey, David.”{/cps}"
                t "Chamei ele, enquanto caminhava em sua direção."
                t "{cps=15}“O que acha daquela janela?”{/cps}"
                t "Aponto para janela acima de mim."
                t "{cps=15}“Parece fácil de abrir.”{/cps}"
                t "David analisa um pouco, e então começa a verificar como escalar até lá."
                d "{cps=15}“Vai ser difícil, mas realmente é uma entrada boa. Eu vou lá, se prepara pra escalar também.”{/cps}"
                t "Parei de gravar e guardei a câmera na mochila. O David já estava escalando e fui o seguindo. Escorreguei algumas vezes mas nada que comprometesse a escalada. Parei do lado dele ao chegar na janela."
                d "{cps=15}“Certo.”{/cps}"
                t "Ofegou ele."
                d "{cps=15}“Empurra desse lado que eu vou empurrar desse. No três vamos juntos.”{/cps}"
                t "Posicionei meu braço direito para empurrar a janela para cima."
                d "{cps=15}“Um... dois... três!”{/cps}"
                t "Começamos a empurrar juntos, a janela estava muito emperrada mas o lado que o David estava empurrando subiu primeiro e logo foi o meu lado. Com mais um pouco de força, abrimos a janela completamente."
                t "{cps=15}“Ah, ufa.”{/cps}"
                t "Suspirei aliviado."
                d "{cps=15}“Ih cara, cansou?”{/cps}"
                t "David soltou uma risadinha."
                d "{cps=15}“Bora, vamos entrar.”{/cps}"
                t "O quarto que estávamos tinha um aspecto infantil, com as paredes pintadas em um azul bebê porém completamente sujas pelo tempo e infiltração."
                t "Havia alguns brinquedos e pelúcias espalhados no chão e em algumas prateleiras. A cama infantil estava quebrada e com o colchão rasgado."
                t "Peguei minha câmera e comecei a gravar."
                d "{cps=15}“Cara...”{/cps}"
                d "{cps=15}“Aqui ta muito sinistro.”{/cps}"
                t "Ele se volta pra câmera com o microfone preparado."
                d "{cps=15}“Conseguimos entrar no primeiro andar, aqui é um quarto infantil com vários brinquedos. Vamos continuar explorando.”{/cps}"
                t "Eu sigo filmando o quarto em vários cantos, gravo a janela de onde viemos, gravo os brinquedos quebrados e as paredes desenhadas por alguma criança."
                d "{cps=15}“Aí cara, tem um quarto aqui na frente com a porta aberta. Entrei lá rapidão e achei esse mapa, não vamos ficar mais perdidos.”{/cps}"
                t "David me entregou o mapa e eu dei uma analisada."

                jump corredor

                label corredor:
                    hide janela_direita
                    #scene :
                        #zoom 2.0
                    play music "audio/upside down grin2.ogg"
                    show theo at right:
                        zoom 0.3
                    show david at left:
                        zoom 0.3

                    t "Saímos para o corredor do andar que estávamos. Estava bem precário e sujo assim como o resto da casa."
                    t "Além dos dois quartos que exploramos, tem mais três de cada lado. Estava escuro então ajustei a luz que está acima da câmera."
                    t "Começo a gravar o David."
                    d "{cps=15}“Galera, estamos no corredor do primeiro andar agora.”{/cps}"
                    t "Começou ele, quase sussurrando."
                    d "{cps=15}“Como podem ver, a casa ta toda esbagaçada e suja por causa do tempo.”{/cps}"
                    t "Gravei um pouco das paredes, do chão e então voltei para David."
                    d "{cps=15} “Há vários quartos que vamos explorar com mais cuidado, to bem curioso para saber o que tem lá.”{/cps}"
                    t "Ele se virou e seguiu para uma porta."

                    jump quartoVisidaEsquerdo

                    label quartoVisidaEsquerdo:
                        #hide janela_direita
                        #scene :
                            #zoom 2.0
                        play music "audio/upside down grin2.ogg"
                        show theo at right:
                            zoom 0.3
                        show david at left:
                            zoom 0.3

                        t "Ao entrarmos pela porta, nos deparamos com um quarto igualmente sujo e deplorável. Tinha uma cama de solteiro sem colchão e com aspecto enferrujado e um armário ."
                        t "As parede um dia era de uma cor branca foi consumida pela infiltração e sujeira."
                        t "A janela estava fechada com tábuas mas era possível ver a a luz passando pela fresta. Dei uma olhada para o David e ele estava distraído vendo algo perto do abajur na parede."

                        jump quartoVisidaDireito

                        label quartoVisidaDireito:
                            #hide janela_direita
                            #scene :
                                #zoom 2.0
                            play music "audio/upside down grin2.ogg"
                            show theo at right:
                                zoom 0.3
                            show david at left:
                                zoom 0.3

                            t "O quarto tinha uma cama de casal mais simples que a do quarto lá atrás."
                            t "Assim como toda a casa possivelmente, o quarto estava sujo e destruído e a janela do quarto estava totalmente tampada por tábuas."
                            t "O chão do quarto estava com rachaduras grotescas, sinto que se pisar ali posso cair junto o chão."
                            d "{cps=15}“Cara..”{/cps}"
                            t "Virei a câmera para David."
                            d "{cps=15}“Esse quarto aqui ta BEM acabado. E nem pensar em pisar nesse chão aí.”{/cps}"
                            t "Filmei melhor o chão, aproximando a imagem com o zoom."
                            t "{cps=15}“Melhor evitar de andar nesse lugar.”{/cps}"

                            jump despensa

                            label despensa:
                                #hide janela_direita
                                #scene :
                                    #zoom 2.0
                                play music "audio/upside down grin2.ogg"
                                show theo at right:
                                    zoom 0.3
                                show david at left:
                                    zoom 0.3

                                t "Desta vez o David foi na frente e abriu a porta. Parecia um armário apertado e tinha várias prateleiras com bolachas, pó de café, sachês de chá, doces..."
                                d "{cps=15}“Pelo mapa, aqui é a despensa...”{/cps}"
                                t "David olhou para o papel que estava em mãos."
                                d "{cps=15}“Estranho ter uma aqui em cima.”  {/cps}"
                                t "{cps=15}“E só coisas pra tomar aquele café da tarde...” {/cps}"
                                t "Aproximei a câmera em um produto."
                                t "{cps=15}“Todos vencidos, claro.”{/cps}"
                                t "Segui filmando a despensa."

                                jump banheiro

                                label banheiro:
                                    #hide janela_direita
                                    #scene :
                                        #zoom 2.0
                                    play music "audio/upside down grin2.ogg"
                                    show theo at right:
                                        zoom 0.3
                                    show david at left:
                                        zoom 0.3

                                    t "Ao abrir a próxima porta, um cheiro forte de esgoto invadiu nossas narinas. Nos afastamos um pouco pra sair desse cheiro."
                                    d "{cps=15}“Caralho...”{/cps}"
                                    t "David colocou a mão no nariz, o tampando."
                                    t "{cps=15}“É, a gente já devia ter esperado por isso.”{/cps}"
                                    d "{cps=15}“Eu não vou entrar aí não.”{/cps}"
                                    t "Ele se virou."
                                    d "{cps=15}“Grava um pouquinho aí e depois vamos pra próxima.”{/cps}"
                                    t "Comecei a gravar da porta e sem dúvidas era o pior lugar da casa. O chão que outrora foi branco está completamente sujo e encardido."
                                    t "A privada tem um aspecto horrível e dava para ver em como a água estava preta, a pia estava mais suja ainda e mais atrás tinha uma banheira que felizmente não tinha água dentro."
                                    t "{cps=15}“Ok, terminei aqui.”{/cps}"
                                    d "{cps=15}“Ótimo, vamos indo.”{/cps}"
                                    t "David foi seguindo para a próxima porta."
                                    d "{cps=15}“E não fecha isso aí, deixa o ar circular um pouco.”{/cps}"

                                    jump salaReuniao

                                    label salaReuniao:
                                        #hide banheiro
                                        #scene :
                                            #zoom 2.0
                                        play music "audio/upside down grin2.ogg"
                                        show theo at right:
                                            zoom 0.3
                                        show david at left:
                                            zoom 0.3

                                        t "A parte que entramos agora se encontrava até bem preservada em comparação com as outras, apesar de ainda estar bem suja."
                                        t "Tinha sofá e poltronas além de uma mesa circular com duas cadeiras. As janelas igualmente fechadas iguais as outras."
                                        d "{cps=15}“Fala no mapa que estamos na sala de reunião.”{/cps}"
                                        t "David olha em volta."
                                        d "{cps=15}“É a melhorzinha de todas que visitamos até então.”{/cps}"
                                        t "Me aproximei do sofá e o filmei um pouco, o cheiro não tava agradável mas em geral o móvel estava em bom estado. Virei a câmera para David."
                                        d "{cps=15}“Galera, esse é o espaço que está bem mais preservado.”{/cps}"
                                        t "Ele caminhou até uma poltrona e sentou de maneira tensa, como se não quisesse sujar as roupas."
                                        d "{cps=15}“Parece que alguém vivia aqui recentemente. O que será que rolava aqui?”{/cps}"

                                        jump escritorio

                                        label escritorio:
                                            #hide salaReuniao
                                            #scene :
                                                #zoom 2.0
                                            play music "audio/upside down grin2.ogg"
                                            show theo at right:
                                                zoom 0.3
                                            show david at left:
                                                zoom 0.3

                                            t "Chegamos em uma porta fechada com um cadeado."
                                            d "{cps=15}“Epa.”{/cps}"
                                            t "David se aproximou mais e examinou o cadeado. "
                                            d "{cps=15}“Parece um cadeado novo.”{/cps}"
                                            t "Aproximei a câmera para mostrar melhor o cadeado."
                                            t "{cps=15}“É daqueles que você precisa colocar a senha girando os números.”{/cps}"
                                            d "{cps=15}“Cara, não é possível isso. A senha tem que estar por aqui, em algum papel, escrita na parede?”{/cps}"
                                            t "David olhou em volta, como se a resposta estivesse em algum lugar do corredor do qual não vimos."
                                            t "{cps=15}“Vamos ter que investigar melhor então.”{/cps}"
                                            d "{cps=15}{/cps}"

    return
