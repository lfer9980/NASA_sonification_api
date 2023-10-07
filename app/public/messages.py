import json

class Message(dict):
    """Messages class"""

    def __init__(self, eng_msg: str, esp_msg: str):
        """Message constructor"""

        self.en = eng_msg
        self.es = esp_msg
    
    def __repr__(self) -> str:
        """Return method"""

        return  f"message: {repr(self.__dict__)}"
    
    def json(self):
        """Return message as dict"""

        return  json.dumps({"message": repr(self.__dict__)})


class Error(Message):
    """Error message class"""

    def __init__(self, eng_msg: str, esp_msg: str):
        """Constructor message"""

        super().__init__(eng_msg, esp_msg)

        self.code = False


class Success(Message):
    """Succes message class"""

    def __init__(self, eng_msg: str, esp_msg: str):
        """Constructor message"""

        super().__init__(eng_msg, esp_msg)

        self.code = True
        
if __name__ == "__main__":
    
    test = Success("test", "prueba")
    
    print(test)