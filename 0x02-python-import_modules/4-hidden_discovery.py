#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for code in dir(hidden_4):
        if code[:2] != "__":
            
            print("{:s}".format(code))
