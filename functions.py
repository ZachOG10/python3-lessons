def display_message(chapter):
    print("Hello " + "everyone i'm learning about the " +
        chapter.title() + " today")
display_message("functions chapter")

def favorite_book(book_title):
    print("One of my favorite books is " + 
        book_title.title() + ".")
favorite_book("alice in wonderland")

def make_shirt(shirt_size, printed_message):
    print("This is a " + shirt_size.upper() + " shirt " +
        " with a printout which goes " +
        printed_message.title() + ".")
make_shirt('xxl',"god's not dead")