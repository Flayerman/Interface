import pygame
import pytmx
import pyscroll
pygame.init()

class Player :
    def __init__(self):
        super().__init__()
        self.health =100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('Player1.png')
        self.rect = self.image.get_rect()


class Game:
    def __init__(self):
        # Creer la fenetre du jeu
        self.screen = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("Pygamon - Aventure")

        # Charger map
        tmx_data = pytmx.util_pygame.load_pygame('Map1poke.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        # Dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

        # Charger notre joueur
        player = Player()
    def run(self):
        # Boucle du jeu
        running = True
        while running:
            screen.blit(player.image)
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()