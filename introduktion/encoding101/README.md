# Introduktion: Encoding 101

- **Skapare:** Mattias Grenfeldt
- **Poäng:** 10
- **Antal lösningar:** ???

## Beskrivning

Man kan skriva om data på många olika sätt. Precis som man i matten kan skriva tal i olika talbaser kan man konvertera data mellan olika format. Dessa olika format kallas "encodings" på engelska. Det finns många onlineverktyg som kan konvertera mellan dem.

Ett populärt format är hexadecimal. Om vi till exempel skriver om strängen "Hello World!" på hexadecimalt format så får vi: 48656c6c6f20576f726c6421

Här är en lista på lite olika encodings som finns: https://en.wikipedia.org/wiki/Binary-to-text_encoding
Försök nu "decode":a denna data, tillslut hittar du nog en flagga.

55314e4e6533526f4d334a6c587a467a587a4e325a573566596a527a5a5638344e563933645852666433563066513d3d

## Flagga
SSM{th3re_1s_3ven_b4se_85_wut_wut}

## Lösning

https://gchq.github.io/CyberChef är väldigt bra verktyg för att konvertera mellan olika encodings.

Här är lösningen för den här uppgiften: https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')From_Base64('A-Za-z0-9%2B/%3D',true)&input=NTUzMTRlNGU2NTMzNTI2ZjRkMzM0YTZjNTg3YTQ2N2E1ODdhNGUzMjVhNTczNTY2NTk2YTUyN2E1YTU2MzgzNDRlNTYzOTMzNjQ1ODUyNjY2NDMzNTYzMDY2NTEzZDNk
