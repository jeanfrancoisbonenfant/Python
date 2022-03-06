#exemple of list
bicycle = ['trek', 'cannondale', 'redline', 'specialized']

#loop through list with Capitalization and skip line

for i in range(len(bicycle)):
    print(bicycle[i].title(), "\n") 


#loop F-string usage with previous skip line using empty print  
 
for i in range(len(bicycle)):
    print()
    print(f'My first mountain bike was a {bicycle[i].title()}')
    
