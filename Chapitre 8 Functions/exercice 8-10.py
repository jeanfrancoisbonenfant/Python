short_text = ["small text", "very small text", "longer text"]
printed_text = []


def show_message(list):
    """
    take a list and print message from it.
    """
    for message in list:
        print(message)


def move_message(listFrom, listTo):
    while listFrom:
        for message in listFrom:
            current_message = listFrom.pop()
            listTo.append(current_message)


show_message(short_text)
move_message(short_text, printed_text)
print(printed_text)
print(short_text)
