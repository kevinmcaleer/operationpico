 def LightUpNose():
    if True:
        pass

def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P1, 1)
    music.set_built_in_speaker_enabled(False)
    music._play_default_background(music.built_in_playable_melody(Melodies.ENTERTAINER),
        music.PlaybackMode.IN_BACKGROUND)
    music.play(music.builtin_playable_sound_effect(soundExpression.hello),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P1, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    while False:
        pass
basic.forever(on_forever)
