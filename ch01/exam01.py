def print_message():
    print("CS101 is fantastic!")
    print("Programming is so much fun!")

print_message()

# print_message() 보다 더 큰 함수
def repeat_message():
    print_message()
    print_message()

repeat_message()