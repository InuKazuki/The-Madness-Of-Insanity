define je = Character("Jenny")
define ydialogo = Character("Yuri", image="ydialogo")
define yu = Character("Yuri")
define ju = Character("Julia")
image rua = "images/fundorua.png"
image side ydialogo = "yuritela.png"
image bg carro = "images/carro.png"


label start:

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
