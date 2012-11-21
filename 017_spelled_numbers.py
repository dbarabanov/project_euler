#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

n = {0: '', 1:'one', 2:'two', 3: 'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10: 'ten', 11:'eleven', 12:'twelve', 13: 'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred'}

total = 0
def emit(s):
    global total
#    print s
    total+=len(s)
for i in  range(1, 10):
    emit(n[i])

for i in  range(10, 20):
    emit(n[i])
for i in [20,30,40,50,60,70,80,90]:
    for j in range(0,10):
        emit(n[i]+n[j])

for h in range(1,10):
    emit(n[h]+n[100])
    pref = n[h]+n[100]+'and'
    for i in  range(1, 10):
        emit(pref+n[i])
    for i in  range(10, 20):
        emit(pref+n[i])
    for i in [20,30,40,50,60,70,80,90]:
        for j in range(0,10):
            emit(pref+n[i]+n[j])
emit('onethousand')

print total
#21124
