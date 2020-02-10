class Mouse:
  # Class to Calculate the evolution of nomber of mice

    def __init__(self):
        ### Initialization method ###

        self.turn = 1

        self.nb_male_plus6 = 1
        self.nb_female_plus6 = 1

        self.nb_femelle_gestation_0s = 0

        self.nb_male_age_0s = 0
        self.nb_female_age_0s = 0

        self.nb_male_age_3s = 0
        self.nb_female_age_3s = 0

        self.update_population()

    def __str__(self):
        # Method to display the number of mice
        return str(self.population_current)


    def update_population(self):
        # Method to display in a hash the population afetr 3 weeks

        self.population_current = {

          'Semaines' : (self.turn-1)*3,
          'nb_male_plus6' : self.nb_male_plus6 ,
          'nb_female_plus6': self.nb_female_plus6 ,

          'nb_femelle_gestation_0s': self.nb_femelle_gestation_0s ,

          'nb_male_age_0s': self.nb_male_age_0s ,
          'nb_female_age_0s': self.nb_female_age_0s ,

          'nb_male_age_3s': self.nb_male_age_3s ,
          'nb_female_age_3s': self.nb_female_age_3s ,

          'Total adulte : ' : self.nb_male_plus6 + self.nb_female_plus6 + self.nb_femelle_gestation_0s , 
          'Total enfant : ' : self.nb_male_age_0s + self.nb_female_age_0s + self.nb_male_age_3s + self.nb_female_age_3s, 
          'Total à venir : ' : self.nb_femelle_gestation_0s *8,
          'total : ' : self.nb_male_plus6 + self.nb_female_plus6 + self.nb_femelle_gestation_0s + self.nb_male_age_0s + self.nb_female_age_0s + self.nb_male_age_3s + self.nb_female_age_3s + self.nb_femelle_gestation_0s *8

        }

        return self.population_current

    def next_turn(self):

        # Tour suivant
        self.turn += 1

        # Sauvegarde tour précédant
        self.population_previous = self.population_current

        # Gestion des adultes
        self.nb_male_plus6 = self.population_previous['nb_male_plus6'] + self.population_previous['nb_male_age_3s']
        self.nb_female_plus6 = self.population_previous['nb_female_age_3s'] + self.population_previous['nb_femelle_gestation_0s']

        # Les femelles tombent enceinte
        self.nb_femelle_gestation_0s = self.population_previous['nb_female_plus6']

        # Naissance Male et femelle à 50% après les 3 s de gestation
        self.nb_male_age_0s = self.population_previous['nb_femelle_gestation_0s']*8/2 
        self.nb_female_age_0s = self.population_previous['nb_femelle_gestation_0s']*8/2

        # Ceux de 0s grandissent à 3s
        self.nb_male_age_3s = self.population_previous['nb_male_age_0s']
        self.nb_female_age_3s = self.population_previous['nb_female_age_0s']

        self.update_population()

        return "ok"
