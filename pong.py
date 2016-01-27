# RJ CHING

import pygame
import random

pygame.init()

display_width = 640
display_height = 480

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PONG')
clock = pygame.time.Clock()
FPS = 90

pygame.mixer.init()
bounce_sound = pygame.mixer.Sound("Bounce.wav")
jump_sound = pygame.mixer.Sound("Jump.wav")

def check_collision(player_x_position, player_y_position, player_width, player_height, box_x_position, box_y_position, box_size, box_speed):
    if player_x_position > box_x_position + box_size or player_x_position + player_width < box_x_position or player_y_position > box_y_position + box_size or player_y_position + player_height < box_y_position:
        return False
    else:
        bounce_sound.play()
        return True


def game_loop():
    paddle_width = 10
    paddle_height = 100
    player_one_x_position = 20
    player_one_y_position = 20
    player_one_direction = "STATIONARY"
    player_one_change = 0
    player_two_x_position = 600
    player_two_y_position = 20
    player_two_direction = "STATIONARY"
    player_two_change = 0
    player_speed = 10

    box_size = 20
    normal_speed = 3
    fast_speed = 6
    box_speed = normal_speed
    box_x_direction = random.randint(1, 2)
    box_y_direction = random.randint(3, 4)
    box_x_position = display_width/2
    box_y_position = display_height/2
    box_change_x = 0
    box_change_y = 0

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_exit = True

                if event.key == pygame.K_w:
                    player_one_change = -player_speed
                    player_one_direction = "UP"
                elif event.key == pygame.K_s:
                    player_one_change = player_speed
                    player_one_direction = "DOWN"

                if event.key == pygame.K_UP:
                    player_two_change = -player_speed
                    player_two_direction = "UP"
                elif event.key == pygame.K_DOWN:
                    player_two_change = player_speed
                    player_two_direction = "DOWN"

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player_one_change = 0
                    player_one_direction = "STATIONARY"

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_two_change = 0
                    player_two_direction = "STATIONARY"

        if box_x_direction == 1:
            box_change_x = -box_speed
        elif box_x_direction == 2:
            box_change_x = box_speed

        if box_y_direction == 3:
            box_change_y = -box_speed
        elif box_y_direction == 4:
            box_change_y = box_speed

        if box_x_position <= 0:
            box_speed = 3
            bounce_sound.play()
            box_x_direction = 2
            box_change_x = -box_change_x
        elif box_x_position + box_size >= display_width:
            box_speed = 3
            bounce_sound.play()
            box_x_direction = 1
            box_change_x = -box_change_x

        if box_y_position <= 0:
            bounce_sound.play()
            box_y_direction = 4
            box_change_y = -box_change_y
        elif box_y_position + box_size >= display_height:
            bounce_sound.play()
            box_y_direction = 3
            box_change_y = -box_change_y

        box_x_position += box_change_x
        box_y_position += box_change_y

        player_one_y_position += player_one_change
        player_two_y_position += player_two_change

        if player_one_y_position <= 0:
            player_one_y_position = 0
        elif player_one_y_position + paddle_height >= display_height:
            player_one_y_position = display_height - paddle_height

        if player_two_y_position <= 0:
            player_two_y_position = 0
        elif player_two_y_position + paddle_height >= display_height:
            player_two_y_position = display_height - paddle_height

        if check_collision(player_one_x_position, player_one_y_position, paddle_width, paddle_height, box_x_position, box_y_position, box_size, box_speed):
            box_x_direction = 2
            box_speed = 3
            if player_one_direction is "UP":
                box_y_direction = 3
                box_speed = 9
            elif player_one_direction is "DOWN":
                box_y_direction = 4
                box_speed = 9

        if check_collision(player_two_x_position, player_two_y_position, paddle_width, paddle_height, box_x_position, box_y_position, box_size, box_speed):
            box_x_direction = 1
            box_speed = 3
            if player_two_direction is "UP":
                box_y_direction = 3
                box_speed = 9
            elif player_two_direction is "DOWN":
                box_y_direction = 4
                box_speed = 9


        game_display.fill((71, 122, 66))
        game_display.fill((255, 255, 255), rect=[display_width/2, 0, 10, display_height])
        game_display.fill((255, 224, 59), rect=[box_x_position, box_y_position, box_size, box_size])
        game_display.fill((255, 255, 255), rect=[player_one_x_position, player_one_y_position, paddle_width, paddle_height])
        game_display.fill((255, 255, 255), rect=[player_two_x_position, player_two_y_position, paddle_width, paddle_height])

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


game_loop()
