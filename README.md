# Markedness
The ```sound_change.py``` script allows an user to specify a phonemic inventory (chosen among English spelling letters) and to specify splitwise and mergerwise markedness for some phonemes. 

After the input is acquired, the program performs sound change for 100 generations and yields the resulting phonemic distribution. The phonemes for which markedness was specified are marked in red.

An alternative to run several simulations with the same settings is to uncomment some parts in the code that allow to perform multiple simulations with the same settings and to calculate some summary statistics for marked phonemes.
