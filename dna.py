import random

class DNA:
    def __init__(self, male_aggressiveness, female_aggressiveness, speed, strength, size_variation, color_variation, eating_speed, attractiveness):
        self._male_aggressiveness = male_aggressiveness
        self._female_aggressiveness = female_aggressiveness
        self._speed = speed
        self._strength = strength
        self._size_variation = size_variation
        self._color_variation = color_variation
        self._eating_speed = eating_speed
        self._attractiveness = attractiveness

    # Getters
    @property
    def male_aggressiveness(self):
        return self._male_aggressiveness

    @property
    def female_aggressiveness(self):
        return self._female_aggressiveness

    @property
    def speed(self):
        return self._speed

    @property
    def strength(self):
        return self._strength

    @property
    def size_variation(self):
        return self._size_variation

    @property
    def color_variation(self):
        return self._color_variation

    @property
    def eating_speed(self):
        return self._eating_speed

    @property
    def attractiveness(self):
        return self._attractiveness

    # Setters
    @male_aggressiveness.setter
    def male_aggressiveness(self, value):
        self._male_aggressiveness = value

    @female_aggressiveness.setter
    def female_aggressiveness(self, value):
        self._female_aggressiveness = value

    @speed.setter
    def speed(self, value):
        self._speed = value

    @strength.setter
    def strength(self, value):
        self._strength = value

    @size_variation.setter
    def size_variation(self, value):
        self._size_variation = value

    @color_variation.setter
    def color_variation(self, value):
        self._color_variation = value

    @eating_speed.setter
    def eating_speed(self, value):
        self._eating_speed = value

    @attractiveness.setter
    def attractiveness(self, value):
        self._attractiveness = value
  
def makeRandomDNA():
    male_aggressiveness = random.uniform(0, 1)
    female_aggressiveness = random.uniform(0, 1)
    speed = random.uniform(5, 15)
    strength = random.uniform(0, 1)
    size_variation = random.uniform(0, 20)
    color_variation = (
        random.randint(0, 50),
        random.randint(0, 50),
        random.randint(0, 50)
    )
    eating_speed = random.uniform(1, 10)
    attractiveness = random.uniform(0, 1)
    return DNA(
        male_aggressiveness,
        female_aggressiveness,
        speed,
        strength,
        size_variation,
        color_variation,
        eating_speed,
        attractiveness
    )
