def green_bottles_song():
    num_bottles = 10

    while num_bottles > 0:
        print(f"There are {num_bottles} green bottles hanging on the wall, {num_bottles} green bottles hanging on the wall, and if 1 green bottle should accidentally fall")
        correct_answer = num_bottles - 1
        while True:
            try:
                user_answer = int(input("How many green bottles will be hanging on the wall? "))
                if user_answer == correct_answer:
                    print(f"There will be {correct_answer} green bottles hanging on the wall")
                    break
                else:
                    print("No, try again.")
            except ValueError:
                print("Please enter a valid number.")
        num_bottles -= 1

    print("There are no more green bottles hanging on the wall")

if __name__ == "__main__":
    green_bottles_song()