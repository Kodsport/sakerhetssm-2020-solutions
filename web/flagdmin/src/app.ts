const RedisServer: any = require('redis-server');

import bodyParser from 'body-parser';
import compression from 'compression';
import cors from 'cors';
import dotenv from 'dotenv';
import express from 'express';
import helmet from 'helmet';
import redis from 'redis';
import { MongoClient, ObjectID } from 'mongodb';
import { MongoMemoryServer } from 'mongodb-memory-server';
import { promisify } from 'util';
import 'express-async-errors';

declare module 'redis' {
  interface RedisClient {
    getAsync(string: string): Promise<string>;
  }
}

(async function init() {
  dotenv.config();

  const app = express();
  const mongod = new MongoMemoryServer();
  const server = new RedisServer(6379);

  try {
    await server.open();
  } catch (e) {
    console.error('redis already started');
  }

  const client = redis.createClient();
  client.getAsync = promisify(client.get).bind(client);

  const mongoUri = await mongod.getConnectionString();

  const connection = await MongoClient.connect(mongoUri, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });

  const db = connection.db(await mongod.getDbName());

  await db.createCollection('flags');
  await db.collection('flags').insertOne({
    _id: new ObjectID().toHexString(),
    flag: process.env.FLAG,
  });

  app.disable('x-powered-by');

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

  app.get('/api/loves_me', async function(req, res) {
    if (Math.random()) {
      if (Math.random() === Math.random()) {
        if (new Date(Math.random() * 10000000000000).getTime() === new Date().getTime()) {
          const flag = await db.collection('flags').findOne({ _id: process.env.flagID });

          return res.status(218).json(flag);
        }
      }
    }

    return res.status(500).send('loves me not');
  });

  app.get('/api/redirect', async function(req, res) {
    return res.redirect('https://digitalungdom.se/');
  });

  app.get('/api/hello', async function(req, res) {
    return res.status(401).send('I AM A TEAPOT');
  });

  app.get('/api/copycat', async function(req, res) {
    return res.status(401).json({
      body: req.body,
      headers: req.headers,
      params: req.params,
      query: req.query,
    });
  });

  app.post('/api/login', async function(req, res, next) {
    if (!req.body.userID || req.body.userID.length < 2) {
      return res.status(401).send('your id has to be more than 2 characters long');
    }

    const userID = req.body.userID || '';

    client.set(userID, 'user');

    return res.status(201).send();
  });

  app.post('/api/get/flag', async function(req, res) {
    if ((await client.getAsync(req.body.userID)) === 'admin') {
      const flagID = req.body.flagID;
      const flag = await db.collection('flags').findOne({ _id: flagID });

      return res.status(218).json(flag);
    }

    return res.status(401).send();
  });

  app.use(function(err: Error, req: express.Request, res: express.Response, next: express.NextFunction) {
    if (typeof err === 'string') {
      err = new Error(err);
    }

    console.error(err.stack);

    return res.status(500).send();
  });

  app.set('port', 6969);

  app.listen(app.get('port'), function() {
    console.log(`Starting server in ${process.env.NODE_ENV}. Listening on ${app.get('port')}`);
  });

  process.on('exit', async function() {
    await client.flushall('ASYNC');
    await server.close();
    await mongod.stop();
  });
})();
