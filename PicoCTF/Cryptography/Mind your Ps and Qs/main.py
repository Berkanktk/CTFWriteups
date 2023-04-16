from Crypto.Util.number import inverse, long_to_bytes

# n = p * q
# phi = (p - 1) * (q - 1)
# d = inverse(e, phi)
# m = pow(c, d, n)
# p and q are prime numbers. We can factor n using factordb.com to get p and q.

n = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e = 65537
c = 964354128913912393938480857590969826308054462950561875638492039363373779803642185

p = 2434792384523484381583634042478415057961
q = 650809615742055581459820253356987396346063

phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)

print(long_to_bytes(m).decode())
