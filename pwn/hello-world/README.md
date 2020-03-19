# Pwn: Hello, World

- **Skapare:** Viktor Edström
- **Poäng:** 250
- **Antal lösningar:** 8

## Beskrivning
I just learned to code my first Hello world. Check it out!

Given fil: overflow (Under tävlingen hette filen hello).  
I den här uppgiften fick man även en ip och port till en server där overflow kördes.

## Flagga
SSM{d_w0RLDz_B1CCEST_0verflow1111}

## Lösning
Buffer overflow på stack mha gets. Anropa `win` för att få flaggan. Se solve.py.
