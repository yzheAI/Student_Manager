

class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, s_id, score):
        super().__init__(self.name)
        self.s_id = s_id
        self.score = score
    def show(self):
        print(f"name: {self.name},id:{self.s_id}, score: {self.score}")
    def to_dict(self):
        return {"name": self.name,
                "s_id": self.s_id,
                "score": self.score}
    @staticmethod
    def from_dict(data):
        return Student(
            data['name'],
            data['s_id'],
            data['score']
        )
