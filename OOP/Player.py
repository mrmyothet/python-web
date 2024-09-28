class Player:
    team = "Man U"

    def __init__(self) -> None:
        self.name = "Aung Aung"
        self._age = 21  # protected # convention
        self.__num = 7  # private

    def show_player_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self._age}")
        print(f"Number : {self.__num}")

    @classmethod
    def show_team_name(cls):
        print("Team Name : {}".format(cls.team))


player_1 = Player()

Player.show_player_info(player_1)
player_1.show_player_info()

# print(player_1.__num)

# Player.__num
