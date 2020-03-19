import 'express-async-errors';
import bcrypt from 'bcrypt';
import bodyParser from 'body-parser';
import compression from 'compression';
import cookieParser from 'cookie-parser';
import cors from 'cors';
import dotenv from 'dotenv';
import express from 'express';
import helmet from 'helmet';
import nodeSchedule from 'node-schedule';
import { validationResult, body } from 'express-validator';

class RequestError extends Error {
  public doNotLog: boolean;
  constructor(errorMessage: string, doNotLog: boolean) {
    super(errorMessage);
    this.doNotLog = doNotLog;
  }
}

const SALT = bcrypt.genSaltSync(10).substr(7, 12);

async function stringToHash(input: string): Promise<string> {
  const salt = `$2b$10$${(SALT + Buffer.from((~~(new Date().getTime() / 1000)).toString() + (~~(new Date().getTime() / 1000)).toString()).toString('base64')).substring(0, 22)}`;

  try {
    const hash = await bcrypt.hash(input, salt);
    return hash;
  } catch (e) {
    const error = new RequestError(`Error using salt: ${salt}`, true);
    throw error;
  }
}

dotenv.config();

const app = express();

app.set('trust proxy', true);

app.use(compression());

app.use(helmet());
app.use(helmet.permittedCrossDomainPolicies());
app.use(helmet.referrerPolicy({ policy: 'same-origin' }));
app.use(
  helmet.hsts({
    includeSubDomains: true,
    maxAge: 31536000,
    preload: true,
  }),
);

app.use(cors({ origin: false }));

app.use(bodyParser.json({ limit: '100kb' }));
app.use(bodyParser.urlencoded({ limit: '100kb', extended: false }));
app.use(bodyParser.raw({ limit: '100kb' }));
app.use(bodyParser.text({ limit: '100kb' }));
app.use(cookieParser());

let cooldown: any = {};
let score: any = {};

nodeSchedule.scheduleJob('*/5 * * * *', function() {
  cooldown = {};
  score = {};
});

app.post('/api/hash', body('input').isIn(['digitalungdom', 'test_string_to_hash', 'testStringToHash', 'TRY_THIS_STRING', 'JK_BUT_THIS_STRING_WILL_WORK']), async function(req, res) {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(422).json({ errors: errors.array() });
  }

  const hash = await stringToHash(req.body.input);

  return res.send(hash.substr(28));
});

app.post('/api/get/flag', async function(req, res) {
  if (cooldown[req.ip] && cooldown[req.ip] < new Date().getTime()) {
    return res.send('wait 137 ms');
  }

  cooldown[req.ip] = new Date().getTime() + 555;
  const id = req.body.id;
  const hash = req.body.hash;
  if (typeof id !== 'string' || typeof hash !== 'string') {
    return res.status(422).send();
  }

  if (!score[id]) {
    score[id] = {
      end: new Date().getTime() + 5000,
      score: 1,
    };

    return res.status(202).send();
  }

  if ((await stringToHash(id + score[id].score.toString())) !== hash) {
    return res.status(422).send();
  }

  score[id].score = score[id].score + 1;

  if (score[id].score > 10 && new Date().getTime() < score[id].end) {
    delete score[id];
    return res.json({ flag: process.env.FLAG });
  }

  if (new Date().getTime() > score[id].end) {
    delete score[id];
    return res.status(422).send();
  }

  return res.status(202).send();
});

app.use(function(err: RequestError, req: express.Request, res: express.Response, next: express.NextFunction) {
  if (typeof err === 'string') {
    err = new RequestError(err as string, true);
  }

  if (!err.doNotLog) {
    console.error(err.stack);
  }

  return res.status(500).send(err.stack);
});

app.set('port', 6969);

app.listen(app.get('port'), function() {
  console.log(`Starting server in ${process.env.NODE_ENV}. Listening on ${app.get('port')}`);
});
