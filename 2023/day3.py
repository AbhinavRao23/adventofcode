file = open("./day3.txt")
text = file.read()
data = [[char for char in line] for line in text.splitlines()]

rows = len(data)
cols = len(data[0])

i,j = 0,0
while i<rows:
    while j < cols:
        num = []
        if data[i][j].isalnum():
            start_col = j
            while j<cols:
                if not data[i][j].isalnum():
                    break
                num.append(data[i][j])
                j+=1
            num_str = ''.join(num)
            num = int(num_str)
            
        j+=1
    j = 0
    i+=1