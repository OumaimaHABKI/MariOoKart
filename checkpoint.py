from surface import Surface

class Checkpoint(Surface): # Hérite de la classe Surface
    
    def __init__(self, x, y, checkpoint_id):
        """
        Constructeur 
        
        :params : x, y, checkpoint_id (integer) : position du bloc checkpoint et numéro du checkpoint
            
        """
        super().__init__(x, y, color=(255, 200, 0)) # constructeur hérité de Surface
        self.__checkpoint_id = checkpoint_id # numéro du checkpoint
        self.__saved_position = [75, 75] # position sauvegardée au passage d'un checkpoint
        self.__saved_orientation = 0 # orientation sauvegardée au passage d'un checkpoint
        
    """
    ========================= METHODES DE CHECKPOINT ===========================
    """
    def affect_kart(self, kart):
        """
        Cette methode vérifie que le kart passe le bon checkpoint et met à jour next_checkpoint.
        
        :param kart (Kart): objet kart
        
        """
        if self.__checkpoint_id == kart.next_checkpoint:
            self.__save_position(kart)  
            if self.__is_last_checkpoint():
                kart.has_finished = True
            else:
                kart.next_checkpoint += 1
                
    
    def __save_position(self, kart):
        """
        Cette methode garde en mémoire la position et l'orientation du kart au passage du ckeckpoint.
        
        :param kart (Kart): objet kart
        
        """
        kart.saved_position = kart.position[:]
        kart.saved_orientation = kart.orientation
        
        
    def __is_last_checkpoint(self): 
        """
        Cette methode vérifie si le kart passe sur le dernier checkpoint.
        
        :returns: un booléen
        
        """
        if self.__checkpoint_id == 3:
            return True
        return False
            
    """
    ========================= FIN DES METHODES DE CHECKPOINT =========================
    """