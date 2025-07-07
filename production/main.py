import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Press, Release, Tap, Macros

kbd = KMKKeyboard()
macros = Macros()
encoder = EncoderHandler()
kbd.modules.append(macros)
kbd.modules.append(encoder)

kbd.matrix = KeysScanner(
    pins=[
        board.D0, board.D1, board.D2,  # 1-3
        board.D3, board.D4, board.D5,  # 4-6
        board.D6, board.D7, board.D8,  # 7-9
    ],
    value_when_pressed=False,
)

kbd.encoders = [
    (board.D10, board.D11, board.D12, False, 4),  # encoder pins: A, B, button, reversed, divisor
]

kbd.keymap = [
    [
        KC.N1, KC.N2, KC.N3,  # 1-3
        KC.N4, KC.N5, KC.N6,  # 4-6
        KC.N7, KC.N8, KC.N9,  # 7-9
    ]
]

kbd.go()