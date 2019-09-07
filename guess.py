import sys
low = 0
high = 1000
guess = (high+low)//2
print(guess)
feedback = input()
sys.stdout.flush()
while(feedback!="correct"):
    if feedback == "lower":
        high = guess-1
    else:
        low = guess+1
    guess = (high+low)//2
    print(guess)
    feedback = input()
    sys.stdout.flush()
