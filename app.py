import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Annisa | Chemical Analysis",
    page_icon="🧪",
    layout="wide",
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

html {
    scroll-behavior: smooth;
}

.stApp {
    background: #f7f6f1;
    color: #17211c;
}

.block-container {
    max-width: 1100px;
    padding-top: 1rem;
}

* {
    font-family: 'DM Sans', sans-serif;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
}

/* NAVIGATION */

.nav {
    padding: 12px 0 30px;
    border-bottom: 1px solid #dfe5e0;
    margin-bottom: 35px;
}

.logo {
    font-family: 'Playfair Display', serif;
    font-size: 25px;
    font-weight: 700;
}

.logo span {
    color: #4e6b5b;
}

/* HERO */

.hero {
    background: #e9eee9;
    border: 1px solid #d9e1db;
    border-radius: 28px;
    padding: 55px;
}

.eyebrow {
    color: #4e6b5b;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 64px;
    line-height: 1;
    letter-spacing: -2px;
    margin: 15px 0;
}

.hero-title span {
    color: #4e6b5b;
}

.hero-text {
    color: #68736d;
    font-size: 16px;
    line-height: 1.8;
    max-width: 650px;
}

/* STAT */

.stat {
    background: white;
    border: 1px solid #dfe5e0;
    border-radius: 16px;
    padding: 18px;
    text-align: center;
}

.stat-number {
    font-family: 'Playfair Display', serif;
    font-size: 28px;
    font-weight: 700;
}

.stat-label {
    color: #68736d;
    font-size: 11px;
}

/* SECTION */

.section {
    padding-top: 70px;
}

.kicker {
    color: #4e6b5b;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 42px;
    margin: 6px 0 25px;
}

/* CARD */

.card {
    background: white;
    border: 1px solid #dfe5e0;
    border-radius: 20px;
    padding: 25px;
    min-height: 190px;
}

.card-icon {
    font-size: 27px;
}

.card-title {
    font-family: 'Playfair Display', serif;
    font-size: 23px;
    margin: 8px 0;
}

.muted {
    color: #68736d;
    line-height: 1.75;
    font-size: 13px;
}

/* TIMELINE */

.timeline-item {
    border-left: 2px solid #cbd7cf;
    padding: 0 0 32px 25px;
    margin-left: 8px;
    position: relative;
}

.timeline-item:before {
    content: '';
    position: absolute;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #4e6b5b;
    left: -6px;
    top: 4px;
}

.date {
    color: #4e6b5b;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
}

.timeline-title {
    font-family: 'Playfair Display', serif;
    font-size: 24px;
    margin: 5px 0;
}

.company {
    font-weight: 600;
    font-size: 13px;
    margin-bottom: 8px;
}

/* SKILLS */

.skill {
    background: white;
    border: 1px solid #dfe5e0;
    border-radius: 15px;
    padding: 15px;
    margin-bottom: 10px;
}

.skill-head {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    font-weight: 600;
}

.track {
    height: 5px;
    background: #e7ece8;
    border-radius: 10px;
    margin-top: 9px;
}

.fill {
    height: 5px;
    background: #4e6b5b;
    border-radius: 10px;
}

/* PROJECT */

.project {
    background: white;
    border: 1px solid #dfe5e0;
    border-radius: 20px;
    padding: 23px;
    min-height: 220px;
    margin-bottom: 18px;
}

.project-number {
    color: #9aa59e;
    font-size: 11px;
    font-weight: 700;
}

.project h3 {
    font-size: 23px;
    margin: 20px 0 8px;
}

.tag {
    display: inline-block;
    background: #e6ece7;
    color: #30483b;
    border-radius: 20px;
    padding: 5px 9px;
    margin: 3px;
    font-size: 9px;
    font-weight: 700;
}

/* CERTIFICATION */

.cert {
    background: white;
    border: 1px solid #dfe5e0;
    border-radius: 18px;
    padding: 20px 10px;
    text-align: center;
    min-height: 140px;
}

.cert-icon {
    font-size: 25px;
}

.cert h3 {
    font-size: 18px;
    margin: 8px 0 4px;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #68736d;
    padding: 70px 0 20px;
    font-size: 11px;
}

/* MOBILE */

@media (max-width: 700px) {

    .hero {
        padding: 30px 22px;
    }

    .hero-title {
        font-size: 45px;
    }

    .section-title {
        font-size: 35px;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# NAVIGATION
# ============================================================

st.markdown("""
<div class="nav">

    <div class="logo">
        Annisa<span>.</span>
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

    <div class="eyebrow">
        CHEMICAL ANALYSIS × R&D
    </div>

    <div class="hero-title">
        Turning Knowledge Into
        <span>Real Experience.</span>
    </div>

    <div class="hero-text">

        Mahasiswi Analis Kimia yang tertarik pada
        pekerjaan laboratorium, research & development,
        quality control, dan formulasi produk.

        Saat ini sedang mengembangkan pengalaman
        melalui kegiatan akademik dan praktik
        di laboratorium R&D.

    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# STATISTICS
# ============================================================

st.write("")

c1, c2, c3, c4 = st.columns(4)

statistics = [
    ("2024", "Started Chemical Analysis"),
    ("R&D", "Current Internship Area"),
    ("10+", "Laboratory Techniques"),
    ("6+", "Instrumental Methods"),
]

for col, number, label in zip(
    [c1, c2, c3, c4],
    [x[0] for x in statistics],
    [x[1] for x in statistics],
):

    with col:

        st.markdown(
            f"""
            <div class="stat">

                <div class="stat-number">
                    {number}
                </div>

                <div class="stat-label">
                    {label}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# ABOUT
# ============================================================

st.markdown(
    '<div class="section" id="about"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="kicker">01 — ABOUT ME</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">More than a title.</div>',
    unsafe_allow_html=True,
)

c1, c2 = st.columns(2)

with c1:

    st.markdown("""
    <div class="card">

        <div class="card-icon">
            🧪
        </div>

        <div class="card-title">
            Chemical Analysis Student
        </div>

        <div class="muted">

            Saya merupakan mahasiswi
            Politeknik AKA Bogor jurusan
            Analis Kimia.

            Saya mempelajari preparasi sampel,
            pembuatan larutan, titrasi,
            analisis instrumen, pengolahan data,
            validasi metode, dan sistem mutu.

        </div>

    </div>
    """, unsafe_allow_html=True)


with c2:

    st.markdown("""
    <div class="card">

        <div class="card-icon">
            🔬
        </div>

        <div class="card-title">
            Exploring R&D
        </div>

        <div class="muted">

            Saat ini menjalani PKL di
            R&D Laboratory PT ADEV Natural Indonesia.

            Pengalaman meliputi pembuatan emulsi lotion,
            penggunaan multimix, pengukuran pH dan
            viskositas, preparasi sampel,
            serta dokumentasi data.

        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# EXPERIENCE
# ============================================================

st.markdown(
    '<div class="section" id="experience"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="kicker">02 — EXPERIENCE</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">My journey.</div>',
    unsafe_allow_html=True,
)

experience = [

    (
        "SEPT 2026 — PRESENT",
        "R&D Laboratory Intern",
        "PT ADEV Natural Indonesia · Bogor",
        "Preparasi sampel, penimbangan, pembuatan emulsi lotion, multimix, pH meter, viskositas, centrifuge, input data, dan pembelajaran fungsi bahan.",
    ),

    (
        "2024 — PRESENT",
        "Chemical Analysis Student",
        "Politeknik AKA Bogor",
        "Pembelajaran analisis kimia, titrasi, kimia organik, kimia lingkungan, instrumentasi, validasi metode, pengolahan data, dan sistem mutu.",
    ),

    (
        "2025 — PRESENT",
        "Organization & Campus Activities",
        "Campus Organizations",
        "Kegiatan koordinasi, komunikasi, administrasi, kepanitiaan, dan kerja sama tim.",
    ),

]

for date, title, company, description in experience:

    st.markdown(
        f"""
        <div class="timeline-item">

            <div class="date">
                {date}
            </div>

            <div class="timeline-title">
                {title}
            </div>

            <div class="company">
                {company}
            </div>

            <div class="muted">
                {description}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# SKILLS
# ============================================================

st.markdown(
    '<div class="section" id="skills"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="kicker">03 — SKILLS</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">Tools & capabilities.</div>',
    unsafe_allow_html=True,
)

skills = [

    ("Sample Preparation", 88),
    ("Titration & Solution Preparation", 85),
    ("pH Measurement", 82),
    ("Viscosity Testing", 78),
    ("Laboratory Documentation", 86),

    ("Excel & Data Entry", 84),
    ("UV-Vis", 70),
    ("FTIR", 65),
    ("AAS / SSA", 62),
    ("GC / HPLC / TLC", 55),

]

left, right = st.columns(2)

for index, (name, value) in enumerate(skills):

    column = left if index < 5 else right

    with column:

        st.markdown(
            f"""
            <div class="skill">

                <div class="skill-head">

                    <span>
                        {name}
                    </span>

                    <span>
                        {value}%
                    </span>

                </div>

                <div class="track">

                    <div
                        class="fill"
                        style="width:{value}%"
                    ></div>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# PROJECTS
# ============================================================

st.markdown(
    '<div class="section" id="projects"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="kicker">04 — PROJECTS</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">Selected projects.</div>',
    unsafe_allow_html=True,
)

projects = [

    (
        "01",
        "Lotion Emulsion Formulation",
        "R&D / FORMULATION",
        "Mempelajari pembuatan emulsi lotion, fungsi bahan, fase minyak dan air, multimix, pH, dan viskositas.",
    ),

    (
        "02",
        "Iodometric Analysis",
        "CHEMICAL ANALYSIS",
        "Praktik analisis berbasis titrasi iodometri, standardisasi larutan, perhitungan kadar, dan pengolahan hasil.",
    ),

    (
        "03",
        "Instrumental Analysis",
        "INSTRUMENTATION",
        "Pengenalan dan pembelajaran instrumen UV-Vis, FTIR, AAS, GC, HPLC, dan TLC.",
    ),

    (
        "04",
        "Laboratory Documentation",
        "DOCUMENTATION",
        "Pengelolaan data sampel, input hasil penimbangan, spreadsheet, pencatatan, dan dokumentasi laboratorium.",
    ),

    (
        "05",
        "Method Validation Study",
        "QUALITY",
        "Pembelajaran linearitas, LOD, LOQ, presisi, akurasi, dan parameter validasi metode.",
    ),

    (
        "06",
        "Food Safety & Quality",
        "QUALITY SYSTEM",
        "Pembelajaran GMP, HACCP, ISO 22000, FSSC 22000, QA & QC.",
    ),

]

cols = st.columns(3)

for i, (
    number,
    title,
    category,
    description,
) in enumerate(projects):

    with cols[i % 3]:

        st.markdown(
            f"""
            <div class="project">

                <div class="project-number">
                    {number}
                </div>

                <h3>
                    {title}
                </h3>

                <div class="muted">
                    {description}
                </div>

                <br>

                <span class="tag">
                    {category}
                </span>

            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# PROJECT DETAIL
# ============================================================

st.markdown("### Explore a project")

project_names = [
    project[1]
    for project in projects
]

selected = st.selectbox(
    "Choose project",
    project_names,
    label_visibility="collapsed",
)

selected_project = next(
    project
    for project in projects
    if project[1] == selected
)

st.info(
    f"""
**{selected_project[1]}**

Category: {selected_project[2]}

{selected_project[3]}
"""
)


# ============================================================
# CERTIFICATIONS
# ============================================================

st.markdown(
    '<div class="section" id="certifications"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="kicker">05 — CERTIFICATIONS</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">Training & learning.</div>',
    unsafe_allow_html=True,
)

certifications = [

    (
        "🛡️",
        "GMP",
        "Good Manufacturing Practice",
    ),

    (
        "✓",
        "HACCP",
        "Hazard Analysis & Critical Control Point",
    ),

    (
        "◈",
        "ISO 22000:2018",
        "Food Safety Management System",
    ),

    (
        "◉",
        "FSSC 22000",
        "Version 6.0",
    ),

    (
        "▦",
        "QA & QC",
        "In Food Industry",
    ),

    (
        "✦",
        "HACCP Documentation",
        "Document Preparation",
    ),

]

cols = st.columns(3)

for i, (
    icon,
    title,
    description,
) in enumerate(certifications):

    with cols[i % 3]:

        st.markdown(
            f"""
            <div class="cert">

                <div class="cert-icon">
                    {icon}
                </div>

                <h3>
                    {title}
                </h3>

                <div class="muted">
                    {description}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# CONTACT
# ============================================================

st.markdown(
    '<div class="section" id="contact"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="kicker">06 — CONTACT</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">Let’s connect.</div>',
    unsafe_allow_html=True,
)

left, right = st.columns([1, 1.3])

with left:

    st.markdown("""
    <div class="card">

        <div class="card-icon">
            ✉️
        </div>

        <div class="card-title">
            Open to opportunities.
        </div>

        <div class="muted">

            Tertarik untuk berdiskusi mengenai
            internship, laboratory work,
            R&D, quality control,
            dan pengembangan profesional.

        </div>

        <br>

        <div class="muted">
            📧 your.email@example.com
        </div>

        <div class="muted">
            🔗 linkedin.com/in/yourusername
        </div>

        <div class="muted">
            📍 Bogor, Indonesia
        </div>

    </div>
    """, unsafe_allow_html=True)


with right:

    with st.form("contact_form"):

        name = st.text_input(
            "Nama"
        )

        email = st.text_input(
            "Email"
        )

        message = st.text_area(
            "Pesan",
            height=120,
        )

        submit = st.form_submit_button(
            "Kirim Pesan"
        )

        if submit:

            if name and email and message:

                st.success(
                    "Pesan berhasil diisi. "
                    "Form ini bisa dihubungkan "
                    "ke email/API nanti."
                )

            else:

                st.warning(
                    "Mohon isi semua kolom."
                )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    <b>Annisa.</b>

    <br><br>

    Chemical Analysis · R&D · Laboratory · Quality

    <br><br>

    © 2026 Annisa Widiyastuti Putri
    · Built with Streamlit

</div>
""", unsafe_allow_html=True)
