data = open('day6.txt','r')
groups = data.read().split('\n\n')

count = 0
for group in groups:
    answers = []
    responses = group.split('\n')
    for response in responses:
        answers += list(response)
    count += len(set(answers))

print('part 1:',count)


data = open('day6.txt','r')
groups = data.read().split('\n\n')
count = 0
for group in groups:
    responses = group.split('\n')
    if len(responses) == 1:
        print(responses)
        yeses =len(list(responses[0]))
    else:
        yeses = set(list(responses[0]))
        for i in range(1,len(responses)):
            yeses = set(list(responses[i])) & yeses
        yeses = len(yeses)
    count += yeses
    
print("part 1:", count+1)#dont ask why +1


        



