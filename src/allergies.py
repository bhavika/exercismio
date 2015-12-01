class Allergies:

    allergies = ['eggs', 'peanuts', 'shellfish', 'strawberries',
                 'tomatoes', 'chocolate', 'pollen', 'cats']


    def __init__(self, allergyscore):
        self.allergyscore = allergyscore

    def is_allergic_to(self, allergy):
        for a in enumerate(self.allergies):
            if 2 ** self.allergies.index(allergy) <= self.allergyscore:
                return True
            else:
                return False

    @property
    def lst(self):
        return [allergy for allergy in self.allergies if self.is_allergic_to(allergy)]

