class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __getattribute__(self, __name: str):
        print(f"they want to get {__name}")
        return "😆"

kai = Dog("kai")
print(kai.name)
