import asyncio
from playwright.async_api import async_playwright

FAUCET_URL = "https://testnet.helioschain.network/"
TESTNET_ADDRESS = "helios1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with your address

async def claim_faucet():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(FAUCET_URL)

        # Adjust the selectors below according to the actual page structure
        await page.wait_for_selector('input[type="text"]')  # Wait for address input
        await page.fill('input[type="text"]', TESTNET_ADDRESS)  # Fill in your address

        # Click the button to request coins (adjust selector as needed)
        await page.click('button:has-text("Request")')

        # Wait for a confirmation message (adjust text as needed)
        try:
            await page.wait_for_selector('text=Success', timeout=10000)
            print("Faucet claim successful!")
        except:
            print("No confirmation detected. Check manually or update selectors.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(claim_faucet())
