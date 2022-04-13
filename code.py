import board, displayio, terminalio, keypad, rotaryio, neopixel, time, random
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
from adafruit_macropad import MacroPad

# Set up macropad variables
macropad = MacroPad()
keys = macropad.keys
pixels = macropad.pixels

# Clear the board
pixels.fill(0)

# Set up display & fonts
display = board.DISPLAY
title_font = bitmap_font.load_font("/fonts/Arial-Bold-12.bdf")
text_font = bitmap_font.load_font("/fonts/Arial-10.bdf")

# Menu display
title = label.Label(title_font, text="", color=0xFFFFFF)
title.anchor_point = (0.0, 0.0)
title.anchored_position = (0, 0)

menu = displayio.Group()
menu.append(title)

# Set up Main Display. Add and remove groups from this group to show/hide them
main_display = displayio.Group()
main_display.append(menu)

display.show(main_display)

# Always keep these arrays exactly 12 long. Each color and tone is assigned to a key in that position
colors = [0xfc0a0a, 0xfc9b0a, 0xfcfc0a, 0x2efc0a, 0x0a0afc, 0x0ae0fc, 0x930afc, 0xfc0af4, 0xfc0a5e, 0x98e0af, 0xb7665f, 0x5fa8b7]
tones = [196, 220, 246, 262, 294, 330, 349, 392, 440, 494, 523, 587]

last_posit = 0
key_pressed = -1
while True:
    if macropad.encoder_switch:
        pass

    if macropad.encoder != last_posit:
        last_posit = macropad.encoder

    event = keys.events.get()
    if event:
        # Key pressed = tone and color
        if event.pressed:
            key_pressed = event.key_number
            pixels[key_pressed] = colors[key_pressed]
            macropad.start_tone(tones[key_pressed])
            title.text = str(tones[key_pressed])

        # Key released = clear color and stop tone
        if event.released:
            key_released = event.key_number
            pixels[key_released] = 0
            macropad.stop_tone()
            title.text = ""

