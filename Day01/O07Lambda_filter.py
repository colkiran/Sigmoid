
l = list(range(1, 31))
print(f"list :{l}")

res = list(filter(lambda x: x % 3 == 0, l))
print(f"res :{res}")

print("-" * 60)

sentence = "the quick brown fox jumps over the lazy dog"
print(F'sentence :{sentence}')

res = list(filter(lambda st: st != 'the', sentence.split()))
print(f"res :{res}")
