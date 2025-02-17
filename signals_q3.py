from django.dispatch import Signal, receiver
from django.db import transaction

my_signal = Signal()

@receiver(my_signal)
def transaction_handler(sender, **kwargs):
    print("Signal received within the same transaction")

print("Starting transaction...")
with transaction.atomic():
    my_signal.send(sender=None)
print("Signal sent within transaction.")
print("Transaction completed.")