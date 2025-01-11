from BlueskyApi import BlueskyApi
from WebScraper import RockawaySurfScraper




def main():
    surf_report_message = RockawaySurfScraper.get_surf_summary()
    BlueskyApi.submit_post(bluesky_handle, bluesky_app_password, surf_report_message)



if __name__ == "__main__":
    main()