#!/bin/sh

TMPDIR=$(mktemp -d)
cp ../dist/zeta-cryptor-pro $TMPDIR/zeta-cryptor-pro # placeholder
# Modify binary here
nsjail -Mo --user 99999 --group 99999 -R /lib/x86_64-linux-gnu/ -R /lib/x86_64-linux-gnu -R /lib64 -R $TMPDIR/zeta-cryptor-pro:/bin/zeta-cryptor-pro -R /dev/urandom --keep_caps -- /bin/zeta-cryptor-pro
rm -rf $TMPDIR
