# Krypto: Konstig kloss

- **Skapare:** Mattias Grenfeldt
- **Poäng:** 500
- **Antal lösningar:** 6

## Beskrivning

Du hittar ett "kloss-chiffer". Något känns bekant men ändå inte.

Anslut till ip:port.
Lägg SSM{} runt flaggan innan du skickar in den.

Given fil: chall.py

## Flagga

`NSA_backd00red_my_c1pher_h3lp!!!`
`SSM{NSA_backd00red_my_c1pher_h3lp!!!}`

## Lösning

Vi kan läsa i koden att detta är AES. Om man googlar runt lite kan man hitta att implementationen är tagen från: https://github.com/bozhu/AES-Python

Om man letar efter skillnader mot originalet inser man att den enda skillnaden är att Sbox har blivit ändrad. S-boxen som ska substituera en byte mot en annan verkar ha ändrats till en identitets-Sbox. Det vill säga att den substituerar något värde mot sig själv.

Det går att läsa på wikipedia att s-boxen i AES är del av subbytes-steget. Detta steg är vad som hindrar krypteringen från att vara linjär. https://en.wikipedia.org/wiki/Advanced_Encryption_Standard#The_SubBytes_step

Då s-boxen är trasig vet vi nu att kryptot är linjärt. Det visar sig att kryptering ser ut så här `c = A*m + B` där `m` är plaintexten, `c` är ciphertexten, `A` är en 128x128 stor matris, `c`, `m`, och `B` är 128x1 vektorer och alla beräkningar sker modulo 2. 

Målet blir nu att hitta `A` och `B`. För om vi har dem kan vi dekryptera den krypterade flaggan vi har fått genom linjär algebra. Vi kan få `B` genom att låta tjänsten kryptera `m = 0` åt oss, för då spelar `A` ingen roll. Alltså:

```
c = A*0 + B = B
```

Vi kan sedan få ut alla kolumner i `A` genom att kryptera `m = (1 << i)` med `0 <= i < 128` och sedan subtrahera `B` som vi redan har listat ut. Alltså:

```
[Kolumn med index i i matris A] = c - B = A*(1 << i) + B - B = A*(1 << i)
```

När vi nu har `A` och `B` kan vi dekryptera den krypterade flagga `cflag` genom att hitta inversen av `A` och multiplicera med den. Vi kan hitta inversen av `A` genom gausseliminering. Flaggan får vi alltså genom:

```
Ainv*(cflag - B) = Ainv*(A*flag + B - B) = Ainv*A*flag = flag
```

Se även solution.py

## Lösning på livestream

Del 1: https://www.youtube.com/watch?v=mEeccIodvFQ&t=8175s
