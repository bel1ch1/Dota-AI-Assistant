from youtube_transcript_api import YouTubeTranscriptApi

# нужно обрабатывать пул video_id
# проводить быструю отчистку текста
# Загружать данные в NoSQL базу данных

# "b-G_gtHqG-Y"
video_id = "XJC5WB2Bwrc"
ytt_api = YouTubeTranscriptApi()
fetched_transcript = ytt_api.fetch(video_id, languages=['ru'])

text = " ".join([snippet.text for snippet in fetched_transcript])
print(text)

# Потенциальная информация для отчистки:
# все что находится в скобках []
# Не релевантная информация по типу: реклама, приветствие...
