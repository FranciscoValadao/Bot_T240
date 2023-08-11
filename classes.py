class Usuario:
    def __init__(self,name,n_workouts):
        self.name = name
        self.n_workouts = n_workouts

    def get_msg(self):
        mess = "{} = {}/240".format(self.name, self.n_workouts)
        return mess

    def set_workout(self):
        self.n_workouts += 1

    def undo_workout(self):
        self.n_workouts -=1

    def get_workout(self):
        return self.n_workouts

    def create_newuser(self):
        pass