from math import sqrt
def factors(n):
	# 1 and n are automatically factors of n
	fact=[1,n]
	# starting at 2 as we have already dealt with 1
	check=2
	# calculate the square root of n and use this as the 
	# limit when checking if a number is divisible as 
	# factors above sqrt(n) will already be calculated as 
	# the inverse of a lower factor IE. finding factors of 
	# 100 only need go up to 10 (sqrt(100)=10) as factors 
	# such as 25 can be found when 5 is found to be a 
	# factor 100/5=25
	rootn=sqrt(n)
	while check<rootn:
		if n%check==0:
			fact.append(check)
			fact.append(n/check)
		check+=1
	# this line checks the sqrt of the number to see if 
	# it is a factor putting it here prevents it appearing 
	# twice in the above while loop and putting it outside
	# the loop should save some time.
	if rootn==check:
		fact.append(check)
	# return an array of factors sorted into numerial order.
	fact.sort()
	return fact

for i in range(1,100000):
	now = (i + 1)*i/2
	factlist = factors(now)
	if len(factlist) > 500:
		print(now)
		break

