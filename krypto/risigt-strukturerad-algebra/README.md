# Krypto: Risigt Strukturerad Algebra

- **Skapare:** Herman Karlsson
- **Poäng:** 400
- **Antal lösningar:** 16

## Beskrivning

Här är ett RSA-krypterat meddelande, avkryptera det.

Given fil: chall.txt

## Flagga

SSM{m0re_pr1m3s_d03s_n0t_n3ces4r11y_mak3_th1ng5_m0re_s3cur3_in_f4ct_it_1s_usu411y_th3_opp0sit3_s1nc3_th3y_g3t_4_1ot_smal13r_qu1te_quick1y_4nd_th4t_15_not_g00d}

## Lösning

Faktorisera n, detta kan göras med exempelvis `factordb.com`, eller med det inbyggda unix-kommandot `factor`. Vi kan göra detta eftersom de som skapade RSAt råkade välja ett modulo som hade många små primtalsfaktorer.

Beräkna `d = e^{-1} (mod phi(n))`.

Beräkna `m = c^d (mod n)`.

Hexdecodea `m`

Möjlig lösning i sage: se `solve.sage`

## Lösning på livestream

https://www.youtube.com/watch?v=mEeccIodvFQ&t=6695s
