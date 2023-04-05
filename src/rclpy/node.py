from .clock import Clock
from .publisher import Publisher


class Node:
    def __init__(self, name):
        self.name = name

    def create_publisher(
        self,
        msg_type,
        topic: str,
        qos_profile=None,
        *,
        callback_group=None,
        event_callbacks=None,
        qos_overriding_options=None,
        publisher_class=Publisher,
    ) -> Publisher:
        print(
            f'create publisher for topic {topic}, type {msg_type.__name__}')

    def create_timer(
            self,
            timer_period_sec: float,
            callback,
            callback_group=None,
            clock: Clock = None,):
        return

    def get_logger(self):
        return

    def destroy_node(self):
        # TODO
        return
