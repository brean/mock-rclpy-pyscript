class PublisherEventCallbacks:
    """Container to provide middleware event callbacks for a Publisher."""

    def __init__(
        self,
        *,
        deadline=None,
        liveliness=None,
        incompatible_qos=None,
        incompatible_type=None,
        matched=None,
        use_default_callbacks: bool = True,
    ) -> None:
        self.use_default_callbacks = use_default_callbacks
