import pygame
import sys
import random

print("Hello World!")

# Inicjalizacja pygame
# pygame.init()

# # Ustawienia okna
# WIDTH, HEIGHT = 640, 480
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Prosty przykład Pygame")

# # Kolory
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)

# # Główna pętla gry
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill(WHITE)  # Wyczyść ekran na biało
#     pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 2), 50)  # Narysuj czerwone koło

#     pygame.display.flip()  # Aktualizuj ekran

# pygame.quit()
# sys.exit()


print("Guess the number!")
sekret = random.randint(1, 100)
proba = 0

while True:
    proba += 1
    guess = input("Number from 1 to 100: ")
    try:
        guess = int(guess)
    except ValueError:
        print("Pro tip: try numbers!")
        continue

    if guess < sekret:
        print("Too little!")
    elif guess > sekret:
        print("Too much!")
    else:
        print(f"Congrats! It took u {proba} tries.")
        break