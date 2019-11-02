# Telegram Bot Basics

# Prerequisites

 - python 3.7
 - pip
 - virtualenv # maybe venv
 - TextToOwO # for following the slides

Slides and code available at [a shared GDrive location][share].

# Procedure

  1. Make a virtual environment to keep libraries separate. Be sure to
     specify the version of Python you intend to use, in this case 3.7.
     `botenv` below is the name of the environment, you can change it.

         $ virtualenv botenv --python=python3.7

  2. Now activate the virtual environment. New libraries you install
     will be kept inside here and not affect your main system.

         $ source botenv/bin/activate

  3. Look through the slides and `echo.py` to see some basic structures:
     `if` and `def`, `while` loops. You can run the file with:

         $ python echo.py
     
  4. `echowo.py` has the `owo-fied` version. Check it out as above:

         $ python echowo.py

  5. The requirements going forward are found in `requirements.txt`. This
     is a list of Python libraries we will be using, and their versions.
     Be careful to install these **within the virtual environment**.

         $ pip install -r requirements.txt

[share]: http://bit.ly/hs-2019-bot-materials
