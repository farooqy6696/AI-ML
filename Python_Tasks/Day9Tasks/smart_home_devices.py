#12. Smart Home Devices (Multiple Inheritance)

class WiFiDevice:

    def wifi(self):
        print("WiFi Connected")


class VoiceAssistant:

    def voice(self):
        print("Voice Assistant Activated")


class SmartSpeaker(WiFiDevice, VoiceAssistant):
    pass


speaker = SmartSpeaker()

speaker.wifi()
speaker.voice()