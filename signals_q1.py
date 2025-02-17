from django.dispatch import Signal, receiver

my_signal = Signal()

@receiver(my_signal)
def my_handler(sender, **kwargs):
    print("Signal received synchronously")

print("Sending signal...")
my_signal.send(sender=None)
print("Signal sent.")