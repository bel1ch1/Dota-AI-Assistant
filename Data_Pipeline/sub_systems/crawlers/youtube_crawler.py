from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

def parse_video_id(url: str) -> str:
    """Parses the url to extract the video_id.
    Args:
        url: str - Full link to the video
    Returns:
        video_id: str - video id for youtube_transcript_api"""
    qs_params = parse_qs(urlparse(url).query)
    video_id = qs_params.get('v', [None][0])

    return video_id

def crawl_youtube(video_id: str) -> str:
    """Gets the subtitle text from the video.
    Args:
        video_id: str - video id from parse_video_id
    Returns:
        text: str - subtitle text from the video"""
    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(video_id, languages=['ru'])
    text = " ".join([snippet.text for snippet in fetched_transcript])

    return text
