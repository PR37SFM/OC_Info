from PIL import Image

from Cacher import changeRGB, numeriser_message, liste_coordonnées_alea, cache_nombre_sur_une_colonne, cacher_message

from retrouver import decoder_message


def test_changeRGB_general():
    """
    Ce programme vérifie que pour une image test, toutes les valeurs R sont bien pair.
    """
    img = Image.open("img_test.png")
    for x in range(img.width):
        for y in range(img.height):
            changeRGB(img,x,y)
            color = img.getpixel((x,y))
            assert color[0]%2 == 0
    print("test_changeRGB ok")
    
    
test_changeRGB_general()

def test_changeRGB_cas_255():
    
    """
    Ce programme vérifie que lorsque la valeur de R est de 255, changeRGB marche quand même.
    """
    img = Image.open("img_test.png")
    img.putpixel((0,0),(255,255,255))
    changeRGB(img,0,0)
    color = img.getpixel((0,0))
    assert color[0]%2 == 0
    print("cas 255 de changeRGB ok")
    
test_changeRGB_cas_255()



def test_numeriser_message_general():
    
    """
    Vérifier que les changement entre valeur ascii et caractère ne change pas le message
    """
    message = numeriser_message("kstgsgrtgsr2734186012784gr^")
    message2 = ""
    for i in message:
        message2 += chr(i)
    assert message2 == "kstgsgrtgsr2734186012784gr^"
    print("numeriser_message ok")
        

test_numeriser_message_general()


def test_numeriser_message_precis():
    
    """
    Vérifier que la fonction numérise correctement différents caractères.
    """
    assert numeriser_message("0") == [48]
    assert numeriser_message("K") == [75]
    assert numeriser_message("a") == [97]
    assert numeriser_message("{") == [123]
    assert numeriser_message("%") == [37]
    
    print("numeriser_message semble ok")
    
test_numeriser_message_precis()
    
    
def test_liste_coordonnées_alea():
    """
    Vérifie que chaque coordonnées léatoire que la fonction choisi est bien dans l'intervalle voulue (hauteur de l'image)
    Et vérifie qu'il y a le bon nombre de coordonnées en comparant la longueur de la liste.
    """
    img = Image.open("img_test.png")
    les_y = liste_coordonnées_alea(img.height, 2)
    for i in les_y:
        assert i in range(img.height)
    assert len(les_y) == 2
    
    les_y2 = liste_coordonnées_alea(img.height, 14)
    for i in les_y2:
        assert i in range(img.height)
    assert len(les_y2) == 14
    
    les_y3 = liste_coordonnées_alea(img.height, 68)
    for i in les_y3:
        assert i in range(img.height)
    assert len(les_y3) == 68
    
    les_y4 = liste_coordonnées_alea(img.height, 270)
    for i in les_y4:
        assert i in range(img.height)
    assert len(les_y4) == 270
    
    print("liste_coordonnées_alea ok")
    

test_liste_coordonnées_alea()



def test_cache_nombre_sur_une_colonne():
    
    """
    Vérifie qu'il y a le bon nombre de R avec une valeur impair par colonne avec différents messsages.
    """
    img = Image.open("img_test.png")
    message = "Farouk"
    x = 2
    
    cache_nombre_sur_une_colonne(img,x,message)
    n_red_impair = 0
    largeur, hauteur = img.size
    for i in range(hauteur):
        red, green, blue,alpha = img.getpixel((x,i))
        if red%2 == 1:
            n_red_impair += 1    
    assert n_red_impair == ord(message[x])
    
    
    message2 = "Hello_World!"
    x2 = 7
    
    cache_nombre_sur_une_colonne(img,x2,message2)
    n_red_impair = 0
    largeur, hauteur = img.size
    for i in range(hauteur):
        red, green, blue,alpha = img.getpixel((x2,i))
        if red%2 == 1:
            n_red_impair += 1    
    assert n_red_impair == ord(message2[x2])
    
    
    message3 = "C'est un test, 1 + 1 = 0..."
    x3 = 17
    
    cache_nombre_sur_une_colonne(img,x3,message3)
    n_red_impair = 0 
    largeur, hauteur = img.size
    for i in range(hauteur):
        red, green, blue, alpha = img.getpixel((x3,i))
        if red %2 == 1:
            n_red_impair += 1
    assert n_red_impair == ord(message3[x3])
    
    message4 = "123 = 57/Farouk?"
    x4 = 12
    
    cache_nombre_sur_une_colonne(img,x4,message4)
    n_red_impair = 0 
    largeur, hauteur = img.size
    for i in range(hauteur):
        red, green, blue, alpha = img.getpixel((x4,i))
        if red %2 == 1:
            n_red_impair += 1
    assert n_red_impair == ord(message4[x4])


    print("cache_nombre_sur_une_colonne ok")


test_cache_nombre_sur_une_colonne()


def test_cacher_et_retrouver_message():
    
    """
    Vérifie que la méthode de cacher et retrouver le message ne change pas le message en cours de route.
    Donc on vérifie que la fonction cacher_message et decoder_message marche ensemble.
    """
    image_to_change = "img_test.png"
    image_changed = "test_changed.png"
    
    message1 = "test1"
    cacher_message(image_to_change,message1,image_changed)
    a = message1
    b = decoder_message(image_changed)[0:len(a)] # On est obligé de restreindre la longeur de b à a, car b contient techniquement une série de chr(0) pour le colonne sans R impair

    assert a == b
    
    message2 = "123 = + ?! CouCOu...::"
    cacher_message(image_to_change,message2,image_changed)
    a = message2
    b = decoder_message(image_changed)[0:len(a)] # On est obligé de restreindre la longeur de b à a, car b contient techniquement une série de chr(0) pour le colonne sans R impair

    assert a == b
    
    message3 = "Cddkcjsndckjifvaj lkmlskdcmsc"
    cacher_message(image_to_change,message3,image_changed)
    a = message3
    b = decoder_message(image_changed)[0:len(a)] # On est obligé de restreindre la longeur de b à a, car b contient techniquement une série de chr(0) pour le colonne sans R impair

    assert a == b
    
    message4 = "La phrase va vérifier quelque chose."
    cacher_message(image_to_change,message4,image_changed)
    a = message4
    b = decoder_message(image_changed)[0:len(a)] # On est obligé de restreindre la longeur de b à a, car b contient techniquement une série de chr(0) pour le colonne sans R impair

    assert a == b
    
    message5 = "Derniere essaye, Farouk va avoir 6."
    cacher_message(image_to_change,message5,image_changed)
    a = message5
    b = decoder_message(image_changed)[0:len(a)] # On est obligé de restreindre la longeur de b à a, car b contient techniquement une série de chr(0) pour le colonne sans R impair

    assert a == b
    print("cacher_message ok")
    
test_cacher_et_retrouver_message()