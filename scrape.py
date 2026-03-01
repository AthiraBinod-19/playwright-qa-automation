import asyncio
from playwright.async_api import async_playwright

seeds = list(range(64, 74))

BASE_URL = "https://sanand0.github.io/tdsdata/table_scrape.html?seed="

async def scrape():
    total_sum = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        for seed in seeds:
            url = BASE_URL + str(seed)
            await page.goto(url)

            # Wait for tables to load
            await page.wait_for_selector("table")

            # Extract all numbers inside tables
            cells = await page.locator("table td").all_text_contents()

            for cell in cells:
                cell = cell.strip()
                if cell.isdigit():
                    total_sum += int(cell)

        await browser.close()

    print("FINAL_TOTAL =", total_sum)

asyncio.run(scrape())
