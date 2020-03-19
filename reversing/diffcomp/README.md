# Reversing: Diff Compare

- **Skapare:** Aron Bergman
- **Poäng:** 250
- **Antal lösningar:** 12

## Beskrivning

Ladda ner det kompilerade programmet.

**Hint:** Bra verktyg för reverse engineering är:
- gdb
- https://ghidra-sre.org/
- https://binary.ninja/
- https://www.hex-rays.com/products/ida/support/download_freeware/
- radare2

Given fil: diffcomp

## Flagga

`SSM{y0u_are_4_mastr_of_d1ffs}`

## Lösning

Programmet kollar om första bokstaven, `pass[0]`, är S och kollar vidare om `pass[i] - pass[i-1] == diff[i]` där `diff[i]` är skillnaden mellan `pass[i]` och `pass[i-1]` i det korrekta lösenordet. 

## Lösning på livestream

https://www.youtube.com/watch?v=CYBGQ9Zp6UQ&t=6260s

