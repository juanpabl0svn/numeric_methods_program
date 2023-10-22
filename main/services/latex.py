from PIL import Image, ImageTk
import io
import matplotlib.pyplot as plt

def render_latex(formula, dpi=150):
    fig, ax = plt.subplots(figsize=(1.5, 0.3))  # Ajusta el tamaño según lo necesario
    ax.text(0, 0.5, "$%s$" % formula, size=8, ha='left', va='center', bbox=dict(pad=-0.1, facecolor='white'))
    ax.axis("off")

    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())

    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=dpi, bbox_inches='tight', pad_inches=0)
    plt.close(fig)
    buf.seek(0)
    
    img = Image.open(buf)
    
    photo = ImageTk.PhotoImage(image=img)

    return photo

# def display_latex_in_tkinter(root, formula):
#     img = render_latex(formula)
    
#     label = Label(root, image=photo)
#     label.image = photo
#     label.pack()

# if __name__ == "__main__":
#     root = tk.Tk()
#     display_latex_in_tkinter(root, r'\frac{\partial f}{\partial x} = 2\pi\int y dy')
#     root.mainloop()
