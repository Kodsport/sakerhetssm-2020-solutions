# Pwn: Echo Service

- **Skapare:** Viktor Edström
- **Poäng:** 350
- **Antal lösningar:** 8

## Beskrivning
Since the Hello World program was so good I decided to build an echo service. Nothing can go wrong... right?

Given fil: echo  
I den här uppgiften fick man även en ip och port till en server där echo kördes.

## Flagga

`SSM{AAAAAAAA_r0pch41n_N_r0pch4in_4cc$$sor1e$_AAAAAAAA}`

## Lösning

Intro till x86_64 rop. Hoppa mellan diverse funktioner med specifika argument för att få flaggan. Se solve.py

## Lösning på livestream

https://www.youtube.com/watch?v=mEeccIodvFQ&t=2410s
