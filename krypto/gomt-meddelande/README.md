# Krypto: Gömt meddelande

- **Skapare:** Axel Boström
- **Poäng:** 200
- **Antal lösningar:** ???

## Beskrivning

Flagga, vadå flagga? Finns inget sånt här. Jag vet inte vad du pratar om, sluta fråga om det! Nä men lägg av, jag gömmer inget här! Kolla filen själv!

Given fil: Inget.txt

## Flagga

SSM{GöMdAmEdElAnDeN}

## Lösning

Man måste lista ut att det finns massvis med gömda non printing unicode karaktärer mellan varje synlig, sen måste man se att de är av två olika typer. Man gör det enklast med en hex editor.
När man listat ut att det är två typer, och åtta av dem mellan varje synlig karaktär, så kan man plocka ut mönstret `"E2808D E2808C E2808D E2808C E2808D E2808D E2808C E2808C  E2808D E2808C E2808D E2808C E2808D E2808D E2808C E2808C  E2808D E2808C E2808D E2808D E2808C E2808C E2808D E2808C  E2808D E2808C E2808C E2808C E2808C E2808D E2808C E2808C  E2808D E2808C E2808D E2808D E2808D E2808C E2808C E2808C  E2808C E2808C E2808D E2808D E2808D E2808D E2808C E2808C  E2808C E2808D E2808C E2808C E2808D E2808C E2808C E2808D  E2808D E2808C E2808D E2808D E2808C E2808C E2808D E2808C  E2808D E2808C E2808C E2808D E2808D E2808C E2808D E2808D  E2808D E2808C E2808D E2808D E2808D E2808D E2808D E2808C  E2808D E2808C E2808C E2808D E2808C E2808C E2808D E2808C  E2808D E2808C E2808D E2808D E2808D E2808C E2808D E2808C  E2808D E2808C E2808C E2808D E2808D E2808C E2808D E2808D  E2808D E2808C E2808D E2808D E2808D E2808C E2808D E2808C  E2808D E2808C E2808C E2808D E2808C E2808C E2808D E2808D  E2808D E2808C E2808D E2808D E2808D E2808D E2808D E2808C  E2808D E2808C E2808C E2808D E2808C E2808C E2808C E2808D  E2808D E2808C E2808D E2808D E2808D E2808C E2808D E2808D  E2808D E2808C E2808C E2808D E2808D E2808C E2808D E2808C  E2808D E2808C E2808D E2808D E2808C E2808C E2808C E2808D  E2808D E2808C E2808C E2808C E2808C E2808C E2808D E2808C"`

Om man ersätter alla E2808D med 0 och alla E2808C med en etta och översätter detta till text så får man fram nyckeln. Om man försöker tvärt om så får man totalt skräp.