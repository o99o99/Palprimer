Palprimer
=========

Primes and Palprimes Finder

Thanks to rschaosid for making the happy number section

This simple Python tool is for listing all primes, palprimes (primes which are also palindromic) and then happy palprimes in a certain range. 

The program will ask you the range at the start. The prime, palprime and happy palprime count will be shown at the bottom of 
each section.

There is no theoretical limit to the range, but very large ranges take a long time. For example, for a range of 0-100,000 
the program takes a few minutes to complete. For 0-100,000,000 you may well have to leave it overnight!

The generation of lists can be stopped at any time, and the program will proceed to the next step using already obtained numbers rather than ending abruptly. This could be useful if you accidentally made the range 0-100k but at 25k decided you wanted to stop. This can be done for every list generation stage. Obviously the overall range will change depending on the time at which you stopped, and it will become progressively smaller every time you do it.

This is currently as fast as I can make it work. The reason I have it list every prime as it finds them is so the user can
see that it is working and not stuck in an infinite loop somewhere.

If you think anything could be improved, or if you have a way of checking for double primes or happy primes, please let me know!
