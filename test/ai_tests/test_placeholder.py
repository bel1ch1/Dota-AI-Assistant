from youtube_transcript_api import YouTubeTranscriptApi

video_ids = [
    "C4MTHAJO9mg",
    "VaNyNRcJz4w",
    "QRWNm4ZKFXM"
]
video = "QRWNm4ZKFXM"

ytt_api = YouTubeTranscriptApi()
transcript_list = ytt_api.list(video)
res = transcript_list.find_transcript(['ru'])
if res:
    print(res.language_code)
else:
    print("no")
