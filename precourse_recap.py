print("Pick a number from 0 - 14")
score = int(input())
if score > 10:
    print("WINNER!!!")
elif score == 10:
    print("draw try again")
elif score < 10:
    print("Better luck next time")