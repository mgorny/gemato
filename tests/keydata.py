# gemato: OpenPGP key data for tests
# vim:fileencoding=utf-8
# (c) 2017-2020 Michał Górny
# Licensed under the terms of 2-clause BSD license

import base64


PUBLIC_KEY = base64.b64decode(b'''
mQENBFnwXJMBCACgaTVz+d10TGL9zR920sb0GBFsitAJ5ZFzO4E0cg3SHhwI+reMJQ6LLKmH
owY/E1dl5FBbnJoRMxXP7/eScQ7HlhYj1gMPN5XiS2pkPwVkmJKBDV42DLwoytC+ot0frRTJ
vSdEPCX81BNMgFiBSpkeZfXqb9XmU03bh6mFnrdd4CsHpTQGcsVXHK8QKhaxuqmHTALdpSzK
Cb/r0N/Z3sQExZhfLcBf/9UUVXj44Nwc6ooqZLRizHydxwQdxNu0aOFGEBn9WTi8Slf7MfR/
pF0dI8rs9w6zMzVEq0lhDPpKFGDveoGfg/+TpvBNXZ7DWH23GM4kID3pk4LLMc24U1PhABEB
AAE=
''')

SECRET_KEY = base64.b64decode(b'''
lQOYBFnwXJMBCACgaTVz+d10TGL9zR920sb0GBFsitAJ5ZFzO4E0cg3SHhwI+reMJQ6LLKmH
owY/E1dl5FBbnJoRMxXP7/eScQ7HlhYj1gMPN5XiS2pkPwVkmJKBDV42DLwoytC+ot0frRTJ
vSdEPCX81BNMgFiBSpkeZfXqb9XmU03bh6mFnrdd4CsHpTQGcsVXHK8QKhaxuqmHTALdpSzK
Cb/r0N/Z3sQExZhfLcBf/9UUVXj44Nwc6ooqZLRizHydxwQdxNu0aOFGEBn9WTi8Slf7MfR/
pF0dI8rs9w6zMzVEq0lhDPpKFGDveoGfg/+TpvBNXZ7DWH23GM4kID3pk4LLMc24U1PhABEB
AAEAB/sEgeBMIXW9ClZvvj9HlfWcLz7yF1ZwKMC1BbOENz43LLxp7i2RJQtrErayxnxq8k6u
4ML3SAe2OwK+ZIZG2aFqL0fw+tb8KvotsSPMrE6o/HaFZMxEZYg19zj1WlsvRCxE3OlJDA2f
NJBUQnj6LQ/vYDsQOtM+VRHnfMDhLcwGObZnNPMwtmwkHLKWTgyTwAGnLObSheVutVbdyU6+
wI3UXwAoilW2e+9pKtwaODjqT7pQ2maVSCY4MPGdLQpbPy61COstdpK/hRdI3liLuwszdlnT
1QhiLsOTHPt4JjYdv2jgDjQobbe/ziKNzFp1eoMHDkbjzAh7oD2FxJcZEYLnBADE5oryW+9G
lyYQe3x74QD5BGTZfvJctvEOgUg8BsoIfXJgBzwnEwOD0XBgJcl5qgt3IBH9Fn3JnYMpw12S
EG2W4N8VCIBxIkDEBABVJfp1Q7HAJ8GSmzENnvt1iaAZPUscaFVpMyuajsCDmyK92NMymGiN
Ab1H5MU4gaFGaEaajwQA0I7gglsehQA2MSyJD0Uj+0b6n9KtiUzjyWEOcITXn4buf4O8Llor
8gU0BWuv3hmIcvNsuJfmgXavVxq2UHtiGaO7T9Vk4Sr8MKS9EYrLNbK41Lyb+tjxk3jYjEyF
qCDNEtWKIZR4ENdRjo5gYKBtuqv1AYYSkflOTeaRlv/kIo8D/jVcyjmO19tNJM8lQE1xCvhp
5maXOoSk1UoUmDprsKA2Em47J83sVivrIwBySB2n9srQynnV+8I47mX7YzYtNQ6uXdL3p/5e
FRW+yfqVCShhSfyQdOmJ978UyQEwY0+0hhK372KatmaL9KEkKSuXgsqshv3XiB9yu3Su1jw5
y2IQNP0=
''')

PUBLIC_SUBKEY = base64.b64decode(b'''
uI0EX0UFkQEEALU4+b/dzg0XLBByu3//Oo/E9eA6evMIzV39ktdXLZr2WiSEaK1lXNpInsmE
8oJg/iF6p2X6bz37WmfgFJtq8z4oPvmD1HYk7e5C8/axM71/K8/QO8W7G4lZdbLBGxyJoySb
2Rpj2B/w44AMBDABYmlzyhM3vdF74V08fYYmUWMTABEBAAE=
''')

UID = base64.b64decode(b'''
tCRnZW1hdG8gdGVzdCBrZXkgPGdlbWF0b0BleGFtcGxlLmNvbT4=
''')

# TODO: why do we have a different UID here?
EXPIRED_KEY_UID = base64.b64decode(b'''
tA9nZW1hdG8gdGVzdCBrZXk=
''')

PUBLIC_KEY_SIG = base64.b64decode(b'''
iQFOBBMBCAA4FiEEgeEsFr2NzWC+GAhFE2iA5yp7E4QFAltY2CkCGwMFCwkIBwIGFQoJCAsC
BBYCAwECHgECF4AACgkQE2iA5yp7E4Tgvwf+LO6xyMFvlS8rs0GhpbqeOsj39555QNEviRIL
19Pbie9QTZDpGBdTeqHcjX7j/KEQTsvBTZ4VHMujdJSQLNonjwvwgF+eDvFY+iAo0XiIoKXh
NkeadzAlz4xmrq2YnreuiR57Rr3o7vJ6y/y31dMmvc4u3662adC4RuAPmI/WpjNo8obE84fl
nN9awICBJeoZhpAZqZg323oiA7cbj/g0TTQLLJ6NL/Hmm1I7QAx51Aj+KgB6NqT/9wBkEs3Y
4wy6Ac9DQ5kwyEL1RCSQaPP6H6HX0eP+ebC1JDKahuPsqrB+1mEXyQJiRP4s4FSmJgQA1spg
1hj62rV11dnAPXryUQ==
''')

PUBLIC_SUBKEY_SIG = base64.b64decode(b'''
iQHrBBgBCAAgFiEEgeEsFr2NzWC+GAhFE2iA5yp7E4QFAl9FBZECGwIAvwkQE2iA5yp7E4S0
IAQZAQgAHRYhBH6d3jy+R+Q3QY33QDi50vdsyDPMBQJfRQWRAAoJEDi50vdsyDPMxF4EAJS/
MW4l9ZRg0JBhapqrE+NFiaym051NXrdWQc34ZVO0oAnStc1U0s7+6+o67tND9X3YDkmPfRvn
4x0FgBcWjfA8T6N/wzJSuTH76JE3voMBX7xebVJ89gP8p9oQx+HNXVtouj6b3cdSTWGHNAb2
Ji71DnkcDLD2l1P8wKSWCIO+K1sH/3WRcRlkZ9PXrsShDdLo8Cxip2tTPdFe8ahfSpix06ge
PPtGIwdGgeYMdZW+be4l5DEXJauXkGJ/EL4ipLg1TnSMcuMe9dglsnC+yE2kx92xcQLOIq0A
myPXdNtm8yxIQg4PFE6cX2lXuVuAb8EG+P5gG//9Waek02f4sWms+JDFjokk9YdUVp9ZHLrg
a9rtwAMhA6P8udfjcDru8Z52H48hTyVw6NMXQzlIxpH7i3N3vsLwzQqZM8+QfzXKslGcvExe
z1dpOqj/4iGFFn5b7X2G/CUak99fa2t6JiDmrtaYD5VX6UWxBvC6tjS4YPThSr77Rv+IbwjK
xQA+ptoUSGE=
''')

EXPIRED_KEY_SIG = base64.b64decode(b'''
iQFMBBMBCgA2AhsDBQsJCg0EAxUKCAIeAQIXgBYhBIHhLBa9jc1gvhgIRRNogOcqexOEBQJZ
8QlkBQkAAf5RAAoJEBNogOcqexOElMkH/2dcbW+AQFcenwmyCRuawABbNxKx2a5EVyvYUjco
NgnQbuuYGmKsm4BoZtZL/b7cGZAZWU5/vtGN4LoK0j8MfhRPDeFwjsVgmtF0gtX6ncdOQuE+
zl82PEfxtPIq2EQTykzSBDd+5nGxo2e/VdtKl/Q/53/LTp6G8YJVjIR7gwc9Xp/piAKs/54+
pC8yoSm+VKLNkT8egWgrLsiTi7Z8M4flFGYig0u/yPWA4rCnn5Kdyy5dV1C5xjuN0VZKAQI4
AYhG/MFsYOr37pxwJAeI47Odxolap4Ie5O82P1Z+jK8pcz6GlBR1JpNRGDPhr3aG0gak43nA
3ujfZW4nPadZdLg=
''')

REVOCATION_SIG = base64.b64decode(b'''
iQE2BCABCAAgFiEEgeEsFr2NzWC+GAhFE2iA5yp7E4QFAltY4FACHQIACgkQE2iA5yp7E4Qt
cAf9GcJV3dGybNGpw+gz+ZYdvcWpdvIKaQar9s74W9tdW2Vn9GlWYqUAid/xOCPeC8Ptemhe
zlVCV/jmQBrfM0myb6tSFsFqQq2cNmfISsYt7xphSvykXk05+l0KcSr9aYdV8SQUKomLp514
hmDhB/PzIv9gWq/tgblPHMxf9ZTIVkn9k2xEv1qOaJCF/BzkgcatDR21BiscX6psQtuEIDSf
qfgbH4Vg3E1oqtoIsMqjr1nroOarPhXZ35YblNzN9SGmEe1PwIY7um3jAPbJMHAp5pgwINbZ
DUXiYXhSEIvfp5xD4CXIju87B5hYsWLu4/9sNyhHLPmsLTMt69F6f1FTDA==
''')

OTHER_PUBLIC_KEY = base64.b64decode(b'''
mQENBFtYfqUBCAC5OuNuaZOMwyegRtKFzzLlwsJaO+q1L5EN8tVHdzRUwBmwKgC8PDNiM7UG
OhyN9Zasbeqvy1oF22nHIUgrDRkiB9m1k6E0FPvD2VzN1O7QiuKCjP8WaYhVRGYOXyCaaSPe
gqyidqPJz6AMDaZ38EWaZwGgJXmxzewUINPbepvyboTMZy5L9QiyfmKbsaW9BhW3qkKyIEnV
+k/S/NQdKcVX5xEXriDt0E5r3NNMC0pxIhwpchLPMnHohMKBUYn3BNA9CyN0V/lRYJFJUrh9
MnGkDkdYPSw9aYhvWEGOYnhW1bCl3ZLW6n2xVBpo5tK6PhJ+3lBCbzU3Lo6CtEbimkTxABEB
AAE=
''')

OTHER_PUBLIC_KEY_UID = base64.b64decode(b'''
tCpPdGhlciBnZW1hdG8gdGVzdCBrZXkgPGdlbWF0b0BleGFtcGxlLmNvbT4=
''')

OTHER_PUBLIC_KEY_SIG = base64.b64decode(b'''
iQFUBBMBCAA+FiEES4NJuQxW7n8FTVKHGCL1Qk622oEFAltYfqUCGwMFCQPCZwAFCwkIBwIG
FQoJCAsCBBYCAwECHgECF4AACgkQGCL1Qk622oGXKQf/fs5OriRSA3pj873WH3kp+7IP5ITn
mswLJkvZOk2aU35j2s7pZkgbKMRZbVxsHhU10q9/LD9HggGod7X2sQSD+B+ixtlmXhyQ4mAz
Ta0qzHp22mnMVr2VmaGRQGH7IzAXrlD1BH7EVfbSVZqdSrKRcXwjkAxlsPzLTQ9onhgLkk77
J3y0erP39ou/64ph2QZ3TglBXJc1gCsntV4Z8P+LGeCiop0rAgXHTe0Fdf8APOoI4qwfK0gs
i9h1aPPupEv+XU+/iQ4QbTsKLYK+XnCAyapgiW2vjYbnRQepmB8zyfvs4W7zH3i7Ah+wupSt
idKDxfLtKvHnpiX/9mfMxre1zA==
''')
