sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

x = sentence.split()

result ={word:len(word) for word in x}

print(result)
