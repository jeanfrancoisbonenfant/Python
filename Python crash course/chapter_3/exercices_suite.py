from audioop import reverse


bucket = ["Japon", "Maroc", "Thailand", "France", "Germany"]

print(bucket)

print()
print(sorted(bucket))

print()
print(bucket)

print()
print(sorted(bucket, reverse=True))

print()
print(bucket)

print()
bucket.reverse()
print(bucket)

print()
bucket.reverse()
print(bucket)

print()
bucket.sort()
print(bucket)

print()
bucket.sort(reverse=True)
print(bucket)
