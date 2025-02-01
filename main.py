import BlueskyApi
import RockawaySurfScraper
from utils import get_secret

def main():
    bluesky_handle = 'rockaway-surf.bsky.social'
    bluesky_app_password = get_secret("BLUESKY_PASSWORD")
    surf_scraper = RockawaySurfScraper.RockawaySurfScraper()
    bluesky_api = BlueskyApi.BlueskyApi()
    surf_report_message = surf_scraper.surf_summary
    bluesky_api.submit_post(bluesky_handle, bluesky_app_password, surf_report_message)

if __name__ == "__main__":
    main()