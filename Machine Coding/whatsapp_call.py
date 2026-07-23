class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def display(self):
        print(f"{self.name} ({self.user_id})")


class Call:
    def __init__(self, caller, receiver):
        self.caller = caller
        self.receiver = receiver
        self.status = "Idle"

    def start_call(self):
        self.status = "Ringing"
        print(f"{self.caller.name} is calling {self.receiver.name}")

    def accept_call(self):
        self.status = "Connected"
        print("Call Connected")

    def reject_call(self):
        self.status = "Rejected"
        print("Call Rejected")

    def end_call(self):
        self.status = "Ended"
        print("Call Ended")


class AudioCall(Call):
    def mute(self):
        print("Audio Muted")

    def unmute(self):
        print("Audio Unmuted")


class VideoCall(Call):
    def mute(self):
        print("Microphone Muted")

    def camera_on(self):
        print("Camera ON")

    def camera_off(self):
        print("Camera OFF")


# ---------------- Driver ----------------

u1 = User(1, "Aadhi")
u2 = User(2, "Rahul")

audio = AudioCall(u1, u2)

audio.start_call()
audio.accept_call()
audio.mute()
audio.unmute()
audio.end_call()

print()

video = VideoCall(u2, u1)

video.start_call()
video.accept_call()
video.camera_on()
video.camera_off()
video.end_call()