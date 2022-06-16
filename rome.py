import pygame, random, time

BLACK = (0, 0, 0)
WHITE = (255,255,255)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
METEORS = 200
MAX_LIFE = 5
METEORS2 = 50
score_value = 0
player_speed = 5
laser_speed = 7
POTIONS = 30
class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load(random.choice(["mask2.png","mask2.png","medusa2.png","medusa2.png"])).convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
	def update(self, player_speed):
		#self.rect.x += sum(random.choices([0,-1], weights=(70,30),k=1))
		self.rect.x -= random.randrange(0, max(2, int((score_value +20)/10))) #- random.randint(-1, abs(player_speed))
		self.rect.y += random.randrange(0,2)
		if self.rect.x > SCREEN_WIDTH or self.rect.x < 0:
			self.rect.x = SCREEN_WIDTH
		if self.rect.y > SCREEN_HEIGHT:
			self.rect.y = 0
		if self.rect.y < 0:
			self.rect.y = SCREEN_HEIGHT

class Potion(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load(random.choice(["red_potion2.png", "blue_potion2.png"])).convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
	def update(self, player_speed):
		#self.rect.x += sum(random.choices([0,-1], weights=(70,30),k=1))
		self.rect.x -= random.randrange(-1, 2)
		self.rect.y += random.randrange(0,2)
		if self.rect.x > SCREEN_WIDTH or self.rect.x < 0:
			self.rect.x = SCREEN_WIDTH
		if self.rect.y > SCREEN_HEIGHT:
			self.rect.y = 0
		if self.rect.y < 0:
			self.rect.y = SCREEN_HEIGHT


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.attack_animation = False
		self.image = pygame.transform.scale(pygame.image.load("barco_griego2.png"), (100, 100)).convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.speed_x = 0
		self.speed_y = 0

	def changespeed(self, x, y):
		self.speed_x += x
		self.speed_y += y

	def update(self, player_speed):
		if self.rect.x < 0:
			self.rect.x = SCREEN_WIDTH
		elif self.rect.x > SCREEN_WIDTH:
			self.rect.x = 0
		else:
			self.rect.x += self.speed_x
		if player.rect.y > SCREEN_HEIGHT:
			player.rect.y = 0
		elif player.rect.y < 0:
			player.rect.y = SCREEN_HEIGHT
		else:
			player.rect.y -= self.speed_y
		

class Laser(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("tidente2.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()

	def update(self, player_speed):
		self.rect.x += laser_speed


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

background = pygame.transform.scale(pygame.image.load("fondo_acropolis.webp"), (SCREEN_WIDTH, SCREEN_HEIGHT)).convert()
pygame.mixer.music.load("gods.mp3")
pygame.mixer.music.play(-1)

meteor_list = pygame.sprite.Group()
meteor2_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
potion_list = pygame.sprite.Group()

for i in range(int(METEORS/2)):
	meteor = Meteor()
	meteor.rect.x = random.randrange(SCREEN_WIDTH - 300, SCREEN_WIDTH, random.randint(5,70))
	meteor.rect.y = random.randrange(0, SCREEN_HEIGHT, random.randint(5,70)) 

	meteor_list.add(meteor)
	all_sprite_list.add(meteor)
for i in range(int(METEORS/2)):
	meteor = Meteor()
	meteor.rect.x = random.randrange(SCREEN_WIDTH - 600, SCREEN_WIDTH + 400, random.randint(10,70))
	meteor.rect.y = random.randrange(0, SCREEN_HEIGHT, random.randint(10,70)) 

	meteor_list.add(meteor)
	all_sprite_list.add(meteor)

for i in range(POTIONS):
	potion = Potion()
	potion.rect.x = random.randrange(SCREEN_WIDTH - 1000, SCREEN_WIDTH, random.randint(5,70))
	potion.rect.y = random.randrange(0, SCREEN_HEIGHT, random.randint(5,70)) 

	potion_list.add(potion)
	all_sprite_list.add(potion)

player = Player()
all_sprite_list.add(player)

sound = pygame.mixer.Sound(random.choice(["planted1.wav", "planted2.wav","planted3.wav"]))
player.rect.x = 0
player.rect.y = 300
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.changespeed(-player_speed,0)
			if event.key == pygame.K_RIGHT:
				player.changespeed(player_speed,0)
			if event.key == pygame.K_UP:
				player.changespeed(0,player_speed)
			if event.key == pygame.K_DOWN:
				player.changespeed(0, -player_speed)
			if event.key == pygame.K_SPACE:
				laser = Laser()
				sound.play()
				laser.rect.x = player.rect.x + 45
				laser.rect.y = player.rect.y + 45

				laser_list.add(laser)
				all_sprite_list.add(laser)
				

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.changespeed(player_speed,0)
			if event.key == pygame.K_RIGHT:
				player.changespeed(-player_speed,0)
			if event.key == pygame.K_UP:
				player.changespeed(0,-player_speed)
			if event.key == pygame.K_DOWN:
				player.changespeed(0, player_speed)


	all_sprite_list.update(player.speed_x) 

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
		#pygame.mixer.Sound(random.choice(["punch.wav", "punch5.wav"])).play()
		life_value -= 1
		
	
	potion_hit_list = pygame.sprite.spritecollide(player, potion_list, True)
	if len(potion_hit_list)>0:
		pygame.mixer.Sound("potion.mp3").play()
		for potion in potion_hit_list:
			all_sprite_list.remove(potion)
			potion_list.remove(potion)
			life_value +=1
			score_value += 2

	#screen.fill([255, 255, 255])
	screen.blit(background, [0,0])
	all_sprite_list.draw(screen)
	show_score(10,10)
	show_life(10,50)

	pygame.display.flip()
	clock.tick(60)

pygame.quit()