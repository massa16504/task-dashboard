# 📊 Task Dashboard (Streamlit)

This is a web-based dashboard for visualizing tasks from an Excel file using Streamlit.

## Features

- Upload an `.xlsx` Excel file (Harsha tab)
- Auto-cleans column names
- Displays key metrics: Completed, In Progress, Not Started, Overdue
- Pie chart visualization of task status
- Interactive table preview

## How to Deploy

1. Fork this repo to your GitHub
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Select `task_dashboard.py` as the main file

You're done! Share the public Streamlit link with your team.

## Local Run (Optional)

```bash
pip install streamlit pandas plotly openpyxl
streamlit run task_dashboard.py
```
