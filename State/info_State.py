import reflex as rx


class InfoState(rx.State):
    event_info: bool = False
    event_alchemy: bool = False

    def info_event(self):
        self.event_info = not self.event_info
    
    def alchemy_event(self):
        self.event_alchemy = not self.event_alchemy