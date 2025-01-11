class BlueskyApi:
    
    def __init__(self):
        self.now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


    def create_post(self, post_text:str):
        """
        Function to create a payload that includes the text to post to BlueSky

        Args:
            post_test (str): Text that will appear in the post on Bluesky
        """
        self.post = {
            "$type": "app.bsky.feed.post",
            "text": post_text,
            "createdAt": self.now,
        }


    def open_session(self, bluesky_handle:str, bluesky_app_password:str):

        """
        Function to open the session from Bluesky, and obtain the session token and session did, which are required to submit the post.

        Args:
            bluesky_handle (str): Handle/username on the bluesky app. Will end with '.bsky.social'
                example: 'example_username.bsky.social'
            bluesky_app_password (str): The password of the Bluesky account
        """


        resp = requests.post(
            "https://bsky.social/xrpc/com.atproto.server.createSession",
            json={"identifier": BLUESKY_HANDLE, "password": BLUESKY_APP_PASSWORD},
        )
        resp.raise_for_status()
        session = resp.json()
        self.session_token = session["accessJwt"]
        self.session_did = session["did"]


    def submit_post(self, bluesky_handle:str, bluesky_app_password:str, post_text:str):
        """
        Post text to the Bluesky Social Platform

        Args:
            bluesky_handle (str): Handle/username on the bluesky app. Will end with '.bsky.social'
                example: 'example_username.bsky.social'
            bluesky_app_password (str): The password of the Bluesky account
            post_test (str): Text that will appear in the post on Bluesky
        """
        self.open_session(bluesky_handle, bluesky_app_password)
        self.create_post(post_text)

        resp = requests.post(
            "https://bsky.social/xrpc/com.atproto.repo.createRecord",
            headers={"Authorization": "Bearer " + self.session_token},
            json={
                "repo": self.session_did,
                "collection": "app.bsky.feed.post",
                "record": self.post,
            },
        )
        print(json.dumps(resp.json(), indent=2))
        resp.raise_for_status()