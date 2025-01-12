import BlueskyApi
import RockawaySurfScraper
import os

def main():
    bluesky_handle = os.getenv('BLUESKY_HANDLE')
    bluesky_app_password = os.getenv("BLUESKY_PASSWORD")
    surf_scraper = RockawaySurfScraper.RockawaySurfScraper()
    bluesky_api = BlueskyApi.BlueskyApi()
    surf_report_message = surf_scraper.surf_summary
    bluesky_api.submit_post(bluesky_handle, bluesky_app_password, surf_report_message)

if __name__ == "__main__":
    main()