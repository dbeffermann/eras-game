import pygame, random, time

BLACK = (0, 0, 0)
WHITE = (255,255,255)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
METEORS = 100
MAX_LIFE = 5
METEORS2 = 50

class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load(random.choice(["mask2.png","medusa2.png"])).convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
	def update(self):
		#self.rect.x += sum(random.choices([0,-1], weights=(70,30),k=1))
		self.rect.x -= random.choice([0,0,1])
		self.rect.y += random.choice([0,0,1])
		if self.rect.x > SCREEN_WIDTH or self.rect.x < 0:
			self.rect.x = SCREEN_WIDTH
		if self.rect.y > SCREEN_HEIGHT:
			self.rect.y = 0

class Meteor2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("momia2.png").convert()
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
	def update(self):
		#self.rect.x += sum(random.choices([0,-1], weights=(70,30),k=1))
		self.rect.x -= 1
		self.rect.y += random.choice([0,1])
		if self.rect.x > SCREEN_WIDTH or self.rect.x < 0:
			self.rect.x = SCREEN_WIDTH
		if self.rect.y > SCREEN_HEIGHT:
			self.rect.y = 0

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("barco_griego2.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()

	def update(self):
		mouse_pos = pygame.mouse.get_pos()
		player.rect.x = mouse_pos[0]
		player.rect.y = SCREEN_HEIGHT - 80

class Laser(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("laser.png").convert()
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y -= 9


pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
done = False
score_value = 0
life_value = MAX_LIFE
font = pygame.font.Font("freesansbold.ttf", 32)

def show_score(x,y):
	score = font.render(f"Score : {score_value}/{METEORS}", True, (255,255, 255))
	screen.blit(score, (x, y))

def show_life(x,y):
	score = font.render(f"Life: {life_value}/{MAX_LIFE}", True, (255,255, 255))
	screen.blit(score, (x, y))

background = pygame.image.load("greece2.jpeg").convert()
pygame.mixer.music.load("gods.mp3")
pygame.mixer.music.play(-1)

meteor_list = pygame.sprite.Group()
meteor2_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()

for i in range(METEORS):
	meteor = Meteor()
	meteor.rect.x = random.randrange(20, SCREEN_WIDTH - 20)
	meteor.rect.y = random.randrange(200) 

	meteor_list.add(meteor)
	all_sprite_list.add(meteor)

player = Player()
all_sprite_list.add(player)

sound = pygame.mixer.Sound("laser5.ogg")

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.MOUSEBUTTONDOWN:
			laser = Laser()
			laser.rect.x = player.rect.x + 45
			laser.rect.y = player.rect.y - 20

			laser_list.add(laser)
			all_sprite_list.add(laser)
			sound.play()


	all_sprite_list.update() 

	for laser in laser_list:
		meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True)	
		for meteor in meteor_hit_list:
			all_sprite_list.remove(meteor)
			meteor_list.remove(meteor)
			all_sprite_list.remove(laser)
			laser_list.remove(laser)
			score_value += 1
			print(score_value)
		if laser.rect.y < -10:
			all_sprite_list.remove(laser)
			laser_list.remove(laser)


	if pygame.sprite.spritecollide(player, meteor_list, True):
		pygame.mixer.Sound("explosion.wav").play()
		#score_value -= 1
		life_value -= 1
		if life_value <= 0:
			player.image = pygame.image.load("explosion2.png").convert()
			
			player.image.set_colorkey(BLACK)

	#screen.fill([255, 255, 255])
	screen.blit(background, [0,0])
	all_sprite_list.draw(screen)
	show_score(10,10)
	show_life(10,50)
	
	pygame.display.flip()
	clock.tick(60)

pygame.quit()