Current Status
---------------
* To run Markov chain portion of the assignment, run markov.py.
* To print a Twitter user's timeline, edit the twitter_api.py file as noted before running
    * The twitter_api.py file does not currently interact with the markov.py file.

Description
------------
You are to produce a random text generator using markov chains. We've provided a very bare skeleton for you to start your program from. Up until now, we've been writing our programs in a very freeform manner, just writing code at the 'top level', the same place where we put our global variables. This is generally considered bad form. Code should always be contained in functions or class methods wherever possible.

The skeleton program we've provided has a recommended set of functions to start with, including a very odd if statement at the bottom. You can ignore how this statement works for now, all it does is it makes sure your program starts inside the main() function.

The program should accept a filename from the command line, and a sample run should look similar to the following:

    meringue:Exercise08 chriszf$ python markov.py shakespeare.txt
    Forsooth, or somesuch.

You can use any text as an input corpus, you might try (Project Gutenberg)[http://www.gutenberg.org/] for some inspiration.
