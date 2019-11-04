class MockSignal:
    def __init__(self):
        self.call_count = 0

    def reset_counter(self):
        self.call_count = 0
        
    def movedSignalReceived(self, x: float, y: float):
        self.call_count += 1
        print("Signal received, call count: {}".format(self.call_count))
        print("Moved to x: {} y: {}".format(x, y))
