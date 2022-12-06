# dyslexicator
Small script to "dyslexicate" a text

The script reads the FILE and shuffles all the letters between the first and the last, then writes them to a new file called dyslexed_FILE.

There are flags to affect words with less than 5 letters.

```
Usage: dislexicaler.exe FILE ... (-f2 | -f3 | -f4 )
Usage: dislexicaler.exe -h
        -h|--help       Show this help.
        -f2             Force swaping two letters words.
        -f3             Force swaping las two letters in three letters words.
        -f4             Force swaping the two letters inside four letters words.
```
