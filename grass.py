from surface import Surface

GRASS_FRICTION = 0.2

class Grass(Surface): # Hérite de la classe Surface
 
    def __init__(self, x, y):
        """
        Constructeur 
        
        :params : x, y (integer) : position du bloc grass
            
        """
        super().__init__(x, y, (0, 150, 0)) # constructeur hérité de Surface
        
    """
    ========================= METHODE DE GRASS ===========================
    """
   
    def affect_kart(self, kart):
        """
        Cette methode met à jour le coefficient de friction de grass
        
        :param kart (Kart): objet kart
        
        """
        kart.friction_coef = GRASS_FRICTION
        
    """
    ========================= FIN METHODE DE GRASS ========================
    """