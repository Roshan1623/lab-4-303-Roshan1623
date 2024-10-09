import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

def set_color(color):
    for i in range(10):  
        pixels[i] = color
    pixels.show()

while True:
    print("\nMenu:")
    print("1. Set LEDs to Red")
    print("2. Set LEDs to Green")
    print("3. Set LEDs to Blue")
    print("Press 'q' to quit.")
    
    user_input = input("Enter your choice: ")
    
    if user_input == 'q':  
        print("You are out of the program")
        break

    try:
        choice = int(user_input)   

        if choice == 1:
            set_color((255, 0, 0))   
            print("LEDs set to Red.")
        elif choice == 2:
            set_color((0, 255, 0))   
            print("LEDs set to Green.")
        elif choice == 3:
            set_color((0, 0, 255))   
            print("LEDs set to Blue.")
        else:
            print("Invalid choice. Please select a number between 1 and 3.")

    except ValueError:
        print("That's not a valid choice. Please enter a number (1-3) or 'q' to quit.")
