#!/bin/sh
cat <<EOF | ./challenge_signed
00112233445566778899AABBCCDDEEFF00112233445566778899AABBCCDDEEFF
Hello!
EOF

cat <<EOF | ./challenge_signed
00112233445566778899AABBCCDDEEFF00112233445566778899AABBCCDDEEFF
Hello world!
EOF