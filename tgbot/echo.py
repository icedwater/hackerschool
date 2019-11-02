# /usr/bin/env python3

def echo(exit_word):
    while True:
        cmd = input("You say: ")
        if cmd == exit_word:
            print("OK, bye!")
            break
        print("...so I say: " + cmd)


if __name__ == "__main__":
    echo("bye")
