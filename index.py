# # # Question 1
# cool_string = "Hello world";
# print (cool_string);

# # # Question 2
# def greeting(name, age):
#     print(f"Hello, {name}! You are {age} years old!");
# # # Must have f before the string for it to pass a variable.
# # # Added more variables to get a better understanding
# greeting("shane", 24);

# # # Question 3
# movieList = ["Shang Chi", "Hachi", "Blade", "Mario"];
# print(movieList);

# # # Question 4
# print(movieList[1]) ;

# # # Question 5
# movieList.append("Iron man");
# print(movieList);

# # # Question 6
# cellphone = {
#     "type": "Iphone",
#     "color": "Rose Gold",
#     "number": "555-404-5555"
# };

# # # Question 7
# print(cellphone["color"]);
# print(cellphone["number"]);
# print(cellphone["type"]);

# # # Question 8
# sentence = "hello, this is a sentence.";

# # # Question 9
# C = sentence.capitalize();
# print(C);

# # # Bonus Question 10
# students_in_order = {
#   1: {'name': 'Esteban', 'age': '27', 'eye color': 'blue'},
#   2: {'name': 'Jackson', 'age': '22', 'eye color': 'brown'},
#   3: {'name': 'Zayn', 'age': '26', 'eye color': 'green'}
# };

# # # Bonus 10 A
# print(students_in_order[2]);

# # # Bonus 10 B
# print(students_in_order[3]["name"]);

# # # Bonus 10 C
# print(students_in_order[1]["name"], students_in_order[1]["age"]);
# Must call the object each time 

# # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# #Section 1 - sets and tuples:
# #Pre-Question: Take a look at this JavaScript Array:
# # let javaScriptArray = [12, 55, 33, 40, 55, 33, 20, 12]

# # How would you remove duplicates from this JavaScript Array? Take a few minutes to consider what steps are necessary to iterate through this array in JavaScript and remove the duplicates values.

# # What advantages are available when we're working with Python? If this Array was instead a set, we wouldn't be able to store multiple values in it. Uncomment the identical set below and run the print statement. What did you notice in the console return?

# my_set = {12, 55, 33, 40, 55, 33, 20, 12}

# print(my_set)

# #Question 1a: Create a set of your own with at least 3 different elements.
# mySet = {"grey", "black", "white", "pink"};

# #Question 1b: Add an item to the set that you just created.
# mySet.add("orange");

# #Question 1c: Print the set with the new data that you added to it:
# print(mySet);

# #Question 2a: Create a tuple with at least 3 elements inside of it.
# myTuple = ("mouse", "keyboard", "headphones", "monitor");

# #Question 2b: Print the tuple you just created.
# print(myTuple);


# #Section 2 - loops:

# # Question 3: Use a for loop to iterate through the 'days' list above and print the days of the week:
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# for x in days:
#   print(x)

# # Question 4:Loop through add_list and add each value to x. Print the value of x at each increment:
# x = 10
# add_list = [10, 6, 12, 4, 5]

# for value in add_list:    
#   results = value + x

#   print(results)

# # Question 5: While Loops 
# #Declare an iterator variable (set to the number 1) and write a While loop that adds 5 to the value of the variable starting_value as long as the iterator is under 10:
# print("<------------------------->")

# starting_value = 5
# iterator = 1 

# while iterator < 10:
#   starting_value += 5
#   print(starting_value)
#   iterator += 1

# #Section 3 - conditionals: if, elif, else statements

# favorite_movie = "Shang Chi"    
# favorite_movie = "Fury"   
 
# #Question 6a: 
# #Below, write a conditional statement that prints the string "that's a great movie" if the favorite_movie variable equals your favorite movie.
# #Otherwise (else), print the string "that's not my favorite movie".  
# #Mess around with the value of the favorite_movie variable and trigger both conditional responses:
# if favorite_movie == "Shang Chi":
#   print("This is a great movie!")
# else:
#   print("That isn't a great movie. :(")


# #Question 6b: Uncomment the movie_list variable below and implement a for loop that iterates through each item in the list. 
# #If the item is a blueberry (or another fruit), print "item is a fruit and not movie"; 
# #if the item is a car manufacturing company like Toyota, print "item is a car and not a movie"; 
# #otherwise, just print the movie in the list:

# movie_list = ["Inception", "blueberries", "Toyota", "Good Will Hunting"]

# for movie in movie_list:
#   print(movie);


# #BONUS - conditional and operators practice:
# a = 5
# b = 5
# c = 12
# #Question 7a: Use the correct operator to add variables a & c:
# results_add = a + c
# print("Adding them together you get", results_add)

# #Question 7b: Use the correct operator to subtract variables b & c:
# resultsSub = b - c
# print("subtracting them you get", resultsSub)

# #Question 7c: Use the correct comparison operator that shows if variables a & b equal each other:
# resultsEqual = a == b
# print(resultsEqual, "a & b are equal.")

# #Question 7d: Use the correct operator to find the quotient of variables c & a
# results_quotient = c / a
# print("the quotient of C & A are", results_quotient)

# #Question 7e: Use the correct operator to find if variables c & b are not equal to each other:
# results_not_equal = c != b
# print("Are C & B not equal?", results_not_equal)


print("Activity 3, Function Definition Practice:")
# 1. Function that accepts no arguments. It's called say_hello and returns nothing, just prints 'hello'.
def say_hello():
    print("Hello World");

say_hello() #this calls the function

# 2. a 'sum' function that accepts two integers and returns the sum.
def sum_of_two(a,b):
    return a + b

result = sum_of_two(10,15)
print("The sum is", result)

# 3. an 'average' function that accepts two numbers and returns the average.
def average_of_two(x,y):
    return(x + y) / 2

result = average_of_two(5, 10)
print("The average is", result)

# 4. A function that accepts a first name and a last name and formats it to "{last_name}, {first_name}" (returns a string).
def first_last(first_name, last_name):
    return f"{last_name}, {first_name}"

formattedName = first_last("Shane", "Fox")
print(formattedName)

# 5. A function that accepts a first name, last name, graduation year, and student number and returns those four items together in a list.
def student_info(first_name, last_name, graduation_year, student_number):
    return[first_name, last_name, graduation_year, student_number]

info = student_info("Shane", "Fox", 2019, "1014796")
print(info)

# 6. A function that accepts an integer and returns whether it is above 18 or not (Boolean).
def above18(age):
    return age > 18

result = above18(24)
print(result)

result = above18(16)
print(result)

#7. A function that accepts a string and prints the string in reverse (no return value).
def printReverse(s):
    print(s[::-1])

printReverse("Hello")
