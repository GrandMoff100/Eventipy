class Defaults:
    fields = {}
    
    def __init__(self, field):
        Defaults.fields[field] = Defaults.fields.get(field, -1)
        Defaults.fields[field] += 1
        self.id = Defaults.fields[field]
        self.field = field
    
    def __str__(self):
        return self.field + '-' + str(self.id)
    
    def __repr__(self):
        return f"'{str(self)}'"
