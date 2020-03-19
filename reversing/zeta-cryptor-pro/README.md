# Reversing: Zeta Cryptor PRO

- **Skapare:** Calle Svensson
- **Poäng:** 500
- **Antal lösningar:** ???

NaCl documentation: https://nacl.cr.yp.to/

## Beskrivning

The best cryptor software out there! Download the demo below.

Use it here: 35.228.52.143 31337

Given fil: zeta-cryptor-pro.tgz

## Flagga

`SSM{c0py_pr0t3ction_p4tch1ng_perfect1i0n}`

## Lösning

???

## Install

Runtime dependencies:
* nsjail
* libsodium

Build dependencies:
* libsodium

To build challenge
```
apt-get install libsodium-dev
pip3 install --user pynacl
./package.sh
```

To run on server
```
apt-get install libsodium23 protobuf-compiler libnl-route-3-dev pkg-config flex bison libprotobuf-dev
git clone https://github.com/google/nsjail.git
cd nsjail
make && cp nsjail /bin/
cd -
pip3 install --user pynacl
cd deploy
./run.sh
```
