from validation import V


class RequiredString:
    def __set_name__(self, owner, name):
        self.property_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.property_name]


class FileDescriptor(RequiredString):
    def __set__(self, instance, value):
        if not V.is_str(value):
            raise TypeError(f"{self.property_name} must be a string")
        if V.file_exists(value):
            instance.__dict__[self.property_name] = value
        else:
            raise FileExistsError
