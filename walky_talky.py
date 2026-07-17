import time
from pathlib import Path

class ConnectionNotFoundError(Exception):
    pass

class bothway:
    def __init__(self,id_code):
        self.id_code = str(id_code)
        try:
            with open(self.id_code + "1") as h:
                pass
            self.id_code += "2"
            print()
        except:
            self.id_code += "1"
        with open(self.id_code, "w"):pass
        tran = True
        if self.id_code[-1] == "1":
            while tran:
                try:
                    open(self.id_code[:-1]+"2")
                    print(self.id_code)
                    tran = False
                except:
                    #print("No connection with the id of {self.id_code[:-1]} was located, waiting for responce")
                    time.sleep(1)
        print(self.id_code)

    def read(self):
        while True:
            try:
                with open(self.id_code[:-1]+ ("1" if self.id_code[-1] == "2" else "2")) as h:
                    self.trasmition_located = True
                    t = h.read()
                    t = t.split(";")
                    self.convo = t
                    if len(t) == 1:
                        return t[-1]
                    else:
                        return t[-2]
            except FileNotFoundError :
                #print(f"The transmiter has closed communications, no other id of {self.id_code[:-1]} is found")
                self.end()
                break
            except PermissionError:
                pass
    
    def write(self, text):
        while True:
            try:
                with open(self.id_code[:-1]+ ("1" if self.id_code[-1] == "2" else "2")) as h:
                    pass
                self.trasmition_located = True
                break
            except FileNotFoundError:
                self.trasmition_located = False
                #print("Warning, the transmter has not been located")
                self.end()
                break
            except PermissionError:
                pass
        with open(self.id_code, "a") as h:
            print(text, file=h, end=";")
    
    def end(self):
        while True:
            try:
                file_path = Path(self.id_code)
                file_path.unlink(missing_ok=True)
                break
            except:
                pass