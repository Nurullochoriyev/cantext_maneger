
# UYGA VAZIFA

class Cantextmanager:
    def __init__(self,file_name,mode):
        self.file_name=file_name
        self.mode=mode
        self.fayl=None

    def __enter__(self):
        print(f"fayl ochyapmiz  {self.file_name}")
        self.fayl=open(self.file_name,self.mode)
        return self.fayl
    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f"faylni yopmoqdamiz {self.file_name}")
        if self.fayl:
            self.fayl.close()
        if exc_type:
            print(f"xatolik {exc_value}")
with Cantextmanager("dekaratr_cantext.py", "r") as file:
    print("fayl o'qilmoqdsa")
    zoo=file.read()
    print("faylni mazmuni")
    print(zoo)