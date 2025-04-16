from ..models.news import News
from fastapi import APIRouter

appRouter = APIRouter(prefix='/news', tags=['news'])

@appRouter.get(path='/', name="app_news_get_list")
async def get_news_list():
    return {"route_name": "app_news_get_list"}

@appRouter.get(path='/{slug}', name="app_news_get_by-slug")
async def get_news_by_slug(slug: str):
    return {"route_name": "app_news_get_by-slug", "params": slug}

@appRouter.post(path='/post', name="app_news_post_news")
async def post_news(news: News):
    return {"resource_created": news}

@appRouter.delete(path="/delete/{id}", name="app_news_delete_news")
async def delete_news(news_id: str):
    return {"resource_deleted": {"id" : news_id}}

@appRouter.put(path="/put/{id}", name="app_news_update_news")
async def put_news(news_id: str, news: News):
    return {"resource_updated": {"id": news_id, "news": news}}