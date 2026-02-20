from PIL import Image

# percorso del PNG originale
input_png = "img/testomaestro.png"

# percorso dell'ICO da creare
output_ico = "img/testomaestro.ico"

img = Image.open(input_png)

img.save(
    output_ico,
    format="ICO",
    sizes=[(16,16), (32,32), (48,48), (256,256)]
)

print("ICO creato con successo!")