import pygame
import math

# Initialize pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

def draw():
    screen.fill((0, 0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Eye positions
    left_eye_x = 150
    left_eye_y = 200
    right_eye_x = 350
    right_eye_y = 200

    # Calculate distances
    left_distance_x = mouse_x - left_eye_x
    left_distance_y = mouse_y - left_eye_y
    right_distance_x = mouse_x - right_eye_x
    right_distance_y = mouse_y - right_eye_y

    # Calculate angles
    left_angle = math.atan2(left_distance_y, left_distance_x)
    right_angle = math.atan2(right_distance_y, right_distance_x)

    # Calculate pupil positions
    pupil_distance = 15
    left_pupil_x = left_eye_x + pupil_distance * math.cos(left_angle)
    left_pupil_y = left_eye_y + pupil_distance * math.sin(left_angle)
    right_pupil_x = right_eye_x + pupil_distance * math.cos(right_angle)
    right_pupil_y = right_eye_y + pupil_distance * math.sin(right_angle)

    # Draw eyes
    pygame.draw.circle(screen, (255, 255, 255), (left_eye_x, left_eye_y), 50)
    pygame.draw.circle(screen, (255, 255, 255), (right_eye_x, right_eye_y), 50)

    # Draw pupils
    pygame.draw.circle(screen, (0, 0, 100), (left_pupil_x, left_pupil_y), 15)
    pygame.draw.circle(screen, (0, 0, 100), (right_pupil_x, right_pupil_y), 15)

    # Draw mouth
    mouth_width = 200
    mouth_height = 50
    mouth_x = 250
    mouth_y = 300

    if mouse_y < mouth_y:
        # Smile
        start_angle = math.radians(45)
        end_angle = math.radians(135)
    else:
        # Sad
        start_angle = math.radians(225)
        end_angle = math.radians(315)

    pygame.draw.arc(screen, (255, 255, 255), 
    (mouth_x - mouth_width // 2, mouth_y - mouth_height // 2,
     mouth_width, mouth_height), start_angle, end_angle, 5)
# Run until the user asks to quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw everything
    draw()

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()