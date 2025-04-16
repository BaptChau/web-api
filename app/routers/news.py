import json
from ..models.news import News
from fastapi import APIRouter

appRouter = APIRouter(prefix='/news', tags=['news'])

FAKE_NEWS_DEV= News(id=1, title='un test', content='lorem ipsium konkn jiuahczh ,nlkjqhfdofi fqjsh f', tag=['SG', 'Match'], slug='un-test')

@appRouter.get(path='/', name="app_news_get_list")
async def get_news_list():
    return FAKE_NEWS_DEV.model_dump()
