from mycroft import MycroftSkill, intent_file_handler


class Kitty(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('kitty.intent')
    def handle_kitty(self, message):
        self.speak_dialog('kitty')


def create_skill():
    return Kitty()

