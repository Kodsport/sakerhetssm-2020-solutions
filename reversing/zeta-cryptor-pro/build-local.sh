#!/bin/sh

echo "Building and signing binary"
cd src
./build.sh
python3 sign_binary.py
cd -

echo "Packaging client materials"
mkdir -p dist
cp src/challenge_signed dist/zeta-cryptor-pro
cp src/license.dat dist/license.dat
cp package/README.md dist/README.md
cd dist
tar czvf zeta-cryptor-pro.tgz ./*
cd -
mv dist/zeta-cryptor-pro.tgz .

echo "Preparing server materials"
mkdir -p deploy
cp src/challenge_signed deploy/zeta-cryptor-pro
cp src/license.dat deploy/license.dat
cp server/server.py deploy/server.py
cp server/run.sh deploy/run.sh
