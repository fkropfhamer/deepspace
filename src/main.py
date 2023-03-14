import pygame

def main():
	pygame.init()
	pygame.display.set_caption("deepspace")
	screen = pygame.display.set_mode((400, 400))
	running = True

	screen.fill((255, 255, 255))
	pygame.draw.circle(screen, (0, 0, 0), (100, 100), 30)
	pygame.display.update()


	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		

if __name__ == "__main__":
	main()
