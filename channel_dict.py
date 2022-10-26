import pickle


channel_dict = {
    "Carlie & Ange": "UC5E0MrgcW45AIqyN0QqJMwQ",
    "Karolina Sowinska": "UCAxnMry1lETl47xQWABvH7g",
    "Max0r": "UCfgh3Ul_dG6plQ7rzuOLx-w",
    "Zach Star": "UCpCSAcbqs-sjEVfk_hMfY9w",
    "fireship": "UCsBjURrPoezykLs9EqgamOA",
    "linus tech tips": "UCXuqSBlHAE6Xw-yeJA0Tunw",
    "network chuck": "UC9x0AN7BWHpCDHSm9NiJFJQ",
    "ziostorm": "UCMjd7Sh1Dwf7mywMEDH4OqA",
    "jomatech": "UCV0qA-eDDICsRR9rPcnG7tw",
    "corridor crew": "UCSpFnDQr88xCZ80N-X7t0nQ",
    "videogamedunkey": "UCsvn_Po0SmunchJYOWpOxMg",
    "chalkeaters": "UCYSvX0lqo-ZinYNQSHVCqlQ",
    "the ai epiphany": "UCj8shE7aIn4Yawwbo2FceCQ",
    "vaatividya": "UCe0DNp0mKMqrYVaTundyr9w",
    "ratatoskr": "UCFysI6mtZ5xBMEqTjUo5DuQ",
    "daniel greene": "UCw--xPGVVxYzRsWyV1nFqgg",
    "jayztwocents": "UCkWQ0gDrqOCarmUKmppD7GQ",
    "aviators": "UCioNNjH3S7X8byCjPDEqZkA",
    "the spiffing brit": "UCRHXUZ0BxbkU2MYZgsuFgkQ",
    "the critical drinker": "UCSJPFQdZwrOutnmSFYtbstA",
    "critical role": "UCpXBGqwsBkpvcYjsJBQ7LEQ",
    "exurb1a": "UCimiUgDLbi6P17BdaCZpVbg",
    "sp4zie": "UCmtQGojT9O2LVzVIVKDGEjw",
    "iron pineapple": "UC477Kvszl9JivqOxN1dFgPQ",
    "seth everman": "UCoNRSwYHJdy-yV1b82ZdHfQ",
    "pc centric": "UC54-Zt4_z6W81N5X3OnHCEw",
    "polyphia": "UCDe08Fs0s0YKJuk5h45csAQ",
    "plini": "UC-MEgsEcEkbSuPWpu4a-PzQ",
    "ok goodnight": "UC2P6xo9P2NbABaPq3sq1Bmg",
    "johnny harris": "UCmGSJVG3mCRXVOP4yZrU1Dw",
    "sithu aye": "UCuD2q7edgCJ3IHyXyB0TOWw",
    "indigo la end": "UCXKSbzihU5cu0U4qbbjB3GA",
    "retroshock": "UCS7UA-DV1X3H0XyWol17N4g",
    "totally not mark": "UCv3LuuW8auzYw1SdLmiLRAw",
    "malinda": "UC8Zo5A8qICfNAzVGDY_VT7w",
    "rob scallon": "UCyDZai57BfE_N0SaBkKQyXg",
    "black gryphon": "UCvzWGXYFDiiJ338KIJPhbhQ"
    }

with open("channel_dict.pkl", "wb") as file:
    pickle.dump(channel_dict, file)
