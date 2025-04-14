class Human:
    def breath(self):
        print("Breathing...")


class Developer(Human):
    def code(self):
        print("Coding...")

    def breath(self):
        super().breath()
        print("Breathing123...")


class Frontend(Developer):
    pass


dev = Frontend()
dev.breath()
dev.code()
