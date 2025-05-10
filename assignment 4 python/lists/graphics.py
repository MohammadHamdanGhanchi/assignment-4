import tkinter as tk

# Constants for the canvas and cells
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase(event):
    """Erase any cells that the eraser touches."""
    x1 = event.x - ERASER_SIZE // 2
    y1 = event.y - ERASER_SIZE // 2
    x2 = x1 + ERASER_SIZE
    y2 = y1 + ERASER_SIZE

    for item in canvas.find_overlapping(x1, y1, x2, y2):
        canvas.itemconfig(item, fill='white')  # Change color to white to erase

# Setting up the main application window
root = tk.Tk()
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
canvas.pack()

# Create a grid of blue cells
for row in range(CANVAS_HEIGHT // CELL_SIZE):
    for col in range(CANVAS_WIDTH // CELL_SIZE):
        x1 = col * CELL_SIZE
        y1 = row * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='')

# Create eraser binding
canvas.bind('<Motion>', erase)

# Start the main event loop
root.mainloop()
