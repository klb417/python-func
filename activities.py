def run(name):
    print(f"{name} ran fast!")


def swing(name):
    print(f"{name} swung high!")


def slide(name):
    print(f"{name} slid far!")


def hide_and_seek(name):
    print(f"Where the hell is {name}?!")


running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

for kid in running_kids:
    run(kid)
for kid in swinging_kids:
    swing(kid)
for kid in sliding_kids:
    slide(kid)
for kid in hiding_kids:
    hide_and_seek(kid)
