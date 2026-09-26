import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Annisa — Chemical Analysis Portfolio",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# DATA
# Ganti bagian ini kalau ingin mengubah isi portfolio
# ============================================================

PROFILE = {
    "name": "Annisa Widiyastuti Putri",
    "short_name": "Annisa",
    "role": "Chemical Analysis Student",
    "location": "Bogor, Indonesia",
    "email": "your.email@example.com",
    "linkedin": "linkedin.com/in/yourusername",
    "instagram": "@yourusername",
}

EXPERIENCE = [
    {
        "date": "SEPT 2026 — PRESENT",
        "title": "R&D Laboratory Intern",
        "company": "PT ADEV Natural Indonesia · Bogor",
        "description": (
            "Preparasi dan penimbangan sampel, pembuatan emulsi lotion, "
            "penggunaan multimix, pengukuran pH dan viskositas, centrifuge, "
            "input data, serta mempelajari fungsi bahan dan tahapan formulasi."
        ),
        "tags": ["R&D", "Formulation", "Laboratory"],
    },
    {
        "date": "2024 — PRESENT",
        "title": "Chemical Analysis Student",
        "company": "Politeknik AKA Bogor",
        "description": (
            "Mempelajari analisis kimia, preparasi larutan, titrasi, "
            "kimia organik, kimia lingkungan, instrumentasi, validasi metode, "
            "pengolahan data, dan sistem mutu."
        ),
        "tags": ["Chemistry", "Analysis", "Laboratory"],
    },
    {
        "date": "2025 — PRESENT",
        "title": "Organization & Campus Activities",
        "company": "Campus Organizations",
        "description": (
            "Terlibat dalam kegiatan organisasi, komunikasi, koordinasi, "
            "administrasi, kepanitiaan, dan kerja sama tim."
        ),
        "tags": ["Leadership", "Communication", "Teamwork"],
    },
]

SKILLS = [
    ("Sample Preparation", 88, "🧪"),
    ("Titration & Solution Preparation", 85, "⚗️"),
    ("pH Measurement", 82, "◉"),
    ("Viscosity Testing", 78, "〰"),
    ("Laboratory Documentation", 86, "▤"),
    ("Excel & Data Entry", 84, "▦"),
    ("UV-Vis", 70, "◌"),
    ("FTIR", 65, "⌁"),
    ("AAS / SSA", 62, "◈"),
    ("GC / HPLC / TLC", 55, "◇"),
]

PROJECTS = [
    {
        "number": "01",
        "title": "Lotion Emulsion Formulation",
        "category": "R&D / FORMULATION",
        "description": (
            "Pembelajaran pembuatan emulsi lotion, fungsi bahan, "
            "fase minyak dan air, penggunaan multimix, serta evaluasi "
            "pH dan viskositas."
        ),
        "tools": [
            "Multimix",
            "pH Meter",
            "Viscometer",
            "Centrifuge",
        ],
        "result": (
            "Memahami alur dasar formulasi emulsi dan faktor yang "
            "memengaruhi pembentukan serta stabilitas emulsi."
        ),
    },
    {
        "number": "02",
        "title": "Iodometric Analysis",
        "category": "CHEMICAL ANALYSIS",
        "description": (
            "Praktik analisis berbasis titrasi iodometri, standardisasi "
            "larutan, perhitungan kadar, dan pengolahan hasil."
        ),
        "tools": [
            "Burette",
            "Analytical Balance",
            "Titration",
        ],
        "result": (
            "Memahami prinsip reaksi redoks dan perhitungan "
            "analisis volumetri."
        ),
    },
    {
        "number": "03",
        "title": "Instrumental Analysis",
        "category": "INSTRUMENTATION",
        "description": (
            "Pengenalan dan pembelajaran penggunaan berbagai instrumen "
            "analisis dalam kegiatan akademik dan laboratorium."
        ),
        "tools": [
            "UV-Vis",
            "FTIR",
            "AAS",
            "GC",
            "HPLC",
            "TLC",
        ],
        "result": (
            "Mengenal prinsip dasar, fungsi, dan penggunaan "
            "instrumen analisis."
        ),
    },
    {
        "number": "04",
        "title": "Laboratory Documentation",
        "category": "DOCUMENTATION",
        "description": (
            "Pengelolaan data sampel, input hasil penimbangan, "
            "spreadsheet, pencatatan, dan penataan informasi laboratorium."
        ),
        "tools": [
            "Excel",
            "Spreadsheet",
            "SOP",
        ],
        "result": (
            "Meningkatkan ketelitian dalam dokumentasi dan "
            "pengelolaan data laboratorium."
        ),
    },
    {
        "number": "05",
        "title": "Method Validation Study",
        "category": "QUALITY",
        "description": (
            "Pembelajaran parameter validasi metode seperti linearitas, "
            "LOD, LOQ, presisi, akurasi, dan parameter terkait."
        ),
        "tools": [
            "Excel",
            "Data Analysis",
            "Validation",
        ],
        "result": (
            "Memahami konsep dasar evaluasi kinerja metode analisis."
        ),
    },
    {
        "number": "06",
        "title": "Food Safety & Quality",
        "category": "QUALITY SYSTEM",
        "description": (
            "Pelatihan dan pembelajaran mengenai GMP, HACCP, "
            "ISO 22000, FSSC 22000, QA & QC."
        ),
        "tools": [
            "GMP",
            "HACCP",
            "ISO 22000",
            "FSSC",
        ],
        "result": (
            "Memahami dasar sistem keamanan pangan dan "
            "quality assurance."
        ),
    },
]

CERTIFICATIONS = [
    ("🛡️", "GMP", "Good Manufacturing Practice"),
    ("✓", "HACCP", "Hazard Analysis & Critical Control Point"),
    ("◈", "ISO 22000:2018", "Food Safety Management System"),
    ("◉", "FSSC 22000", "Version 6.0"),
    ("▦", "QA & QC", "In Food Industry"),
    ("✦", "HACCP Documentation", "Document Preparation"),
]


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
<style>

@import url(
'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap'
);

/* ---------- VARIABLES ---------- */

:root {
    --bg: #f6f5ef;
    --paper: #ffffff;
    --ink: #18221d;
    --muted: #69746e;
    --sage: #496957;
    --sage-dark: #304a3b;
    --sage-soft: #e6ece7;
    --line: #dfe5e0;
}


/* ---------- GLOBAL ---------- */

html {
    scroll-behavior: smooth;
}

.stApp {
    background: var(--bg);
    color: var(--ink);
}

.block-container {
    max-width: 1180px;
    padding: 0 1.2rem 4rem;
}

[data-testid="stHeader"] {
    background: transparent;
}

footer {
    visibility: hidden;
}

* {
    font-family: "DM Sans", sans-serif;
}

h1,
h2,
h3,
h4 {
    font-family: "Playfair Display", serif !important;
    color: var(--ink) !important;
}


/* ---------- NAVBAR ---------- */

.topbar {
    position: sticky;
    top: 0;
    z-index: 999;

    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 16px 20px;
    margin-bottom: 28px;

    background: rgba(246, 245, 239, 0.88);
    backdrop-filter: blur(18px);

    border-bottom:
        1px solid rgba(223, 229, 224, 0.85);
}

.logo {
    font-family: "Playfair Display", serif;
    font-size: 24px;
    font-weight: 700;
}

.logo span {
    color: var(--sage);
}

.nav a {
    color: var(--ink);
    text-decoration: none;
    margin-left: 22px;
    font-size: 12px;
    font-weight: 600;
}

.nav a:hover {
    color: var(--sage);
}


/* ---------- HERO ---------- */

.hero {
    min-height: 650px;

    border:
        1px solid var(--line);

    border-radius: 34px;

    overflow: hidden;

    padding:
        70px 70px 55px;

    position: relative;

    background:
        radial-gradient(
            circle at 84% 18%,
            rgba(88, 121, 101, 0.18),
            transparent 24%
        ),

        radial-gradient(
            circle at 18% 86%,
            rgba(216, 225, 216, 0.75),
            transparent 30%
        ),

        linear-gradient(
            135deg,
            #f0f3ee,
            #e8ede8
        );
}

.hero-grid {
    display: grid;
    grid-template-columns:
        1.2fr 0.8fr;

    gap: 40px;

    align-items: center;
}

.eyebrow {
    color: var(--sage);

    text-transform: uppercase;

    letter-spacing: 3px;

    font-size: 11px;

    font-weight: 700;
}

.hero h1 {
    font-size:
        clamp(54px, 7vw, 86px);

    line-height: 0.94;

    letter-spacing: -4px;

    margin:
        18px 0 25px;
}

.hero h1 em {
    color: var(--sage);

    font-style: normal;
}

.hero p {
    color: var(--muted);

    font-size: 16px;

    line-height: 1.85;

    max-width: 610px;
}


/* ---------- HERO ART ---------- */

.hero-art {
    min-height: 390px;

    border-radius:
        38% 38% 42% 42%;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,.9),
            rgba(214,224,216,.8)
        );

    border:
        1px solid rgba(255,255,255,.9);

    display: flex;

    align-items: center;

    justify-content: center;

    position: relative;

    box-shadow:
        0 30px 80px
        rgba(42,62,51,.08);
}

.lab-orbit {
    width: 250px;
    height: 250px;

    border:
        1px solid #aebdb2;

    border-radius: 50%;

    display: flex;

    align-items: center;

    justify-content: center;
}

.flask {
    font-size: 100px;

    filter:
        grayscale(.2);
}

.floating {
    position: absolute;

    padding:
        13px 17px;

    background:
        rgba(255,255,255,.86);

    border:
        1px solid var(--line);

    border-radius: 15px;

    box-shadow:
        0 10px 30px
        rgba(40,60,48,.08);

    font-size: 11px;

    font-weight: 700;
}

.f1 {
    top: 22px;
    left: 20px;
}

.f2 {
    right: 15px;
    bottom: 60px;
}

.f3 {
    left: 20px;
    bottom: 25px;
}


/* ---------- BUTTON ---------- */

.btn {
    display: inline-block;

    padding:
        13px 20px;

    border-radius: 999px;

    text-decoration: none !important;

    font-size: 12px;

    font-weight: 700;

    margin:
        16px 7px 0 0;
}

.btn-dark {
    background: var(--sage-dark);

    color: white !important;
}

.btn-light {
    background: white;

    color: var(--ink) !important;

    border:
        1px solid var(--line);
}


/* ---------- STATS ---------- */

.stats {
    display: grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap: 12px;

    margin-top: 16px;
}

.stat {
    background:
        rgba(255,255,255,.68);

    border:
        1px solid var(--line);

    border-radius: 18px;

    padding: 20px;
}

.stat b {
    font-family:
        "Playfair Display",
        serif;

    font-size: 28px;
}

.stat small {
    display: block;

    color: var(--muted);

    margin-top: 4px;

    font-size: 10px;
}


/* ---------- SECTIONS ---------- */

.section {
    padding-top: 90px;

    scroll-margin-top: 80px;
}

.kicker {
    color: var(--sage);

    text-transform: uppercase;

    letter-spacing: 2.5px;

    font-size: 10px;

    font-weight: 700;
}

.section-title {
    font-size: 46px;

    margin:
        7px 0 28px;
}


/* ---------- CARDS ---------- */

.card {
    background: var(--paper);

    border:
        1px solid var(--line);

    border-radius: 22px;

    padding: 28px;

    height: 100%;

    box-shadow:
        0 10px 30px
        rgba(35,51,42,.035);
}

.card:hover {
    transform:
        translateY(-3px);

    transition:
        .25s;

    box-shadow:
        0 18px 42px
        rgba(35,51,42,.08);
}

.card-icon {
    font-size: 28px;

    margin-bottom: 15px;
}

.card-title {
    font-family:
        "Playfair Display",
        serif;

    font-size: 23px;

    margin-bottom: 9px;
}

.muted {
    color: var(--muted);

    line-height: 1.75;

    font-size: 13px;
}


/* ---------- QUOTE ---------- */

.quote {
    border-left:
        3px solid var(--sage);

    padding:
        12px 20px;

    margin:
        20px 0;

    color: var(--muted);

    font-family:
        "Playfair Display",
        serif;

    font-size: 20px;
}


/* ---------- TAG ---------- */

.tag {
    display: inline-block;

    background:
        var(--sage-soft);

    color:
        var(--sage-dark);

    border-radius:
        999px;

    padding:
        6px 9px;

    margin:
        3px 2px;

    font-size: 9px;

    font-weight: 700;
}


/* ---------- TIMELINE ---------- */

.timeline {
    border-left:
        2px solid #cfd8d1;

    margin-left: 8px;

    padding-left: 28px;
}

.timeline-item {
    position: relative;

    margin-bottom: 40px;
}

.timeline-item:before {
    content: "";

    width: 11px;
    height: 11px;

    border-radius: 50%;

    background:
        var(--sage);

    position: absolute;

    left: -35px;

    top: 5px;

    box-shadow:
        0 0 0 5px var(--bg);
}

.date {
    color: var(--sage);

    font-size: 10px;

    letter-spacing: 1.5px;

    font-weight: 700;
}

.timeline-title {
    font-family:
        "Playfair Display",
        serif;

    font-size: 26px;

    margin:
        5px 0;
}

.company {
    font-weight: 700;

    font-size: 13px;

    margin-bottom: 7px;
}


/* ---------- SKILLS ---------- */

.skill {
    background:
        var(--paper);

    border:
        1px solid var(--line);

    border-radius: 17px;

    padding:
        16px 18px;

    margin-bottom: 11px;
}

.skilltop {
    display: flex;

    justify-content: space-between;

    font-size: 12px;

    font-weight: 600;
}

.track {
    height: 5px;

    background: #e8ece8;

    border-radius: 20px;

    margin-top: 9px;

    overflow: hidden;
}

.fill {
    height: 100%;

    background:
        var(--sage);

    border-radius: 20px;
}


/* ---------- PROJECT ---------- */

.project {
    background:
        var(--paper);

    border:
        1px solid var(--line);

    border-radius: 23px;

    padding: 25px;

    min-height: 285px;

    margin-bottom: 18px;
}

.project:hover {
    transform:
        translateY(-3px);

    transition:
        .25s;

    box-shadow:
        0 18px 42px
        rgba(35,51,42,.08);
}

.project-num {
    color: #a2aaa4;

    font-size: 11px;

    font-weight: 700;
}

.project h3 {
    font-size: 24px;

    margin:
        23px 0 8px;
}


/* ---------- PROJECT DETAIL ---------- */

.project-detail {
    background:
        linear-gradient(
            135deg,
            #edf1ec,
            #ffffff
        );

    border:
        1px solid var(--line);

    border-radius: 24px;

    padding: 30px;

    margin-top: 20px;
}


/* ---------- CERTIFICATION ---------- */

.cert {
    background:
        var(--paper);

    border:
        1px solid var(--line);

    border-radius: 20px;

    text-align: center;

    padding:
        24px 12px;

    min-height: 160px;
}

.cert:hover {
    transform:
        translateY(-3px);

    transition:
        .25s;

    box-shadow:
        0 18px 42px
        rgba(35,51,42,.08);
}

.cert-icon {
    font-size: 27px;
}

.cert h4 {
    font-size: 18px;

    margin:
        10px 0 5px;
}


/* ---------- FOOTER ---------- */

.footer {
    text-align: center;

    padding-top: 80px;

    color: var(--muted);

    font-size: 11px;
}


/* ---------- MOBILE ---------- */

@media (max-width: 850px) {

    .nav {
        display: none;
    }

    .hero {
        padding:
            42px 26px;
    }

    .hero-grid {
        grid-template-columns:
            1fr;
    }

    .hero-art {
        min-height: 300px;
    }

    .stats {
        grid-template-columns:
            repeat(2, 1fr);
    }

    .section-title {
        font-size: 38px;
    }
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# NAVIGATION
# ============================================================

st.markdown(
    """
<div class="topbar">

    <div class="logo">
        Annisa<span>.</span>
    </div>

    <div class="nav">

        <a href="#about">
            ABOUT
        </a>

        <a href="#experience">
            EXPERIENCE
        </a>

        <a href="#skills">
            SKILLS
        </a>

        <a href="#projects">
            PROJECTS
        </a>

        <a href="#certifications">
            CERTIFICATIONS
        </a>

        <a href="#contact">
            CONTACT
        </a>

    </div>

</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HERO
# ============================================================

st.markdown(
    f"""
<div class="hero">

    <div class="hero-grid">

        <div>

            <div class="eyebrow">
                Chemical Analysis × R&D
            </div>

            <h1>
                Turning<br>
                Knowledge Into<br>
                <em>Real Experience.</em>
            </h1>

            <p>
                {PROFILE["role"]} dengan ketertarikan pada
                laboratory analysis, research & development,
                quality control, dan product formulation.
                Saya senang belajar melalui praktik,
                dokumentasi, dan pengalaman langsung
                di laboratorium.
            </p>

            <a
                class="btn btn-dark"
                href="#projects"
            >
                Explore Projects →
            </a>

            <a
                class="btn btn-light"
                href="#contact"
            >
                Let's Connect
            </a>

        </div>


        <div class="hero-art">

            <div class="floating f1">
                🧪 LABORATORY
            </div>

            <div class="floating f2">
                🔬 R&D / FORMULATION
            </div>

            <div class="floating f3">
                📊 DATA & QUALITY
            </div>

            <div class="lab-orbit">
                <div class="flask">
                    ⚗️
                </div>
            </div>

        </div>

    </div>

</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# STATS
# ============================================================

st.markdown(
    """
<div class="stats">

    <div class="stat">
        <b>2024</b>
        <small>
            Started Chemical Analysis
        </small>
    </div>

    <div class="stat">
        <b>R&D</b>
        <small>
            Current Internship Area
        </small>
    </div>

    <div class="stat">
        <b>10+</b>
        <small>
            Laboratory Techniques
        </small>
    </div>

    <div class="stat">
        <b>6+</b>
        <small>
            Instrumental Methods
        </small>
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
    '<div class="kicker">01 — About Me</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">More than a title.</div>',
    unsafe_allow_html=True,
)

about_left, about_right = st.columns(2)


with about_left:

    st.markdown(
        """
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

        Pembelajaran saya mencakup
        preparasi sampel, larutan,
        titrasi, analisis instrumen,
        pengolahan data, validasi metode,
        serta sistem mutu.

    </div>

    <div class="quote">

        “Belajar bukan hanya memahami teori,
        tetapi juga memahami bagaimana teori
        bekerja di laboratorium.”

    </div>

</div>
""",
        unsafe_allow_html=True,
    )


with about_right:

    st.markdown(
        """
<div class="card">

    <div class="card-icon">
        🌿
    </div>

    <div class="card-title">
        Currently Exploring R&D
    </div>

    <div class="muted">

        Saat ini menjalani PKL di bagian
        R&D Laboratory pada perusahaan
        maklon skincare.

        Fokus pengalaman mencakup formulasi
        emulsi, pengukuran pH dan viskositas,
        penggunaan multimix, preparasi sampel,
        dokumentasi, dan evaluasi sederhana.

    </div>

    <br>

    <span class="tag">
        Laboratory
    </span>

    <span class="tag">
        R&D
    </span>

    <span class="tag">
        Formulation
    </span>

    <span class="tag">
        Documentation
    </span>

</div>
""",
        unsafe_allow_html=True,
    )


# ============================================================
# EXPERIENCE
# ============================================================

st.markdown(
    '<div class="section" id="experience"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="kicker">02 — Experience</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">My journey.</div>',
    unsafe_allow_html=True,
)

timeline_html = '<div class="timeline">'

for item in EXPERIENCE:

    tags_html = ""

    for tag in item["tags"]:
        tags_html += f"""
        <span class="tag">
            {tag}
        </span>
        """

    timeline_html += f"""
    <div class="timeline-item">

        <div class="date">
            {item["date"]}
        </div>

        <div class="timeline-title">
            {item["title"]}
        </div>

        <div class="company">
            {item["company"]}
        </div>

        <div class="muted">
            {item["description"]}
        </div>

        <div style="margin-top:10px;">
            {tags_html}
        </div>

    </div>
    """

timeline_html += "</div>"

st.markdown(
    timeline_html,
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
    '<div class="kicker">03 — Skills</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">Tools & capabilities.</div>',
    unsafe_allow_html=True,
)

skill_left, skill_right = st.columns(2)

for column_index, column in enumerate(
    [skill_left, skill_right]
):

    with column:

        skills_part = SKILLS[
            column_index * 5:
            (column_index + 1) * 5
        ]

        for name, percentage, icon in skills_part:

            st.markdown(
                f"""
<div class="skill">

    <div class="skilltop">

        <span>
            {icon}
            &nbsp;
            {name}
        </span>

        <span>
            {percentage}%
        </span>

    </div>

    <div class="track">

        <div
            class="fill"
            style="width:{percentage}%"
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
    '<div class="kicker">04 — Projects</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">Selected projects.</div>',
    unsafe_allow_html=True,
)


# Interactive project selector

project_names = [
    project["title"]
    for project in PROJECTS
]

selected_project = st.selectbox(
    "Explore project detail",
    project_names,
    label_visibility="collapsed",
)

selected_data = next(
    project
    for project in PROJECTS
    if project["title"] == selected_project
)


tools_html = ""

for tool in selected_data["tools"]:

    tools_html += f"""
    <span class="tag">
        {tool}
    </span>
    """


st.markdown(
    f"""
<div class="project-detail">

    <div class="kicker">
        {selected_data["category"]}
    </div>

    <h2
        style="
        font-size:38px;
        margin:8px 0 12px;
        "
    >
        {selected_data["title"]}
    </h2>

    <div
        class="muted"
        style="
        font-size:14px;
        max-width:850px;
        "
    >
        {selected_data["description"]}
    </div>

    <br>

    <b>
        Tools / Methods
    </b>

    <br>

    {tools_html}

    <br><br>

    <b>
        Key Learning
    </b>

    <div class="muted">

        {selected_data["result"]}

    </div>

</div>
""",
    unsafe_allow_html=True,
)


# Project cards

st.markdown(
    "<br>",
    unsafe_allow_html=True,
)

project_columns = st.columns(3)


for index, project in enumerate(PROJECTS):

    with project_columns[index % 3]:

        st.markdown(
            f"""
<div class="project">

    <div class="project-num">
        {project["number"]}
    </div>

    <h3>
        {project["title"]}
    </h3>

    <div class="muted">
        {project["description"]}
    </div>

    <div style="margin-top:15px;">

        <span class="tag">
            {project["category"]}
        </span>

    </div>

</div>
""",
            unsafe_allow_html=True,
        )


# ============================================================
# CERTIFICATIONS
# ============================================================

st.markdown(
    '<div class="section" id="certifications"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="kicker">05 — Certifications</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">Training & learning.</div>',
    unsafe_allow_html=True,
)

cert_columns = st.columns(3)


for index, (
    icon,
    title,
    description,
) in enumerate(CERTIFICATIONS):

    with cert_columns[index % 3]:

        st.markdown(
            f"""
<div class="cert">

    <div class="cert-icon">
        {icon}
    </div>

    <h4>
        {title}
    </h4>

    <div
        class="muted"
        style="font-size:11px;"
    >
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
    '<div class="kicker">06 — Contact</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">Let’s connect.</div>',
    unsafe_allow_html=True,
)

contact_left, contact_right = st.columns(
    [0.85, 1.15]
)


with contact_left:

    st.markdown(
        f"""
<div class="card">

    <div class="card-icon">
        ✉️
    </div>

    <div class="card-title">
        Open to opportunities.
    </div>

    <div class="muted">

        Tertarik untuk berdiskusi mengenai
        internship, laboratory work, R&D,
        quality control, dan pengembangan
        profesional.

    </div>

    <br>

    <div class="muted">
        📧 {PROFILE["email"]}
    </div>

    <div class="muted">
        🔗 {PROFILE["linkedin"]}
    </div>

    <div class="muted">
        📍 {PROFILE["location"]}
    </div>

</div>
""",
        unsafe_allow_html=True,
    )


with contact_right:

    with st.form("contact_form"):

        name = st.text_input(
            "Your name"
        )

        email = st.text_input(
            "Your email"
        )

        message = st.text_area(
            "Message",
            height=130,
        )

        submitted = st.form_submit_button(
            "Send Message →"
        )

        if submitted:

            if (
                name
                and email
                and message
            ):

                st.success(
                    "Form berhasil digunakan. "
                    "Untuk mengirim pesan sungguhan, "
                    "hubungkan form ini ke email/API."
                )

            else:

                st.warning(
                    "Mohon isi semua kolom."
                )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="footer">

    <b>Annisa.</b>

    <br><br>

    Chemical Analysis · R&D · Laboratory · Quality

    <br><br>

    © 2026 Annisa Widiyastuti Putri
    · Built with Streamlit

</div>
""",
    unsafe_allow_html=True,
)
