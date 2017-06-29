file_obj = open('lyrics.txt','r')
string = file_obj.read()

for x in string:
    if (x in [',','.','\'']):
        string = string.replace(x, '')

arr = string.split()
sum = 0

for x in arr:
    sum = sum + (len(x))

float(sum)/len(arr)
