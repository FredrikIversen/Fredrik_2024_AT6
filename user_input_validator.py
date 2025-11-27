class UserInputValidator: 
    
    def validate_positive_integers(self, items):
        list_positive_integers = []
        for s in items: 
            if s.isdigit(): 
                num = int(s)
                if num > 0:
                    list_positive_integers.append(num)
        return list_positive_integers
    
    def validation_message(self, items):
        # Only prints a message if a real list or tuple and has items
        if items and isinstance(items, (list, tuple)):
            result = self.validate_positive_integers(items)
            print("List has been validated!")
            return result
        else:
            # No message if empty, not a list, or string
            return self.validate_positive_integers(items)
