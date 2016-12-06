class StorageRoomListRequestObject(object):
    @classmethod
    def from_dict(cls, adict):
        return StorageRoomListRequestObject()

    def __nonzero__(self):
        return True

    __bool__ = __nonzero__
