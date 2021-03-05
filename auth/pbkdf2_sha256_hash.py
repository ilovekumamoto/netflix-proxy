#!/usr/bin/env python

import sys
from passlib.hash import pbkdf2_sha256
from passlib.hash import plaintext as plaintext
from passlib import pwd

try:
  plaintext = sys.argv[1]
except IndexError:
  plaintext = pwd.genword()

<<<<<<< HEAD
print plaintext, pbkdf2_sha256.encrypt(plaintext, rounds=200000, salt_size=16)
=======
print(plaintext, pbkdf2_sha256.hash(plaintext, rounds=200000, salt_size=16))
>>>>>>> 56274388f3f5f891e30a30f026e6d0358c3335d6
