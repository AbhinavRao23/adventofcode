count = 0
for i in range(146810,612565):
    digits = [int(char) for char in str(i)]
    if digits == sorted(digits):
        if len(digits) > len(set(digits)):
            count += 1
    else:
        pass
print(count)


count = 0
for i in range(146810,612565):
    digits = [int(char) for char in str(i)]
    if digits == sorted(digits):
        if len(digits) > len(set(digits)):
            freq = []
            for digit in digits:
                freq.append(digits.count(digit))
            if 2 in freq:
                count+=1
    else:
        pass
print(count)