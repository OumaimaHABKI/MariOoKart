import pygame
import math

MAX_ANGLE_VELOCITY = 0.05
MAX_ACCELERATION = 0.25
BLOCK_SIZE = 50


class Kart:
    def __init__(self, controller): 
        """
        Constructeur 
        
        :params : controller(Human)
            
        """
        self.controller = controller
        self.has_finished = False
        
    # Attributs impactant le mouvement du kart
        self.__position = [0, 0]  # (x, y) composantes position
        self.__velocity_coord = [0, 0]  # (vx, vy) composantes de la vitesse
        self.__velocity = 0 # vitesse
        self.__orientation = 0  # Angle theta
        self.__previous_orientation = 0  # Angle theta(t - 1)
        self.__acceleration = 0  # accélération
        self.__ac = 0 # accélération ac
        self.__friction_coef = 0 # coefficient de friction
        
    # Attributs de la taille de la fenêtre du jeu
        self.__track_width = 0
        self.__track_height = 0
        
    # Attribut pour stocker la listes des objets composant le track
        self.__track_objects = None
        
    # Attributs pour le fonctionnement de checkpoint
        self.__next_checkpoint = 0 # Prochain checkpoint à atteindre
        self.__saved_position = [75, 75] # position sauvegardée au passage d'un checkpoint
        self.__saved_orientation = 0 # orientation sauvegardée au passage d'un checkpoint
    
    """
    ========================= LES PROPERTIES ===========================
    """
    
    @property 
    def position(self): # Position récupérée dans Checkpoint
        return self.__position
    
    @position.setter 
    def position(self, new_position): # Position mise à jour dans Lava
        self.__position = new_position
        
    @property 
    def orientation(self): # Orientation récupérée dans Checkpoint
        return self.__orientation
    
    @orientation.setter 
    def orientation(self, new_orientation): # Orientation mise à jour dans Lava
        self.__orientation = new_orientation
        
    @property
    def friction_coef(self): # Permet d'implémenter le setter
        return self.__friction_coef
    
    @friction_coef.setter
    def friction_coef(self, new_friction_coef): # Coef de friction mis à jour dans Road et Grass
        self.__friction_coef = new_friction_coef
    
    @property 
    def velocity(self): # Permet d'implémenter le setter
        return self.__velocity
    
    @velocity.setter
    def velocity(self, new_velocity): # Vitesse mise à jour dans Boost
        self.__velocity = new_velocity
        
    @property 
    def velocity_coord(self): # Permet d'implémenter le setter
        return self.__velocity_coord
    
    @velocity_coord.setter
    def velocity_coord(self, new_velocity_coord): # Coordonnées de la vitesse mise à jour dans Lava
        self.__velocity_coord = new_velocity_coord
    
    @property 
    def next_checkpoint(self): # checkpoint suivant récupéré dans Checkpoint
        return self.__next_checkpoint
    
    @next_checkpoint.setter 
    def next_checkpoint(self, value): # checkpoint suivant mis à jour dans Checkpoint
        self.__next_checkpoint = value
        
    @property 
    def saved_position(self): # Position enregistrée récupérée dans Lava
        return self.__saved_position
    
    @saved_position.setter
    def saved_position(self, new_saved_position): # Position enregistrée mise à jour dans Checkpoint
        self.__saved_position = new_saved_position
    
    @property 
    def saved_orientation(self): # Orientation enregistrée récupérée dans Lava
        return self.__saved_orientation
    
    @saved_orientation.setter
    def saved_orientation(self, new_saved_orientation): # Orientation enregistrée mise à jour dans Checkpoint
        self.__saved_orientation = new_saved_orientation

    """
    ========================= FIN DES PROPERTIES =========================
    """


    """
    ========================= METHODES DE KART ===========================
    """

    def set_track_dimensions(self, width, height):
        """
        Cette methode récupère les dimensions du track.
        
        :params width et height (Integer): valeurs des dimensions de la fenêtre de jeu
            
        """
        self.__track_width = width
        self.__track_height = height
    
        
    def set_track_objects(self, track_objects):
        """
        Cette methode récupère la liste des objets composant le track.
        
        :param track_objects (Surface[1*...]): Liste des objets du track
        
        """
        self.__track_objects = track_objects
    
    
    def reset(self, initial_position, initial_orientation):
        """
        Cette methode remet les paramètres du kart à l'état initial

        :param initial_position (integer[2]) et initial_orientation (real): Position et orientation initales du kart 
        
        """
        
        self.__position = list(initial_position)
        self.__orientation = initial_orientation
        self.__previous_orientation = initial_orientation
        self.__velocity_coord = [0, 0]
        self.__velocity = 0
        self.__acceleration = 0

    """
    --------------------- Méthodes régissant les 4 directions du kart ------------------------
    """
    def forward(self):
        # Avance en modifiant l'accélération
        self.__ac = MAX_ACCELERATION

    def backward(self):
        # Recule en modifiant l'accélération
        self.__ac = - MAX_ACCELERATION
        
    def turn_left(self):
        # Tourne à gauche en diminuant l'angle d'orientation
        self.__orientation = self.__previous_orientation - MAX_ANGLE_VELOCITY

    def turn_right(self):
        # Tourne à droite en augmentant l'angle d'orientation
        self.__orientation = self.__previous_orientation + MAX_ANGLE_VELOCITY
        
    """
    -------------------------------------------------------------------------------------------
    """
            
    def update_position(self, string, screen):
        """
        Cette methode définit la dynamique du jeu.

        :param string (String) et screen : chaîne de caractère définissant le track et son affichage.
        
        """
        
        # Récupération des commandes du controller
        keys = self.controller.move(string)
        
        # Vérifie si les commandes forward et backward sont activées en même temps ou si aucune ne le sont
        if (keys[pygame.K_UP] and keys[pygame.K_DOWN]) or (not keys[pygame.K_UP] and not keys[pygame.K_DOWN]):
            self.__ac = 0
        
        # EQUATIONS DU MOUVEMENT DEFINIES DANS LE SUJET (première version)
        
        # Calcul de theta(t-1)
        self.__previous_orientation = math.atan2(self.__velocity_coord[1], self.__velocity_coord[0])
        
        # Calcul de |v(t-1)|
        magnitude = math.hypot(self.__velocity_coord[0], self.__velocity_coord[1])
        
        # Calcul de a(t)
        self.__acceleration = self.__ac - self.__friction_coef * magnitude * math.cos(self.__orientation - self.__previous_orientation)
        
        # Calcul de v(t)
        self.__velocity += self.__acceleration 
         
        # Calcul de vx(t) et vy(t)
        self.__velocity_coord[0] = self.__velocity * math.cos(self.__orientation)
        self.__velocity_coord[1] = self.__velocity * math.sin(self.__orientation)
        
        # Vérifie sur quel type de surface le kart se trouve et modifie les paramètres en conséquence
        surface = self.__get_surface_type()
        if surface:
            surface.affect_kart(self)
                    
        # Met à jour la position x(t) et y(t)
        self.__position[0] += int(self.__velocity_coord[0])
        self.__position[1] += int(self.__velocity_coord[1])
        
        # Vérifie que le kart se trouve dans la fenêtre du jeu
        self.__check_boundaries()
        
        
    def __check_boundaries(self):
        """
        Cette methode vérifie que le kart se trouve dans la fenêtre et le ramène au dernier checkpoint validé s'il en sort.'
        
        """
        
        out_of_bounds = (
            self.position[0] < 0 or 
            self.position[0] > self.__track_width or 
            self.position[1] < 0 or 
            self.position[1] > self.__track_height
        )
        if out_of_bounds:
            self.__position = self.__saved_position[:]
            self.__orientation = self.__saved_orientation
            self.__velocity_coord = [0, 0]
            
            
    def __get_surface_type(self):
        """
        Cette methode vérifie sur quel type de surface le kart se situe.
        
        :returns: surface : objet sur lequel le kart se trouve.
    
        """
        if self.__track_objects is None:
            return None  # Or handle it in another appropriate way
        for surface in self.__track_objects:
            if self.__is_on_surface(surface):
                return surface
        return None


    def __is_on_surface(self, surface):
        """
        Cette methode calcule les limites d'un bloc de surface et vérifie si le kart se trouve sur ce bloc'

        :param surface: bloc de surface
        :returns: Un booléen
           
        """
        
        left_bound = surface.x_pos
        right_bound = surface.x_pos + BLOCK_SIZE
        top_bound = surface.y_pos
        bottom_bound = surface.y_pos + BLOCK_SIZE

        # Kart's position
        kart_x, kart_y = self.__position

        # Check if the kart is within the bounds of the surface
        if left_bound <= kart_x < right_bound and top_bound <= kart_y < bottom_bound:
            return True
        return False
        
    
    def draw(self, screen):
       """
       Cette methode dessine le kart en un cercle

       :param screen: affichage de la fenêtre de jeu
        
       """
       # Définition de la couleur du kart
       kart_color = (255, 100, 0)
       kart_radius = 20

       # Position du kart
       kart_position = (int(self.__position[0]), int(self.__position[1]))

       # Dessine le cercle représentatn le kart à sa position actuelle
       pygame.draw.circle(screen, kart_color, kart_position, kart_radius)
       
       # Paramètres du nez du kart
       nose_color = (255, 255, 255)  
       nose_length = 15
       nose_end_position = (
       kart_position[0] + nose_length * math.cos(self.__orientation),
       kart_position[1] + nose_length * math.sin(self.__orientation)
       )

       # Position du nez du kart
       nose_end_position = (int(nose_end_position[0]), int(nose_end_position[1]))

       # Dessine le cercle représentant le nez du kart
       pygame.draw.circle(screen, nose_color, nose_end_position, 5)
       
       """
       =========================FIN DES METHODES DE KART ===========================
       """