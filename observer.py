
class Subject:

    def __init__(self):
        self.observers = set()

    def add_observer(self, observer):
        self.observers.add(observer)

    def notify(self):
        for observer in observers:
            pass


class Observer:

    def __init__(self):
        pass

    def add_subjects(self, subjects):
        for subject in subjects:
            subject.add_observer(self)

    def notified(self, subject):
        print(subject)
