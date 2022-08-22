from browser import document, alert
import string
import random


def generate(add_num, letters, symbol, length):
    password = ""
    special_characters = ["!", "@", "#", "$", "(", ")", "/", "-"]
    upper_letters = [chr(up) for up in range(65, 91)]
    lower_letters = [chr(up) for up in range(97, 123)]


    for _ in range(1, length + 1):
        if add_num:
            password += random.choice(string.digits)
        if letters:
            password += random.choice(upper_letters)
            password += random.choice(lower_letters)
        if symbol:
            password += random.choice(special_characters)

    pwd = list(password)

    while len(pwd) != length:
        delete = int(random.randrange(0, len(pwd)))
        pwd.pop(delete)

    random.shuffle(pwd)
    document['password'].text = f"Your password is: {''.join(pwd)}"

def show(ev):
    check_box_one = document.getElementById("option1")
    check_box_two = document.getElementById("option2")
    check_box_three = document.getElementById("option3")
    try:
        number = int(document["option4"].value)
    except:
        number = 0

    add_numbers = False
    only_letters = False
    special_symbol = False
    numbers = 0

    if not check_box_one.checked and not check_box_two.checked and not check_box_three.checked:
        alert("Please check one of options")
    else:
        if check_box_one.checked:
            add_numbers = True

        if check_box_two.checked:
            only_letters = True

        if check_box_three.checked:
            special_symbol = True

        if number > 0:
            numbers = number
        else:
            alert("Enter valid number")

        generate(add_numbers, only_letters, special_symbol, number)

def clear(ev):
    document['password'].text = "Your password is: "


document['generate'].bind("click", show)
document['clear'].bind("click", clear)

