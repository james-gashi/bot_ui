from botasaurus.request import request, Request
from botasaurus import bt
from botasaurus.browser import browser, Driver
from botasaurus.sitemap import Sitemap, Filters, Extractors
from botasaurus.soupify import soupify

# @request
# def scrape_heading_task(request: Request, data):
#     # Navigate to the Link
#     response = request.get(data["link"])

#     # Create a BeautifulSoup object    
#     soup = soupify(response)
    
#     # Retrieve the heading element's text
#     headings = [heading.get_text() for heading in soup.find_all('h1')]

#     # Save the data as a JSON file in output/scrape_heading_task.json
#     return {
#         "heading": headings
#     }

@browser
def scrape_heading_task(driver: Driver, data):
    # Navigate to the Link
    driver.get(data["link"])

    # Retrieve the heading element's text
    heading = driver.get_text("h1")

    # Save the data as a JSON file in output/scrape_heading_task.json
    return {
        "heading": heading
    }
     
# @request
# def scrape_links(request: Request, data):
#     links = (
#         Sitemap("link")
#         .filter(Filters.first_segment_equals("products"))
#         .extract(Extractors.extract_link_upto_second_segment())
#         .write_links('g2-products')
# )
    #response = request.get(data[links])
    #soup = soupify(response)