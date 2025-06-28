from .NewsCreate import NewsCreateAPIView
from .NewsList import NewsListAPIView
from .NewsUpdate import NewsUpdateAPIView
from .NewsDelete import NewsDeleteAPIView

from .MediaFileCreate import MediaFileCreateAPIView
from .MediaFileList import MediaFileListAPIView
from .MediaFileRetrieve import MediaFileRetrieveAPIView
from .MediaFileUpdate import MediaFileUpdateAPIView
from .MediaFileDelete import MediaFileDeleteAPIView

__all__ = [
    "NewsCreateAPIView",
    "NewsListAPIView",
    "NewsRetrieveAPIView",
    "NewsUpdateAPIView",
    "NewsDeleteAPIView",
    
    "CommentCreateAPIView",
    "CommentListAPIView",
    "CommentRetrieveAPIView",
    "CommentUpdateAPIView",
    "CommentDeleteAPIView",

    "MediaFileCreateAPIView",
    "MediaFileListAPIView",
    "MediaFileRetrieveAPIView",
    "MediaFileUpdateAPIView",
    "MediaFileDeleteAPIView",
]
