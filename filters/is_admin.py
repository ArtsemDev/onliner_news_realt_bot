from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message


class IsAdmin(BoundFilter):
    key = 'is_admin'

    async def check(self, message: Message) -> bool:
        return message.from_user.id == 12345678
