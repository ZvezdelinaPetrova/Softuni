from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        current_names = [x.name for x in System._hardware]
        if hardware_name not in current_names:
            return f"Hardware does not exist"

        hardware = System.find_object(hardware_name, System._hardware)

        new_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        result = hardware.install(new_software)
        if result:
            System._software.append(new_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        current_names = [x.name for x in System._hardware]
        if hardware_name not in current_names:
            return f"Hardware does not exist"

        hardware = System.find_object(hardware_name, System._hardware)

        new_software = LightSoftware(name, capacity_consumption, memory_consumption)
        result = hardware.install(new_software)
        if result:
            System._software.append(new_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.find_object(hardware_name, System._hardware)
        software = System.find_object(software_name, System._software)
        if hardware and software:
            hardware.uninstall(software)
            System._software.remove(software)
        else:
            return f"Some of the components do not exist"

    @staticmethod
    def analyze():
        result = f"System Analysis" + "\n"
        result += f"Hardware Components: {len(System._hardware)}" + "\n"
        result += f"Software Components: {len(System._software)}" + "\n"
        result += f"Total Operational Memory: " \
                  f"{sum([x.memory_consumption for x in System._software])} / " \
                  f"{sum([x.memory for x in System._hardware])}" + "\n"

        result += f"Total Capacity Taken: " \
                  f"{sum([x.capacity_consumption for x in System._software])} / " \
                  f"{sum([x.capacity for x in System._hardware])}"
        return result

    @staticmethod
    def system_split():
        result = ""
        for x in System._hardware:
            result += f"Hardware Component - {x.name}" + "\n"
            result += f"Express Software Components: " \
                      f"{len([b for b in x.software_components if b.software_type == 'Express'])}" + "\n"
            result += f"Light Software Components: " \
                      f"{len([k for k in x.software_components if k.software_type == 'Light'])}" + "\n"
            result += f"Memory Usage: " \
                      f"{sum([m.memory_consumption for m in x.software_components])} / " \
                      f"{x.memory}" + "\n"
            result += f"Capacity Usage: " \
                      f"{sum([c.capacity_consumption for c in x.software_components])} / " \
                      f"{x.capacity}" + "\n"
            result += f"Type: {x.hardware_type}" + "\n"
            if System._software:
                result += f"Software Components: {', '.join(n.name for n in x.software_components)}" + "\n"
            else:
                result += f"Software Components: None" + "\n"
        return result.strip()

    @staticmethod
    def find_object(h_name, list_with_objects):
        for obj in list_with_objects:
            if obj.name == h_name:
                return obj

