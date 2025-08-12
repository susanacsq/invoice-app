import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

# =========================
# GOOGLE SHEETS CONNECTION
# =========================
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Use your local service_account.json file
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", SCOPE)
client = gspread.authorize(creds)

# Open your Google Sheet by name
SHEET_NAME = "Invoice Records"  # change if your sheet name is different
sheet = client.open(SHEET_NAME).sheet1

# =========================
# STREAMLIT PAGE
# =========================
st.set_page_config(page_title="Invoice Entry Form", page_icon="🧾", layout="centered")

st.title("🧾 Invoice Entry Form")

# Form inputs
with st.form("invoice_form", clear_on_submit=True):
    date = st.date_input("Date", value=datetime.date.today())
    invoice_number = st.text_input("Invoice Number")
    description = st.text_area("Description")
    category = st.selectbox(
        "Category",
        ["Gifting", "Vouchers", "Road Show", "Meals", "Courses", "Entertainment", "Other"]
    )
    amount = st.number_input("Amount (SGD)")
    remarks = st.text_area("Remarks")
    
    submitted = st.form_submit_button("Submit")

if submitted:
    sheet.append_row([
        date.strftime("%d/%m/%Y"),
        invoice_number,
        description,
        category,
        amount,
        remarks
    ])
    st.success("Added successfully")




