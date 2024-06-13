def interleave(a, b):
    return ''.join(''.join(pair) for pair in zip(a, b))
print(interleave('lzr','iad'))

zipped = list(zip([2,4,6,8],[5,10,15,20]))
print(zipped)
unzipped = zip(*zipped)
print(list(unzipped))

midterms = [89,91,78]
finals = [86,98,76]
students = ["Andy","Haley","Dylan"]

scorelist_combined = zip(students,finals,midterms)
print(list(scorelist_combined))

scorelist_final = dict(zip(students,max(finals,midterms)))
print(scorelist_final)