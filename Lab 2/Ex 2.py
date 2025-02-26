s = input("cuvantul este ")
pl = s[0]
sn = s.replace(pl, '', -1)
n = len(sn)
print(f"După ștergerea literei '{pl}' șirul obținut este '{sn}' de lungime {n}")
print("După ștergerea literei '{}' șirul obținut este '{}' de lungime {}".format(pl, sn, n))
print("După ștergerea literei '{0}' șirul obținut este '{1}' de lungime {2}".format(pl, sn, n))