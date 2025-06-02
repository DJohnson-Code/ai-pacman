import pygame  # Main Pygame library for handling graphics and events
import pygame.locals  # Access constants like QUIT, KEYDOWN, etc.
import constants  # Import our custom constants (screen size, colors, etc.)


# GameController controls the setup, update loop, and basic window logic
class GameController:
    def __init__(self):
        pygame.init()  # Initialize all imported Pygame modules
        # Create the game window with specified screen size
        self.screen = pygame.display.set_mode(constants.SCREENSIZE, 0, 32)
        self.background = None  # Placeholder for the background surface
        self.clock = pygame.time.Clock()  # Ensure consistent frame rate

    # Sets up the background color/surface
    def setBackground(self):
        # Create a Surface object that fills the screen size
        self.background = pygame.surface.Surface(constants.SCREENSIZE).convert()
        # Fill it with black (as defined in constants.py)
        self.background.fill(constants.BLACK)

    # Called once when the game starts
    def startGame(self):
        self.setBackground()  # Setup the background (currently black)

    # This runs every frame (like a heartbeat for the game)
    def update(self):
        dt = self.clock.tick(30) / 1000.0
        self.checkEvents()  # Handle user input or window close
        self.render()  # Redraw the screen

    # Checks for Pygame events like quitting the game
    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                exit()  # Exit the game if the window's close (X) is clicked

    # Draws everything to the screen (currently just refreshes the display)
    def render(self):
        pygame.display.update()  # Update the entire display


# Main entry point of the program
if __name__ == "__main__":
    game = GameController()  # Create a new instance of the game
    game.startGame()  # Initialize background, setup
    while True:  # Infinite game loop
        game.update()  # Keep updating events and rendering the screen
