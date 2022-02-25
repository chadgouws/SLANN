import random


class TestModel:

    def feedforward(self):
        return random.random()


if __name__ == '__main__':
    model = TestModel()
    print(model.feedforward())
