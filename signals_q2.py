from django.dispatch import Signal, receiver
import threading

my_signal = Signal()

@receiver(my_signal)
def thread_handler(sender, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")

print(f"Sending signal from thread: {threading.current_thread().name}")
my_signal.send(sender=None)
print("Signal sent.")