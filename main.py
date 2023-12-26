from track import Track
#from ai import AI
from human import Human
from kart import Kart

# La chaine de caractere decrivant le terrain
string = """GGGGGGGGGGGGGGGGGGGGGGGGGG
GRRRRRRCRRRRRRRRRBRRRRRRRG
GRRRRRRCRRRRRRRRRBRRRRRRRG
GRRRRRRCRRRRRRRRRRRRRRRRRG
GRRRRRRCRRRRRRRRRRRRRRRRRG
GGGGGGGGGGGGGGGGGGGGGRRRRG
GGGGGGGGGGGGGGGGGGGGGRRRRG
GRRRRGGGGGGGGGGGGGGGGRRRRG
GFFRRGGGGGGGGGGGGGGGGRRRRG
GLRRRGGGGGGGGGGGGGGGGRRRRG
GRRRRGGGGGGGGGGGGGGGGDDDDG
GRRRRRERRRRRRRBRRRRRRRRLLG
GRRRRRERRRRRRRBRRRRRRRRRRG
GLRRRRERRRRRGGBRRRRRRRRRRG
GLLRRRERRRRRGGBRRRRRRRRRRG
GGGGGGGGGGGGGGGGGGGGGGGGGG"""

# La position et l'orientation initiale du kart
initial_position = [75, 75]
initial_angle = 0

controller =  Human()  # ou AI()
"""
==================== ATTENTION =====================
Vous ne devez pas modifier ces quatre lignes de code 
====================================================
"""
kart = Kart(controller)
track = Track(string, initial_position, initial_angle)

# -----------AJOUT------------
# Récupère les dimensions de la fenêtre de jeu depuis la classe Track à la classe Kart
kart.set_track_dimensions(track.width, track.height)

# Récupère la liste des objets de track depuis la classe Track à la classe Kart
kart.set_track_objects(track.track_objects)
# ---------FIN AJOUT----------

track.add_kart(kart)
track.play()

"""
====================================================
"""
