import random


class TestModel:

    def feedforward(self, data):
        return random.random()

    def mutate(self):
        pass


if __name__ == '__main__':
    model = TestModel()
    print(model.feedforward())
