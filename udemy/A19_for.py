"""
Laço For
for / else em Python
"""

volante = ["01", "02", "03", "14", "15", "06"]

for n in volante:
    if n.startswith("1"):
        print('Esse começa com 1:', n)
    else:
        print('Esse não começa com 1:', n)
