# Krypto: Kryptiska apkonster

- **Skapare:** Herman Karlsson
- **Poäng:** 400
- **Antal lösningar:** ???

## Beskrivning

Vi har en server och klient som pratar med varandra, de verkar kommunicera något hemligt?

Servern kör på `35.228.52.143:5678`

Klienten kör på `35.228.52.143:8765`

Givna  filer: client.py server.py lib.py pub_secret.py 

## Flagga

`SSM{D0nt_f0rg3t_y3r_MACs_kids_0r_1t_w1l1_0nly_l34d_to_gre4t_gr3at_sadn35s_4nd_many_st01en_fl4g5}`

## Lösning

Gör en man in the middle attack på en diffie hellman.

Går att göra manuellt, men det är pilligt:

Automatiserad lösning: `solution.py`

Halvautomatiserad lösning: `solution_manual.py`, man får copypastea till och från server och klient
