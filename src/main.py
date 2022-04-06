from Pablo import Pablo
import sys

pablo = Pablo()

while not pablo.died:
    print(f"""
    Pablo's stats:
    health: {pablo.health}
    energy: {pablo.energy}
    happiness: {pablo.happiness}
    
    1 - Play with Pablo
    2 - Feed Pablo
    0 - End
    """)
    i = input("Your choice> ")
    if i == '0':
        print("Bye!")
        sys.exit(0)
    if i == '1':
        pablo.play()
        pablo.step_end()
    elif i == '2':
        pablo.feed()
        pablo.step_end()
