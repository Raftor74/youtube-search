import requests


class YouTubeVideo(object):

    YOUTUBE_VIDEO_URL = 'https://www.youtube.com/watch'

    def __init__(self, id, title, img_url):
        self.id = id
        self.title = title
        self.url = self.get_video_url(id)
        self.img_url = img_url

    def get_video_url(self, video_id):
        return "{0}?v={1}".format(self.YOUTUBE_VIDEO_URL, video_id)

    def __str__(self):
        return "id:{}, url:{}".format(self.id, self.url)


class YouTubeVideoSearch(object):
    API_KEY = 'AIzaSyCQ95H4gyUFPeNgLRNp_cHCkeT75lGKK2Y'
    API_URL = 'https://www.googleapis.com/youtube/v3/search'

    def search(self, query, max_results=20):
        params = self.get_search_params(query, max_results)
        response = requests.get(self.API_URL, params)
        json_response = response.json()
        return self.make_video_list_from_json_response(json_response)

    def get_search_params(self, query, max_results):
        return {
            'key': self.API_KEY,
            'part': 'snippet',
            'maxResults': max_results,
            'q': query,
            'type': 'video',
        }

    @staticmethod
    def make_video_list_from_json_response(json_response):
        items = json_response['items']
        video_list = list()
        for video_item in items:
            snippet = video_item['snippet']
            images = snippet['thumbnails']
            video_id = video_item['id']['videoId']
            title = snippet['title']
            img_url = images['medium']['url']
            video = YouTubeVideo(video_id, title, img_url)
            video_list.append(video)
        return video_list


def main():
    search = YouTubeVideoSearch()
    query = "Котики"
    video_list = search.search(query)
    for video in video_list:
        print(video)


if __name__ == '__main__':
    main()