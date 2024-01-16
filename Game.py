import pygame
import pytmx
import pyscroll
from Player import Player
pygame.init()
pygame.mixer.init()  # Initialiser le module mixer
pygame.mixer.music.load('Title.ogg')  # Charger la musique de fond

class Game:
    def __init__(self):
        # Creer la fenetre du jeu
        self.screen = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("Pygamon - Aventure")

        # Charger map
        tmx_data = pytmx.util_pygame.load_pygame('Map1poke.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        # Generer un joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x,player_position.y)

        # Jouer la musique en boucle indéfinie
        pygame.mixer.music.play(-1)

        # Définir une liste stock rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')

    def update(self):
        self.group.update()

        # vérification collision
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
               sprite.move_back()

    def run(self):
        clock =pygame.time.Clock()
        # Boucle du jeu
        running = True
        while running:
            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect.center)
            # self.screen.blit(self.player.sprite_sheet, self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            clock.tick(60)

        pygame.mixer.music.stop()
        pygame.quit()
