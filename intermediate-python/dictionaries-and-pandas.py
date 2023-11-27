""" Motivation for dictionaries
To see why dictionaries are useful, have a look at the two lists defined in the script. countries contains the names of some European countries. capitals lists the corresponding names of their capital.

Instructions
Use the index() method on countries to find the index of 'germany'. Store this index as ind_ger.
Use ind_ger to access the capital of Germany from the capitals list. Print it out.
"""

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ing_ger = countries.index("germany")

# Use ind_ger to print out capital of Germany
print(capitals[ing_ger])


""" Create dictionary
The countries and capitals lists are again available in the script. It's your job to convert this data to a dictionary where the country names are the keys and the capitals are the corresponding values. As a refresher, here is a recipe for creating a dictionary:

my_dict = {
   "key1":"value1",
   "key2":"value2",
}
In this recipe, both the keys and the values are strings. This will also be the case for this exercise.

Instructions
With the strings in countries and capitals, create a dictionary called europe with 4 key:value pairs. Beware of capitalization! Make sure you use lowercase characters everywhere.
Print out europe to see if the result is what you expected.
"""

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid', "france":"paris", "germany":"berlin", "norway":"oslo" }

# Print europe
print(europe)


""" Access dictionary
If the keys of a dictionary are chosen wisely, accessing the values in a dictionary is easy and intuitive. For example, to get the capital for France from europe you can use:

europe['france']
Here, 'france' is the key and 'paris' the value is returned.

Instructions
Check out which keys are in europe by calling the keys() method on europe. Print out the result.
Print out the value that belongs to the key 'norway'.
"""

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe["norway"])


""" Dictionary Manipulation (1)
If you know how to access a dictionary, you can also assign a new value to it. To add a new key-value pair to europe you can use something like this:

europe['iceland'] = 'reykjavik'
Instructions
Add the key 'italy' with the value 'rome' to europe.
To assert that 'italy' is now a key in europe, print out 'italy' in europe.
Add another key:value pair to europe: 'poland' is the key, 'warsaw' is the corresponding value.
Print out europe.
"""

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe["italy"] = "rome"

# Print out italy in europe
print("italy" in europe)

# Add poland to europe
europe["poland"] = "warsaw"

# Print europe
print(europe)


""" Dictionary Manipulation (2)
Somebody thought it would be funny to mess with your accurately generated dictionary. An adapted version of the europe dictionary is available in the script.

Can you clean up? Do not do this by adapting the definition of europe, but by adding Python commands to the script to update and remove key:value pairs.

Instructions
The capital of Germany is not 'bonn'; it's 'berlin'. Update its value.
Australia is not in Europe, Austria is! Remove the key 'australia' from europe.
Print out europe to see if your cleaning work paid off.
"""

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe["germany"] = "berlin"

# Remove australia
europe.pop("australia")

# Print europe
print(europe)


""" Dictionariception
Remember lists? They could contain anything, even other lists. Well, for dictionaries the same holds. Dictionaries can contain key:value pairs where the values are again dictionaries.

As an example, have a look at the script where another version of europe - the dictionary you've been working with all along - is coded. The keys are still the country names, but the values are dictionaries that contain more information than just the capital.

It's perfectly possible to chain square brackets to select elements. To fetch the population for Spain from europe, for example, you need:

europe['spain']['population']
Instructions
Use chained square brackets to select and print out the capital of France.
Create a dictionary, named data, with the keys 'capital' and 'population'. Set them to 'rome' and 59.83, respectively.
Add a new key-value pair to europe; the key is 'italy' and the value is data, the dictionary you just built.
"""

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe["france"]["capital"])

# Create sub-dictionary data
data = {
    "capital": "rome",
    "population": 59.83,
}

# Add data to europe under key 'italy'
europe["italy"] = data

# Print europe
print(europe)


