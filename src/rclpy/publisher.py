from rclpy.callback_groups import CallbackGroup
from rclpy.event_handler import PublisherEventCallbacks


class Publisher:

    def __init__(
        self,
        publisher_impl,  # unused
        msg_type,
        topic: str,
        qos_profile,  # unused
        event_callbacks: PublisherEventCallbacks,
        callback_group: CallbackGroup,
    ) -> None:
        return
