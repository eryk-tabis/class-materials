class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channel_list = []

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        print(f"TV is on, channel {self.channel_no}") if self.is_on else print("TV is off")

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channel_list):
        self.channel_list = channel_list

    def show_channels(self):
        print("Chanel list:")
        for i in range(len(self.channel_list)):
            print(f"{i+1}.{self.channel_list[i]}")


tv = TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.show_channels()
tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
tv.show_channels()
tv.show_status()
tv.turn_off()
