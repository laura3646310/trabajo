def on_forever():
    basic.show_leds("""
        # # . . .
        # # . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(3000)
    basic.show_leds("""
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(1000)
    basic.show_leds("""
        . # . . .
        . # . . .
        # . . . .
        # . . . .
        . . . . .
        """)
    basic.pause(3000)
    basic.show_leds("""
        # . . . .
        . # . . .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(5000)
    basic.show_leds("""
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
basic.forever(on_forever)
