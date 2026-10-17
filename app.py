
import streamlit as st

st.set_page_config(
    page_title="سامانه ویزیتور آرد میثم",
    page_icon="🌾",
    layout="wide"
)

st.markdown("""
<style>
html, body, [class*="css"] {
    direction: rtl;
    text-align: right;
}
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.title("🌾 سامانه شخصی ویزیتور آرد")
st.caption("نسخه آزمایشی | شرکت آرد میثم")

st.info("این نسخه نمایشی است و اطلاعات آن ساختگی است.")

st.subheader("داشبورد مدیریتی")

col1, col2, col3, col4 = st.columns(4)

col1.metric("تعداد نانوایان", "25", "+2")
col2.metric("سفارش‌های امروز", "12", "+3")
col3.metric("مبلغ برداشت آزمایشی", "85 میلیون ریال")
col4.metric("مانده بدهی آزمایشی", "42 میلیون ریال")

st.divider()

menu = st.sidebar.selectbox(
    "انتخاب بخش",
    [
        "داشبورد",
        "مدیریت نانوایان",
        "ثبت سفارش",
        "ورود فایل برداشت‌ها",
        "تطبیق سفارش و برداشت",
        "گزارش بدهی و مطالبات"
    ]
)

st.header(menu)

if menu == "داشبورد":
    st.write("خلاصه وضعیت سفارش‌ها و حساب مشتریان در این بخش نمایش داده می‌شود.")

elif menu == "مدیریت نانوایان":
    st.write("در این بخش اطلاعات نانوایان ثبت و جست‌وجو خواهد شد.")
    st.text_input("نام نانوایی")
    st.text_input("نام نانوا")
    st.text_input("شماره تماس")

elif menu == "ثبت سفارش":
    st.write("در این بخش سفارش آرد ثبت یا از اکسل وارد خواهد شد.")
    st.text_input("کد پیگیری سفارش")
    st.selectbox("نوع آرد", ["آرد یارانه‌ای", "آرد آزاد"])
    st.number_input("تعداد کیسه", min_value=0, step=1)

elif menu == "ورود فایل برداشت‌ها":
    st.write("در نسخه بعدی، فایل اکسل برداشت‌ها در این قسمت بارگذاری می‌شود.")
    st.file_uploader("انتخاب فایل اکسل", type=["xlsx", "csv"])

elif menu == "تطبیق سفارش و برداشت":
    st.write("هدف این بخش، اتصال برداشت‌های بانکی به سفارش‌ها با کد پیگیری است.")

elif menu == "گزارش بدهی و مطالبات":
    st.write("گزارش مانده هر نانوا و مغایرت‌های احتمالی در این قسمت نمایش داده خواهد شد.")

st.divider()
st.caption("سامانه در حال توسعه است؛ ارقام نمایش‌داده‌شده واقعی نیستند.")
