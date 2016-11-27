from PIL import Image, ImageDraw

def draw_grid(img):
    pixels = img.load()
    width = img.size[0]
    height = img.size[1]

    draw = ImageDraw.Draw(img)
    draw.rectangle([width*0.1, height*0.1, width*0.9, height*0.9], outline=0, fill=0xFFFFFF)
    

board = Image.new('RGB', (600, 600), "white")

draw_grid(board)

board.save("board.png")
