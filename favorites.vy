# pragma version 0.4.0
# @ license MIT

struct Person:
    favorite_number: uint256
    name: String[100]

# state variable
my_name: public(String[100])
my_favorite_number: public(uint256)
favorite_number: public(uint256)


list_of_numbers: public(uint256[5])
list_of_people: public(Person[5])
index: public(uint256)

# Hashmap or mappings
name_to_favorite_number: public( HashMap [String[100], uint256] )
# Mark, 124

# deploy Function
@deploy
def __init__():
    self.my_favorite_number = 7
    self.index = 0
    self.my_name= "Imran"
    self.favorite_number = 10

# store function
@external
def store (new_number: uint256):
    self.my_favorite_number = new_number

@external
def add (new_number: uint256):
    self.favorite_number = new_number + 1 

# view function
@external
@view
def retrieve() -> uint256:
    return self.my_favorite_number

@external
def add_person(name: String[100], favorite_number: uint256):
    # Add favorite number to the number list
    self.list_of_numbers[self.index] = favorite_number

    # Add the person to the person's list 
    new_person: Person = Person(favorite_number = favorite_number, name = name)
    self.list_of_people[self.index] = new_person

# Add the person to the hashmap
    self.name_to_favorite_number[name] = favorite_number
 
    self.index = self.index + 1
    
