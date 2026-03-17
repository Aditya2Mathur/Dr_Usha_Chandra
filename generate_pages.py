import os
import re

base_dir = r"e:\WebsiteProject(2026)\VarnikaHealthcare"
services_html_path = os.path.join(base_dir, "services.html")

with open(services_html_path, "r", encoding="utf-8") as f:
    template_content = f.read()

# Fix asset paths
template_content = template_content.replace('href="Assets/', 'href="../Assets/')
template_content = template_content.replace('src="Assets/', 'src="../Assets/')
template_content = template_content.replace('href="index.html"', 'href="../index.html"')
template_content = template_content.replace('href="about.html"', 'href="../about.html"')
template_content = template_content.replace('href="services.html"', 'href="../services.html"')
template_content = template_content.replace('href="doctor.html"', 'href="../doctor.html"')
template_content = template_content.replace('href="contact.html"', 'href="../contact.html"')

locations = ["sitapur", "shahjahanpur"]
location_names = ["Sitapur", "Shahjahanpur"]
clinics = ["Varnika Skin Care", "Shree Balaji Skin Care"]

services = [
    {
        "id": "acne-treatment",
        "title": "Acne & Pimples",
        "seo_title": "Best Acne Treatment in {loc} | Pimple Care - Dr. Usha",
        "desc": "Looking for the best acne and pimple treatment in {loc}? Visit {clinic} for expert solutions by Dermatologist Dr. Usha Chandra. Book today!",
        "h1": "Advanced Acne & Pimple Treatment in {loc}",
        "img": "../Assets/service/AcnePimplesTreatment.jpg",
        "content_template": """
        <div class="container" style="padding: 60px 0;">
            <div class="row" style="display: flex; flex-wrap: wrap; gap: 40px;">
                <div class="col-lg-8" style="flex: 1 1 60%;">
                    <h2 style="font-size: 32px; margin-bottom: 20px;">Understanding Acne / Muhase</h2>
                    <p style="font-size: 16px; line-height: 1.8; color: var(--text-color); margin-bottom: 20px;">Acne is a common skin condition that occurs when hair follicles become plugged with oil and dead skin cells. At {clinic} in {loc}, we provide comprehensive acne care tailored to adolescent and adult outbreaks.</p>
                    
                    <h3 style="font-size: 24px; margin-bottom: 15px;">Hormonal Imbalances & Triggers</h3>
                    <p style="font-size: 16px; line-height: 1.8; color: var(--text-color); margin-bottom: 20px;">Many factors like diet, stress, and hormonal changes cause acne. Dr. Usha Chandra specializes in identifying the root cause of your breakouts before beginning therapy.</p>

                    <h2 style="font-size: 32px; margin-bottom: 20px; margin-top: 40px;">Our Acne Treatment Solutions in {loc}</h2>
                    <h3 style="font-size: 24px; margin-bottom: 15px;">Medical Grade Topicals & Medications</h3>
                    <p style="font-size: 16px; line-height: 1.8; color: var(--text-color); margin-bottom: 20px;">We securely prescribe advanced, evidence-based creams, gels, and oral treatments targeted at reducing inflammation and clearing severe pimples effectively.</p>
                    
                    <h3 style="font-size: 24px; margin-bottom: 15px;">Chemical Peels for Acne Scars</h3>
                    <p style="font-size: 16px; line-height: 1.8; color: var(--text-color); margin-bottom: 20px;">For stubborn acne and post-acne dark spots, our <a href="chemical-peels.html" style="color: var(--primary-green); font-weight: 600;">Acne Corrective Chemical Peels</a> provide deep exfoliation and skin renewal.</p>
                </div>
                <div class="col-lg-4" style="flex: 1 1 30%;">
                    <img src="{img}" alt="Acne Treatment in {loc}" style="width: 100%; border-radius: var(--radius-lg); box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                    <div style="background: var(--light-bg); padding: 30px; border-radius: var(--radius-lg); margin-top: 30px;">
                        <h3 style="font-size: 20px; margin-bottom: 15px;">Book Consultation</h3>
                        <p style="margin-bottom: 20px; font-size: 15px;">Contact our {loc} clinic directly.</p>
                        <a href="../contact.html" class="btn btn-primary" style="width: 100%; text-align: center;">Book Now</a>
                    </div>
                </div>
            </div>
        </div>
        """
    },
    {
        "id": "pigmentation-melasma-treatment",
        "title": "Pigmentation & Melasma",
        "seo_title": "Pigmentation & Melasma Treatment in {loc} | Dr. Usha",
        "desc": "Effective solutions for dark spots, uneven skin tone, and melasma treatment in {loc}. Visit Dermatology expert Dr. Usha Chandra at {clinic}.",
        "h1": "Pigmentation & Melasma Treatment in {loc}",
        "img": "../Assets/service/PigmentationMelasmaTreatment.jpg",
        "content_template": """
        <div class="container" style="padding: 60px 0;">
            <div class="row" style="display: flex; flex-wrap: wrap; gap: 40px;">
                <div class="col-lg-8" style="flex: 1 1 60%;">
                    <h2 style="font-size: 32px; margin-bottom: 20px;">Understanding Pigmentation & Melasma (Jhaiya)</h2>
                    <p style="font-size: 16px; line-height: 1.8; color: var(--text-color); margin-bottom: 20px;">Hyperpigmentation and melasma can be extremely stubborn to remove utilizing over-the-counter methods. At {clinic} in {loc}, we offer targeted clinical treatments to restore your natural, pristine even skin tone and boost your confidence natively.</p>
                    
                    <h2 style="font-size: 32px; margin-bottom: 20px; margin-top: 40px;">Our Treatment Approach</h2>
                    <p style="font-size: 16px; line-height: 1.8; color: var(--text-color); margin-bottom: 20px;">Through a combination of customized topical brightening agents, strict sun protection protocols, and advanced procedures like deep <a href="chemical-peels.html" style="color: var(--primary-green); font-weight: 600;">Chemical Peels</a>, we significantly reduce dark patches with minimal downtime.</p>
                </div>
                <div class="col-lg-4" style="flex: 1 1 30%;">
                    <img src="{img}" alt="Melasma Treatment in {loc}" style="width: 100%; border-radius: var(--radius-lg); box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                    <div style="background: var(--light-bg); padding: 30px; border-radius: var(--radius-lg); margin-top: 30px;">
                        <h3 style="font-size: 20px; margin-bottom: 15px;">Book Consultation</h3>
                        <p style="margin-bottom: 20px; font-size: 15px;">Ready to restore your glow in {loc}?</p>
                        <a href="../contact.html" class="btn btn-primary" style="width: 100%; text-align: center;">Book Now</a>
                    </div>
                </div>
            </div>
        </div>
        """
    },
    {
        "id": "hair-fall-treatment",
        "title": "Hair Fall & Dandruff",
        "seo_title": "Best Hair Fall Treatment in {loc} | PRP Expert Dr. Usha",
        "desc": "Stop hair fall with Dr. Usha Chandra's advanced treatments in {loc}. Comprehensive care for dandruff, alopecia, and hair regrowth at {clinic}.",
        "h1": "Advanced Hair Fall & Dandruff Treatment in {loc}",
        "img": "../Assets/service/HairFallDandruffTreatment.jpg",
        "content_template": """
        <div class="container" style="padding: 60px 0;">
            <div class="row" style="display: flex; flex-wrap: wrap; gap: 40px;">
                <div class="col-lg-8" style="flex: 1 1 60%;">
                    <h2 style="font-size: 32px; margin-bottom: 20px;">Stop Hair Loss in {loc}</h2>
                    <p style="font-size: 16px; line-height: 1.8; color: var(--text-color); margin-bottom: 20px;">Whether it's seasonal hair fall, persistent dandruff, or early pattern baldness, expert medical intervention is crucial to stopping follicle loss early. Dr. Usha Chandra at {clinic} provides proven hair restoration therapies with massive success rates.</p>
                    
                    <h2 style="font-size: 32px; margin-bottom: 20px; margin-top: 40px;">PRP Therapy & Growth Solutions</h2>
                    <p style="font-size: 16px; line-height: 1.8; color: var(--text-color); margin-bottom: 20px;">We specialize in stimulating dormant hair follicles using medical-grade serums, nutritional support, and regenerative treatments like Platelet-Rich Plasma (PRP) explicitly tailored for our {loc} patients.</p>
                </div>
                <div class="col-lg-4" style="flex: 1 1 30%;">
                    <img src="{img}" alt="Hair Fall Treatment {loc}" style="width: 100%; border-radius: var(--radius-lg); box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                    <div style="background: var(--light-bg); padding: 30px; border-radius: var(--radius-lg); margin-top: 30px;">
                        <h3 style="font-size: 20px; margin-bottom: 15px;">Book Consultation</h3>
                        <a href="../contact.html" class="btn btn-primary" style="width: 100%; text-align: center;">Book Now</a>
                    </div>
                </div>
            </div>
        </div>
        """
    },
    {
        "id": "anti-aging-rejuvenation",
        "title": "Anti-Aging & Rejuvenation",
        "seo_title": "Anti-Aging & Skin Rejuvenation in {loc} | Dermatologist",
        "desc": "Medical-grade anti-aging treatments and skin rejuvenation therapies in {loc}. Reverse signs of aging with Dr. Usha Chandra at {clinic}.",
        "h1": "Anti-Aging & Skin Rejuvenation in {loc}",
        "img": "../Assets/service/AntiAgingRejuvenation.jpg",
        "content_template": """
        <div class="container" style="padding: 60px 0;">
            <div class="row" style="display: flex; flex-wrap: wrap; gap: 40px;">
                <div class="col-lg-8" style="flex: 1 1 60%;">
                    <h2 style="font-size: 32px; margin-bottom: 20px;">Youthful Glow & Wrinkle Reduction</h2>
                    <p style="font-size: 16px; line-height: 1.8; color: var(--text-color); margin-bottom: 20px;">Aging is organic, but its visible signs on the face and neck can be gracefully managed and reversed. At {clinic} in {loc}, we seamlessly provide safe, highly effective aesthetic dermatological procedures to restore volume, clear blemishes, and smooth fine lines.</p>
                </div>
                <div class="col-lg-4" style="flex: 1 1 30%;">
                    <img src="{img}" alt="Anti-aging Treatment {loc}" style="width: 100%; border-radius: var(--radius-lg); box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                    <div style="background: var(--light-bg); padding: 30px; border-radius: var(--radius-lg); margin-top: 30px;">
                        <h3 style="font-size: 20px; margin-bottom: 15px;">Book Consultation</h3>
                        <a href="../contact.html" class="btn btn-primary" style="width: 100%; text-align: center;">Book Now</a>
                    </div>
                </div>
            </div>
        </div>
        """
    },
    {
        "id": "infections-allergies",
        "title": "Infections & Allergies",
        "seo_title": "Skin Infection & Allergy Doctor in {loc} | Dr. Usha Chandra",
        "desc": "Expert diagnosis and care for fungal infections, rashes, and skin allergies in {loc}. Visit Board-certified dermatologist Dr. Usha Chandra.",
        "h1": "Treatment for Skin Infections & Allergies in {loc}",
        "img": "../Assets/service/InfectionsAllergies.jpg",
        "content_template": """
        <div class="container" style="padding: 60px 0;">
            <div class="row" style="display: flex; flex-wrap: wrap; gap: 40px;">
                <div class="col-lg-8" style="flex: 1 1 60%;">
                    <h2 style="font-size: 32px; margin-bottom: 20px;">Expert Clinical Dermatology in {loc}</h2>
                    <p style="font-size: 16px; line-height: 1.8; color: var(--text-color); margin-bottom: 20px;">Bacterial spots, highly contagious fungal infections, eczema, psoriasis, and unexplained rashes require an expert eye. Do not use generic market tubes that exacerbate the issue. Dr. Usha Chandra intimately provides accurate diagnosis, comprehensive testing, and prompt relief therapies directly at {clinic}.</p>
                </div>
                <div class="col-lg-4" style="flex: 1 1 30%;">
                    <img src="{img}" alt="Skin Infection Treatment {loc}" style="width: 100%; border-radius: var(--radius-lg); box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                    <div style="background: var(--light-bg); padding: 30px; border-radius: var(--radius-lg); margin-top: 30px;">
                        <h3 style="font-size: 20px; margin-bottom: 15px;">Book Consultation</h3>
                        <a href="../contact.html" class="btn btn-primary" style="width: 100%; text-align: center;">Book Now</a>
                    </div>
                </div>
            </div>
        </div>
        """
    },
    {
        "id": "chemical-peels",
        "title": "Chemical Peels",
        "seo_title": "Advanced Chemical Peels in {loc} | Acne Scars & Glow",
        "desc": "Rejuvenate your skin with medical-grade Chemical Peels at {clinic} in {loc}. Highly effective for acne scars, pigmentation, and dull skin.",
        "h1": "Medical-Grade Chemical Peels in {loc}",
        "img": "../Assets/service/ChemicalPeels.jpg",
        "content_template": """
        <div class="container" style="padding: 60px 0;">
            <div class="row" style="display: flex; flex-wrap: wrap; gap: 40px;">
                <div class="col-lg-8" style="flex: 1 1 60%;">
                    <h2 style="font-size: 32px; margin-bottom: 20px;">Reveal Fresh, Glowing Skin</h2>
                    <p style="font-size: 16px; line-height: 1.8; color: var(--text-color); margin-bottom: 20px;">Chemical peeling is a clinical procedure that accelerates skin exfoliation. At our {loc} clinic, we formally craft and specifically formulate peels (Glycolic, Salicylic, TCA, Mandelic) based precisely on your unique skin tone and type.</p>
                    
                    <h3 style="font-size: 24px; margin-bottom: 15px;">What Does It Treat?</h3>
                    <p style="font-size: 16px; line-height: 1.8; color: var(--text-color); margin-bottom: 20px;">They are universally heralded and highly utilized for treating deep-seated acne scars, severe sun tanning, melasma, dark circles, and returning that overall youthful vibrancy lost to pollution.</p>
                </div>
                <div class="col-lg-4" style="flex: 1 1 30%;">
                    <img src="{img}" alt="Chemical Peel {loc}" style="width: 100%; border-radius: var(--radius-lg); box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                    <div style="background: var(--light-bg); padding: 30px; border-radius: var(--radius-lg); margin-top: 30px;">
                        <h3 style="font-size: 20px; margin-bottom: 15px;">Book Consultation</h3>
                        <a href="../contact.html" class="btn btn-primary" style="width: 100%; text-align: center;">Book Now</a>
                    </div>
                </div>
            </div>
        </div>
        """
    }
]

for i, loc in enumerate(locations):
    loc_dir = os.path.join(base_dir, loc)
    os.makedirs(loc_dir, exist_ok=True)
    
    clinic = clinics[i]
    loc_name = location_names[i]
    
    # 1. Generate Hub Page
    hub_content = template_content
    # Clean the Title and Description
    # We'll use simple search-replace for the specific `<title>` in the template to be safe.
    hub_content = re.sub(r'<title>.*?</title>', f'<title>Best Dermatologist in {loc_name} | {clinic}</title>', hub_content, flags=re.IGNORECASE|re.DOTALL)
    hub_content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="Looking for the best dermatologist in {loc_name}? Visit {clinic} for expert treatments by Dr. Usha Chandra.">', hub_content, flags=re.IGNORECASE|re.DOTALL)
    
    # Update H1 and Page Banner
    hub_content = hub_content.replace('Skin & Hair Treatments', f'Skin & Hair Treatments in {loc_name}')
    hub_content = hub_content.replace('Specialized dermatology services for every skin need', f'Specialized dermatology services in {loc_name}')
    
    # Replace contact.html mapping for linking to localized service pages. 
    lines = hub_content.splitlines()
    link_idx = 0
    new_lines = []
    for line in lines:
        if '<a href="../contact.html" class="service-link">' in line and link_idx < len(services):
            line = line.replace('../contact.html', f"{services[link_idx]['id']}.html")
            link_idx += 1
        new_lines.append(line)
        
    hub_content = "\\n".join(new_lines)
    
    with open(os.path.join(loc_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(hub_content)
        
    print(f"Created Hub logic for {loc_name}.")
        
    # 2. Generate Detailed Service Pages
    for s in services:
        page_content = template_content
        page_title = s["seo_title"].format(loc=loc_name, clinic=clinic)
        page_desc = s["desc"].format(loc=loc_name, clinic=clinic)
        
        page_content = re.sub(r'<title>.*?</title>', f'<title>{page_title}</title>\\n    <meta name="description" content="{page_desc}">', page_content, flags=re.IGNORECASE|re.DOTALL)
        
        # H1
        page_content = page_content.replace('Skin & Hair Treatments', f'{s["h1"].format(loc=loc_name, clinic=clinic)}')
        
        # Breadcrumb
        page_content = page_content.replace('<span>Services</span>', f'<span><a href="index.html" style="color:rgba(30, 41, 59, 1);">Services in {loc_name}</a></span> <span class="breadcrumb-separator"><i class="fa-solid fa-chevron-right"></i></span> <span>{s["title"]}</span>')
        
        start_pattern = '<section id="services" class="services-section section-bg-light">'
        end_pattern = '</section>'
        
        parts = page_content.split(start_pattern)
        if len(parts) > 1:
            before = parts[0]
            rest = parts[1]
            section_end_idx = rest.find('</section>') + len('</section>')
            after = rest[section_end_idx:]
            
            new_section = start_pattern + "\\n" + s["content_template"].format(loc=loc_name, clinic=clinic, img=s["img"]) + "\\n</section>"
            page_content = before + new_section + after
            
        with open(os.path.join(loc_dir, f"{s['id']}.html"), "w", encoding="utf-8") as f:
            f.write(page_content)

print("Generated all 14 localized SEO pages successfully.")
