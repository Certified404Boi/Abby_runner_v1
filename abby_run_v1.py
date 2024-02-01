import pgzrun
# ^^^ remove this part if your running with command line

# import the randint function
from random import randint

# define the actors
player = Actor('walk1')
level = Actor('grass')
level2 = Actor('grass')
spike = Actor('spike')

# screen size
WIDTH = 400
HEIGHT = 500

# variables that control the game
speedy = 0
level_speed = 10
player.pos = 100, 200
level.pos =200, 420
level2.pos =600, 420
spike.pos = 1000, 300
updates = 0
score = 0
score2 = 0

# these variables control th menu and game over screen
game_over = False
menu = True   

# this function draws everything onscreen
def draw():
	screen.fill('blue')
	if game_over:
		screen.draw.text('GAME OVER', center=(200, 200), color='red', fontsize=80)
		
		level.draw()
		level2.draw()
	elif menu:
		screen.draw.text('Abby Runner 1.0', center=(200, 40), fontsize=60)
		player.draw()
		level.draw()
		level2.draw()
		screen.draw.text('Press SPACE to start', center=(200, 290), fontsize=40)
	else:
		level.draw()
		level2.draw()
		player.draw()
		spike.draw()
		screen.draw.text('SCORE: ' + str(score), topleft=(10, 10))

# this is themain game loop
def update():
	# make the variables global
	global speedy, updates, level_speed,score, game_over, menu, score2

	# menu controls
	if menu:
		if keyboard.space:
			menu = False
	else:
		# game loop
		speedy += 1
		player.y += speedy
		if player.colliderect(level) or player.colliderect(level2):
			player.y -= round(speedy)
			speedy = 0
			if keyboard.space:
				speedy = -18
				
		level.x -= level_speed
		level2.x -= level_speed
		spike.x -= level_speed
		if level.x < -200:
			level.x += 800
		if level2.x < -200:
			level2.x += 800
		if spike.x < -50:
			spike.x = randint(350, 1000)
			level_speed += 0.25
			score += 1

		if updates < 3:
			updates += 1
		else:
			updates = 0
			if player.image == 'walk1':
				player.image = 'walk2'
			else:
				player.image = 'walk1'
				
		if player.collidepoint(spike.x, spike.y):
			game_over = True
pgzrun.go()
# ^^^ remove this too if you run on the command line
