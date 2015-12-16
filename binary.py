numbf = 0
numb = 0
t_total = 0
f_total = 0

while numb < 998:
    numb = numb + 3
    #print numb
    t_total += numb

print "The total for items divisible by three is: "
print t_total

while numbf < 995:
    numbf = numbf + 5
    #print numbf
    f_total += numbf

print "The total for items divisible by five is: "
print f_total

total = t_total + f_total
print total

totalx = 0

for nuts in range(0, 995):

    if nuts % 15 == 0:
        #print nuts
        totalx += nuts

print "The total for numbers divisible by both is: "
print totalx

tt_total = total - totalx

print "Our final number is: "
print tt_total
