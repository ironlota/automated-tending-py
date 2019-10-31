from enum import Enum

class EnumAutoName(Enum):
    def _generate_next_value_(self, name, start, count, last_values):
        return name
