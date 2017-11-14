class MemoryHandel:

    def __init__(self, filename):
        self.filename = filename

    def get_saved_values(self):
        file = open(self.filename, 'r')
        str_num = file.readline().rstrip("\n\r")
        ip = file.readline().rstrip("\n\r")
        file.close()
        return str_num, ip

    def save_values(self, num, ip):
        # Using 'w' will clear the file before it writes. This makes things less complicated
        file = open(self.filename, 'w')
        # Because of the above comment I need to rewrite the ip.
        file.write(str(num) + "\n" + str(ip))
        file.close()