# Question 1
cool_string = "Hello world";
print (cool_string);

# Question 2
def greeting(name):
    print(f"Hello, {name}! Welcome to Python!");
# Must have f before the string for it to pass name variable.
greeting("shane");

# Question 3
movieList = ["Shang Chi", "Hachi", "Blade", "Mario"];
print(movieList);

# Question 4
print(movieList[1]) ;

# Question 5
movieList.append("Iron man");
print(movieList);

# Question 6
cellphone = {
    "type": "Iphone",
    "color": "Rose Gold",
    "number": "555-404-5555"
};

# Question 7
print(cellphone["color"]);
print(cellphone["number"]);
print(cellphone["type"]);

# Question 8
sentence = "hello, this is a sentence.";

# Question 9
C = sentence.capitalize();
print(C);

# Bonus Question 10
students_in_order = {
  1: {'name': 'Esteban', 'age': '27', 'eye color': 'blue'},
  2: {'name': 'Jackson', 'age': '22', 'eye color': 'brown'},
  3: {'name': 'Zayn', 'age': '26', 'eye color': 'green'}
};

# Bonus 10 A
print(students_in_order[2]);

# Bonus 10 B
print(students_in_order[3]["name"]);

# Bonus 10 C
print(students_in_order[1]["name"], students_in_order[1]["age"]);
# Must call the object each time 