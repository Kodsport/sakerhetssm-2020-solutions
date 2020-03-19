# Reversing: Double Protection

- **Skapare:** Alexander Stenlund
- **Poäng:** 300
- **Antal lösningar:** 11

## Beskrivning

Double the passwords, double the protection.

Given fil: double-protection

## Flagga

`SSM{Y3s_Th1s_1s_wh4t_y0u_n33d!}`

## Lösning
Öppnat i radare2 med flagga "-AAA"
Om vi kollar i main (med kommandot "s main" sedan "pdf") så ser vi att det finns två olika funktioner som vi kallar på vilket ligger i slutet av main, dessa kallar vi func.1 och func.2, där func.1 är den första vi kallar medans func.2 är den andra.
Om vi går in i func.2 (med kommandot "s [namnePåFunc.2]" sedan "pdf") så ser vi att mot mitten av funktionen så jämför den två strängar med strcmp och beroende på om de var lika eller ej så kommer den skriva ut "SSM{%s}". Om vi följer det ena argumentet till strcmp:en så ser vi att det är argumentet till våran func.2 som vi är i just nu, samt om vi följer den lite längre (alltså ut ur funktionen till main) så ser vi även att det är retur värdet av func.1 i main samt att func.1 tar in användarens två inmatningar (Password1 & password2). Om vi istället följer den andra strängen i strcmp:en så ser vi att den kommer från retur värden av func.1 men denna func.1 (som ligger i func.2) har två andra argument. Om vi sedan kollar vad som finns i argumenten så är det de två lösenorden som behövs för att få flaggan.

## Lösning på livestream

https://www.youtube.com/watch?v=CYBGQ9Zp6UQ&t=7630s
