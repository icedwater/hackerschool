# /usr/bin/env python3

from TextToOwO import owo

def echowo(exit_word):
    while True:
        cmd = input("You say: ")
        if cmd == exit_word:
            print("OK, bye!")
            break
        print("...so I say: " + owo.text_to_owo(cmd))

if __name__ == "__main__":
    echowo("bye")
