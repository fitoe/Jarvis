const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

async function launchBrowser() {
  const candidates = [
    "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  ];
  const executablePath = candidates.find((candidate) => fs.existsSync(candidate));
  return chromium.launch({ headless: true, ...(executablePath ? { executablePath } : {}) });
}

(async () => {
  const browser = await launchBrowser();
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  const consoleErrors = [];
  page.on("console", (message) => {
    if (message.type() === "error") consoleErrors.push(message.text());
  });
  try {
    await page.goto(process.env.BASE_URL, { waitUntil: "networkidle" });
    assert((await page.title()).toLowerCase().includes("inventory"), "page title must identify inventory");
    assert(await page.getByRole("heading", { name: /inventory/i }).isVisible(), "inventory heading missing");
    await page.getByLabel("SKU").fill("bolt");
    await page.getByLabel("Quantity").fill("5");
    await page.getByRole("button", { name: /receive stock/i }).click();
    const balance = page.getByTestId("stock-bolt");
    await balance.waitFor({ state: "visible" });
    assert((await balance.textContent()).includes("5"), "received balance must be 5");
    await page.reload({ waitUntil: "networkidle" });
    assert((await page.getByTestId("stock-bolt").textContent()).includes("5"), "balance must persist after reload");
    assert(consoleErrors.length === 0, `browser console errors: ${consoleErrors.join(" | ")}`);
    const screenshot = path.join(process.cwd(), "browser-evidence.png");
    await page.screenshot({ path: screenshot, fullPage: false });
    console.log(`Browser journey passed; screenshot=${screenshot}`);
  } finally {
    await browser.close();
  }
})().catch((error) => {
  console.error(error.stack || error.message);
  process.exit(1);
});
