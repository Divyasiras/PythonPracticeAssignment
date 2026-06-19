#3. Predict the output:
# Which line will raise an error and why?

# Error
#line 5 tpl[0] = 100
#TypeError: 'tuple' object does not support item

# Why? 
# tpl[0] = 100 causes an error because tuples are immutable, while lists are mutable. 

lst = [10, 20, 30]
tpl = (10, 20, 30)

lst[0] = 100
tpl[0] = 100

