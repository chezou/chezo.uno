# pip install git+https://github.com/chezou/prelims.git@followup
from prelims import StaticSitePostsHandler
from prelims.processor import Recommender

handler = StaticSitePostsHandler(r'content/blog')
handler.register_processor(
	Recommender(permalink_base='/blog', stop_words='english')
)
handler.execute()
