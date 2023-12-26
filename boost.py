from surface import Surface

BOOST_VELOCITY = 25

class Boost(Surface): # Hérite de la classe Surface
    
    def __init__(self, x, y):
        """
        Constructeur 
        
        :params : x, y (integer) : position du bloc boost
            
        """
        super().__init__(x, y, (0, 255, 255)) # constructeur hérité de Surface
        
    """
    ========================= METHODE DE BOOST ===========================
    """
        
    def affect_kart(self,kart):
        """
        Cette methode met à jour la vitesse du kart.
        
        :param kart (Kart): objet kart
        
        """
        kart.velocity = BOOST_VELOCITY
        
    """
    ========================= FIN METHODE DE BOOST =========================
    """