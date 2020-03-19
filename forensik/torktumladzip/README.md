# Forensik: Torktumlad ZIP

- **Skapare:** Mattias Grenfeldt
- **Poäng:** 500
- **Antal lösningar:** ???

## Beskrivning

Jag tappade min ZIP-fil i torktumlaren. Lycka till.

Given fil: file.zip

## Flagga

SSM{tur_att_det_inte_var_en_zip_bomb_i_alla_fall}

## Lösning

Om en fil har blivit torktumlad kan nog inte så mycket vara rätt i filen.
Vi hittar lite resurser för att förstå zip-filformatet
+ https://github.com/corkami/pics/blob/master/binary/zip101/zip101.pdf
+ https://github.com/corkami/formats/blob/master/archive/ZIP.md

Efter att ha analyserat filen byte för byte, fält för fält enligt filspecifikationen så inser man att alla fält är off by one. Det är enklast att se detta på något av längdfälten för filnamnet, fildatan eller central directory. Man kan också se att det är off by one genom att titta på fälten "offset of start of central directory with respect to the starting disk number" och "offset to local file header".

Efter man ha insett att alla fält är off by one är det bara att ändra tillbaka fälten och sedan dekomprimera zippen. Här kan en hexeditor vara lämpligt att använda. Till exempel: 
+ Hxd: https://mh-nexus.de/en/hxd/
+ 010 editor: https://www.sweetscape.com/010editor/

Ett till trevligt verktyg är:
+ kaitai: https://ide.kaitai.io/
