from surface import Surface

ROAD_FRICTION = 0.02

class Road(Surface): # Hérite de la classe Surface
    
    def __init__(self, x, y):
        """
        Constructeur 
        
        :params : x, y (integer) : position du bloc road
            
        """
        super().__init__(x, y, (128, 128, 128)) # constructeur hérité de Surface
        
    
    """
    ========================= METHODE DE ROAD ===========================
    """
    
    def affect_kart(self, kart):
        """
        Cette methode met à jour le coefficient de friction de road
        
        :param kart (Kart): objet kart
        
        """
        kart.friction_coef = ROAD_FRICTION
        
    """
    ========================= FIN METHODE DE ROAD ========================
    """