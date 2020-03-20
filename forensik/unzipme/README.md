# Forensik: Unzip me

- **Skapare:** Fredrik Ljung
- **Poäng:** 200
- **Antal lösningar:** 35

## Beskrivning

Jag hittade den här zip-filen, men lyckas inte komma åt innehållet.
Kan du få fram vad den innehåller?

Given fil: rockyou.zip

## Flagga

`SSM{Its_eaRly_mornIng,_tHe_sUn_cOmes_out_LaSt_niGHt_w4s_shaKIng_and_preTTy_lOUd}`

## Lösning

Vi ser att zip-filen är skyddad med lösenord. Filnamnet rockyou hintar till en stor lista med vanliga lösenord som finns att ladda ner online. T.ex. här: https://www.scrapmaker.com/download/data/wordlists/dictionaries/rockyou.txt

Vi kan nu brute-forcea lösenordet för zip-filen mha. verktyget fcrackzip: https://github.com/hyc/fcrackzip Använd rockyou.txt som wordlist.

```fcrackzip -u -D -p './rockyou.txt' rockme.zip```

Lösenordet är BESTFRIENDS4EVER

Vi hittar sedan flaggan i en textfil inuti zip-filen.

## Lösning på livestream

https://www.youtube.com/watch?v=Od8QJwQpbkk&t=795s
