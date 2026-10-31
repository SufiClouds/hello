import os

# Helper to load common header & footer
from generate_product_pages import render_header, render_footer

def create_page(filename, title, description, active_nav, content):
  html = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title} | Adeel Engineering Works</title>
    <meta name="description" content="{description}" />
    
    <meta property="og:title" content="{title} | Adeel Engineering Works" />
    <meta property="og:description" content="{description}" />
    <meta property="og:image" content="/assets/images/branding/hero-packaging-line.png" />
    <meta name="twitter:card" content="summary_large_image" />

    <link rel="icon" type="image/png" href="/assets/images/branding/logo-badge.png" />
    <link rel="stylesheet" href="/assets/css/main.css" />
    <link rel="stylesheet" href="/assets/css/responsive.css" />
  </head>
  <body>
    {render_header(active_nav)}
    {content}
    {render_footer()}
  </body>
</html>
"""
  with open(filename, "w", encoding="utf-8") as f:
    f.write(html)
  print(f"Generated {filename}")

# 1. ABOUT US (about.html)
about_content = """
    <div class="page-hero">
      <div class="container">
        <nav class="breadcrumbs">
          <a href="/index.html">Home</a> <span>/</span> <span style="color: #fff;">About Us</span>
        </nav>
        <span class="kicker">Corporate Profile</span>
        <h1 class="page-hero-title">About Adeel Engineering Works</h1>
        <p class="page-hero-desc">
          Specialized industrial manufacturer of automatic and semi-automatic packaging machines for granules, powders, and liquids since 2005.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 48px;">
          <div>
            <span class="kicker">Founded 2005</span>
            <h2 class="section-title">Two Decades of Packaging Machinery Excellence</h2>
            <p style="font-size: 1.0625rem; color: var(--color-text-muted); line-height: 1.7; margin-bottom: 20px;">
              <strong>Adeel Engineering Works</strong>, established in 2005 in Faisalabad, is a professional engineering enterprise specializing in producing packing machines. Our product portfolio includes full-auto and semi-auto packing machines for granules, powder, and liquid formulations.
            </p>
            <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.7; margin-bottom: 24px;">
              The competitive techniques and manufacturing facilities of Adeel Engineering Works make our machinery well known across Pakistan and in international markets. In addition to standard machinery lines, our facility offers dedicated engineering services for design inquiries and manufactures irregular packing machines according to the special requirements of our customers.
            </p>
            <div style="background: var(--color-bg-soft); border-left: 4px solid var(--color-accent); padding: 20px; border-radius: var(--radius-sm); margin-bottom: 24px;">
              <p style="font-style: italic; color: var(--color-primary-dark); font-size: 0.9375rem; line-height: 1.6;">
                "The operation principle of Adeel Engineering Works is to attract customers with high quality products; to move customers with considerate service; and to benefit customers with favorite price."
              </p>
              <div style="font-weight: 700; font-size: 0.8125rem; color: var(--color-accent); margin-top: 8px;">— Adeel Ahmed Niazi, CEO</div>
            </div>
          </div>

          <div style="background: #F8FAFC; border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 36px; text-align: center;">
            <img src="/assets/images/branding/ceo-adeel-ahmed-niazi.png" alt="Adeel Ahmed Niazi, CEO" style="width: 220px; height: 240px; object-fit: cover; border-radius: var(--radius-md); margin: 0 auto 20px; border: 3px solid #ffffff; box-shadow: var(--shadow-md);" />
            <h3 style="font-size: 1.25rem; color: var(--color-primary-dark); margin-bottom: 4px;">Adeel Ahmed Niazi</h3>
            <div style="font-size: 0.875rem; font-weight: 700; color: var(--color-accent); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 12px;">Chief Executive Officer</div>
            <p style="font-size: 0.875rem; color: var(--color-text-muted); line-height: 1.5;">
              Guiding engineering innovation, customer trust, and robust machinery construction at Adeel Engineering Works since 2005.
            </p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-soft">
      <div class="container">
        <div class="section-header text-center">
          <span class="kicker">Core Philosophy</span>
          <h2 class="section-title">Company Concept & Operational Creed</h2>
        </div>
        <div class="grid-3">
          <div class="feature-card">
            <h3 class="feature-title">People-Oriented & Innovation</h3>
            <p class="feature-text">Technological innovation and practical engineering dedicated to delivering forever service to manufacturing partners.</p>
          </div>
          <div class="feature-card">
            <h3 class="feature-title">Practical, Realistic & Sincere</h3>
            <p class="feature-text">Upholding faith, honest specifications, and durable machine build quality without inflated claims or unverified shortcuts.</p>
          </div>
          <div class="feature-card">
            <h3 class="feature-title">Mutual & Bright Future</h3>
            <p class="feature-text">Sincerely welcoming all customers both within Pakistan and abroad to cooperate with us for long-term production success.</p>
          </div>
        </div>
      </div>
    </section>
"""
create_page("about.html", "About Us", "Company profile, philosophy, and history of Adeel Engineering Works, founded in 2005 by Adeel Ahmed Niazi.", "about", about_content)

# 2. HISTORY (history.html)
history_content = """
    <div class="page-hero">
      <div class="container">
        <nav class="breadcrumbs">
          <a href="/index.html">Home</a> <span>/</span> <a href="/about.html">About Us</a> <span>/</span> <span style="color: #fff;">Company History</span>
        </nav>
        <span class="kicker">Our Journey</span>
        <h1 class="page-hero-title">Company History Since 2005</h1>
        <p class="page-hero-desc">
          Building packaging machinery reliability across Pakistan and international export markets for over two decades.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div style="max-width: 800px; margin: 0 auto;">
          <div style="border-left: 3px solid var(--color-accent); padding-left: 32px; display: flex; flex-direction: column; gap: 48px;">
            <div>
              <div class="kicker" style="margin-bottom: 4px;">2005 — Foundation</div>
              <h2 style="font-size: 1.5rem; color: var(--color-primary-dark); margin-bottom: 12px;">Establishment in Faisalabad</h2>
              <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.7;">
                Adeel Engineering Works was founded in Faisalabad, Pakistan by CEO Adeel Ahmed Niazi as a dedicated industrial engineering workshop specializing in packaging equipment. Starting with mechanical form-fill-seal machines, the company quickly established a reputation for robust construction and honest service.
              </p>
            </div>

            <div>
              <div class="kicker" style="margin-bottom: 4px;">2010 — Granule & Powder Line Modernization</div>
              <h2 style="font-size: 1.5rem; color: var(--color-primary-dark); margin-bottom: 12px;">Pillow Seal & Volumetric Feeder Systems</h2>
              <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.7;">
                Expanded into specialized vertical packaging solutions including the Central Seal Pillow Pack series and Back Seal Feeder machines for high-weight bulk commodities (1kg to 2kg) serving rice, tea, snacks, and washing powder processors.
              </p>
            </div>

            <div>
              <div class="kicker" style="margin-bottom: 4px;">2016 — PLC & Electronic Automation</div>
              <h2 style="font-size: 1.5rem; color: var(--color-primary-dark); margin-bottom: 12px;">Integration of Siemens & Delta PLC Automation</h2>
              <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.7;">
                Pioneered the integration of programmable logic controllers (PLCs), 7-inch color touchscreens, servo motion controls, and high-sensitivity photoelectric print registration cameras across multi-lane shampoo and high-speed powder screw packing machines.
              </p>
            </div>

            <div>
              <div class="kicker" style="margin-bottom: 4px;">2020 — Advanced Material Science & Turnkey Systems</div>
              <h2 style="font-size: 1.5rem; color: var(--color-primary-dark); margin-bottom: 12px;">GMP SS304/316 Steel & German Engineered Components</h2>
              <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.7;">
                Standardized on 12mm 304/316 stainless steel structures, Festo pneumatic solenoid assemblies, and critical German components for bearings, motor valves, and heavy-duty jacks, serving premier client brands across Pakistan.
              </p>
            </div>

            <div>
              <div class="kicker" style="margin-bottom: 4px;">Present Day</div>
              <h2 style="font-size: 1.5rem; color: var(--color-primary-dark); margin-bottom: 12px;">100+ Machine Solutions & Global Cooperation</h2>
              <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.7;">
                Today, Adeel Engineering Works produces high-speed tobacco filter pouch machines, 2-in-1 cosmetic sachet machines, 6-line liquid VFFS systems, horizontal tray wrappers, and full supporting lines of screw feeders, ribbon mixers, and coding systems.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
"""
create_page("history.html", "Company History", "Chronological history and manufacturing milestones of Adeel Engineering Works since 2005.", "about", history_content)

# 3. LEADERSHIP (leadership.html)
leadership_content = """
    <div class="page-hero">
      <div class="container">
        <nav class="breadcrumbs">
          <a href="/index.html">Home</a> <span>/</span> <a href="/about.html">About Us</a> <span>/</span> <span style="color: #fff;">Leadership</span>
        </nav>
        <span class="kicker">Executive Team</span>
        <h1 class="page-hero-title">CEO & Management Leadership</h1>
        <p class="page-hero-desc">
          Direct engineering leadership and responsive customer communication from the Niazi management team.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="grid-3">
          <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 32px; text-align: center; box-shadow: var(--shadow-sm);">
            <img src="/assets/images/branding/ceo-adeel-ahmed-niazi.png" alt="Adeel Ahmed Niazi" style="width: 200px; height: 220px; object-fit: cover; border-radius: var(--radius-md); margin: 0 auto 20px; border: 2px solid var(--color-border);" />
            <h3 style="font-size: 1.35rem; color: var(--color-primary-dark); margin-bottom: 4px;">Adeel Ahmed Niazi</h3>
            <div style="font-size: 0.875rem; font-weight: 700; color: var(--color-accent); margin-bottom: 16px;">CEO & Founder</div>
            <p style="font-size: 0.875rem; color: var(--color-text-muted); line-height: 1.6; margin-bottom: 20px;">
              Oversees engineering design, technical quality assurance, and international client relationships at Adeel Engineering Works since its foundation in 2005.
            </p>
            <div style="font-size: 0.875rem; font-weight: 600; color: var(--color-primary);">
              Phone / WhatsApp: <a href="https://wa.me/923027012696" target="_blank" style="color: var(--color-accent);">0302-7012696</a>
            </div>
          </div>

          <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 32px; text-align: center; box-shadow: var(--shadow-sm);">
            <div style="width: 200px; height: 220px; background: var(--color-bg-steel); border-radius: var(--radius-md); margin: 0 auto 20px; display: flex; align-items: center; justify-content: center; font-size: 3rem; color: var(--color-primary);">
              ⚙️
            </div>
            <h3 style="font-size: 1.35rem; color: var(--color-primary-dark); margin-bottom: 4px;">Noshad Niazi</h3>
            <div style="font-size: 0.875rem; font-weight: 700; color: var(--color-accent); margin-bottom: 16px;">Technical Operations & Inquiries</div>
            <p style="font-size: 0.875rem; color: var(--color-text-muted); line-height: 1.6; margin-bottom: 20px;">
              Manages factory floor fabrication, machine assembly, client testing runs, and on-site technical deployment.
            </p>
            <div style="font-size: 0.875rem; font-weight: 600; color: var(--color-primary);">
              Direct Line: <a href="tel:+923078870007" style="color: var(--color-accent);">0307-8870007</a>
            </div>
          </div>

          <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 32px; text-align: center; box-shadow: var(--shadow-sm);">
            <div style="width: 200px; height: 220px; background: var(--color-bg-steel); border-radius: var(--radius-md); margin: 0 auto 20px; display: flex; align-items: center; justify-content: center; font-size: 3rem; color: var(--color-primary);">
              🔧
            </div>
            <h3 style="font-size: 1.35rem; color: var(--color-primary-dark); margin-bottom: 4px;">Abdul Manan Niazi</h3>
            <div style="font-size: 0.875rem; font-weight: 700; color: var(--color-accent); margin-bottom: 16px;">Client Support & Logistics</div>
            <p style="font-size: 0.875rem; color: var(--color-text-muted); line-height: 1.6; margin-bottom: 20px;">
              Directs spare parts dispatch, imported accessories coordination, and continuous post-sale customer maintenance.
            </p>
            <div style="font-size: 0.875rem; font-weight: 600; color: var(--color-primary);">
              Direct Line: <a href="tel:+923080450696" style="color: var(--color-accent);">0308-0450696</a>
            </div>
          </div>
        </div>
      </div>
    </section>
"""
create_page("leadership.html", "Leadership & Management", "Meet CEO Adeel Ahmed Niazi and the executive management team at Adeel Engineering Works.", "about", leadership_content)

# 4. MISSION & VISION (mission-vision.html)
mission_content = """
    <div class="page-hero">
      <div class="container">
        <nav class="breadcrumbs">
          <a href="/index.html">Home</a> <span>/</span> <a href="/about.html">About Us</a> <span>/</span> <span style="color: #fff;">Mission & Vision</span>
        </nav>
        <span class="kicker">Strategic Purpose</span>
        <h1 class="page-hero-title">Our Mission, Vision & Core Values</h1>
        <p class="page-hero-desc">
          Empowering global industries with reliable, technologically advanced packaging solutions, ensuring unparalleled product quality and process efficiency.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="gap: 40px;">
          <div style="background: #ffffff; border: 1px solid var(--color-border); border-top: 4px solid var(--color-primary); border-radius: var(--radius-lg); padding: 40px; box-shadow: var(--shadow-sm);">
            <span class="kicker">Corporate Vision</span>
            <h2 style="font-size: 1.75rem; margin-bottom: 16px; color: var(--color-primary-dark);">Our Vision</h2>
            <p style="font-size: 1.0625rem; color: var(--color-text-muted); line-height: 1.7;">
              Established as a premier name in industrial innovation, Adeel Engineering Works is dedicated to the precise design and manufacture of high-performance packing machines and processing systems. Our vision is to empower global industries with reliable, technologically advanced solutions, ensuring unparalleled product quality and process efficiency.
            </p>
          </div>

          <div style="background: #ffffff; border: 1px solid var(--color-border); border-top: 4px solid var(--color-accent); border-radius: var(--radius-lg); padding: 40px; box-shadow: var(--shadow-sm);">
            <span class="kicker">Corporate Mission</span>
            <h2 style="font-size: 1.75rem; margin-bottom: 16px; color: var(--color-primary-dark);">Our Mission</h2>
            <p style="font-size: 1.0625rem; color: var(--color-text-muted); line-height: 1.7;">
              To provide products of high quality and excellent after-sales service to make our machinery trustable and reliable to customers worldwide. We strive to attract customers with high quality products, move customers with considerate service, and benefit customers with favorite factory pricing.
            </p>
          </div>
        </div>

        <div style="margin-top: 60px;">
          <div class="section-header text-center">
            <span class="kicker">Core Principles</span>
            <h2 class="section-title">Values Derived from the Company Catalogue</h2>
          </div>
          <div class="grid-4">
            <div class="feature-card">
              <h3 style="font-size: 1.125rem; margin-bottom: 8px;">Practical & Realistic</h3>
              <p style="font-size: 0.875rem; color: var(--color-text-muted);">Sincere engineering grounded in real production demands and durable workshop craftsmanship.</p>
            </div>
            <div class="feature-card">
              <h3 style="font-size: 1.125rem; margin-bottom: 8px;">Material Superiority</h3>
              <p style="font-size: 0.875rem; color: var(--color-text-muted);">Using high-grade materials like SS-304 and SS-316 for longevity, hygiene, and corrosion resistance.</p>
            </div>
            <div class="feature-card">
              <h3 style="font-size: 1.125rem; margin-bottom: 8px;">Advanced Engineering</h3>
              <p style="font-size: 0.875rem; color: var(--color-text-muted);">Integrating PLC systems, servo drives, and photo-registration sensors for maximum cadence.</p>
            </div>
            <div class="feature-card">
              <h3 style="font-size: 1.125rem; margin-bottom: 8px;">Turnkey Solutions</h3>
              <p style="font-size: 0.875rem; color: var(--color-text-muted);">Providing end-to-end processing and packing lines from raw materials to sealed finished goods.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
"""
create_page("mission-vision.html", "Mission & Vision", "Official corporate mission, vision, and core competencies of Adeel Engineering Works.", "about", mission_content)

# 5. ENGINEERING CAPABILITIES (engineering-capabilities.html)
cap_content = """
    <div class="page-hero">
      <div class="container">
        <nav class="breadcrumbs">
          <a href="/index.html">Home</a> <span>/</span> <a href="/about.html">About Us</a> <span>/</span> <span style="color: #fff;">Engineering Capabilities</span>
        </nav>
        <span class="kicker">Technical Superiority</span>
        <h1 class="page-hero-title">Engineering Capabilities & Standards</h1>
        <p class="page-hero-desc">
          Robust mechanical design, certified SS304/316 fabrication, Delta/Siemens PLC automation, and German component integration.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 48px; margin-bottom: 60px;">
          <div>
            <span class="kicker">Structural Engineering</span>
            <h2 class="section-title">Heavy-Gauge 12mm 304 Stainless Steel Construction</h2>
            <p style="font-size: 1.0625rem; color: var(--color-text-muted); line-height: 1.7; margin-bottom: 20px;">
              While typical commercial packaging machines cut costs with light sheet metal, Adeel Engineering Works uses <strong>12mm 304 steel sheet</strong> for structural frames and SUS304 / SUS316 stainless steel for product-contact areas.
            </p>
            <ul style="display: flex; flex-direction: column; gap: 12px; font-size: 0.9375rem; color: var(--color-text-main);">
              <li><strong>✓ Zero Machine Vibration:</strong> 12mm thick chassis dampens high-speed cycle vibrations, extending component life.</li>
              <li><strong>✓ GMP & Industrial Food Grade:</strong> Resists acidic food products, cooking oils, corrosive shampoos, and chemical detergents.</li>
              <li><strong>✓ 18-Gauge Precision Guides:</strong> Hardened steel forming collars ensure crisp, consistent pouch folds without creasing.</li>
            </ul>
          </div>
          <div style="background: #F8FAFC; border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 32px;">
            <img src="/assets/images/machines/filter-tobacco-pouch-packing-machine.png" alt="Engineering Detail" style="max-height: 380px; margin: 0 auto; object-fit: contain;" />
          </div>
        </div>

        <div class="grid-3">
          <div class="feature-card">
            <h3 class="feature-title">German Component Sourcing</h3>
            <p class="feature-text">We explicitly source critical high-wear parts from Germany, including precision bearings, pneumatic motor valves, and heavy-duty main jacks.</p>
          </div>
          <div class="feature-card">
            <h3 class="feature-title">Dual Inverter & Servo Motion</h3>
            <p class="feature-text">Equipped with 1.5 kW main inverters, 1.5 kW supply inverters, and 0.75 kW (1 HP) servo drives with 1/10 reduction gearing for micrometer accuracy.</p>
          </div>
          <div class="feature-card">
            <h3 class="feature-title">Festo Solenoid Pneumatics</h3>
            <p class="feature-text">Integrated Festo solenoid valve assemblies (24V DC / 220V AC) provide instantaneous valve switching and airtight jaw closure pressure.</p>
          </div>
        </div>
      </div>
    </section>
"""
create_page("engineering-capabilities.html", "Engineering Capabilities", "Detailed technical analysis of Adeel Engineering Works materials, PLCs, German components, and build standards.", "about", cap_content)

# 6. INDUSTRIES (industries.html)
ind_content = """
    <div class="page-hero">
      <div class="container">
        <nav class="breadcrumbs">
          <a href="/index.html">Home</a> <span>/</span> <span style="color: #fff;">Industries</span>
        </nav>
        <span class="kicker">Application Domains</span>
        <h1 class="page-hero-title">Industries We Serve</h1>
        <p class="page-hero-desc">
          Proven packaging solutions engineered for specific product rheology, hygiene compliance, and high-cadence production lines.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="grid-3">
          <div class="feature-card">
            <h3 class="feature-title">Food & Beverage</h3>
            <p class="feature-text">Cooking oil, pasteurized milk, sauces, fruit juices, pasta, biscuits, nimko snacks, and popcorn.</p>
            <div style="margin-top: 16px;"><a href="/products/automatic-liquid-pouch-packing-machine.html" style="color: var(--color-accent); font-weight: 600; font-size: 0.875rem;">View AS1000 Liquid Machine →</a></div>
          </div>
          <div class="feature-card">
            <h3 class="feature-title">Cosmetics & Personal Care</h3>
            <p class="feature-text">Multi-sachet hair colors, shampoo sachets, beauty creams, bleaching creams, hair oils, and lotions.</p>
            <div style="margin-top: 16px;"><a href="/products/2in1-hair-color-pouch-packing-machine.html" style="color: var(--color-accent); font-weight: 600; font-size: 0.875rem;">View Hair Color Machine →</a></div>
          </div>
          <div class="feature-card">
            <h3 class="feature-title">Powder & Spice Processing</h3>
            <p class="feature-text">Milk powder, starch, tea powder, bulk spice blends, rice, and fine culinary seasonings.</p>
            <div style="margin-top: 16px;"><a href="/products/back-cover-powder-screw-packing-machine-1kg.html" style="color: var(--color-accent); font-weight: 600; font-size: 0.875rem;">View Auger Powder Machine →</a></div>
          </div>
          <div class="feature-card">
            <h3 class="feature-title">Detergents & Household</h3>
            <p class="feature-text">Washing powders, dishwashing soap bars, dishwashing foam sponges, laundry bars, and household bleach.</p>
            <div style="margin-top: 16px;"><a href="/products/multi-functional-tray-packing-machine.html" style="color: var(--color-accent); font-weight: 600; font-size: 0.875rem;">View Flow-Wrap Machine →</a></div>
          </div>
          <div class="feature-card">
            <h3 class="feature-title">Tobacco & Oral Nicotine</h3>
            <p class="feature-text">Nicotine pouches, snus/suns pouch, filter khaini, and small dry portion herbal packets.</p>
            <div style="margin-top: 16px;"><a href="/products/filter-tobacco-pouch-packing-machine.html" style="color: var(--color-accent); font-weight: 600; font-size: 0.875rem;">View Filter Tobacco Machine →</a></div>
          </div>
          <div class="feature-card">
            <h3 class="feature-title">Industrial & Disposables</h3>
            <p class="feature-text">Surgical potty, medical trays, plastic powders, hardware components, and chemical formulations.</p>
            <div style="margin-top: 16px;"><a href="/products/back-seal-feeder-automatic-packing-machine.html" style="color: var(--color-accent); font-weight: 600; font-size: 0.875rem;">View Back Seal Feeder →</a></div>
          </div>
        </div>
      </div>
    </section>
"""
create_page("industries.html", "Industries We Serve", "Packaging machinery applications across Food, Cosmetics, Powders, Detergents, and Tobacco sectors.", "industries", ind_content)

# 7. SOLUTIONS (solutions.html)
sol_content = """
    <div class="page-hero">
      <div class="container">
        <nav class="breadcrumbs">
          <a href="/index.html">Home</a> <span>/</span> <span style="color: #fff;">Solutions</span>
        </nav>
        <span class="kicker">Engineered Systems</span>
        <h1 class="page-hero-title">Customized Machinery & Turnkey Solutions</h1>
        <p class="page-hero-desc">
          Bespoke packaging machine designs, irregular sachet tooling, and fully integrated plant processing lines.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 48px; margin-bottom: 60px;">
          <div>
            <span class="kicker">Bespoke Manufacturing</span>
            <h2 class="section-title">Irregular Packaging Machines Built to Specification</h2>
            <p style="font-size: 1.0625rem; color: var(--color-text-muted); line-height: 1.7; margin-bottom: 20px;">
              As explicitly stated in the Adeel Engineering Works catalogue, our factory offers dedicated services on design and produces <strong>irregular packing machines according to special requirements of customers</strong>.
            </p>
            <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.7; margin-bottom: 24px;">
              Whether your product requires a non-standard sachet geometry (such as custom contours, twin perforations, or square pouches), special product heating jackets, or synchronized twin-product metering, our Faisalabad engineering team can design the complete mechanical and electronic tooling.
            </p>
            <a href="/request-quote.html" class="btn btn-primary">Request Custom Machine Consultation</a>
          </div>
          <div style="background: #F8FAFC; border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 36px; text-align: center;">
            <img src="/assets/images/machines/hair-color-pouch-packing-machine.png" alt="Custom Dual Sachet Machine" style="max-height: 400px; margin: 0 auto; object-fit: contain;" />
          </div>
        </div>

        <div class="section-header text-center">
          <span class="kicker">End-to-End Plant Integration</span>
          <h2 class="section-title">Turnkey Processing & Packaging Lines</h2>
        </div>
        <div class="grid-3">
          <div class="feature-card">
            <h3 class="feature-title">1. Bulk Material Handling</h3>
            <p class="feature-text">Automated screw feeders and gentle Z-bucket conveyors continuously lift dry solids, powders, or candies into high hoppers.</p>
          </div>
          <div class="feature-card">
            <h3 class="feature-title">2. Blending & Conditioning</h3>
            <p class="feature-text">Stainless steel ribbon mixers and U-trough blenders create homogeneous batches before feeding packaging lines.</p>
          </div>
          <div class="feature-card">
            <h3 class="feature-title">3. High-Speed Packaging & Coding</h3>
            <p class="feature-text">High-speed VFFS packaging synchronized with ink-roll or thermal inkjet coders for automated lot marking.</p>
          </div>
        </div>
      </div>
    </section>
"""
create_page("solutions.html", "Customized Machinery Solutions", "Bespoke packaging machine engineering, irregular sachet tooling, and complete turnkey processing lines.", "solutions", sol_content)

# 8. CLIENTS (clients.html)
clients_content = """
    <div class="page-hero">
      <div class="container">
        <nav class="breadcrumbs">
          <a href="/index.html">Home</a> <span>/</span> <span style="color: #fff;">Our Clients</span>
        </nav>
        <span class="kicker">Verified Client Portfolio</span>
        <h1 class="page-hero-title">Companies Featured in Our Client Portfolio</h1>
        <p class="page-hero-desc">
          Authentic commercial client brands featured directly on page 18 of the Adeel Engineering Works company catalogue.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="section-header text-center">
          <span class="kicker">Documented Client Showcase</span>
          <h2 class="section-title">21 Industry Brands Across Pakistan</h2>
          <p class="section-subtitle">
            All brand logos shown below are extracted directly from the official Adeel Engineering Works catalogue (Page 18).
          </p>
        </div>

        <div class="client-grid" style="grid-template-columns: repeat(4, 1fr); gap: 24px;">
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-lazzat-bhara.png" alt="Lazzat Bhara" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">Lazzat Bhara</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-sunder-food.png" alt="Sunder Food" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">Sunder Food</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-bin-tariq.png" alt="Bin Tariq" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">Bin Tariq</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-adil-foods.png" alt="Adil Foods" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">Adil Foods</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-zz-food.png" alt="Z&Z Food" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">Z&Z Food</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-karela.png" alt="Karela Washing Powder" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">Karela Washing Powder</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-markhor.png" alt="Markhor" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">Markhor Iodized Salt</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-crescent-cotton.png" alt="Crescent Cotton Industries" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">Crescent Cotton Industries</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-alm.png" alt="ALM" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">ALM</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-chaah-foods.png" alt="Chaah Foods" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">Chaah Foods</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-foods.png" alt="Foods Premium Quality" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">Foods Premium Quality</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-st.png" alt="ST" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">ST</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-waris-khan.png" alt="Waris Khan Tobacco" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">Waris Khan Tobacco</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-shehenshah.png" alt="Shehenshah" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">Shehenshah</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-nice-999.png" alt="999 Nice" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">999 Nice</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-chill.png" alt="Chill Filter Khaini" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">Stay Cool Chill Khaini</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-manzoor-khan.png" alt="Manzoor Khan Tobacco" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">Manzoor Khan Tobacco</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-five-star.png" alt="Five Star Filter Khaini" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">Five Star Filter Khaini</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-555.png" alt="555" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">555</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-ameer-hamza.png" alt="AH Ameer Hamza Soap" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">AH Ameer Hamza Soap</div></div>
          <div class="client-card" style="height: 150px;"><img src="/assets/images/clients/client-imran-adnan.png" alt="Imran Adnan Masala Jat" style="max-height: 80px;" /><div class="client-card-name" style="font-size: 0.8125rem;">Imran Adnan Masala Jat</div></div>
        </div>

        <div style="margin-top: 60px; background: #F8FAFC; border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 36px; text-align: center;">
          <h3 style="font-size: 1.25rem; color: var(--color-primary-dark); margin-bottom: 12px;">Original Catalogue Client Grid</h3>
          <p style="font-size: 0.875rem; color: var(--color-text-muted); max-width: 700px; margin: 0 auto 24px;">
            The original client board as printed on Page 18 of the Adeel Engineering Works official company catalogue.
          </p>
          <img src="/assets/images/clients/clients-showcase-grid.png" alt="Original Client Showcase from Catalogue Page 18" style="max-width: 900px; width: 100%; margin: 0 auto; border-radius: var(--radius-md); box-shadow: var(--shadow-sm); border: 1px solid var(--color-border);" />
        </div>
      </div>
    </section>
"""
create_page("clients.html", "Our Clients", "Authentic commercial client brands featured on Page 18 of the Adeel Engineering Works catalogue.", "clients", clients_content)

# 9. PRODUCT CATALOGUE (products.html)
products_content = """
    <div class="page-hero">
      <div class="container">
        <nav class="breadcrumbs">
          <a href="/index.html">Home</a> <span>/</span> <span style="color: #fff;">Products Catalogue</span>
        </nav>
        <span class="kicker">Complete Machinery Portfolio</span>
        <h1 class="page-hero-title">Industrial Machinery Catalogue</h1>
        <p class="page-hero-desc">
          Search and filter automatic packing machines, precision screw augers, multi-lane liquid systems, and processing equipment.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <!-- TOOLBAR & FILTERS -->
        <div class="catalogue-toolbar">
          <div class="toolbar-top">
            <div class="search-box">
              <svg class="search-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
              <input type="text" id="search-input" placeholder="Search machines (e.g. tobacco, shampoo, powder, liquid, 50g)..." />
            </div>

            <div style="display: flex; align-items: center; gap: 12px;">
              <span id="results-count" style="font-size: 0.875rem; font-weight: 600; color: var(--color-text-muted);">Showing 11 machines</span>
              <select id="sort-select" class="sort-select">
                <option value="default">Default Catalogue Order</option>
                <option value="alpha-asc">Name (A–Z)</option>
                <option value="alpha-desc">Name (Z–A)</option>
              </select>
            </div>
          </div>

          <!-- CATEGORY TABS -->
          <div class="category-tabs">
            <button class="tab-btn active" data-category="all">All Equipment</button>
            <button class="tab-btn" data-category="pouch">Pouch Packaging</button>
            <button class="tab-btn" data-category="liquid">Liquid Packaging</button>
            <button class="tab-btn" data-category="powder">Powder Packaging</button>
            <button class="tab-btn" data-category="flow-wrap---tray">Flow-Wrap & Tray</button>
            <button class="tab-btn" data-category="processing">Processing Equipment</button>
            <button class="tab-btn" data-category="imported">Imported Products</button>
          </div>
        </div>

        <!-- DYNAMIC CATALOGUE GRID -->
        <div id="catalogue-grid" class="grid-3">
          <!-- Populated by assets/js/catalogue.js -->
        </div>
      </div>
    </section>
    <script type="module" src="/assets/js/catalogue.js"></script>
"""
create_page("products.html", "Industrial Product Catalogue", "Explore all 11 core packaging machines, processing equipment, and imported machinery from Adeel Engineering Works.", "products", products_content)

# 10. IMPORTED PRODUCTS (imported-products.html)
imp_content = """
    <div class="page-hero">
      <div class="container">
        <nav class="breadcrumbs">
          <a href="/index.html">Home</a> <span>/</span> <span style="color: #fff;">Imported Products & Processing</span>
        </nav>
        <span class="kicker">Catalogue Pages 15–17</span>
        <h1 class="page-hero-title">Processing Equipment & Imported Machinery</h1>
        <p class="page-hero-desc">
          High-performance material elevators, mixers, dryers, band sealers, induction sealers, and online date coding printers.
        </p>
      </div>
    </div>

    <!-- PROCESSING EQUIPMENT SECTION (PAGE 15) -->
    <section class="section" id="processing">
      <div class="container">
        <div class="section-header">
          <span class="kicker">Catalogue Page 15</span>
          <h2 class="section-title">Processing & Material Handling Equipment</h2>
          <p class="section-subtitle">
            Complementary plant machinery engineered to feed, convey, blend, and condition raw materials for high-cadence packaging.
          </p>
        </div>

        <div class="grid-3">
          <div class="machine-card" id="screw-feeder">
            <div class="machine-card-media"><img src="/assets/images/processing/screw-feeder.png" alt="Screw Feeder" /></div>
            <div class="machine-card-body">
              <h3 class="machine-card-title">Screw Feeder</h3>
              <p class="machine-card-desc">Stainless steel inclined screw auger elevator for automated dust-free powder and granule hopper loading.</p>
              <div class="machine-card-footer mt-4">
                <a href="/request-quote.html?machine=Screw%20Feeder" class="btn btn-primary btn-sm" style="width: 100%;">Inquire About Screw Feeder</a>
              </div>
            </div>
          </div>

          <div class="machine-card" id="z-conveyor">
            <div class="machine-card-media"><img src="/assets/images/processing/z-conveyor.png" alt="Z-Conveyor" /></div>
            <div class="machine-card-body">
              <h3 class="machine-card-title">Z-Conveyor</h3>
              <p class="machine-card-desc">Z-bucket elevator conveyor system engineered for gentle vertical elevation of fragile snacks, candies, and chips.</p>
              <div class="machine-card-footer mt-4">
                <a href="/request-quote.html?machine=Z-Conveyor" class="btn btn-primary btn-sm" style="width: 100%;">Inquire About Z-Conveyor</a>
              </div>
            </div>
          </div>

          <div class="machine-card" id="coating-pan">
            <div class="machine-card-media"><img src="/assets/images/processing/coating-pan.png" alt="Coating Pan" /></div>
            <div class="machine-card-body">
              <h3 class="machine-card-title">Coating Pan</h3>
              <p class="machine-card-desc">Rotary stainless steel spherical coating pan for uniform confectionery seasoning, sugar coating, and tablet polishing.</p>
              <div class="machine-card-footer mt-4">
                <a href="/request-quote.html?machine=Coating%20Pan" class="btn btn-primary btn-sm" style="width: 100%;">Inquire About Coating Pan</a>
              </div>
            </div>
          </div>

          <div class="machine-card" id="u-mixer">
            <div class="machine-card-media"><img src="/assets/images/processing/u-mixer.png" alt="U-Mixer" /></div>
            <div class="machine-card-body">
              <h3 class="machine-card-title">U-Mixer</h3>
              <p class="machine-card-desc">Heavy-duty horizontal U-trough industrial mixer engineered for consistent blending of semi-solids, moist compounds, and doughs.</p>
              <div class="machine-card-footer mt-4">
                <a href="/request-quote.html?machine=U-Mixer" class="btn btn-primary btn-sm" style="width: 100%;">Inquire About U-Mixer</a>
              </div>
            </div>
          </div>

          <div class="machine-card" id="ribbon-mixer">
            <div class="machine-card-media"><img src="/assets/images/processing/ribbon-mixer.png" alt="Ribbon Mixer" /></div>
            <div class="machine-card-body">
              <h3 class="machine-card-title">Ribbon Mixer</h3>
              <p class="machine-card-desc">Precision double-helical ribbon blender delivering fast, homogeneous blending of dry powders, spices, and detergents.</p>
              <div class="machine-card-footer mt-4">
                <a href="/request-quote.html?machine=Ribbon%20Mixer" class="btn btn-primary btn-sm" style="width: 100%;">Inquire About Ribbon Mixer</a>
              </div>
            </div>
          </div>

          <div class="machine-card" id="dryer-machine">
            <div class="machine-card-media"><img src="/assets/images/processing/dryer-machine.png" alt="Dryer Machine" /></div>
            <div class="machine-card-body">
              <h3 class="machine-card-title">Dryer Machine</h3>
              <p class="machine-card-desc">Industrial vertical spin/fluid hot-air drying unit configured for moisture removal, granule conditioning, and post-wash drying.</p>
              <div class="machine-card-footer mt-4">
                <a href="/request-quote.html?machine=Dryer%20Machine" class="btn btn-primary btn-sm" style="width: 100%;">Inquire About Dryer Machine</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- IMPORTED PRODUCTS SECTION (PAGES 16 & 17) -->
    <section class="section section-soft" id="imported">
      <div class="container">
        <div class="section-header">
          <span class="kicker">Catalogue Pages 16 & 17</span>
          <h2 class="section-title">Imported Products & Line Accessories</h2>
          <p class="section-subtitle">
            Reliable imported sealing, printing, coding, tube finishing, and bottle labeling systems supplied by Adeel Engineering Works.
          </p>
        </div>

        <div class="grid-3">
          <div class="machine-card" id="liquid-filling-machine">
            <div class="machine-card-media"><img src="/assets/images/imported-products/liquid-filling-machine.png" alt="Liquid Filling Machine" /></div>
            <div class="machine-card-body">
              <h3 class="machine-card-title">Liquid Filling Machine</h3>
              <p class="machine-card-desc">Pneumatic piston-driven benchtop dosing filler suitable for liquid oils, lotions, syrups, and cosmetic pastes.</p>
              <div class="machine-card-footer mt-4"><a href="/request-quote.html?machine=Liquid%20Filling%20Machine" class="btn btn-secondary btn-sm" style="width: 100%;">Request Technical Details</a></div>
            </div>
          </div>

          <div class="machine-card" id="dk-1100a-ink-roll-coder">
            <div class="machine-card-media"><img src="/assets/images/imported-products/dk-1100a-ink-roll-coder.png" alt="DK-1100A Ink Roll Coder" /></div>
            <div class="machine-card-body">
              <h3 class="machine-card-title">DK-1100A Ink Roll Coder</h3>
              <p class="machine-card-desc">High-speed rotary hot-ink roll contact date and batch number coder designed for bagging machines.</p>
              <div class="machine-card-footer mt-4"><a href="/request-quote.html?machine=DK-1100A%20Ink%20Roll%20Coder" class="btn btn-secondary btn-sm" style="width: 100%;">Request Technical Details</a></div>
            </div>
          </div>

          <div class="machine-card" id="continuous-band-sealer">
            <div class="machine-card-media"><img src="/assets/images/imported-products/continuous-band-sealer.png" alt="Continuous Band Sealer" /></div>
            <div class="machine-card-body">
              <h3 class="machine-card-title">Continuous Band Sealer</h3>
              <p class="machine-card-desc">Motorized continuous band heat sealer with integrated conveyor belt for sealing plastic, foil, and composite bags.</p>
              <div class="machine-card-footer mt-4"><a href="/request-quote.html?machine=Continuous%20Band%20Sealer" class="btn btn-secondary btn-sm" style="width: 100%;">Request Technical Details</a></div>
            </div>
          </div>

          <div class="machine-card" id="thermal-ink-jet-printer">
            <div class="machine-card-media"><img src="/assets/images/imported-products/thermal-ink-jet-printer.png" alt="Thermal Ink-Jet Printer" /></div>
            <div class="machine-card-body">
              <h3 class="machine-card-title">Thermal Ink-Jet Printer</h3>
              <p class="machine-card-desc">High-resolution handheld TIJ printer with intuitive touchscreen for barcodes, QR codes, batch codes, and logos.</p>
              <div class="machine-card-footer mt-4"><a href="/request-quote.html?machine=Thermal%20Ink-Jet%20Printer" class="btn btn-secondary btn-sm" style="width: 100%;">Request Technical Details</a></div>
            </div>
          </div>

          <div class="machine-card" id="continuous-ink-jet-printer">
            <div class="machine-card-media"><img src="/assets/images/imported-products/continuous-ink-jet-printer.png" alt="Continuous Ink-Jet Printer" /></div>
            <div class="machine-card-body">
              <h3 class="machine-card-title">Continuous Ink-Jet Printer</h3>
              <p class="machine-card-desc">Industrial CIJ non-contact production line inkjet printer for high-speed marking on curved bottles and boxes.</p>
              <div class="machine-card-footer mt-4"><a href="/request-quote.html?machine=Continuous%20Ink-Jet%20Printer" class="btn btn-secondary btn-sm" style="width: 100%;">Request Technical Details</a></div>
            </div>
          </div>

          <div class="machine-card" id="automatic-induction-sealer">
            <div class="machine-card-media"><img src="/assets/images/imported-products/automatic-induction-sealer.png" alt="Automatic Induction Sealer" /></div>
            <div class="machine-card-body">
              <h3 class="machine-card-title">Automatic Induction Sealer</h3>
              <p class="machine-card-desc">In-line electromagnetic induction cap sealer for tamper-evident, hermetic foil sealing of bottles and jars.</p>
              <div class="machine-card-footer mt-4"><a href="/request-quote.html?machine=Automatic%20Induction%20Sealer" class="btn btn-secondary btn-sm" style="width: 100%;">Request Technical Details</a></div>
            </div>
          </div>

          <div class="machine-card" id="ultrasonic-tube-sealing">
            <div class="machine-card-media"><img src="/assets/images/imported-products/ultrasonic-tube-sealing.png" alt="Ultrasonic Tube Sealing Machine" /></div>
            <div class="machine-card-body">
              <h3 class="machine-card-title">Ultrasonic Tube Sealing</h3>
              <p class="machine-card-desc">Ultrasonic plastic and laminate tube tail sealer with pneumatic trimming for cosmetic creams and pharmaceutical ointments.</p>
              <div class="machine-card-footer mt-4"><a href="/request-quote.html?machine=Ultrasonic%20Tube%20Sealing" class="btn btn-secondary btn-sm" style="width: 100%;">Request Technical Details</a></div>
            </div>
          </div>

          <div class="machine-card" id="semi-auto-round-bottle-sticker-labeller">
            <div class="machine-card-media"><img src="/assets/images/imported-products/semi-auto-round-bottle-sticker-labeller.png" alt="Round Bottle Sticker Labeller" /></div>
            <div class="machine-card-body">
              <h3 class="machine-card-title">Bottle Sticker Labeller</h3>
              <p class="machine-card-desc">Precision motorized benchtop label applicator for wrinkle-free self-adhesive sticker labeling on cylindrical containers.</p>
              <div class="machine-card-footer mt-4"><a href="/request-quote.html?machine=Round%20Bottle%20Sticker%20Labeller" class="btn btn-secondary btn-sm" style="width: 100%;">Request Technical Details</a></div>
            </div>
          </div>

          <div class="machine-card" id="sleeve-wrapper-shrink-tunnel">
            <div class="machine-card-media"><img src="/assets/images/imported-products/sleeve-wrapper-shrink-tunnel.png" alt="Sleeve Wrapper & Shrink Tunnel" /></div>
            <div class="machine-card-body">
              <h3 class="machine-card-title">Sleeve Wrapper & Shrink Tunnel</h3>
              <p class="machine-card-desc">Heavy-duty automated sleeve wrapping system and circulating thermal shrink tunnel for bundling bottles, cans, and cartons.</p>
              <div class="machine-card-footer mt-4"><a href="/request-quote.html?machine=Sleeve%20Wrapper%20%26%20Shrink%20Tunnel" class="btn btn-secondary btn-sm" style="width: 100%;">Request Technical Details</a></div>
            </div>
          </div>
        </div>
      </div>
    </section>
"""
create_page("imported-products.html", "Imported Products & Processing Equipment", "Processing machines (mixers, conveyors, dryers) and imported sealers, coders, and labelers.", "products", imp_content)

# 11. REQUEST A QUOTATION (request-quote.html)
quote_content = """
    <div class="page-hero">
      <div class="container">
        <nav class="breadcrumbs">
          <a href="/index.html">Home</a> <span>/</span> <span style="color: #fff;">Request a Quotation</span>
        </nav>
        <span class="kicker">Direct Factory Pricing</span>
        <h1 class="page-hero-title">Request a Machine Quotation</h1>
        <p class="page-hero-desc">
          Submit your product specifications, desired packaging speed, and container geometry directly to our engineering team in Faisalabad.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: start; gap: 48px;">
          <!-- Left: Form Card -->
          <div class="form-card">
            <h2 style="font-size: 1.5rem; color: var(--color-primary-dark); margin-bottom: 8px;">Machinery Inquiry Form</h2>
            <p style="font-size: 0.875rem; color: var(--color-text-muted); margin-bottom: 24px;">
              Fields marked with an asterisk (<span style="color: #dc2626;">*</span>) are required. Choose to send via direct WhatsApp Business or official email.
            </p>

            <form id="quotation-form">
              <div class="form-row">
                <div class="form-group">
                  <label class="form-label" for="fullname">Full Name <span class="required">*</span></label>
                  <input type="text" id="fullname" class="form-control" placeholder="e.g. Muhammad Usman" required />
                </div>
                <div class="form-group">
                  <label class="form-label" for="company">Company / Business Name</label>
                  <input type="text" id="company" class="form-control" placeholder="e.g. Usman Foods Industries" />
                </div>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label class="form-label" for="phone">Phone / WhatsApp <span class="required">*</span></label>
                  <input type="tel" id="phone" class="form-control" placeholder="e.g. 0300-1234567 or +92..." required />
                </div>
                <div class="form-group">
                  <label class="form-label" for="email">Email Address <span class="required">*</span></label>
                  <input type="email" id="email" class="form-control" placeholder="e.g. usman@company.com" required />
                </div>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label class="form-label" for="country">City & Country</label>
                  <input type="text" id="country" class="form-control" placeholder="e.g. Faisalabad, Pakistan" />
                </div>
                <div class="form-group">
                  <label class="form-label" for="industry">Industry Sector</label>
                  <select id="industry" class="form-control">
                    <option value="Food & Beverage">Food & Beverage</option>
                    <option value="Cosmetics & Personal Care">Cosmetics & Personal Care</option>
                    <option value="Powders, Spices & Granules">Powders, Spices & Granules</option>
                    <option value="Detergents & Household">Detergents & Household</option>
                    <option value="Tobacco & Nicotine Pouches">Tobacco & Nicotine Pouches</option>
                    <option value="Pharmaceuticals">Pharmaceuticals</option>
                    <option value="Other">Other Application</option>
                  </select>
                </div>
              </div>

              <div class="form-group">
                <label class="form-label" for="machine-select">Interested Machine <span class="required">*</span></label>
                <select id="machine-select" class="form-control" required>
                  <option value="">-- Select an Industrial Machine --</option>
                </select>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label class="form-label" for="material">Product / Material to Pack</label>
                  <input type="text" id="material" class="form-control" placeholder="e.g. Liquid Cooking Oil, 15g Spice Powder..." />
                </div>
                <div class="form-group">
                  <label class="form-label" for="capacity">Required Speed / Capacity</label>
                  <input type="text" id="capacity" class="form-control" placeholder="e.g. 50 packs/min or 2,000 bags/hr" />
                </div>
              </div>

              <div class="form-group">
                <label class="form-label" for="notes">Additional Requirements & Inquiries</label>
                <textarea id="notes" rows="4" class="form-control" placeholder="Please specify pouch dimensions, custom voltage requirements, or delivery schedule preferences..."></textarea>
              </div>

              <div style="display: flex; gap: 14px; flex-wrap: wrap;">
                <button type="submit" data-action="whatsapp" class="btn btn-whatsapp" style="flex: 1;">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.698.077-2.227-.56-1.954-.813-3.21-2.793-3.307-2.923-.098-.129-.789-1.049-.789-2.001 0-.952.499-1.417.676-1.611.177-.193.387-.242.516-.242.128 0 .258 0 .37.006.118.006.276-.045.431.328.156.373.535 1.306.582 1.402.047.097.078.21.015.335-.062.126-.094.205-.188.314-.094.11-.197.246-.282.33-.095.094-.194.197-.083.388.111.192.495.815 1.062 1.32.73.651 1.346.853 1.538.949.192.096.305.08.419-.048.114-.129.49-1.57.621-.77.13.8.261.161.439.096.177-.064 1.134-.535 1.328-.631.194-.097.324-.145.37-.225.048-.08.048-.466-.096-.871z"></path></svg>
                  <span>Submit via WhatsApp</span>
                </button>
                <button type="submit" data-action="email" class="btn btn-primary" style="flex: 1;">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                  <span>Submit via Email</span>
                </button>
              </div>
            </form>
          </div>

          <!-- Right: Guidance & Contacts -->
          <div>
            <div style="background: var(--color-bg-soft); border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 32px; margin-bottom: 24px;">
              <span class="kicker">Direct Consultation</span>
              <h3 style="font-size: 1.25rem; color: var(--color-primary-dark); margin-bottom: 12px;">Contact Management Directly</h3>
              <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.6; margin-bottom: 20px;">
                You can also call or message our executive leadership directly for urgent tenders, factory line assessments, and custom machinery consultations:
              </p>
              <ul style="display: flex; flex-direction: column; gap: 14px; font-size: 0.9375rem;">
                <li>
                  <strong>Adeel Ahmed Niazi (CEO):</strong><br>
                  <a href="tel:+923027012696" style="color: var(--color-accent); font-weight: 600;">0302-7012696</a> (WhatsApp Available)
                </li>
                <li>
                  <strong>Noshad Niazi:</strong><br>
                  <a href="tel:+923078870007" style="color: var(--color-accent); font-weight: 600;">0307-8870007</a>
                </li>
                <li>
                  <strong>Abdul Manan Niazi:</strong><br>
                  <a href="tel:+923080450696" style="color: var(--color-accent); font-weight: 600;">0308-0450696</a>
                </li>
              </ul>
            </div>

            <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 32px;">
              <h4 style="font-size: 1.125rem; color: var(--color-primary-dark); margin-bottom: 12px;">What Happens Next?</h4>
              <ol style="display: flex; flex-direction: column; gap: 12px; font-size: 0.875rem; color: var(--color-text-muted); padding-left: 20px; list-style: decimal;">
                <li>Our engineering team reviews your product viscosity, material film type, and target output.</li>
                <li>We recommend the exact machine variant, required motor ratings, and forming collar dimensions.</li>
                <li>You receive a formal price quotation with factory lead time and payment terms.</li>
                <li>You are invited to our Faisalabad facility to witness live machine test runs with your sample product.</li>
              </ol>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- INQUIRY SUBMISSION MODAL -->
    <div id="inquiry-modal" style="display: none; position: fixed; inset: 0; background: rgba(6, 27, 48, 0.6); backdrop-filter: blur(4px); z-index: 2000; align-items: center; justify-content: center; padding: 20px;">
      <div style="background: #ffffff; max-width: 500px; width: 100%; border-radius: 12px; padding: 32px; box-shadow: var(--shadow-xl); text-align: center;">
        <div style="font-size: 3rem; margin-bottom: 12px;">✅</div>
        <h3 style="font-size: 1.5rem; color: var(--color-primary-dark); margin-bottom: 12px;">Quotation Request Prepared</h3>
        <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.6; margin-bottom: 24px;">
          Your inquiry has been formatted and opened in your chosen application (WhatsApp / Email). Our team at Adeel Engineering Works will respond promptly.
        </p>
        <button data-close-modal class="btn btn-primary" style="width: 100%;">Close Confirmation</button>
      </div>
    </div>

    <script type="module" src="/assets/js/quote.js"></script>
"""
create_page("request-quote.html", "Request a Quotation", "Get official factory pricing and technical specifications for Adeel Engineering Works machines.", "quote", quote_content)

# 12. CONTACT US (contact.html)
contact_content = """
    <div class="page-hero">
      <div class="container">
        <nav class="breadcrumbs">
          <a href="/index.html">Home</a> <span>/</span> <span style="color: #fff;">Contact Us</span>
        </nav>
        <span class="kicker">Headquarters & Factory</span>
        <h1 class="page-hero-title">Contact Adeel Engineering Works</h1>
        <p class="page-hero-desc">
          Get in touch with our team in Faisalabad, Pakistan for machinery inquiries, factory visits, and technical support.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: start; gap: 48px; margin-bottom: 60px;">
          <div>
            <span class="kicker">Get in Touch</span>
            <h2 class="section-title">Direct Manufacturing Office</h2>
            <p style="font-size: 1.0625rem; color: var(--color-text-muted); line-height: 1.7; margin-bottom: 28px;">
              Adeel Engineering Works warmly welcomes all clients from Pakistan and abroad to contact us for partnerships, plant consultations, and machine demonstrations.
            </p>

            <div style="display: flex; flex-direction: column; gap: 24px; margin-bottom: 36px;">
              <div style="display: flex; gap: 16px;">
                <div style="width: 48px; height: 48px; background: var(--color-bg-soft); border: 1px solid var(--color-border); border-radius: var(--radius-md); display: flex; align-items: center; justify-content: center; font-size: 1.25rem; color: var(--color-accent); flex-shrink: 0;">📍</div>
                <div>
                  <h3 style="font-size: 1.125rem; color: var(--color-primary-dark); margin-bottom: 4px;">Factory Location</h3>
                  <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.5;">
                    College Road, near Jawala Nagar Railway Phatak (Crossing), Opposite Laboratory High School in Saminabad, Faisalabad, Punjab, Pakistan.
                  </p>
                </div>
              </div>

              <div style="display: flex; gap: 16px;">
                <div style="width: 48px; height: 48px; background: var(--color-bg-soft); border: 1px solid var(--color-border); border-radius: var(--radius-md); display: flex; align-items: center; justify-content: center; font-size: 1.25rem; color: var(--color-accent); flex-shrink: 0;">📞</div>
                <div>
                  <h3 style="font-size: 1.125rem; color: var(--color-primary-dark); margin-bottom: 4px;">Direct Phone Lines</h3>
                  <div style="font-size: 0.9375rem; color: var(--color-text-main); line-height: 1.6;">
                    <strong>Adeel Ahmed Niazi (CEO):</strong> <a href="tel:+923027012696" style="color: var(--color-accent); font-weight: 600;">0302-7012696</a><br>
                    <strong>Noshad Niazi:</strong> <a href="tel:+923078870007" style="color: var(--color-accent); font-weight: 600;">0307-8870007</a><br>
                    <strong>Abdul Manan Niazi:</strong> <a href="tel:+923080450696" style="color: var(--color-accent); font-weight: 600;">0308-0450696</a>
                  </div>
                </div>
              </div>

              <div style="display: flex; gap: 16px;">
                <div style="width: 48px; height: 48px; background: var(--color-bg-soft); border: 1px solid var(--color-border); border-radius: var(--radius-md); display: flex; align-items: center; justify-content: center; font-size: 1.25rem; color: var(--color-accent); flex-shrink: 0;">✉️</div>
                <div>
                  <h3 style="font-size: 1.125rem; color: var(--color-primary-dark); margin-bottom: 4px;">Email & Web</h3>
                  <div style="font-size: 0.9375rem; color: var(--color-text-main); line-height: 1.6;">
                    Email: <a href="mailto:adeelahmad69638@gmail.com" style="color: var(--color-accent); font-weight: 600;">adeelahmad69638@gmail.com</a><br>
                    Catalogue Domain: <a href="http://www.adeelengineeringpk.com" target="_blank" style="color: var(--color-accent); font-weight: 600;">www.adeelengineeringpk.com</a>
                  </div>
                </div>
              </div>

              <div style="display: flex; gap: 16px;">
                <div style="width: 48px; height: 48px; background: var(--color-bg-soft); border: 1px solid var(--color-border); border-radius: var(--radius-md); display: flex; align-items: center; justify-content: center; font-size: 1.25rem; color: var(--color-accent); flex-shrink: 0;">🌐</div>
                <div>
                  <h3 style="font-size: 1.125rem; color: var(--color-primary-dark); margin-bottom: 4px;">Verified Social Channels</h3>
                  <div style="font-size: 0.875rem; color: var(--color-text-muted); line-height: 1.6;">
                    • <strong>Facebook:</strong> Adeel Engineering Work's<br>
                    • <strong>YouTube:</strong> Adeel Engineering Work's<br>
                    • <strong>Instagram:</strong> adeelengineeringworks<br>
                    • <strong>TikTok:</strong> AdeelEngineering.works
                  </div>
                </div>
              </div>
            </div>

            <a href="https://wa.me/923027012696" target="_blank" class="btn btn-whatsapp btn-lg">
              Open WhatsApp Chat (+92 302 7012696)
            </a>
          </div>

          <!-- Right: Interactive Google Map Embed -->
          <div>
            <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-md);">
              <div style="padding: 16px 20px; background: var(--color-primary-dark); color: #ffffff; font-weight: 700; font-size: 0.9375rem;">
                📍 Saminabad, Faisalabad Facility Map
              </div>
              <iframe 
                title="Adeel Engineering Works Factory Map"
                src="https://maps.google.com/maps?q=Saminabad,+Faisalabad,+Pakistan&t=&z=14&ie=UTF8&iwloc=&output=embed" 
                width="100%" 
                height="450" 
                style="border:0;" 
                allowfullscreen="" 
                loading="lazy">
              </iframe>
              <div style="padding: 16px 20px; font-size: 0.8125rem; color: var(--color-text-muted); background: var(--color-bg-soft);">
                <strong>Landmark:</strong> Near Jawala Nagar Railway Crossing, Opposite Laboratory High School, Saminabad, Faisalabad.
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
"""
create_page("contact.html", "Contact Us", "Physical address, phone numbers, WhatsApp, and Google Map for Adeel Engineering Works in Faisalabad.", "contact", contact_content)

# 13. FAQ (faq.html)
faq_content = """
    <div class="page-hero">
      <div class="container">
        <nav class="breadcrumbs">
          <a href="/index.html">Home</a> <span>/</span> <span style="color: #fff;">FAQs</span>
        </nav>
        <span class="kicker">Technical Clarifications</span>
        <h1 class="page-hero-title">Frequently Asked Questions</h1>
        <p class="page-hero-desc">
          Answers to common technical questions regarding machinery specifications, electrical power, customization, and factory testing.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container" style="max-width: 900px;">
        <div class="accordion">
          <div class="accordion-item active">
            <div class="accordion-header">
              <span>What types of packaging machines does Adeel Engineering Works manufacture?</span>
              <span>+</span>
            </div>
            <div class="accordion-content">
              Adeel Engineering Works specializes in automatic and semi-automatic packing machines for granules, powders, and liquids. Our range includes high-speed tobacco filter pouch packing machines (180–250 pouches/min), 2-in-1 hair color twin-sachet machines, 6-line liquid VFFS shampoo machines, AS1000 series automatic liquid oil and milk pouch machines, horizontal flow-wrappers, central seal pillow pack machines, 3-edge and 4-edge grain packers, and precision servo auger screw powder packers (5g to 1kg).
            </div>
          </div>

          <div class="accordion-item">
            <div class="accordion-header">
              <span>Can Adeel Engineering build customized or irregular packaging machines?</span>
              <span>+</span>
            </div>
            <div class="accordion-content">
              Yes. As documented in our company concept, Adeel Engineering Works offers dedicated services on design inquiry and manufactures irregular packing machines according to special requirements of customers, including custom sachet contours, twin perforations, special volumetric dosing hoppers, and custom voltage configurations.
            </div>
          </div>

          <div class="accordion-item">
            <div class="accordion-header">
              <span>What grade of stainless steel is used in your machine construction?</span>
              <span>+</span>
            </div>
            <div class="accordion-content">
              We construct our machine chassis using heavy-gauge 12mm 304 steel sheet, and all fluid or product-contact components are fabricated from corrosion-resistant SUS304 or SUS316 stainless steel meeting strict industrial hygiene and Good Manufacturing Practice (GMP) sanitary standards.
            </div>
          </div>

          <div class="accordion-item">
            <div class="accordion-header">
              <span>What automation controls and electronics are integrated?</span>
              <span>+</span>
            </div>
            <div class="accordion-content">
              Our automated systems feature imported PLC controllers (Siemens or Delta), 7-inch color HMI touchscreens (Weintek/Wecon), servo drives with 1/10 reduction gearing, dual motor inverters, Festo pneumatic solenoid valve assemblies, and high-sensitivity optical photocell cameras for eye-mark registration.
            </div>
          </div>

          <div class="accordion-item">
            <div class="accordion-header">
              <span>What electrical power supply is required for your machines?</span>
              <span>+</span>
            </div>
            <div class="accordion-content">
              Most standard models (such as the Central Seal, 3-Edge, 4-Edge, and Back Seal Feeder) operate on single-phase 220V power with approximately 3 kW total power consumption. High-speed multi-lane and heavy models are protected by 65A/66A main breakers and internal step-down transformers (48V 50A / 24V DC logic).
            </div>
          </div>

          <div class="accordion-item">
            <div class="accordion-header">
              <span>Can clients visit the factory in Faisalabad to witness live testing?</span>
              <span>+</span>
            </div>
            <div class="accordion-content">
              Yes, we warmly welcome clients from Pakistan and abroad to visit our facility on College Road in Saminabad, Faisalabad. We encourage customers to bring sample packaging films and products for live testing runs before taking delivery.
            </div>
          </div>
        </div>
      </div>
    </section>
"""
create_page("faq.html", "Frequently Asked Questions", "Common technical and operational questions regarding Adeel Engineering Works machinery.", "faq", faq_content)

# 14. PRIVACY POLICY (privacy-policy.html)
privacy_content = """
    <div class="page-hero">
      <div class="container">
        <nav class="breadcrumbs">
          <a href="/index.html">Home</a> <span>/</span> <span style="color: #fff;">Privacy Policy</span>
        </nav>
        <span class="kicker">Legal & Governance</span>
        <h1 class="page-hero-title">Privacy Policy</h1>
        <p class="page-hero-desc">
          How Adeel Engineering Works handles customer quotation inquiries and business communication data.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container" style="max-width: 850px;">
        <h2 style="font-size: 1.5rem; color: var(--color-primary-dark); margin-bottom: 16px;">1. Information Collection</h2>
        <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.7; margin-bottom: 24px;">
          Adeel Engineering Works collects information that you provide directly when requesting machinery quotations, submitting technical inquiries, or contacting our management team via WhatsApp or email. This information may include your name, business name, phone number, email address, and product packaging specifications.
        </p>

        <h2 style="font-size: 1.5rem; color: var(--color-primary-dark); margin-bottom: 16px;">2. Use of Information</h2>
        <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.7; margin-bottom: 24px;">
          The information you provide is utilized solely to prepare engineering quotations, respond to machinery inquiries, coordinate factory demonstration visits, and provide ongoing after-sales technical support. We do not sell or rent commercial contact details to third parties.
        </p>

        <h2 style="font-size: 1.5rem; color: var(--color-primary-dark); margin-bottom: 16px;">3. Direct Communication</h2>
        <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.7; margin-bottom: 24px;">
          Our website implements direct client-side WhatsApp Business and email draft pathways. We do not maintain unencrypted remote contact databases. All inquiries submitted via WhatsApp are transmitted directly to our official company lines (+92 302 7012696).
        </p>

        <h2 style="font-size: 1.5rem; color: var(--color-primary-dark); margin-bottom: 16px;">4. Contact & Inquiries</h2>
        <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.7;">
          If you have questions regarding this privacy policy or your business data, please contact Adeel Engineering Works directly at <strong>adeelahmad69638@gmail.com</strong> or College Road, Saminabad, Faisalabad, Pakistan.
        </p>
      </div>
    </section>
"""
create_page("privacy-policy.html", "Privacy Policy", "Official privacy policy for Adeel Engineering Works corporate website.", "privacy", privacy_content)

# 15. TERMS OF USE (terms.html)
terms_content = """
    <div class="page-hero">
      <div class="container">
        <nav class="breadcrumbs">
          <a href="/index.html">Home</a> <span>/</span> <span style="color: #fff;">Terms of Use</span>
        </nav>
        <span class="kicker">Legal Agreement</span>
        <h1 class="page-hero-title">Terms of Use</h1>
        <p class="page-hero-desc">
          Terms governing the use of the Adeel Engineering Works website and catalogue specifications.
        </p>
      </div>
    </div>

    <section class="section">
      <div class="container" style="max-width: 850px;">
        <h2 style="font-size: 1.5rem; color: var(--color-primary-dark); margin-bottom: 16px;">1. Catalogue Specifications & Quotations</h2>
        <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.7; margin-bottom: 24px;">
          All technical specifications, production speeds (pouches per minute), and electrical ratings presented on this website are sourced from the official Adeel Engineering Works catalogue. Operational speeds may vary based on product density, film thickness, operator skill, and packaging geometry. Official binding quotations and delivery schedules are provided upon written confirmation by company management.
        </p>

        <h2 style="font-size: 1.5rem; color: var(--color-primary-dark); margin-bottom: 16px;">2. Intellectual Property & Client Trademarks</h2>
        <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.7; margin-bottom: 24px;">
          The Adeel Engineering name, logo, machinery photographs, and catalogue documentation are the property of Adeel Engineering Works. Third-party client logos displayed in our client showcase remain the trademarks of their respective company owners and are presented solely as documented in our commercial catalogue portfolio.
        </p>

        <h2 style="font-size: 1.5rem; color: var(--color-primary-dark); margin-bottom: 16px;">3. Governing Law</h2>
        <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.7;">
          These terms and commercial agreements with Adeel Engineering Works are governed by and construed in accordance with the laws of the Islamic Republic of Pakistan, with jurisdiction in Faisalabad.
        </p>
      </div>
    </section>
"""
create_page("terms.html", "Terms of Use", "Terms of service and catalogue usage conditions for Adeel Engineering Works.", "terms", terms_content)

# 16. 404 PAGE (404.html)
notFound_content = """
    <div class="page-hero">
      <div class="container text-center">
        <span class="kicker">Error 404</span>
        <h1 class="page-hero-title">Page Not Found</h1>
        <p class="page-hero-desc" style="margin: 0 auto;">
          The industrial machinery page or resource you requested cannot be located.
        </p>
      </div>
    </div>

    <section class="section text-center">
      <div class="container" style="max-width: 600px;">
        <div style="font-size: 4rem; color: var(--color-accent); font-weight: 800; line-height: 1; margin-bottom: 20px;">404</div>
        <h2 style="font-size: 1.5rem; color: var(--color-primary-dark); margin-bottom: 16px;">Looking for Packaging Machinery?</h2>
        <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.6; margin-bottom: 32px;">
          Please use the links below to return to our verified catalogue of packing and processing machinery or contact our engineering team directly.
        </p>
        <div style="display: flex; gap: 14px; justify-content: center; flex-wrap: wrap;">
          <a href="/index.html" class="btn btn-secondary">Return to Homepage</a>
          <a href="/products.html" class="btn btn-primary">Browse Machine Catalogue</a>
          <a href="/contact.html" class="btn btn-outline" style="border: 1px solid var(--color-border);">Contact Us</a>
        </div>
      </div>
    </section>
"""
create_page("404.html", "404 Page Not Found", "Page not found - Adeel Engineering Works.", "404", notFound_content)

print("All corporate pages successfully generated!")
