# discount calculation on the cost
# cost > 10,000 => 20% 
# cost > 7,000 => 15%
# cost > 5,000 => 10%
# cost > 3,000 => 5%
# cost < 3,000 => 0% 

cost = int(input("Enter the value of the cost : "))

discount = 0 

# calculate discount 
if cost >= 10000: 
    discount = cost * (20/100)
elif cost >= 7000:
    discount = cost * (15/100)
elif cost >= 5000:
    discount = cost * (10/100)
elif cost >= 3000: 
    discount = cost * (5/100)
else: 
    discount = 0 

# calculate actual cost 
actual_cost = cost - discount

print(f"Actual Cost : {actual_cost}")