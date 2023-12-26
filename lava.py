from surface import Surface

class Lava(Surface): # Hérite de la classe Surface
    
    def __init__(self, x, y):
        """
        Constructeur 
        
        :params : x, y (integer) : position du bloc lava
            
        """
        super().__init__(x, y, (255, 0, 0)) # constructeur hérité de Surface
        
    """
    ========================= METHODE DE LAVA ===========================
    """
    
    def affect_kart(self, kart):
        """
        Cette methode met à jour la postion et l'orientation du kart à la position et à l'orientation du dernier checkpoint validé
        
        :param kart (Kart): objet kart
        
        """
        kart.position = kart.saved_position[:]
        kart.orientation = kart.saved_orientation
        kart.velocity_coord = [0, 0]

    """
    ========================= FIN METHODE DE LAVA ===========================
    """