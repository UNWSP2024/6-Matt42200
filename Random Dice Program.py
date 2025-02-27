import random


def randDice():
    """Simulates rolling two dice and returns their sum."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2


def main():
    total = 0
    rolls = 100


    for _ in range(rolls):
        total += randDice()
    
    average = total / rolls
    print(f"Average roll over {rolls} rolls: {round(average, 2)}")


if __name__ == "__main__":
    main()