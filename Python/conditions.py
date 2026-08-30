# if/elif/else statement 
tokens = 1000
if tokens > 500:
    print(f"tokens used is greater than 500, {tokens} tokens used.")
elif tokens >  100:
    print(f"tokens used is equal to 500, {tokens} tokens used.")
else:
    print(f"tokens used is less than 100, {tokens} tokens used.")      

#short hand if/else statement
if tokens > 500: print(f"tokens used is greater than 500, {tokens} tokens used.")
elif tokens >  100: print(f"tokens used is equal to 500, {tokens} tokens used.")    
else: print(f"tokens used is less than 100, {tokens} tokens used.")