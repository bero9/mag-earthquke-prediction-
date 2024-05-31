import pygame
import importing_Data as id
import Linear_regression as LG
import Decision_Tree as DT
import matplotlib.pyplot as plt
import KNN as KN
pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Earthquke Predection")

background_color = (255, 255, 255)  # RGB values for white
screen.fill(background_color)

button_width = 200
button_height = 50
button_color = (0, 128, 0)  # RGB values for green
button_text_color = (255, 255, 255)  # RGB values for white
button_font = pygame.font.Font(None, 32)  # Font for button text


# Define different game screens or states
SCREEN_MAIN_MENU = 0
SCREEN_DAT_INTERFACE = 1
SCREEN_LinearRegression_INTERFACE = 2
SCREEN_DecisionTree_INTERFACE = 3
SCREEN_Show_Data_INTERFACE = 4
SCREEN_KNN_INTERFACE=5
# Initialize the current screen

current_screen = SCREEN_MAIN_MENU



def ImportingData():
    data = id.ImportingData()
    return data
def KNN_button_action():
    global current_screen
    current_screen = SCREEN_KNN_INTERFACE

def import_data_action():
    global current_screen

    current_screen = SCREEN_Show_Data_INTERFACE


def OK_Bottom_action():
    global current_screen
    current_screen = SCREEN_DAT_INTERFACE


def Linear_regression_action():
    global current_screen
    current_screen = SCREEN_LinearRegression_INTERFACE


def Decesion_tree_action():
    global current_screen
    current_screen = SCREEN_DecisionTree_INTERFACE



def Compare_accuracy_action():
    models = ["linear regression", "decision tree", "knn"]
    accuracies = [0.4584097443549777, 0.6059615148472124, 0.7643756510746718]
    plt.bar(models, accuracies, color='maroon',
            width=0.25)
    plt.xlabel("Models")
    plt.ylabel("Accuracies")
    plt.title("Accuracy Comparison Graph")
    plt.show()


def draw_button(x, y, text, action):
    button_rect = pygame.Rect(x, y, button_width, button_height)

    pygame.draw.rect(screen, button_color, button_rect)

    text_surface = button_font.render(text, True, button_text_color)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    if button_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0] == 1:
            action()


def draw_main_menu():
    text_surface = button_font.render(
        f"Welcome !! ", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2-320, height // 2-250))
    screen.blit(text_surface, text_rect)
    text_surface = button_font.render(
        f" Let's calculate the strength of the earthquake depending on :", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2-50, height // 2-200))
    screen.blit(text_surface, text_rect)
    text_surface = button_font.render(
        f" the depth, longitude and latitude", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2-150, height // 2-150))
    screen.blit(text_surface, text_rect)


    text_surface = button_font.render(
        f"First : Let's fetch the data from the database and print the first five rows", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2, height // 2 + 100))
    screen.blit(text_surface, text_rect)
    button11_x = width // 2 - button_width // 2
    button11_y = height // 2 - button_height // 2 + 200
    button11_text = "Importing Data"
    draw_button(button11_x, button11_y, button11_text, import_data_action)


def draw_SCREEN_DAT_INTERFACE():
    text_surface = button_font.render(
        f" Choose one of the algorithms you want to implement", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2, height // 2 - 200))
    screen.blit(text_surface, text_rect)
    text_surface = button_font.render(
        f" You can see the accuracy for each algorithm", True, (0, 0, 0))
    text_rect = text_surface.get_rect(
        center=(width // 2-150, height // 2 + 200))
    screen.blit(text_surface, text_rect)

    button1_x = width // 2 - button_width // 2
    button1_y = height // 2 - button_height // 2 - 100

    button2_x = width // 2 - button_width // 2
    button2_y = height // 2 - button_height // 2

    button3_x = width // 2 - button_width // 2
    button3_y = height // 2 - button_height // 2 + 100

    button4_x = width // 2 - button_width // 2 - 250
    button4_y = height // 2 - button_height // 2 + 250

    button1_text = "LinearRegression"
    button2_text = "Decision Tree"
    button3_text = "KNN Model"
    button4_text = "Compare Accuracy"

    draw_button(button1_x, button1_y, button1_text, Linear_regression_action)
    draw_button(button2_x, button2_y, button2_text, Decesion_tree_action)
    draw_button(button3_x, button3_y, button3_text, KNN_button_action)
    draw_button(button4_x, button4_y, button4_text, Compare_accuracy_action)


def draw_SCREEN_LinearRegression_INTERFACE():
    global input_fields
    global input_texts
    # Clear the screen
    screen.fill((255, 255, 255))
    text_surface = button_font.render(
        f"depth", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2+50, height // 2-232))
    screen.blit(text_surface, text_rect)
    text_surface = button_font.render(
        f"Latitude", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2+50, height // 2-182))
    screen.blit(text_surface, text_rect)
    text_surface = button_font.render(
        f"Longitude", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2+50, height // 2-132))
    screen.blit(text_surface, text_rect)

    # Draw the input fields
    for i, input_field in enumerate(input_fields):
        pygame.draw.rect(screen, (0, 0, 0), input_field)
        input_text = font.render(input_texts[i], True, (255, 255, 255))
        screen.blit(input_text, (input_field.x + 5, input_field.y + 5))

    # Draw the button
    button_rect = pygame.Rect(50, 200, 100, 50)
    button_text = font.render("Pred", True, (255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), button_rect)
    screen.blit(button_text, (button_rect.x + 25, button_rect.y + 15))

    text_surface = button_font.render(
        f"magnitudo of your earthquake will appear here:", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2-140, height // 2+100))
    screen.blit(text_surface, text_rect)

    text_surface = button_font.render(
        f"{final_pred[-1][0]}", True, (255, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2+225, height // 2+100))
    screen.blit(text_surface, text_rect)
    # Update the display
    pygame.display.flip()


def draw_SCREEN_DecisionTree_INTERFACE():

    global input_fields
    global input_texts
    # Clear the screen
    screen.fill((255, 255, 255))
    text_surface = button_font.render(
        f"depth", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2+50, height // 2-232))
    screen.blit(text_surface, text_rect)
    text_surface = button_font.render(
        f"Latitude", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2+50, height // 2-182))
    screen.blit(text_surface, text_rect)
    text_surface = button_font.render(
        f"Longitude", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2+50, height // 2-132))
    screen.blit(text_surface, text_rect)

    # Draw the input fields
    for i, input_field in enumerate(input_fields):
        pygame.draw.rect(screen, (0, 0, 0), input_field)
        input_text = font.render(input_texts[i], True, (255, 255, 255))
        screen.blit(input_text, (input_field.x + 5, input_field.y + 5))

    # Draw the button
    button_rect = pygame.Rect(50, 200, 100, 50)
    button_text = font.render("Pred", True, (255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), button_rect)
    screen.blit(button_text, (button_rect.x + 25, button_rect.y + 15))

    text_surface = button_font.render(
        f"magnitudo of your earthquake will appear here:", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2-140, height // 2+100))
    screen.blit(text_surface, text_rect)

    text_surface = button_font.render(
        f"{final_pred[-1][0]}", True, (255, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2+225, height // 2+100))
    screen.blit(text_surface, text_rect)
    # Update the display
    pygame.display.flip()

def draw_SCREEN_KNN_INTERFACE():

    global input_fields
    global input_texts
    # Clear the screen
    screen.fill((255, 255, 255))
    text_surface = button_font.render(
        f"depth", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2+50, height // 2-232))
    screen.blit(text_surface, text_rect)
    text_surface = button_font.render(
        f"Latitude", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2+50, height // 2-182))
    screen.blit(text_surface, text_rect)
    text_surface = button_font.render(
        f"Longitude", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2+50, height // 2-132))
    screen.blit(text_surface, text_rect)

    # Draw the input fields
    for i, input_field in enumerate(input_fields):
        pygame.draw.rect(screen, (0, 0, 0), input_field)
        input_text = font.render(input_texts[i], True, (255, 255, 255))
        screen.blit(input_text, (input_field.x + 5, input_field.y + 5))

    # Draw the button
    button_rect = pygame.Rect(50, 200, 100, 50)
    button_text = font.render("Pred", True, (255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), button_rect)
    screen.blit(button_text, (button_rect.x + 25, button_rect.y + 15))

    text_surface = button_font.render(
        f"magnitudo of your earthquake will appear here:", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2-140, height // 2+100))
    screen.blit(text_surface, text_rect)

    text_surface = button_font.render(
        f"{final_pred[-1][0]}", True, (255, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2+225, height // 2+100))
    screen.blit(text_surface, text_rect)
    # Update the display
    pygame.display.flip()


def draw_SCREEN_Show_Data_INTERFACE(data):
    text_surface = button_font.render(
        f"Well!! let's apply one of our machine learning algorithms", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2, height // 2 - 200))
    screen.blit(text_surface, text_rect)

    numerical_columns = ["magnitudo", "depth", "latitude", "longitude"]
    data_numeric = data[numerical_columns]

    text_surface = button_font.render(
        f" {data_numeric.head()}", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2, height // 2))
    screen.blit(text_surface, text_rect)
    button1_x = width // 2 - button_width // 2 + 200
    button1_y = height // 2 - button_height // 2 + 200
    button1_text = "OK!"
    draw_button(button1_x, button1_y, button1_text, OK_Bottom_action)


# Define a flag to track if a button action is triggered
button_action_triggered = False

# Set up the fonts
font = pygame.font.Font(None, 32)

button_rect = pygame.Rect(50, 200, 100, 50)
# Set up the input fields
input_fields = [
    pygame.Rect(50, 50, 300, 30),
    pygame.Rect(50, 100, 300, 30),
    pygame.Rect(50, 150, 300, 30)
]
input_texts = ["", "", ""]
# Set up the button
button_text = pygame.font.Font(None, 32).render("Print", True, (255, 255, 255))
# Add a new variable to store the predicted values:
predicted_values = []
final_pred = [" "]
#set the data 
data = ImportingData()
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            for i, input_field in enumerate(input_fields):
                if input_field.collidepoint(pygame.mouse.get_pos()):
                    if event.key == pygame.K_BACKSPACE:
                        input_texts[i] = input_texts[i][:-1]
                    else:
                        input_texts[i] += event.unicode

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                # Print the input field values in the terminal
                predicted_value1 = input_texts[0]
                predicted_value2 = input_texts[1]
                predicted_value3 = input_texts[2]

                # Store the predicted values in the list
                predicted_values = [predicted_value1,
                                    predicted_value2, predicted_value3]
                
                if(current_screen==SCREEN_LinearRegression_INTERFACE):
                    final_pred.append(LG.LinearRegresionBottom(data, predicted_values))
                if(current_screen==SCREEN_DecisionTree_INTERFACE):
                    final_pred.append(DT.DecisionTreeBottom(data, predicted_values))
                if(current_screen==SCREEN_KNN_INTERFACE):
                    final_pred.append(KN.KNeighborsBottom(data, predicted_values))

    screen.fill(background_color)

    if current_screen == SCREEN_MAIN_MENU:
        draw_main_menu()

    elif (current_screen == SCREEN_DAT_INTERFACE):
        draw_SCREEN_DAT_INTERFACE()

    elif (current_screen == SCREEN_LinearRegression_INTERFACE):
        
        draw_SCREEN_LinearRegression_INTERFACE()

    elif (current_screen == SCREEN_DecisionTree_INTERFACE):
        
        draw_SCREEN_DecisionTree_INTERFACE()
    elif (current_screen == SCREEN_Show_Data_INTERFACE):
        draw_SCREEN_Show_Data_INTERFACE(data)
    elif (current_screen == SCREEN_KNN_INTERFACE):
        draw_SCREEN_KNN_INTERFACE()
    pygame.display.flip()  # Update the display

pygame.quit()  # Quit Pygame
