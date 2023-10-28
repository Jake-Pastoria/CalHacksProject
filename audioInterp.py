import asyncio
from hume import HumeStreamClient
from hume.models.config import ProsodyConfig

def find_top_three_emotions(data):
    emotions = data['prosody']['predictions'][0]['emotions']

    # Sort the emotions by score in descending order
    sorted_emotions = sorted(emotions, key=lambda x: x['score'], reverse=True)

    # Get the top three emotions
    top_three_emotions = [emotion['name'] for emotion in sorted_emotions[:3]]

    return top_three_emotions

async def main(content):
    client = HumeStreamClient("4pLMpdxQgho6hO7YaPvFrm4xssArylydAIgfUfAZrh6A44xu")
    configs = [ProsodyConfig()]
    async with client.connect(configs) as socket:
        result = await socket.send_file(content)
        return find_top_three_emotions(result)
