import streamlit as st

# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="Annisa | Chemical Analysis",
    page_icon="🧪",
    layout="wide",
)

# =========================================================
# CSS
# HANYA UNTUK TAMPILAN
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f7f6f1;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Text */

h1, h2, h3 {
    color: #18221d !important;
}

p {
    color: #59645e;
}

/* Navbar */

.navbar {
    padding: 15px 0;
    border-bottom: 1px solid #dfe5e0;
    margin-bottom: 40px;
}

/* Hero */

.hero-box {
    background-color: #e9eee9;
    border: 1px solid #d8e1da;
    border-radius: 28px;
    padding: 45px;
    margin-bottom: 20px;
}

/* Cards */

.card {
    background-color: white;
    border: 1px solid #dfe5e0;
    border-radius: 18px;
    padding: 25px;
    min-height: 180px;
    margin-bottom: 15px;
}

/* Project */

.project {
    background-color: white;
    border: 1px solid #dfe5e0;
    border-radius: 18px;
    padding: 22px;
    min-height: 230px;
    margin-bottom: 20px;
}

/* Skill */

.skill {
    background-color: white;
    border: 1px solid #dfe5e0;
    border-radius: 15px;
    padding: 18px;
    margin-bottom: 12px;
}

/* Certification */

.cert {
    background-color: white;
    border: 1px solid #dfe5e0;
    border-radius: 18px;
    padding: 22px;
    text-align: center;
    min-height: 140px;
}

/* Timeline */

.timeline {
    background-color: white;
    border-left: 3px solid #4e6b5b;
    padding: 20px 25px;
    margin-bottom: 20px;
    border-radius: 0 15px 15px 0;
}

/* Button */

.stButton > button {
    border-radius: 30px;
    border: 1px solid #4e6b5b;
    background-color: #4e6b5b;
    color: white;
}

/* Mobile */

@media (max-width: 700px) {

    .hero-box {
        padding: 25px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# NAVBAR
# =========================================================

st.markdown(
    '<div class="navbar"></div>',
    unsafe_allow_html=True
)

nav1, nav2 = st.columns([3, 2])

with nav1:
    st.markdown("## Annisa.")

with nav2:
    st.caption(
        "ABOUT  •  EXPERIENCE  •  SKILLS  •  PROJECTS  •  CONTACT"
    )


# =========================================================
# HERO
# =========================================================

st.markdown(
    '<div class="hero-box">',
    unsafe_allow_html=True
)

st.caption("CHEMICAL ANALYSIS × R&D")

st.title(
    "Turning Knowledge Into Real Experience."
)

st.write(
    "Mahasiswi Analis Kimia yang tertarik pada "
    "laboratory analysis, Research & Development, "
    "quality control, dan product formulation."
)

st.write("")

button1, button2, empty = st.columns([1, 1, 3])

with button1:
    st.button(
        "View My Projects",
        use_container_width=True
    )

with button2:
    st.button(
        "Contact Me",
        use_container_width=True
    )

st.markdown(
    "</div>",
    unsafe_allow_html=True
)


# =========================================================
# QUICK STATS
# =========================================================

st.write("")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Started",
        "2024"
    )

with col2:
    st.metric(
        "Current Area",
        "R&D"
    )

with col3:
    st.metric(
        "Techniques",
        "10+"
    )

with col4:
    st.metric(
        "Methods",
        "6+"
    )


# =========================================================
# ABOUT
# =========================================================

st.write("")
st.write("")
st.caption("01 — ABOUT ME")
st.header("More than a title.")

about1, about2 = st.columns(2)

with about1:

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("🧪 Chemical Analysis Student")

    st.write(
        "Saya merupakan mahasiswi Politeknik AKA Bogor "
        "jurusan Analis Kimia."
    )

    st.write(
        "Saya mempelajari preparasi sampel, pembuatan "
        "larutan, titrasi, analisis instrumen, "
        "pengolahan data, validasi metode, "
        "dan sistem mutu."
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


with about2:

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("🔬 Exploring R&D")

    st.write(
        "Saat ini saya menjalani PKL di bagian "
        "R&D Laboratory PT ADEV Natural Indonesia."
    )

    st.write(
        "Pengalaman meliputi pembuatan emulsi lotion, "
        "penggunaan multimix, pengukuran pH dan "
        "viskositas, preparasi sampel, dan dokumentasi."
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# =========================================================
# EXPERIENCE
# =========================================================

st.write("")
st.write("")
st.caption("02 — EXPERIENCE")
st.header("My journey.")

experience = [
    (
        "SEPTEMBER 2026 — PRESENT",
        "R&D Laboratory Intern",
        "PT ADEV Natural Indonesia · Bogor",
        "Preparasi sampel, penimbangan, pembuatan emulsi lotion, multimix, pH meter, viskositas, centrifuge, input data, dan pembelajaran fungsi bahan."
    ),
    (
        "2024 — PRESENT",
        "Chemical Analysis Student",
        "Politeknik AKA Bogor",
        "Mempelajari analisis kimia, titrasi, kimia organik, kimia lingkungan, instrumentasi, validasi metode, pengolahan data, dan sistem mutu."
    ),
    (
        "2025 — PRESENT",
        "Organization & Campus Activities",
        "Campus Organizations",
        "Mengembangkan pengalaman dalam komunikasi, koordinasi, administrasi, kepanitiaan, dan kerja sama tim."
    )
]

for date, title, company, description in experience:

    st.markdown(
        '<div class="timeline">',
        unsafe_allow_html=True
    )

    st.caption(date)

    st.subheader(title)

    st.write(
        f"**{company}**"
    )

    st.write(description)

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# =========================================================
# SKILLS
# =========================================================

st.write("")
st.write("")
st.caption("03 — SKILLS")
st.header("Tools & capabilities.")

skill_left, skill_right = st.columns(2)

skills = [
    ("Sample Preparation", 88),
    ("Titration", 85),
    ("pH Measurement", 82),
    ("Viscosity Testing", 78),
    ("Laboratory Documentation", 86),
    ("Excel & Data Entry", 84),
    ("UV-Vis", 70),
    ("FTIR", 65),
    ("AAS / SSA", 62),
    ("GC / HPLC / TLC", 55),
]

for i, (name, value) in enumerate(skills):

    column = (
        skill_left
        if i < 5
        else skill_right
    )

    with column:

        st.markdown(
            '<div class="skill">',
            unsafe_allow_html=True
        )

        st.write(
            f"**{name}** — {value}%"
        )

        st.progress(
            value / 100
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


# =========================================================
# PROJECTS
# =========================================================

st.write("")
st.write("")
st.caption("04 — PROJECTS")
st.header("Selected projects.")

projects = [
    (
        "01",
        "Lotion Emulsion Formulation",
        "R&D / Formulation",
        "Mempelajari pembuatan emulsi lotion, fungsi bahan, fase minyak dan air, penggunaan multimix, pH, dan viskositas."
    ),
    (
        "02",
        "Iodometric Analysis",
        "Chemical Analysis",
        "Praktik analisis berbasis titrasi iodometri, standardisasi larutan, perhitungan kadar, dan pengolahan hasil."
    ),
    (
        "03",
        "Instrumental Analysis",
        "Instrumentation",
        "Pengenalan dan pembelajaran instrumen UV-Vis, FTIR, AAS, GC, HPLC, dan TLC."
    ),
    (
        "04",
        "Laboratory Documentation",
        "Documentation",
        "Pengelolaan data sampel, input hasil penimbangan, spreadsheet, dan dokumentasi laboratorium."
    ),
    (
        "05",
        "Method Validation Study",
        "Quality",
        "Pembelajaran linearitas, LOD, LOQ, presisi, akurasi, dan parameter validasi metode."
    ),
    (
        "06",
        "Food Safety & Quality",
        "Quality System",
        "Pembelajaran GMP, HACCP, ISO 22000, FSSC 22000, QA & QC."
    )
]

project_cols = st.columns(3)

for i, project in enumerate(projects):

    number, title, category, description = project

    with project_cols[i % 3]:

        st.markdown(
            '<div class="project">',
            unsafe_allow_html=True
        )

        st.caption(number)

        st.subheader(title)

        st.write(description)

        st.info(category)

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


# =========================================================
# PROJECT DETAIL
# =========================================================

st.write("")
st.subheader("Explore Project")

project_titles = [
    project[1]
    for project in projects
]

selected_project = st.selectbox(
    "Select a project",
    project_titles
)

for project in projects:

    if project[1] == selected_project:

        st.success(
            f"### {project[1]}\n\n"
            f"**Category:** {project[2]}\n\n"
            f"{project[3]}"
        )


# =========================================================
# CERTIFICATIONS
# =========================================================

st.write("")
st.write("")
st.caption("05 — CERTIFICATIONS")
st.header("Training & learning.")

certifications = [
    (
        "🛡️",
        "GMP",
        "Good Manufacturing Practice"
    ),
    (
        "✓",
        "HACCP",
        "Hazard Analysis & Critical Control Point"
    ),
    (
        "◈",
        "ISO 22000:2018",
        "Food Safety Management System"
    ),
    (
        "◉",
        "FSSC 22000",
        "Version 6.0"
    ),
    (
        "▦",
        "QA & QC",
        "In Food Industry"
    ),
    (
        "✦",
        "HACCP Documentation",
        "Document Preparation"
    )
]

cert_cols = st.columns(3)

for i, cert in enumerate(certifications):

    icon, title, description = cert

    with cert_cols[i % 3]:

        st.markdown(
            '<div class="cert">',
            unsafe_allow_html=True
        )

        st.write(icon)

        st.subheader(title)

        st.caption(description)

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


# =========================================================
# CONTACT
# =========================================================

st.write("")
st.write("")
st.caption("06 — CONTACT")
st.header("Let's connect.")

contact1, contact2 = st.columns(2)

with contact1:

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("✉️ Open to opportunities.")

    st.write(
        "Tertarik untuk berdiskusi mengenai "
        "internship, laboratory work, R&D, "
        "quality control, dan pengembangan profesional."
    )

    st.write("📧 your.email@example.com")
    st.write("🔗 linkedin.com/in/yourusername")
    st.write("📍 Bogor, Indonesia")

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


with contact2:

    st.subheader("Send a message")

    name = st.text_input(
        "Name"
    )

    email = st.text_input(
        "Email"
    )

    message = st.text_area(
        "Message"
    )

    if st.button(
        "Send Message"
    ):

        if name and email and message:

            st.success(
                "Message form berhasil diisi!"
            )

        else:

            st.warning(
                "Silakan isi semua kolom."
            )


# =========================================================
# FOOTER
# =========================================================

st.write("")
st.write("")
st.divider()

st.caption(
    "Annisa · Chemical Analysis · R&D · Laboratory · Quality"
)

st.caption(
    "© 2026 Annisa Widiyastuti Putri · Built with Streamlit"
)
