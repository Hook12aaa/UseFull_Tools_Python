
class ascii_validator():
    """ This is an ascii validator
    To use it enter with the folowing type you want begining with only
        * "only_caps" = For captial letters,
        * "only_lower" = For only lower charracters,
        * "only_chr" = Full strings no matter if it's caps or not,
        * "only_num" = Only numbers with no characters
    Example of the code
        if ____.only_caps(WordToCheck):
            print("The word is correct")

    """

    def only_caps(self,Value):
        """ For only captial letters Look at ascii vaildator for an example"""
        Error= False
        for i in Value:
            if ord(i) < 65 or 90 < ord(i) and ord(i) != 32:
                Error = True
        return Error

    def only_num(self,Value):
        """ For only numbers Look at ascii vaildator for an example"""
        Error= False
        for i in Value:
            if ord(i) < 48 or 57 < ord(i):
                Error = True
        return Error

    def only_lower(self,Value):
        """ For only lower letters Look at ascii vaildator for an example"""
        Error= False
        for i in Value:
            if ord(i) < 97 or 122 < ord(i) and ord(i) != 32:
                Error = True
        return Error

    def only_chr(self,Input):
        """ For only strings with no other charracters Look at ascii vaildator for an example"""
        Value= Input.lower()
        Error= False
        for i in Value:
            if ord(i) < 97 or 122 < ord(i) and ord(i) != 32:
                Error = True
        return Error

