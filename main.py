# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def display_message():
    """displays a message about what I am learning"""
    print("I am learning about functions in this chapter.")

display_message()

def favorite_book(book):
    """displays a custom message about the users favorite book"""
    print(f"One of my favorite books is {book.title()}")

favorite_book("warm bodies")

def make_shirt(shirt_size='large', shirt_text='I love Python'):
    """displays custom shirt"""
    print(f"This is a {shirt_size} shirt that says: {shirt_text}.")

make_shirt()
make_shirt(shirt_size='medium')
make_shirt(shirt_text='I love pizza')
