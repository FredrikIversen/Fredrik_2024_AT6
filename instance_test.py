from user_input_validator import UserInputValidator

validator1 = UserInputValidator()
validator2 = UserInputValidator()

list1 = ["34","32","0","fdas","43"]
list2 = ("safw","2","-4","0","32")

validator = UserInputValidator()


# Instance 1
a = validator.validate_positive_integers(list1)
print(a)
a2 = validator.validation_message(list1)


# Instance 2
b = validator.validate_positive_integers(list2)
print(b)
b2 = validator.validation_message(list2)
