from ..models.favorite import Favorite


class FavoriteController:
    def __init__(self, favorite_repository):
        self.favorite_repository = favorite_repository

    async def create(self, favorite: Favorite):
        return await self.favorite_repository.create(favorite)

    async def update(self, favorite: Favorite):
        return await self.favorite_repository.update(favorite)

    async def delete(self, address_code, user_id):
        return await self.favorite_repository.delete(user_id, address_code)

    async def get_by_user(self, user_id):
        return await self.favorite_repository.get_by_user(user_id)