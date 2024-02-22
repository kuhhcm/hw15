class MainClass:
    def __init__(self, text):
        self.text_field = text

    def set_text(self, new_text=""):
        self.text_field = new_text

class SubClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.number_field = number

    def set_text(self, new_text="", additional_text=""):
        super().set_text(new_text)
        self.text_field += additional_text

if __name__ == "__main__":
    main_obj = MainClass("Initial Text")
    print("Main Class - Initial Text Field:", main_obj.text_field)

    main_obj.set_text("New Text")
    print("Main Class - Updated Text Field:", main_obj.text_field)

    sub_obj = SubClass("Subclass Text", 42)
    print("Subclass - Initial Text Field:", sub_obj.text_field)
    print("Subclass - Initial Number Field:", sub_obj.number_field)

    sub_obj.set_text("Updated Subclass Text", " Additional Text")
    print("Subclass - Updated Text Field:", sub_obj.text_field)
    print("Subclass - Updated Number Field:", sub_obj.number_field)