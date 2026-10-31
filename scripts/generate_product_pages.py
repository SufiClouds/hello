import json
import os

# Authoritative product specifications from Adeel Engineering Works Catalogue
MACHINES = [
  {
    "id": "filter-tobacco-pouch-packing-machine",
    "slug": "filter-tobacco-pouch-packing-machine",
    "name": "Filter Tobacco Pouch Packing Machine",
    "category": "Pouch Packaging",
    "page": 4,
    "image": "/assets/images/machines/filter-tobacco-pouch-packing-machine.png",
    "overview": "High-speed precision automated pouch packaging machine engineered specifically for products like nicotine pouches, snus/suns pouch, or similar small portioned items.",
    "speed": "180 to 250 pouches per minute",
    "powerSupply": "220V Single Phase / 24V DC logic",
    "totalPower": "1.5 kW Main Motor Inverter + 1.5 kW Supply Motor Inverter",
    "specs": [
      ("Production Speed", "180 to 250 pouches per minute"),
      ("Automation & Control", "PLC & HMI Control (Siemens or comparable high-quality brand / Delta PLC 220V)"),
      ("Drive System", "Servo Motor (0.75 kW / 1 HP) with 1/10 ratio gear and dual inverter motors"),
      ("Main Motor Inverter", "1.5 kW Main Motor Inverter"),
      ("Supply Motor Inverter", "1.5 kW Supply Motor Inverter"),
      ("Conveyor Motor", "90V Conveyor Motor"),
      ("HMI Interface", "Weintek / Wecon 7-inch Touch Screen"),
      ("PLC System", "Delta PLC 220V with PLC communication cable"),
      ("Pneumatic Valves", "Festo Solenoid Valve Assembly (24V DC / 220V AC)"),
      ("Heating Transformer", "48 Volt 50 Amps Transformer for sealing heaters"),
      ("Electrical Protection", "Protected by a 65A/66A Main Breaker"),
      ("Body Construction", "12mm (304) Stainless Steel Sheet"),
      ("German Components", "Critical parts: Bearings, motor valves, and main jacks sourced from Germany"),
      ("Temperature Management", "Comprehensive multi-zone digital temperature control system for consistent sealing")
    ],
    "features": [
      "High-speed production capacity reaching 180 to 250 finished pouches per minute",
      "Precision servo motor & drive ensures accurate registration and uniform bag dimensions",
      "Rigid 12mm 304 stainless steel sheet body structure resists operational vibration",
      "German-engineered bearings, valves, and heavy-duty main jacks guarantee extended operational life",
      "Festo solenoid valve assembly provides rapid pneumatic response and tight seal actuation",
      "Digital temperature control system ensures airtight seams across continuous high-volume shifts"
    ],
    "applications": [
      "Nicotine pouches",
      "Snus / suns pouch",
      "Small portion herbal sachets",
      "Dry fine tobacco and aromatic blends"
    ],
    "materials": "Heat-sealable non-woven filter paper, porous composite fleece, barrier pouch films"
  },
  {
    "id": "2in1-hair-color-pouch-packing-machine",
    "slug": "2in1-hair-color-pouch-packing-machine",
    "name": "2-in-1 Hair Color Pouch Packing Machine",
    "category": "Liquid Packaging",
    "page": 5,
    "image": "/assets/images/machines/hair-color-pouch-packing-machine.png",
    "overview": "Multi-Pouch High-Speed automated packaging machine designed specifically for synchronized packing of twin hair color and developer sachets across cosmetic, pharmaceutical, and health industries.",
    "speed": "High-speed synchronized dual-pouch output",
    "powerSupply": "220V Industrial",
    "totalPower": "High-torque German-engineered motor with customizable options",
    "specs": [
      ("Machine Category", "Multi-Pouch High-Speed Packing Machine (Dual Functionality)"),
      ("Sachet Format", "Dual multi-sachet hair color / twin connected sachets"),
      ("Synchronization", "PLC control for real-time synchronization between dosing lanes"),
      ("Forming Guides", "Steel forming guides precision-machined from 18-gauge steel for precise bag forming"),
      ("Material Quality", "Entire machine body constructed from corrosion-resistant SUS304 / SUS316 stainless steel"),
      ("Standards Compliance", "Meets industrial and Good Manufacturing Practice (GMP) standards"),
      ("Power & Monitoring", "High-torque, German-engineered motor with customizable options"),
      ("Electrical Components", "Critical electrical parts sourced from Germany for maximum reliability"),
      ("Safety Systems", "Comprehensive internal temperature monitoring with automatic cutoff & large emergency stop button"),
      ("Customization", "Offers custom modifications and variable sachet shapes (e.g. square, contour, special shapes) upon request")
    ],
    "features": [
      "Dual functionality capable of simultaneously metering and sealing colorant and developer lotions",
      "Entire machine body fabricated from SUS304 / SUS316 stainless steel for chemical resistance",
      "18-gauge steel forming guides maintain crisp, wrinkle-free edge definition",
      "Automatic thermal cutoff and prominent emergency stop button ensure full operator safety",
      "Custom tooling available for twin perforations, custom contours, and square formats"
    ],
    "applications": [
      "Hair color creams and developer emulsions",
      "Cosmetic bleaching kits and hair masks",
      "Twin pharmaceutical creams and antibacterial ointments",
      "Personal care shampoo and conditioner duos"
    ],
    "materials": "Multi-layer barrier laminate films, aluminium foil composites, PET/PE"
  },
  {
    "id": "multi-functional-tray-packing-machine",
    "slug": "multi-functional-tray-packing-machine",
    "name": "Multi-Functional & Tray Packing Machine",
    "category": "Flow Wrap & Tray",
    "page": 6,
    "image": "/assets/images/machines/multi-functional-tray-packing-machine.png",
    "overview": "Continuous horizontal flow-wrapper and tray packing machine designed for packaging bakery treats, soaps, personal care bars, and industrial products with precision photocell tracking.",
    "speed": "Continuous variable flow-wrap packaging rate",
    "powerSupply": "220V / 200V reverse-forward drive",
    "totalPower": "2.5 kVA Inverter with 1 HP tractor motor",
    "specs": [
      ("Machine Type", "Horizontal Pillow Pack / Tray Packing Machine (Pilorip flow-wrap style)"),
      ("Optical Tracking", "High-precision photocell camera in elastic parts for perfect cutting design"),
      ("Drive Inverter", "2.5 kVA, 220 Voltage inverter system"),
      ("Tractor Motor", "1 HP heavy-duty tractor motor"),
      ("Feed Motor", "200V Reverse / Forward motor for flexible film movement"),
      ("Speed Adjustment", "Speed control volume dial with convenient push-button inching"),
      ("Instrumentation", "Integrated RPM meter, digital temperature controller, and power meter"),
      ("Body Construction", "Easy-to-clean sanitary stainless steel contact surfaces")
    ],
    "features": [
      "Optical photocell camera alignment tracks eye-marks for exact cut placement",
      "Push-button inching allows quick, safe setup and effortless film threading",
      "Dual forward-reverse motorized drive simplifies clearing jams and film roll changes",
      "Accommodates a vast range of solid products from frozen kulfi to dishwashing soap bars",
      "Integrated meters monitor line RPM, operational voltage, and sealing temperatures"
    ],
    "applications": [
      "Kulfi and ice-cream sticks",
      "Cupcakes, cookies, and bakery biscuits",
      "Dishwashing soap bars and laundry soaps",
      "Dishwashing foam sponges and scouring pads",
      "Surgical potty, medical trays, and sterile pads",
      "Bleach cream pots and cosmetic plastic powders"
    ],
    "materials": "Heat-sealable BOPP, composite laminate films, pearlized films"
  },
  {
    "id": "6-line-shampoo-packing-machine",
    "slug": "6-line-shampoo-packing-machine",
    "name": "6-Line Shampoo Packing Machine",
    "category": "Multi-Lane & Sachet",
    "page": 7,
    "image": "/assets/images/machines/6-line-shampoo-packing-machine.png",
    "overview": "Heavy-duty 6-lane multi-line Vertical Form Fill Seal (VFFS) liquid packing machine engineered for high-cadence commercial packaging of shampoo and liquid sachets.",
    "speed": "6 Synchronized parallel lines (High-capacity commercial output)",
    "powerSupply": "220V / 65 Ampere Main Breaker",
    "totalPower": "0.5 HP Induction Motor + 90V DC / Servo Film Pulling Drive",
    "specs": [
      ("Machine Architecture", "6-Lane / Line Vertical Form Fill Seal (VFFS) Liquid Packing Machine"),
      ("Packing Seal Types", "Pillow Pouch / 3-Side Seal / 4-Side Seal (Shampoo Sachets)"),
      ("Main Motor", "0.5 HP Induction Motor to drive main machine and liquid piston pump"),
      ("Film Pulling Motor", "90V DC Motor or Servo Motor to control paper movement and cutting length"),
      ("PLC Controller", "Amoman Delta or Siemens brand Programmable Logic Controller"),
      ("Operator Interface", "HMI Touch Screen Panel to configure packing speed, pouch size, and temperature"),
      ("Print Registration", "High sensitivity photoelectric sensor (Photocell camera eye)"),
      ("Temperature Controller", "Solid State Relay (SSR) heating sealing jaw controller"),
      ("Electrical Breaker", "65 Ampere heavy-duty load protection breaker"),
      ("Safety Controls", "On / Off push button and large emergency stop button"),
      ("Chassis & Body Material", "Stainless Steel (SS304 or SS316) for hygiene and rust resistance"),
      ("Component Standard", "Standard industrial electrical parts (PLC, HMI, PhotoCell, Motors)")
    ],
    "features": [
      "Six independent lanes run in parallel to multiply factory throughput sixfold",
      "Multi-piston liquid dosing unit ensures precise fill volume across every individual sachet",
      "HMI touch screen provides real-time monitoring and swift pouch length adjustments",
      "Photoelectric sensor guarantees straight, synchronized cuts on pre-printed film rolls",
      "Full SS304/SS316 stainless contact parts withstand surfactants, fragrances, and chemicals"
    ],
    "applications": [
      "Hair shampoo sachets",
      "Hair conditioner sachets",
      "Body lotions and moisturizing creams",
      "Liquid hand soap and antibacterial gels",
      "Cosmetic face serums and oils"
    ],
    "materials": "Multi-layer barrier laminate films, PET/AL/PE, PET/PE"
  },
  {
    "id": "automatic-liquid-pouch-packing-machine",
    "slug": "automatic-liquid-pouch-packing-machine",
    "name": "Automatic Liquid Pouch Packing Machine",
    "category": "Liquid Packaging",
    "page": 8,
    "image": "/assets/images/machines/automatic-liquid-pouch-packing-machine.png",
    "overview": "Vertical liquid pouch packaging machine for 500 gram to 1 kg cooking oil and milk pouches, automating ultraviolet sterilization, bag-forming, filling, and sealing.",
    "speed": "1,500 to 2,000 bags per hour",
    "powerSupply": "220V / 65 kVA Main Breaker",
    "totalPower": "1 HP Main Motor (1.5 kVA Inverter) + 90V Paper Motor (0.75 kVA Inverter)",
    "specs": [
      ("Model Series", "AS1000 Series Industrial Liquid Pouch System"),
      ("Packaging Range", "500 Gram to 1 kg (Cooking Oil, Milk, Beverages)"),
      ("Production Speed", "1,500 to 2,000 bags per hour for standard beverages"),
      ("Automated Process Cycle", "Ultraviolet (UV) sterilization, bag-forming, date printing, dosing, filling, sealing, cutting"),
      ("Main Motor System", "1 HP Main Motor with 1.5 kVA Inverter"),
      ("Film Feed Motor", "90V Paper Motor with 0.75 kVA Inverter"),
      ("Registration Sensor", "Photocell camera for optical eye-mark tracking"),
      ("Electrical Protection", "65 kVA Main Breaker"),
      ("Dimensions", "Approximately 850 x 1100 x 1850 mm"),
      ("Machine Weight", "Approximately 320 kg"),
      ("Hygiene Construction", "Stainless steel fluid path meeting food and beverage sanitation standards")
    ],
    "features": [
      "Comprehensive 7-in-1 cycle: UV sterilization, forming, date coding, dosing, sealing, and cutting",
      "High hourly output reaching up to 2,000 bags per hour for liquid milk and edible oil",
      "Integrated date coder prints lot numbers and expiration dates during the sealing stroke",
      "Dual variable-frequency inverters ensure smooth bag feeding and synchronized filling",
      "Built with sanitary food-grade stainless steel fluid path and durable chassis"
    ],
    "applications": [
      "Cooking oil and vegetable ghee",
      "Pasteurized fresh milk and dairy liquids",
      "Fruit juices and non-carbonated drinks",
      "Sauces, vinegar, and syrups",
      "Agricultural liquid fertilizers"
    ],
    "materials": "Co-extruded LDPE film, specialized milk/oil barrier pouch rolls"
  },
  {
    "id": "central-seal-packing-machine",
    "slug": "central-seal-packing-machine",
    "name": "Central Seal Packing Machine",
    "category": "Pouch Packaging",
    "page": 9,
    "image": "/assets/images/machines/central-seal-packing-machine.png",
    "overview": "Pillow-shape vertical form-fill-seal packaging machine configured for crispy snacks, nimko products, bulk candies, tea, and dry fruits with optical fault interlock.",
    "speed": "36 pouches per minute",
    "powerSupply": "220 V",
    "totalPower": "3 kW",
    "specs": [
      ("Packaging Speed", "36 Pouches per minute"),
      ("Bag Shape Profile", "Pillow Shape (Center back seam seal)"),
      ("Packaging Material", "Any heat-sealable composite film"),
      ("Electrical Supply", "220 V Single Phase"),
      ("Total Power Energy", "3 kW"),
      ("Process Operations", "Bag, measure, filling, count, print date, lot number, cutting, product output (one complete cycle)"),
      ("Coder Option", "Print date & lot number (optional reprovision coder)"),
      ("Cutting Device", "Optional automatic cutting device with transfer bag chute"),
      ("Optical Interlock", "Set optical fault: Tray No material / No Wrapper Auto-shutdown to avoid waste bags"),
      ("Speed Readout", "Automatically displays real-time packaging speed")
    ],
    "features": [
      "Optical sensor automatically stops machine if material hopper or film roll is depleted",
      "Classic pillow back-seal design provides robust package integrity and tamper resistance",
      "Complete automated cycle from volumetric measurement to discharge chute output",
      "Low power consumption (3 kW) running reliably on standard 220V electrical supply",
      "Easy-clean stainless steel hopper and product contact chutes"
    ],
    "applications": [
      "Nimko products and kurkure snacks",
      "Pastas, macaroni, and crackers",
      "Bulk candies and toffees",
      "Popcorn and puffed snacks",
      "Loose tea and herbal tea",
      "Detergent powders and dry fruits",
      "Spices and seeds"
    ],
    "materials": "Any heat-sealable film, BOPP/CPP, metalized PET, laminated paper"
  },
  {
    "id": "four-edge-sealing-grain-packaging-machine",
    "slug": "four-edge-sealing-grain-packaging-machine",
    "name": "Four Edge Sealing Grain Packaging Machine",
    "category": "Pouch Packaging",
    "page": 10,
    "image": "/assets/images/machines/four-edge-sealing-grain-packing-machine.png",
    "overview": "Precision 4-side perimeter seal form-fill-seal machine equipped with 5-recipe parameter memory and independent dual-axis temperature controls for creams, oils, and sauces.",
    "speed": "40 to 50 pouches per minute",
    "powerSupply": "220 V",
    "totalPower": "3 kW",
    "specs": [
      ("Packaging Speed", "40 to 50 Pouches per minute"),
      ("Bag Shapes", "Sheet Shape / 4-Edge Perimeter Flat Seal"),
      ("Seal Width", "Up and down seal width can be customized according to client requirements"),
      ("Packaging Material", "Any heat-sealable film, composite film, or single layer film"),
      ("Power Supply", "220 V"),
      ("Total Power Energy", "3 kW"),
      ("Complete Process", "Pouch, measure, filling, count, printing date & batch number, cutting, product output (one complete cycle)"),
      ("Formula Parameter Memory", "Can store 5 groups formula parameters; product changeovers are more accurate and fast"),
      ("Thermal Control", "Transverse and longitudinal sealing temperature controlled independently for multi-layer films")
    ],
    "features": [
      "Independent cross and longitudinal temperature controls ensure flawless seals on delicate films",
      "Five-group formula memory allows rapid product switching without manual recalibration",
      "Produces flat 4-edge sealed sachets preferred for premium retail samples and condiments",
      "Reliable 40 to 50 pouches per minute output with synchronized batch code imprinting",
      "Sanitary stainless steel contact parts suitable for acidic foods and viscous cosmetic gels"
    ],
    "applications": [
      "Beauty creams and whitening lotions",
      "Hair remover creams",
      "Hair oils and scented hair treatments",
      "Tomato ketchup and chili garlic sauce",
      "Mayonnaise and food pastes"
    ],
    "materials": "Composite films, single-layer films, multi-ply barrier laminates"
  },
  {
    "id": "three-edge-sealing-grain-packaging-machine",
    "slug": "three-edge-sealing-grain-packaging-machine",
    "name": "Three Edge Sealing Grain Packaging Machine",
    "category": "Pouch Packaging",
    "page": 11,
    "image": "/assets/images/machines/three-edge-sealing-grain-packing-machine.png",
    "overview": "High-accuracy 3-side seal form-fill-seal packaging machine tailored for 15g to 20g portion sachets of powders, foaming materials, and spices with recipe storage.",
    "speed": "40 to 50 pouches per minute",
    "powerSupply": "220 V",
    "totalPower": "3 kW",
    "specs": [
      ("Packaging Speed", "40 to 50 Pouches per minute"),
      ("Target Measuring Range", "15 to 20 Gram pouch packaging"),
      ("Bag Geometry", "3-Edge Sealing Pouch (Form of the back cover)"),
      ("Seal Width", "Up and down seal width can be customized according to need"),
      ("Packaging Material", "Any heat-sealable film, composite film, or single layer film"),
      ("Power Supply", "220 V"),
      ("Total Power Energy", "3 kW"),
      ("Process Automation", "Pouch, measure, filling, count, printing date and batch number, cutting, product output (one complete cycle)"),
      ("Formula Parameter Memory", "Stores 5 groups of formula parameters for rapid, accurate variety changes"),
      ("Thermal Control", "Transverse and longitudinal sealing temperature controlled independently")
    ],
    "features": [
      "Targeted dosing precision for 15g to 20g small portion spice sachets and foaming powders",
      "Internal 5-group memory bank stores complete sealing and feeding parameters",
      "Separate transverse and vertical heat controllers accommodate composite or single-layer films",
      "High-cadence 40 to 50 pouches per minute cycle with automated batch dating",
      "Compact structural footprint fits easily into modular factory lines"
    ],
    "applications": [
      "All powder materials & spice powders (15/20g)",
      "Liquid foam materials and foaming agents",
      "Single-serve seasoning packets",
      "Herbal powders and instant drink powders"
    ],
    "materials": "Heat-sealable composite films, single-layer films, barrier foils"
  },
  {
    "id": "back-seal-feeder-automatic-packing-machine",
    "slug": "back-seal-feeder-automatic-packing-machine",
    "name": "Back Seal Feeder Automatic Packing Machine",
    "category": "Powder Packaging",
    "page": 12,
    "image": "/assets/images/machines/back-seal-feeder-packing-machine.png",
    "overview": "Heavy-duty back-seal vertical packaging machine with integrated hopper feeder engineered for bulk packaging up to 1kg to 2kg of rice, candies, spices, and washing powders.",
    "speed": "20 to 30 bags per minute",
    "powerSupply": "220V",
    "totalPower": "3 kW",
    "specs": [
      ("Production Speed", "20 to 30 bags per minute"),
      ("Maximum Package Weight", "1 kg to 2 kg capacity"),
      ("Bag Formation", "Back Seal (Pillow-shaped bulk bag)"),
      ("Packaging Material", "Any heat-sealable material"),
      ("Power Supply", "220V"),
      ("Total Power Energy", "3 kW"),
      ("Full Cycle Operations", "Bag, measure, filling, count, print date, lot number, cutting, product output (one complete cycle)"),
      ("Speed Indicator", "Automatically displays real-time packaging speed"),
      ("Cutting System", "Optional automatic cutting device with transfer bag chute"),
      ("Waste Prevention Interlock", "Set optical fault: Tray No material / No Wrapper Auto-shutdown to avoid waste bags")
    ],
    "features": [
      "Large weight capacity designed specifically for heavy 1 kg to 2 kg retail and wholesale packs",
      "Integrated feeder chute ensures consistent flow of dense granules and free-flowing powders",
      "Optical anti-waste shutdown automatically halts the cycle if wrapper or material runs dry",
      "Sturdy back-seal pillow geometry withstands drop impacts and bulk storage handling",
      "Operates efficiently on single-phase 220V 3 kW power"
    ],
    "applications": [
      "Food: Snacks, bulk candies, rice, tea, popcorn, and dry fruits",
      "Spices & Powders: Various ground spices, milk powder, washing powder",
      "General: Suited for most free-flowing granules and fine industrial powders"
    ],
    "materials": "Heavy-gauge heat-sealable composite films, laminated plastics"
  },
  {
    "id": "back-cover-powder-screw-packing-machine-50g",
    "slug": "back-cover-powder-screw-packing-machine-50g",
    "name": "Back Cover Powder Screw Automatic Packing Machine (5g to 50g)",
    "category": "Powder Packaging",
    "page": 13,
    "image": "/assets/images/machines/back-cover-powder-screw-packing-machine-50g.png",
    "overview": "High-speed servo auger screw vertical packaging machine designed for dosing and packaging 5g to 50g fine powders with multilingual PLC touchscreen interface.",
    "speed": "30 to 90 bags per minute",
    "powerSupply": "220V",
    "totalPower": "Integrated auger screw drive with smart PLC",
    "specs": [
      ("Measuring Range", "5 gram to 50 gram"),
      ("Packing Speed", "30 to 90 bags per minute"),
      ("Compatible Materials", "Composite films like OPP/CPP, PET/PE, and MST/PE"),
      ("Automation Level", "Full Automation: Handles measuring, filling, counting, and printing in one cycle"),
      ("Smart Controls", "Uses an imported PLC system for stable, non-stop parameter adjustments"),
      ("Multilingual Interface", "Touch screen supports Chinese, English, Russian, and Spanish"),
      ("Precision Engineering", "Independent temperature controls for horizontal and vertical sealing"),
      ("Formula Memory", "Can store five different product settings for fast changeovers"),
      ("Visual Summary", "Includes precision screw feeder, sealing jaws, and industrial control panel")
    ],
    "features": [
      "High-precision auger screw dosing eliminates dusting and guarantees exact weight accuracy",
      "Remarkable operational speed reaching up to 90 bags per minute for high-demand lines",
      "Multilingual touch screen supports Chinese, English, Russian, and Spanish for global operations",
      "Non-stop parameter tuning allows operators to adjust speeds and weights during live runs",
      "5-product formula memory minimizes changeover downtime between powder varieties"
    ],
    "applications": [
      "Milk powder and infant formula sachets",
      "Corn starch, tapioca, and baking powders",
      "Tea powder, instant coffee, and matcha",
      "Fine pharmaceutical and chemical powders"
    ],
    "materials": "Composite films like OPP/CPP, PET/PE, MST/PE, and barrier foil pouches"
  },
  {
    "id": "back-cover-powder-screw-packing-machine-1kg",
    "slug": "back-cover-powder-screw-packing-machine-1kg",
    "name": "Back Cover Powder Screw Automatic Packing Machine (50g to 1kg)",
    "category": "Powder Packaging",
    "page": 14,
    "image": "/assets/images/machines/back-cover-powder-screw-packing-machine-1kg.png",
    "overview": "Large-capacity servo auger screw vertical powder packaging system engineered for high-speed, versatile production of 50g up to 1kg powder bags.",
    "speed": "30 to 90 bags per minute",
    "powerSupply": "220V",
    "totalPower": "Heavy-duty auger drive with imported PLC control",
    "specs": [
      ("Measuring Range", "50 gram to 1 kg"),
      ("Packing Speed", "30 to 90 bags per minute"),
      ("Compatible Materials", "Composite films like OPP/CPP, PET/PE, and MST/PE"),
      ("Full Automation", "Handles measuring, filling, counting, and printing in one cycle"),
      ("Smart Controls", "Imported PLC system for stable, non-stop parameter adjustments"),
      ("Multilingual Touchscreen", "Supports Chinese, English, Russian, and Spanish"),
      ("Precision Engineering", "Independent temperature controls for horizontal and vertical sealing"),
      ("Formula Memory", "Stores five different product settings for fast changeovers"),
      ("Application Environment", "Intended for industrial food or chemical packaging environments")
    ],
    "features": [
      "Broad 50g to 1000g dosing capability handles medium retail to bulk 1kg powder packages",
      "Heavy-duty stainless steel auger flighting feeds non-free-flowing powders consistently",
      "Touchscreen with English, Chinese, Russian, and Spanish language options",
      "Dual independent thermal PID loops create leak-proof horizontal and vertical seams",
      "Stores 5 separate product recipes for instantaneous factory changeovers"
    ],
    "applications": [
      "Retail milk powder pouches",
      "Industrial starches, flour, and baking ingredients",
      "Tea powder, cocoa, and beverage blends",
      "Fine ground spices and seasoning mixes",
      "Chemical, detergent, and agrochemical powders"
    ],
    "materials": "Composite barrier films (OPP/CPP, PET/PE, MST/PE), laminated pouches"
  }
]

def render_header(active_nav="products"):
  return """
    <!-- TOP INFO BAR -->
    <div class="topbar">
      <div class="container topbar-content">
        <div class="topbar-left">
          <div class="topbar-item">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
            <span>College Road, near Jawala Nagar Railway Phatak, Saminabad, Faisalabad</span>
          </div>
          <span class="topbar-divider">|</span>
          <div class="topbar-item">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
            <a href="mailto:adeelahmad69638@gmail.com">adeelahmad69638@gmail.com</a>
          </div>
        </div>
        <div class="topbar-right">
          <div class="topbar-item">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            <a href="tel:+923027012696">0302-7012696</a>
          </div>
          <span class="topbar-divider">|</span>
          <div class="topbar-item">
            <span>WhatsApp:</span>
            <a href="https://wa.me/923027012696" target="_blank" style="color: #4ade80; font-weight: 600;">+92 302 7012696</a>
          </div>
        </div>
      </div>
    </div>

    <!-- MAIN HEADER -->
    <header class="header">
      <div class="container nav-container">
        <a href="/index.html" class="brand">
          <img src="/assets/images/branding/logo-badge.png" alt="Adeel Engineering Works" class="brand-logo-img" />
          <div class="brand-text">
            <span class="brand-title">ADEEL ENGINEERING</span>
            <span class="brand-subtitle">PACKING & PROCESSING MACHINES</span>
          </div>
        </a>

        <nav class="nav-menu">
          <div class="nav-item">
            <a href="/index.html" class="nav-link">Home</a>
          </div>

          <div class="nav-item">
            <a href="/about.html" class="nav-link">
              About Us
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </a>
            <div class="dropdown-menu">
              <a href="/about.html" class="dropdown-link">Company Overview</a>
              <a href="/history.html" class="dropdown-link">Our History (Since 2005)</a>
              <a href="/leadership.html" class="dropdown-link">CEO & Leadership</a>
              <a href="/mission-vision.html" class="dropdown-link">Mission & Vision</a>
              <a href="/engineering-capabilities.html" class="dropdown-link">Engineering Capabilities</a>
            </div>
          </div>

          <div class="nav-item nav-item-mega">
            <a href="/products.html" class="nav-link active">
              Machinery
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </a>
            <div class="mega-menu">
              <div class="container">
                <div class="mega-grid">
                  <div class="mega-column">
                    <div class="mega-column-title">Pouch Packaging</div>
                    <div class="mega-list">
                      <a href="/products/filter-tobacco-pouch-packing-machine.html" class="mega-link">
                        <span class="mega-link-title">Filter Tobacco Pouch Machine</span>
                        <span class="mega-link-subtitle">180–250 pouches/min, Servo</span>
                      </a>
                      <a href="/products/central-seal-packing-machine.html" class="mega-link">
                        <span class="mega-link-title">Central Seal Packing Machine</span>
                        <span class="mega-link-subtitle">Pillow shape, snacks & tea</span>
                      </a>
                      <a href="/products/four-edge-sealing-grain-packaging-machine.html" class="mega-link">
                        <span class="mega-link-title">4-Edge Sealing Grain Machine</span>
                        <span class="mega-link-subtitle">Flat sheet sachets, 5-formula</span>
                      </a>
                      <a href="/products/three-edge-sealing-grain-packaging-machine.html" class="mega-link">
                        <span class="mega-link-title">3-Edge Sealing Machine</span>
                        <span class="mega-link-subtitle">15–20g portion sachets</span>
                      </a>
                    </div>
                  </div>

                  <div class="mega-column">
                    <div class="mega-column-title">Liquid & Multi-Lane</div>
                    <div class="mega-list">
                      <a href="/products/6-line-shampoo-packing-machine.html" class="mega-link">
                        <span class="mega-link-title">6-Line Shampoo Machine</span>
                        <span class="mega-link-subtitle">6-Lane VFFS, Delta/Siemens PLC</span>
                      </a>
                      <a href="/products/automatic-liquid-pouch-packing-machine.html" class="mega-link">
                        <span class="mega-link-title">Automatic Liquid Pouch Machine</span>
                        <span class="mega-link-subtitle">500g–1kg Oil/Milk, UV Sterilization</span>
                      </a>
                      <a href="/products/2in1-hair-color-pouch-packing-machine.html" class="mega-link">
                        <span class="mega-link-title">2-in-1 Hair Color Pouch Machine</span>
                        <span class="mega-link-subtitle">Twin cosmetic sachets, German motor</span>
                      </a>
                    </div>
                  </div>

                  <div class="mega-column">
                    <div class="mega-column-title">Powder & Flow-Wrap</div>
                    <div class="mega-list">
                      <a href="/products/back-cover-powder-screw-packing-machine-50g.html" class="mega-link">
                        <span class="mega-link-title">Powder Screw Machine (5g–50g)</span>
                        <span class="mega-link-subtitle">Precision auger, 30–90 bags/min</span>
                      </a>
                      <a href="/products/back-cover-powder-screw-packing-machine-1kg.html" class="mega-link">
                        <span class="mega-link-title">Powder Screw Machine (50g–1kg)</span>
                        <span class="mega-link-subtitle">Heavy auger screw, milk & flour</span>
                      </a>
                      <a href="/products/back-seal-feeder-automatic-packing-machine.html" class="mega-link">
                        <span class="mega-link-title">Back Seal Feeder Machine</span>
                        <span class="mega-link-subtitle">1kg–2kg bulk rice & granules</span>
                      </a>
                      <a href="/products/multi-functional-tray-packing-machine.html" class="mega-link">
                        <span class="mega-link-title">Multi-Functional Tray Machine</span>
                        <span class="mega-link-subtitle">Horizontal flow-wrapper, photocell</span>
                      </a>
                    </div>
                  </div>

                  <div class="mega-column">
                    <div class="mega-column-title">Processing & Imported</div>
                    <div class="mega-list">
                      <a href="/imported-products.html#processing" class="mega-link">
                        <span class="mega-link-title">Processing Equipment</span>
                        <span class="mega-link-subtitle">Screw feeders, ribbon mixers, dryers</span>
                      </a>
                      <a href="/imported-products.html#imported" class="mega-link">
                        <span class="mega-link-title">Imported Products</span>
                        <span class="mega-link-subtitle">Coders, band sealers, induction</span>
                      </a>
                      <a href="/products.html" class="mega-link" style="color: var(--color-accent); font-weight: 700; margin-top: 8px;">
                        Explore Complete Catalogue →
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="nav-item">
            <a href="/industries.html" class="nav-link">Industries</a>
          </div>

          <div class="nav-item">
            <a href="/solutions.html" class="nav-link">Solutions</a>
          </div>

          <div class="nav-item">
            <a href="/clients.html" class="nav-link">Our Clients</a>
          </div>

          <div class="nav-item">
            <a href="/contact.html" class="nav-link">Contact</a>
          </div>
        </nav>

        <div class="nav-cta">
          <a href="/request-quote.html" class="btn btn-primary btn-sm btn-quote-desktop">Request a Quote</a>
          <button class="mobile-toggle" aria-label="Open Menu">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
          </button>
        </div>
      </div>
    </header>

    <!-- MOBILE DRAWER -->
    <div class="drawer-overlay"></div>
    <div class="mobile-drawer">
      <div class="drawer-header">
        <div class="brand">
          <img src="/assets/images/branding/logo-badge.png" alt="Adeel Engineering Works" style="height: 38px;" />
          <span style="font-weight: 800; font-size: 1.125rem; color: var(--color-primary-dark);">ADEEL ENG.</span>
        </div>
        <button class="drawer-close" aria-label="Close Menu" style="font-size: 1.5rem; color: var(--color-text-muted);">&times;</button>
      </div>
      <nav class="drawer-nav-list">
        <a href="/index.html" class="drawer-nav-link">Home</a>
        <div>
          <div class="drawer-nav-link" style="color: var(--color-primary);">About Us</div>
          <div class="drawer-sublist">
            <a href="/about.html" class="drawer-sublink">• Company Overview</a>
            <a href="/history.html" class="drawer-sublink">• History Since 2005</a>
            <a href="/leadership.html" class="drawer-sublink">• CEO & Leadership</a>
            <a href="/mission-vision.html" class="drawer-sublink">• Mission & Vision</a>
            <a href="/engineering-capabilities.html" class="drawer-sublink">• Engineering Capabilities</a>
          </div>
        </div>
        <a href="/products.html" class="drawer-nav-link">Product Catalogue</a>
        <a href="/imported-products.html" class="drawer-nav-link">Imported Equipment</a>
        <a href="/industries.html" class="drawer-nav-link">Industries We Serve</a>
        <a href="/solutions.html" class="drawer-nav-link">Customized Machinery</a>
        <a href="/clients.html" class="drawer-nav-link">Client Portfolio</a>
        <a href="/faq.html" class="drawer-nav-link">Technical FAQs</a>
        <a href="/contact.html" class="drawer-nav-link">Contact Us</a>
        <a href="/request-quote.html" class="btn btn-primary mt-4">Request a Quotation</a>
      </nav>
    </div>
"""

def render_footer():
  return """
    <!-- FOOTER -->
    <footer class="footer">
      <div class="container">
        <div class="footer-grid">
          <div>
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">
              <img src="/assets/images/branding/logo-badge.png" alt="Adeel Engineering Works" style="height: 48px;" />
              <div>
                <div style="font-weight: 800; font-size: 1.125rem; color: #ffffff;">ADEEL ENGINEERING</div>
                <div style="font-size: 0.6875rem; color: #38bdf8; font-weight: 700; letter-spacing: 0.08em;">PACKING & PROCESSING MACHINES</div>
              </div>
            </div>
            <p class="footer-text">
              Professional manufacturing enterprise established in 2005. Engineered packing machines for granules, powders, and liquids, built with SS-304/316 stainless steel, PLC automation, and German components.
            </p>
            <div style="font-size: 0.8125rem; color: #94a3b8;">
              <strong>CEO:</strong> Adeel Ahmed Niazi<br>
              <strong>Catalogue:</strong> www.adeelengineeringpk.com
            </div>
          </div>

          <div>
            <div class="footer-col-title">Core Machinery</div>
            <div class="footer-links">
              <a href="/products/filter-tobacco-pouch-packing-machine.html" class="footer-link">Filter Tobacco Pouch Machine</a>
              <a href="/products/2in1-hair-color-pouch-packing-machine.html" class="footer-link">2-in-1 Hair Color Machine</a>
              <a href="/products/6-line-shampoo-packing-machine.html" class="footer-link">6-Line Shampoo Machine</a>
              <a href="/products/automatic-liquid-pouch-packing-machine.html" class="footer-link">Automatic Liquid Pouch (AS1000)</a>
              <a href="/products/back-cover-powder-screw-packing-machine-50g.html" class="footer-link">Powder Screw Machine (5g–50g)</a>
              <a href="/products/back-cover-powder-screw-packing-machine-1kg.html" class="footer-link">Powder Screw Machine (50g–1kg)</a>
              <a href="/products/multi-functional-tray-packing-machine.html" class="footer-link">Multi-Functional Tray Machine</a>
            </div>
          </div>

          <div>
            <div class="footer-col-title">Company & Links</div>
            <div class="footer-links">
              <a href="/about.html" class="footer-link">About Adeel Engineering</a>
              <a href="/history.html" class="footer-link">Company History Since 2005</a>
              <a href="/leadership.html" class="footer-link">CEO & Leadership</a>
              <a href="/mission-vision.html" class="footer-link">Mission & Vision</a>
              <a href="/engineering-capabilities.html" class="footer-link">Engineering Capabilities</a>
              <a href="/industries.html" class="footer-link">Industries We Serve</a>
              <a href="/solutions.html" class="footer-link">Custom Machinery Solutions</a>
              <a href="/clients.html" class="footer-link">Our Clients</a>
              <a href="/faq.html" class="footer-link">Frequently Asked Questions</a>
            </div>
          </div>

          <div>
            <div class="footer-col-title">Faisalabad Headquarters</div>
            <div class="footer-contact-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              <span>College Road, near Jawala Nagar Railway Phatak, Opposite Laboratory High School, Saminabad, Faisalabad, Pakistan</span>
            </div>
            <div class="footer-contact-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
              <div>
                Adeel Niazi: 0302-7012696<br>
                Noshad Niazi: 0307-8870007<br>
                Abdul Manan Niazi: 0308-0450696
              </div>
            </div>
            <div class="footer-contact-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              <span>adeelahmad69638@gmail.com</span>
            </div>
            <div style="margin-top: 16px;">
              <a href="/request-quote.html" class="btn btn-primary btn-sm" style="width: 100%;">Request a Quotation</a>
            </div>
          </div>
        </div>

        <div class="footer-bottom">
          <div class="footer-bottom-content">
            <div>
              &copy; 2005–2026 Adeel Engineering Works. All Rights Reserved. Faisalabad, Pakistan.
            </div>
            <div class="footer-legal-links">
              <a href="/privacy-policy.html">Privacy Policy</a>
              <span>·</span>
              <a href="/terms.html">Terms of Use</a>
              <span>·</span>
              <a href="/sitemap.xml">Sitemap</a>
            </div>
          </div>
        </div>
      </div>
    </footer>

    <!-- FLOATING WHATSAPP -->
    <a href="https://wa.me/923027012696" target="_blank" class="floating-whatsapp" aria-label="Contact Adeel Engineering on WhatsApp">
      <svg viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.698.077-2.227-.56-1.954-.813-3.21-2.793-3.307-2.923-.098-.129-.789-1.049-.789-2.001 0-.952.499-1.417.676-1.611.177-.193.387-.242.516-.242.128 0 .258 0 .37.006.118.006.276-.045.431.328.156.373.535 1.306.582 1.402.047.097.078.21.015.335-.062.126-.094.205-.188.314-.094.11-.197.246-.282.33-.095.094-.194.197-.083.388.111.192.495.815 1.062 1.32.73.651 1.346.853 1.538.949.192.096.305.08.419-.048.114-.129.49-1.57.621-.77.13.8.261.161.439.096.177-.064 1.134-.535 1.328-.631.194-.097.324-.145.37-.225.048-.08.048-.466-.096-.871z"></path></svg>
      <span>WhatsApp Us</span>
    </a>

    <!-- BACK TO TOP -->
    <button class="back-to-top" aria-label="Back to Top">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="18 15 12 9 6 15"></polyline></svg>
    </button>

    <script type="module" src="/assets/js/main.js"></script>
"""

# Generate Product Detail Pages
os.makedirs("products", exist_ok=True)

for m in MACHINES:
  specs_rows = "".join([f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in m["specs"]])
  features_lis = "".join([f"<li><strong>✓</strong> {f}</li>" for f in m["features"]])
  apps_lis = "".join([f"<li>• {a}</li>" for a in m["applications"]])
  
  html = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{m['name']} | Adeel Engineering Works</title>
    <meta name="description" content="{m['overview']} Verified technical specifications from Adeel Engineering Works catalogue page {m['page']}." />
    
    <meta property="og:title" content="{m['name']} - Adeel Engineering Works" />
    <meta property="og:description" content="{m['overview']}" />
    <meta property="og:image" content="{m['image']}" />
    <meta name="twitter:card" content="summary_large_image" />

    <link rel="icon" type="image/png" href="/assets/images/branding/logo-badge.png" />
    <link rel="stylesheet" href="/assets/css/main.css" />
    <link rel="stylesheet" href="/assets/css/responsive.css" />
    
    <!-- Structured Data (Schema.org) -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org/",
      "@type": "Product",
      "name": "{m['name']}",
      "image": "{m['image']}",
      "description": "{m['overview']}",
      "brand": {{
        "@type": "Brand",
        "name": "Adeel Engineering Works"
      }},
      "manufacturer": {{
        "@type": "Organization",
        "name": "Adeel Engineering Works"
      }}
    }}
    </script>
  </head>
  <body>
    {render_header("products")}

    <!-- PAGE HERO & BREADCRUMBS -->
    <div class="page-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="/index.html">Home</a>
          <span>/</span>
          <a href="/products.html">Machinery Catalogue</a>
          <span>/</span>
          <span style="color: #ffffff;">{m['name']}</span>
        </nav>
        <span class="kicker">Catalogue Page {m['page']} · {m['category']}</span>
        <h1 class="page-hero-title">{m['name']}</h1>
        <p class="page-hero-desc">{m['overview']}</p>
      </div>
    </div>

    <!-- MAIN PRODUCT SECTION -->
    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: start; gap: 48px;">
          <!-- Left: Product Image & Quick Actions -->
          <div>
            <div style="background: #F8FAFC; border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 36px; text-align: center; margin-bottom: 24px; box-shadow: var(--shadow-sm);">
              <img src="{m['image']}" alt="{m['name']}" style="max-height: 480px; margin: 0 auto; object-fit: contain;" />
            </div>

            <div style="background: var(--color-bg-soft); border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 24px;">
              <h3 style="font-size: 1.125rem; margin-bottom: 12px; color: var(--color-primary-dark);">Inquire About This Machine</h3>
              <p style="font-size: 0.875rem; color: var(--color-text-muted); margin-bottom: 16px;">
                Direct consultation with our engineering team in Faisalabad. Fast quotations and custom tooling advice.
              </p>
              <div style="display: flex; flex-direction: column; gap: 10px;">
                <a href="/request-quote.html?machine={m['slug']}" class="btn btn-primary" style="width: 100%;">
                  Request Official Quotation
                </a>
                <a href="https://wa.me/923027012696?text=Hello%20Adeel%20Engineering,%20I%20am%20interested%20in%20the%20{m['name']}.%20Please%20share%20its%20specifications,%20quotation%20and%20availability." target="_blank" class="btn btn-whatsapp" style="width: 100%;">
                  Inquire on WhatsApp (+92 302 7012696)
                </a>
                <a href="tel:+923027012696" class="btn btn-secondary" style="width: 100%;">
                  Call CEO Adeel Niazi (0302-7012696)
                </a>
              </div>
            </div>
          </div>

          <!-- Right: Technical Details & Specifications -->
          <div>
            <span class="kicker">Verified Catalogue Specifications</span>
            <h2 style="font-size: 1.875rem; margin-bottom: 16px; color: var(--color-primary-dark);">Technical Specifications</h2>
            <p style="font-size: 0.9375rem; color: var(--color-text-muted); margin-bottom: 20px;">
              Information documented directly in the official <strong>Adeel Engineering Works</strong> company catalogue (Page {m['page']}).
            </p>

            <div class="spec-table-container">
              <table class="spec-table">
                <tbody>
                  {specs_rows}
                </tbody>
              </table>
            </div>

            <!-- Features -->
            <div style="margin-top: 36px;">
              <h3 style="font-size: 1.35rem; margin-bottom: 16px; color: var(--color-primary-dark);">Key Features & Engineering Benefits</h3>
              <ul style="display: flex; flex-direction: column; gap: 12px; font-size: 0.9375rem; color: var(--color-text-main);">
                {features_lis}
              </ul>
            </div>

            <!-- Applications & Packaging Materials -->
            <div style="margin-top: 36px; padding: 24px; background: var(--color-bg-soft); border-radius: var(--radius-md); border: 1px solid var(--color-border);">
              <h4 style="font-size: 1.125rem; margin-bottom: 12px; color: var(--color-primary-dark);">Suitable Applications & Packaging Materials</h4>
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                <div>
                  <strong style="font-size: 0.8125rem; text-transform: uppercase; color: var(--color-text-light);">Documented Applications:</strong>
                  <ul style="margin-top: 6px; font-size: 0.875rem; color: var(--color-text-main);">
                    {apps_lis}
                  </ul>
                </div>
                <div>
                  <strong style="font-size: 0.8125rem; text-transform: uppercase; color: var(--color-text-light);">Packaging Materials:</strong>
                  <p style="margin-top: 6px; font-size: 0.875rem; color: var(--color-text-main); line-height: 1.5;">
                    {m['materials']}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- RELATED MACHINES CTA -->
    <section class="section section-soft">
      <div class="container text-center">
        <h2 style="font-size: 1.75rem; margin-bottom: 12px; color: var(--color-primary-dark);">Looking for Additional Machinery or Custom Tooling?</h2>
        <p style="color: var(--color-text-muted); max-width: 650px; margin: 0 auto 24px;">
          Adeel Engineering Works also engineers customized and irregular packaging machines according to special requirements of customers.
        </p>
        <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
          <a href="/products.html" class="btn btn-secondary">Browse All 11 Packaging Machines</a>
          <a href="/request-quote.html" class="btn btn-primary">Request Custom Machine Inquiry</a>
        </div>
      </div>
    </section>

    {render_footer()}
  </body>
</html>
"""
  filepath = f"products/{m['slug']}.html"
  with open(filepath, "w", encoding="utf-8") as f:
    f.write(html)
  print(f"Generated {filepath}")

print("All 11 product pages successfully generated!")
