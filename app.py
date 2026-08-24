import pandas as pd
import streamlit as st

# ضبط إعدادات الصفحة (تم تصحيح المسمى هنا)
st.set_page_config(
    page_title="نظام إدارة الجودة الشاملة للمعامل الطبية",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# عنوان التطبيق
st.title("🧪 نظام إدارة الجودة الشاملة في المعامل الطبية (TQM)")
st.caption(
    "وفق عناصر النظام الأساسية الـ 12 للجودة (Quality System Essentials)"
)

# القائمة الجانبية للأقسام الـ 12
sections = [
    "1. الكوادر والموظفون (Personnel)",
    "2. التنظيم والإدارة (Organization)",
    "3. الأجهزة والمعدات (Equipment)",
    "4. الشراء والمخزون (Purchasing & Inventory)",
    "5. ضبط العمليات (Process Control)",
    "6. إدارة المعلومات (Information Management)",
    "7. الوثائق والسجلات (Documents & Records)",
    "8. إدارة الحوادث والحيود (Occurrence Management)",
    "9. التقييم والمراجعة (Assessment)",
    "10. التحسين المستمر (Process Improvement)",
    "11. خدمة العملاء (Customer Service)",
    "12. السلامة والمرافق (Facilities & Safety)",
]

selected_section = st.sidebar.radio("اختر قسم الجودة:", sections)

# --- 1. قسم الكوادر والموظفون ---
if "1. الكوادر والموظفون" in selected_section:
    st.header("👨‍⚕️ قسم الكوادر والموظفون")
    st.write(
        "إدارة القوى البشرية وتحديد الصلاحيات والأدوار لكل فرد داخل المختبر:"
    )

    # خيارات القوائم المنسدلة
    roles_options = [
        "مدير المعمل",
        "مسؤول الجودة",
        "رئيس قسم التحاليل",
        "أخصائي تحاليل",
        "فني معمل",
        "مستلم العينات",
    ]
    access_options = [
        "صلاحية كاملة (Full Control)",
        "إدخال واعتماد النتائج",
        "إدخال البيانات فقط",
        "تسجيل العينات فقط",
        "قراءة فقط (Read-Only)",
    ]
    status_options = ["نشط", "في إجازة", "تحت التدريب"]

    # البيانات الأولية للجدول
    if "personnel_df" not in st.session_state:
        st.session_state.personnel_df = pd.DataFrame([
            {
                "اسم الموظف": "د. أحمد محمود",
                "المسمى الوظيفي": "مدير المعمل",
                "الصلاحيات": "صلاحية كاملة (Full Control)",
                "الحالة": "نشط",
            },
            {
                "اسم الموظف": "سارة علي",
                "المسمى الوظيفي": "مسؤول الجودة",
                "الصلاحيات": "صلاحية كاملة (Full Control)",
                "الحالة": "نشط",
            },
            {
                "اسم الموظف": "محمد عمر",
                "المسمى الوظيفي": "أخصائي تحاليل",
                "الصلاحيات": "إدخال واعتماد النتائج",
                "الحالة": "نشط",
            },
        ])

    # عرض الجدول التفاعلي بالقوائم المنسدلة
    edited_df = st.data_editor(
        st.session_state.personnel_df,
        num_rows="dynamic",
        use_container_width=True,
        column_config={
            "اسم الموظف": st.column_config.TextColumn("اسم الموظف", required=True),
            "المسمى الوظيفي": st.column_config.SelectboxColumn(
                "الدور / المسمى الوظيفي", options=roles_options, required=True
            ),
            "الصلاحيات": st.column_config.SelectboxColumn(
                "مستوى الصلاحية", options=access_options, required=True
            ),
            "الحالة": st.column_config.SelectboxColumn(
                "حالة الموظف", options=status_options, required=True
            ),
        },
    )

    if st.button("💾 حفظ التغيرات"):
        st.session_state.personnel_df = edited_df
        st.success("تم حفظ بيانات الكوادر والصلاحيات بنجاح!")

# --- بقية الأقسام الـ 12 ---
else:
    st.header(selected_section)
    st.info(
        f"شاشة إدارة **{selected_section}**. يمكنك إضافة النماذج والجداول الخاصة بهذا القسم هنا."
    )
