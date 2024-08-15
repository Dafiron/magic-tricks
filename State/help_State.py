import reflex as rx


class HelpState(rx.State):
    event_help: bool = False
    event_info:bool = False

    def help_event(self):
        self.event_help = not self.event_help
    
    def scroll_to_help(self):
        self.help_event()
        rx.scroll_to("help_section")

    def info_event(self):
        self.event_info = not self.event_info
