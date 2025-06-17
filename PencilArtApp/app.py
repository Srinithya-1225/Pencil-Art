import cv2
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

# Function to convert image to pencil sketch
def convert_to_sketch():
    filepath = filedialog.askopenfilename()
    if not filepath:
        return

    # Read and process the image
    img = cv2.imread(filepath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(gray)
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    inverted_blur = cv2.bitwise_not(blurred)
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)

    # Save the sketch
    output_path = os.path.splitext(filepath)[0] + "_sketch.jpg"
    cv2.imwrite(output_path, sketch)

    # Display the sketch in the GUI
    sketch_img = Image.fromarray(sketch)
    sketch_img = sketch_img.resize((300, 300))
    imgtk = ImageTk.PhotoImage(sketch_img)
    panel.config(image=imgtk)
    panel.image = imgtk

    result_label.config(text=f"✅ Sketch saved to:\n{output_path}")

# Setup GUI window
root = Tk()
root.title("🎨 Pencil Art App")
root.geometry("400x450")
root.resizable(False, False)

Label(root, text="🖼️ Pencil Art Generator", font=("Helvetica", 16, "bold")).pack(pady=10)

Button(root, text="Choose Image & Convert", command=convert_to_sketch, bg="blue", fg="white", padx=10, pady=5).pack(pady=10)

panel = Label(root)
panel.pack(pady=10)

result_label = Label(root, text="", font=("Helvetica", 10), wraplength=350, justify="center")
result_label.pack(pady=10)

root.mainloop()
