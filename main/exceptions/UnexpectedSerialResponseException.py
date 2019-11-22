class UnexpectedSerialResponseException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    # that's all you need fam
