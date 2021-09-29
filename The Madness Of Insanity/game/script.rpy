define je = Character("Jenny")
define ydialogo = Character("Yuri", image="ydialogo", who_color="#0302ff")
define yu = Character("Yuri", who_color="#0302ff")
define ju = Character("Julia", who_color="#8aefe8")
define n = Character(" ")
image rua = "images/fundorua.png"
image side ydialogo = "yuritela.png"
image bg carro = "images/carro.png"


label start:

    scene black

    n "Tudo está escuro"

    scene rua

    ydialogo "Aquele carro, eu quero ele!"

    call screen rua

    if _return == "carro":
        jump carro

label carro:
    hide bg rua
    scene bg carro:
    with dissolve

    show yurinormal

    yu "Baita carro"

    hide yurinormal
    show julianormal

    ju "abababab"

    hide julianormal
    return

screen rua:
    imagemap:
        ground "images/ground.png"
        hover "images/hover.png"

        hotspot(756, 294, 49, 69) action Return("carro")
