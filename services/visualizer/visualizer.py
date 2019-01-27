# import required classes

from PIL import Image, ImageDraw, ImageFont

# create Image object with the input image

image = Image.open('background.png')

# initialise the drawing context with
# the image object as background

def generateImage(profName, courses, rating, approval, average, passing):
    draw = ImageDraw.Draw(image)
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    # import required classes

    # initialise the drawing context with
    # the image object as background

    draw = ImageDraw.Draw(image)

    # create font object with the font file and specify
    # desired size

    font = ImageFont.truetype('BEBAS.TTF', size=45)
    smallFont = ImageFont.truetype('BEBAS.TTF', size=21)
    mediumFont = ImageFont.truetype('BEBAS.TTF', size = 36)

    # starting position of the message

    (x, y) = (33, 117)
    color = 'rgb(255, 255, 255)'  # black color

    # draw the message on the background
    draw.text((x, y), profName, fill=color, font=font)

    (x, y) = (35, 175)
    draw.text((x, y), courses, fill=color, font=smallFont)

    (x, y) = (275, 290)
    rating = rating + '/5'
    draw.text((x, y), rating, fill=color, font=mediumFont)

    (x, y) = (275, 365)
    approval = approval + '%'
    draw.text((x, y), approval, fill=color, font=mediumFont)

    (x, y) = (27, 518)
    rawInt = int(average.strip('%'))
    averageString = ""
    for i in range(rawInt//2):
        averageString = averageString + "|"
    draw.text((x, y+3), averageString, fill=color, font=smallFont)
    draw.text((x + 270, y+1), average, fill=color, font=smallFont)
    # save the edited image

    rawInt = int(passing.strip('%'))
    passingString = ""
    for i in range(rawInt//2):
        passingString = passingString + "|"
    draw.text((x, y+80), passingString, fill=color, font=smallFont)
    draw.text((x + 270, y+78), passing, fill=color, font=smallFont)

    image.save('profStats.png')

generateImage("Gregor Kiczales", "CPSC 110", '3.2', '82', '80%', "94%")