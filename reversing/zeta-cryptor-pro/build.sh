#!/bin/sh

echo "Building and signing binary"
docker build -t zetacryptorpro .

echo "Packaging client materials"
mkdir -p dist
docker container create --name extract zetacryptorpro:latest
docker cp extract:/home/zetacryptorpro/zeta-cryptor-pro dist/zeta-cryptor-pro
docker cp extract:/home/zetacryptorpro/license.dat dist/license.dat
docker container rm -f extract
cp package/README.md dist/README.md
cd dist
tar czvf zeta-cryptor-pro.tgz ./*
cd -
mv dist/zeta-cryptor-pro.tgz .
