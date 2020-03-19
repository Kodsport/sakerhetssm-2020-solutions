# Web: Dos Protection

- **Skapare:** Kelvin Szolnoky
- **Poäng:** 400
- **Antal lösningar:** 7

## Beskrivning

Min DOS protection är bättre än cloudflares.

http://35.228.52.143:9696/

Given fil: src/app.ts

## Flagga

`SSM{D0_nOT_TrUSt_X-Forwarded-For_ok?}`

## Lösning

**Se `src/solution.js` för ett exempel.**

1. Det första vi måste göra är att få den random genererade saltet från servern. Detta måste göras genom att få `stringToHash()` funktionen att krasha då detta kommer spotta ut saltet till oss. Detta görs via att skicka en special designad post request (se nedan) för att kring gå express-validator och krasha `stringToHash()` funktionen genom att den får en array som input istället för en sträng. För att få den konstanta delen tar man de 12 första bokstäver efter det sista \$.

Post request body till `/api/hash`:

```json
{
  "input": ["digitalungdom"]
}
```

Ex. response:
`Error: Error using salt: $2b$10$wA1//grw2nN6cMTU4MTE5O at stringToHash (/home/alpha/git/kodsport/sakerhetssm-2020/web-spoofing/src/build/app.js:28:15) at processTicksAndRejections (internal/process/task_queues.js:97:5)`

Detta görs för att det finns en bugg i express-validator funktion `inIn()`. Egentligen ska den ta en sträng och kolla ifall den finns i en lista. Men ifall man skickar en array istället och index 0 av input och validation array är samma kommer validationen att passera och då kommer `stringToHash()` crasha då den förväntar en sträng och inte en array.

2. Nu när man har saltet kan man använda dess salt för att tillverka samma hash funktion som servern har. I JavaScript skulle det se ut såhär:

```javascript
async function stringToHash(input) {
  const salt = `$2b$10$${(SALT + Buffer.from((~~(new Date().getTime() / 1000)).toString() + (~~(new Date().getTime() / 1000)).toString()).toString('base64')).substring(0, 22)}`;
  return await bcrypt.hash(input, salt);
}
```

3. Ǹu kan vi börja skicka requests till `/api/get/flag` när vi vet hela hash funktionen. Men problemet här är att vi måste skicka 11 requests inom 1500ms sekunder men vår ip blir rate limeted på 137ms. Vi kan enkelt kring gå detta system då servern litar på X-Forwarded-For headern men eftersom det inte finns en reverse proxy mellan oss och servern kan vi bara spoofa den headern. Igenom att sätta X-Forwarden-For headern till random ips i vår request kan vi skicka så många requests vi behöver.

4. Nu när vi vet både hashing funktionen och kan komma undan rate limeting kan vi få flaggan. Detta görs genom att skicka 11 på varandra requests till `/api/get/flag` som ser ungefär ut såhär:

```json
{
  "id": "<ID>",
  "score": "<score>",
  "hash": "hash(<ID> + <score>)"
}
```

Där:

- ID: är ett random ID vi genererar som samma för varje request
- score: är den score vi har. kan ses som hur många requests vi har utfört om score börjar på 0
- hash: är den hashen vi får när vi hashar vårt ID och score med den funktion vi fick från innan

5. Efter 11 sådana request får man tillbaka flaggan.


