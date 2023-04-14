import tkinter as tk
from PIL import ImageGrab

def snip():
    # Capture the screen
    im = ImageGrab.grab()
    # Show the image
    im.show()

# Create a GUI window



root = tk.Tk()
root.title("Snipping Tool")

# Create a "Snip" button
snip_button = tk.Button(root, text="Snip", command=snip)
snip_button.pack()

# Run the GUI event loop
root.mainloop()