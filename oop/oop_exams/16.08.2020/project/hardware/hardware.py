from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []   # all software's components installed on that hardware

    def install(self, software: Software):
        if software.capacity_consumption <= self.capacity and software.memory_consumption <= self.memory:
            self.software_components.append(software)
            return True
        else:
            raise Exception(f"Software cannot be installed")

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)


