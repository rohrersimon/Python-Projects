import clr
clr.AddReference('System')

from System import Environment

class Configuration:
    def __init__(self):
        self.username = Environment.UserName
        self.domain = Environment.UserDomainName
        self.file_transfer_dialog = self.get_file_transfer_dialog()

    def get_file_transfer_dialog(self):
        # This is a placeholder method as accessing the registry is not directly possible using Python.NET
        # You would need to use a .NET class that provides this functionality
        return None

    def set_file_transfer_dialog(self, value):
        # This is a placeholder method as modifying the registry is not directly possible using Python.NET
        # You would need to use a .NET class that provides this functionality
        pass

config = Configuration()
print(config)