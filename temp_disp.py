import board
import displayio
import time
from adafruit_st7789 import ST7789
from adafruit_display_text import label
import terminalio
from analogio import AnalogIn
import pwmio

BORDER = 20
FONTSCALE = 1
BACKGROUND_COLOR = 0x00FF00  # Bright Green
FOREGROUND_COLOR = 0xAA0088  # Purple
TEXT_COLOR = 0xFFFF00

# Release any previously configured displays
displayio.release_displays()

# Establish SPI interface
spi = board.SPI()
tft_cs = board.D2  # this is the CS pin you chose on the board
tft_dc = board.D3 # this is the DC pin you chose on the board
disp_bus = displayio.FourWire(spi, command = tft_dc, chip_select = tft_cs)
display = ST7789(disp_bus, rotation = 270, width = 240, height = 135, rowstart = 40, colstart = 53)

# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = BACKGROUND_COLOR

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(
    display.width - BORDER * 2, display.height - BORDER * 2, 1
)
inner_palette = displayio.Palette(1)
inner_palette[0] = FOREGROUND_COLOR
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

MAX_VALUE = 65535
temp = AnalogIn(board.A0)

while True:
    tempC = (temp.value / MAX_VALUE * 3.3 - 0.5) * 100
    tempF = (tempC * 9 / 5 + 32)
    print((tempC, tempF))
    time.sleep(5)
    text = "The Temperature is " + str(tempF)
    text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    text_width = text_area.bounding_box[2] * FONTSCALE
    text_group = displayio.Group(
        scale=FONTSCALE,
        x=display.width // 2 - text_width // 2,
        y=display.height // 2,
    )
    text_group.append(text_area)
    splash.append(text_group)

