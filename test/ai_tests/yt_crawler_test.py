from ai.feature.youtube_crawler import YT_Crawler

video_ids = [
    "C4MTHAJO9mg",
    "VaNyNRcJz4w",
    "QRWNm4ZKFXM"
]

crawler = YT_Crawler(video_ids=video_ids, languages=["ru"])
res = crawler.get_transcriptions()
print(len(res))
