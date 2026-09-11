# Data Analyst Assessment – Global Superstore

# Important build note
The assessment requires a public dataset. The assignment plan uses the **Global Superstore** dataset hosted on Kaggle:
https://www.kaggle.com/datasets/shekpaul/global-superstore

# Business problem
Identify profitable growth opportunities and profitability leaks across categories, markets, discount levels and shipping operations.

# Main findings from the working copy
- Total Sales: 46.88M
- Total Profit: 4.52M
- Overall Profit Margin: 9.7%
- Orders/rows: 51,290
- Average Delivery Days: about 3.75
- Loss-row rate: 17.5%
- Technology is the largest category by sales and profit.
- Furniture has about 10.80M sales but only about 1.9% margin.
- 30%+ discounts are loss-making.
- Canada has the strongest market margin, but a relatively small sales share.

## Files
- Data_Analyst_Assessment.xlsx — Data, Processed Data, Q1–Q8, Q10 and calculation sheets.
- analysis.py — Python cleaning and analysis workflow.
- Processed_Data.csv — analysis-ready working copy.
- dashboard_mockup.png — management dashboard layout.
- Management_Presentation.pptx — 7-slide presentation.
- README.md — methodology and handover notes.
- requirements.txt — Python dependencies.

## Looker Studio steps
1. Open Google Drive → New → Google Sheets.
2. Import `Processed_Data.csv` or copy the `Processed Data` worksheet into Google Sheets.
3. Open Looker Studio → Create → Report.
4. Add Google Sheets as the data source.
5. Select the `Processed Data` sheet.
6. Add KPI scorecards: Sales, Profit, Profit Margin, Orders, Loss Order % and Avg Delivery Days.
7. Add a monthly Sales + Profit trend.
8. Add Category Sales vs Profit.
9. Add Discount Band Profit Margin.
10. Add Market Sales + Margin.
11. Add filters: Year, Market, Category, Segment and Ship Mode.
12. Take a screenshot and paste it into Q8.
13. Share the Looker Studio link with the hiring team.

## Final folder
Your final Google Drive folder should contain:
1. Google Sheet
2. Python notebook/script
3. Supporting analysis
4. 5–7 slide presentation
5. README / Methodology
