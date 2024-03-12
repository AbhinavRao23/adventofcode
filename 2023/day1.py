file = open("./day1.txt")
text = file.read()

chardig = {'one':'1', 
           'two':'2', 
           'three':'3', 
           'four':'4', 
           'five':'5',
           'six':'6', 
           'seven':'7', 
           'eight':'8', 
           'nine':'9'}

def charcheck(chars):
    string = ''.join(chars)
    if string[-3:] in chardig:
        return chardig[string[-3:]]
    elif string[-4:] in chardig:
        return chardig[string[-4:]]
    elif string[-5:] in chardig:
        return chardig[string[-5:]]
    else:
        return False

ans = 0
for line in text.splitlines():
    nums = []
    chars = []
    for char in line:
        if char.isdigit():
            nums.append(char)
            chars = []
        else:
            chars.append(char)
            flag = charcheck(chars)
            if flag != False:
                nums.append(flag)
    ans += int(nums[0] + nums[-1])
    
print(ans)