from PIL import Image, ImageDraw


def rounded_image(size=(110, 76), radius=15, color="#000000"):
    img = Image.new("RGB", size, color)

    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)

    draw.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=255)

    img.putalpha(mask)
    return img


def round_corners(img, radius=50):
    img = img.convert("RGBA")  # important

    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)

    draw.rounded_rectangle(
        (0, 0, img.size[0], img.size[1]),
        radius=radius,
        fill=255
    )

    img.putalpha(mask)
    return img