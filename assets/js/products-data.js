// Authoritative Product Database for Adeel Engineering Works
// Sourced strictly from the 18-page Company Catalogue

export const COMPANY_INFO = {
  name: "Adeel Engineering Works",
  tagline: "Packing & Processing Machines",
  founded: 2005,
  ceo: "Adeel Ahmed Niazi",
  email: "adeelahmad69638@gmail.com",
  website: "www.adeelengineeringpk.com",
  location: "College Road, near Jawala Nagar Railway Phatak (Crossing), Opposite Laboratory High School in Saminabad, Faisalabad, Pakistan",
  contacts: [
    { name: "Adeel Niazi", phone: "0302-7012696", intl: "+923027012696", whatsapp: true },
    { name: "Noshad Niazi", phone: "0307-8870007", intl: "+923078870007", whatsapp: false },
    { name: "Abdul Manan Niazi", phone: "0308-0450696", intl: "+923080450696", whatsapp: false }
  ],
  socials: {
    facebook: "Adeel Engineering Work's",
    youtube: "Adeel Engineering Work's",
    instagram: "adeelengineeringworks",
    tiktok: "AdeelEngineering.works"
  }
};

export const CORE_MACHINES = [
  {
    id: "filter-tobacco-pouch-packing-machine",
    slug: "filter-tobacco-pouch-packing-machine",
    name: "Filter Tobacco Pouch Packing Machine",
    category: "Pouch Packaging",
    page: 4,
    image: "/assets/images/machines/filter-tobacco-pouch-packing-machine.png",
    overview: "High-speed precision automated pouch packaging machine engineered specifically for products like nicotine pouches, snus/suns pouch, and small herbal or tea portions requiring precise high-cadence sealing.",
    speed: "180 to 250 pouches per minute",
    powerSupply: "220V / 24V DC control",
    totalPower: "Dual inverter system (1.5 kW Main + 1.5 kW Supply Motor)",
    specs: [
      { label: "Production Speed", value: "180 to 250 pouches per minute" },
      { label: "Automation Control", value: "PLC & HMI Control (Siemens or comparable Delta brand)" },
      { label: "Drive System", value: "Servo Motor (0.75 kW / 1 HP) with 1/10 ratio gear & dual inverter drives" },
      { label: "Main Motor Inverter", value: "1.5 kW Inverter" },
      { label: "Supply Motor Inverter", value: "1.5 kW Inverter" },
      { label: "Conveyor Motor", value: "90V Conveyor Motor" },
      { label: "HMI Interface", value: "Weintek / Wecon 7-inch Touch Screen" },
      { label: "PLC Unit", value: "Delta PLC 220 Volt with communication cable" },
      { label: "Solenoid Valves", value: "Festo Solenoid Valve Assembly (24V DC / 220V AC)" },
      { label: "Heating Transformer", value: "48 Volt 50 Amps Transformer for sealing heaters" },
      { label: "Electrical Protection", value: "Protected by 65A/66A Main Breaker" },
      { label: "Body Structure", value: "12mm (304) Stainless Steel Sheet" },
      { label: "Critical Components", value: "German components for bearings, motor valves, and main jacks" },
      { label: "Temperature System", value: "Comprehensive multi-zone temperature control system" }
    ],
    features: [
      "Ultra-high speed output delivering 180 to 250 finished pouches per minute",
      "Precision servo-driven motion control ensuring accurate bag length registration",
      "Heavy-duty 12mm 304-grade stainless steel frame construction",
      "German-sourced bearings, motor valves, and heavy-load main jacks for long life",
      "Festo solenoid valve assembly ensuring responsive pneumatic actuation",
      "Comprehensive digital temperature control for consistent seam seal integrity"
    ],
    applications: [
      "Nicotine pouches",
      "Snus / suns pouch",
      "Small portion herbal sachets",
      "Dry fine tobacco and aromatic blends"
    ],
    materials: "Heat-sealable composite non-woven and specialized porous barrier pouch filter paper",
    isFeatured: true
  },
  {
    id: "2in1-hair-color-pouch-packing-machine",
    slug: "2in1-hair-color-pouch-packing-machine",
    name: "2-in-1 Hair Color Pouch Packing Machine",
    category: "Liquid Packaging",
    page: 5,
    image: "/assets/images/machines/hair-color-pouch-packing-machine.png",
    overview: "Multi-Pouch High-Speed automated packaging system engineered for synchronized packing of twin hair color and developer sachets across cosmetic and pharmaceutical sectors.",
    speed: "Synchronized high-speed multi-lane output",
    powerSupply: "220V Industrial",
    totalPower: "High-torque German-engineered motor with customizable options",
    specs: [
      { label: "Functionality", value: "Dual Functionality (Twin-chamber / dual-sachet hair color)" },
      { label: "Precision Control", value: "PLC control for real-time synchronization" },
      { label: "Forming Guides", value: "Steel forming guides precision-machined from 18-gauge steel" },
      { label: "Body Construction", value: "Corrosion-resistant SUS304 / SUS316 Stainless Steel (GMP compliant)" },
      { label: "Main Drive Motor", value: "High-torque, German-engineered motor with customizable options" },
      { label: "Electrical Components", value: "Critical electrical parts sourced from Germany for reliability" },
      { label: "Safety System", value: "Internal temperature monitoring with automatic cutoff & emergency stop" },
      { label: "Sachet Customization", value: "Custom modifications and variable sachet shapes (square, twin, contour)" }
    ],
    features: [
      "Dual sachet synchronization allowing hair dye and developer creams to be packaged concurrently",
      "Industrial GMP compliant SUS304/SUS316 stainless steel fluid-contact and chassis parts",
      "Rigid 18-gauge steel bag-forming collars for precise, wrinkle-free pouch edges",
      "Automatic thermal safety cutoff system with oversized operator emergency stop",
      "Customizable tooling for square, perforated twin, or special contour shapes"
    ],
    applications: [
      "Hair color creams and developers",
      "Twin cosmetic lotions and bleaches",
      "Pharmaceutical dual-formula gels and pastes",
      "Personal care conditioner and shampoo pairs"
    ],
    materials: "Multi-layer barrier laminate films, aluminium foil composites, PET/PE",
    isFeatured: true
  },
  {
    id: "multi-functional-tray-packing-machine",
    slug: "multi-functional-tray-packing-machine",
    name: "Multi-Functional & Tray Packing Machine",
    category: "Flow Wrap & Tray",
    page: 6,
    image: "/assets/images/machines/multi-functional-tray-packing-machine.png",
    overview: "Versatile horizontal flow-wrapping and tray packing machine designed for solid bars, bakery treats, soaps, and industrial hardware with optical photocell tracking.",
    speed: "Continuous adjustable flow-wrap line speed",
    powerSupply: "220V",
    totalPower: "2.5 kVA Inverter with 1 HP tractor motor",
    specs: [
      { label: "Machine Type", value: "Horizontal flow-wrapper / pillow-pack tray packaging line" },
      { label: "Optical Registration", value: "High-precision photocell camera with elastic parts alignment" },
      { label: "Drive Inverter", value: "2.5 kVA, 220 Voltage inverter" },
      { label: "Tractor Motor", value: "1 HP Main Motor" },
      { label: "Feed / Reverse Motor", value: "200V Reverse-Forward Motor" },
      { label: "Speed Regulation", value: "Electronic speed control volume dial with push-button inching" },
      { label: "Monitoring Meters", value: "Integrated RPM meter, temperature controller, power meter" },
      { label: "Sanitation", value: "Hygienic easy-clean stainless steel surfaces" }
    ],
    features: [
      "Optical photocell camera alignment ensuring precise wrapper cut at printed eye-marks",
      "Push-button inching control for fast, safe mechanical setup and roll changeover",
      "Dual reverse-forward motor control for effortless web feeding and jam clearing",
      "Broad product handling from individual frozen kulfi to household soap bars",
      "Stable 2.5 kVA variable-frequency inverter drive for smooth acceleration"
    ],
    applications: [
      "Kulfi and ice-cream sticks",
      "Cupcakes and bakery biscuits",
      "Dishwashing soap and beauty soap bars",
      "Dishwashing foam sponges",
      "Surgical potty and medical disposable goods",
      "Bleach cream pots and plastic powder trays"
    ],
    materials: "Heat-sealable BOPP, composite laminate films, pearlized films",
    isFeatured: true
  },
  {
    id: "6-line-shampoo-packing-machine",
    slug: "6-line-shampoo-packing-machine",
    name: "6-Line Shampoo Packing Machine",
    category: "Multi-Lane & Sachet",
    page: 7,
    image: "/assets/images/machines/6-line-shampoo-packing-machine.png",
    overview: "Industrial 6-lane multi-track Vertical Form Fill Seal (VFFS) liquid packaging machine engineered for high-volume commercial production of shampoo and cosmetic sachets.",
    speed: "High-volume multi-lane simultaneous output (6 parallel lines)",
    powerSupply: "220V / 65 Ampere Main Breaker",
    totalPower: "0.5 HP Induction Motor + 90V DC / Servo Film Pulling Drive",
    specs: [
      { label: "Machine Type", value: "6-Lane / Line Vertical Form Fill Seal (VFFS) Liquid Packing Machine" },
      { label: "Seal Configurations", value: "Pillow Pouch, 3-Side Seal, or 4-Side Seal (Shampoo Sachets)" },
      { label: "Main Drive Motor", value: "0.5 HP Induction Motor driving machine mechanics and piston pump" },
      { label: "Film Pulling Motor", value: "90V DC Motor or Servo Motor for precise film feed and cutoff" },
      { label: "PLC Controller", value: "Delta or Siemens Brand Programmable Logic Controller" },
      { label: "Operator Interface", value: "HMI Touch Screen for speed, pouch size, and temperature setup" },
      { label: "Registration Sensor", value: "High sensitivity photoelectric sensor (Photocell camera eye)" },
      { label: "Temperature Control", value: "Digital temperature controllers with Solid State Relay (SSR)" },
      { label: "Main Breaker", value: "65 Ampere heavy-duty electrical protection" },
      { label: "Body Material", value: "Stainless Steel (SS304 or SS316) for rust resistance & hygiene" },
      { label: "Component Origin", value: "Standard industrial grade electrical components (PLC, HMI, Motors)" }
    ],
    features: [
      "Six synchronized packaging lanes dramatically multiplying factory production capacity",
      "Multi-piston liquid dosing unit ensuring uniform volume across all 6 channels",
      "Programmable HMI touch screen for instant length, speed, and heat parameter adjustments",
      "Photocell eye-mark sensor delivering consistent, straight cuts across all web streams",
      "Industrial SS304/SS316 stainless contact parts resisting corrosive shampoos and surfactants"
    ],
    applications: [
      "Hair shampoo sachets",
      "Hair conditioner",
      "Liquid cosmetics and lotions",
      "Shower gels and liquid hand soap",
      "Cosmetic face serums and oils"
    ],
    materials: "Multi-layer barrier laminate films, PET/AL/PE, PET/PE",
    isFeatured: true
  },
  {
    id: "automatic-liquid-pouch-packing-machine",
    slug: "automatic-liquid-pouch-packing-machine",
    name: "Automatic Liquid Pouch Packing Machine (500g to 1kg)",
    category: "Liquid Packaging",
    page: 8,
    image: "/assets/images/machines/automatic-liquid-pouch-packing-machine.png",
    overview: "Heavy-duty vertical liquid form-fill-seal system specifically designed for packaging 500g to 1kg cooking oil and milk pouches with built-in ultraviolet sterilization.",
    speed: "1,500 to 2,000 bags per hour",
    powerSupply: "220V / 65 kVA Main Breaker",
    totalPower: "1 HP Main Motor (1.5 kVA Inverter) + 90V Paper Motor (0.75 kVA Inverter)",
    specs: [
      { label: "Model Series", value: "AS1000 Series Industrial Liquid Pouch Machine" },
      { label: "Dosing Range", value: "500 Gram to 1 kg" },
      { label: "Production Speed", value: "1,500 to 2,000 bags per hour (standard beverages & liquids)" },
      { label: "Automated Cycle", value: "UV sterilization, bag forming, date printing, dosing, filling, sealing, cutting" },
      { label: "Main Motor", value: "1 HP Main Motor with 1.5 kVA Inverter" },
      { label: "Paper Feeding Motor", value: "90V Paper Motor with 0.75 kVA Inverter" },
      { label: "Photocell Unit", value: "Photocell camera eye for print registration" },
      { label: "Sealing Control", value: "Temperature controller with contactors and push buttons" },
      { label: "Dimensions", value: "Approximately 850 x 1100 x 1850 mm" },
      { label: "Machine Weight", value: "Approximately 320 kg" },
      { label: "Sanitary Standard", value: "Food-grade stainless steel fluid path and hygienic body structure" }
    ],
    features: [
      "Complete 7-in-1 automated cycle from film UV sterilization to finished sealed pouch",
      "High output capability delivering up to 2,000 pouches per hour for beverages and cooking oil",
      "Integrated date coder for lot number and expiry date printing on the pouch seam",
      "Heavy-duty 320 kg chassis engineered for continuous high-viscosity liquid duty",
      "Dual variable-speed inverters for main mechanical stroke and film unwinding"
    ],
    applications: [
      "Cooking oil and edible ghee",
      "Fresh milk, pasteurized dairy, and lassi",
      "Sauces, syrups, and vinegar",
      "Fruit juices and non-carbonated drinks",
      "Agricultural liquid fertilizers"
    ],
    materials: "Co-extruded LDPE film, specialized milk/oil barrier pouch rolls",
    isFeatured: true
  },
  {
    id: "central-seal-packing-machine",
    slug: "central-seal-packing-machine",
    name: "Central Seal Packing Machine",
    category: "Pouch Packaging",
    page: 9,
    image: "/assets/images/machines/central-seal-packing-machine.png",
    overview: "Pillow-shape vertical packaging machine engineered for snacks, nimko, bulk candies, tea, and dry goods with intelligent optical fault detection to eliminate film waste.",
    speed: "36 pouches per minute",
    powerSupply: "220 V",
    totalPower: "3 kW",
    specs: [
      { label: "Production Speed", value: "36 Pouches per minute" },
      { label: "Bag Formation", value: "Pillow Shape (Center back seam seal)" },
      { label: "Packaging Material", value: "Any heat-sealable composite or single-layer film" },
      { label: "Electrical Supply", value: "220 V Single Phase" },
      { label: "Total Power Energy", value: "3 kW" },
      { label: "Packaging Cycle", value: "Bagging, measuring, filling, counting, printing date, cutting, product output" },
      { label: "Coder Option", value: "Print date & lot number (optional reprovision coder)" },
      { label: "Cutting Mechanism", value: "Automated rotary/pneumatic cutting device with transfer bag chute" },
      { label: "Anti-Waste Sensor", value: "Optical fault detection: No material in tray / No wrapper auto shut-down" },
      { label: "Speed Display", value: "Digital real-time packaging speed read-out" }
    ],
    features: [
      "Automatic optical sensor shuts machine down immediately when hopper is empty or film runs out",
      "Classic pillow back-seal format providing strong, tamper-evident packaging",
      "Integrated batch counting and automatic product discharge onto conveyor",
      "Reliable 3 kW low-consumption electrical system operating on standard 220V",
      "Quick-change forming collar for rapid pouch width transitions"
    ],
    applications: [
      "Nimko, kurkure, and salted snacks",
      "Pasta, macaroni, and crackers",
      "Bulk candies and toffees",
      "Popcorn and puffed corn",
      "Loose black tea and herbal tea",
      "Dry fruits, nuts, and whole spices",
      "Detergent powders"
    ],
    materials: "Any heat-sealable film, BOPP/CPP, metalized PET, laminated paper",
    isFeatured: true
  },
  {
    id: "four-edge-sealing-grain-packaging-machine",
    slug: "four-edge-sealing-grain-packaging-machine",
    name: "Four Edge Sealing Grain Packaging Machine",
    category: "Pouch Packaging",
    page: 10,
    image: "/assets/images/machines/four-edge-sealing-grain-packing-machine.png",
    overview: "Precision 4-side perimeter seal packaging system equipped with 5-group recipe parameter memory and independent dual-axis temperature controls for cosmetic creams and viscous sauces.",
    speed: "40 to 50 pouches per minute",
    powerSupply: "220 V",
    totalPower: "3 kW",
    specs: [
      { label: "Production Speed", value: "40 to 50 Pouches per minute" },
      { label: "Bag Geometry", value: "Sheet Shape / 4-Edge Perimeter Flat Seal" },
      { label: "Seal Width", value: "Upper and lower seal widths customizable according to client need" },
      { label: "Packaging Material", value: "Any heat-sealable film, composite film, or single-layer film" },
      { label: "Power Supply", value: "220 V" },
      { label: "Total Power", value: "3 kW" },
      { label: "Process Cycle", value: "Pouch formation, measuring, filling, counting, batch/date printing, cutting" },
      { label: "Formula Memory", value: "Stores 5 groups of formula parameters for rapid, accurate changeover" },
      { label: "Temperature Control", value: "Transverse and longitudinal sealing temperatures controlled independently" }
    ],
    features: [
      "Independent transverse and longitudinal temperature PID loops for defect-free sealing",
      "Built-in 5-recipe memory eliminates manual recalibration between different product runs",
      "Crisp 4-edge flat sheet profile ideal for premium cosmetic sample and food sachet presentation",
      "High speed 40-50 pouches/minute output with synchronized date stamp",
      "Heavy-duty stainless steel contact parts for food and chemical stability"
    ],
    applications: [
      "Beauty creams and whitening lotions",
      "Hair remover creams",
      "Hair oils and scented hair tonics",
      "Tomato ketchup and chili garlic sauce",
      "Mayonnaise and dipping sauces",
      "Fine pastes and medicinal emulsions"
    ],
    materials: "Composite films, single-layer films, multi-ply barrier laminates",
    isFeatured: true
  },
  {
    id: "three-edge-sealing-grain-packaging-machine",
    slug: "three-edge-sealing-grain-packaging-machine",
    name: "Three Edge Sealing Grain Packaging Machine",
    category: "Pouch Packaging",
    page: 11,
    image: "/assets/images/machines/three-edge-sealing-grain-packing-machine.png",
    overview: "High-accuracy 3-side seal form-fill-seal packaging machine configured for 15g to 20g portion sachets of powders, foaming materials, and spices with independent thermal controls.",
    speed: "40 to 50 pouches per minute",
    powerSupply: "220 V",
    totalPower: "3 kW",
    specs: [
      { label: "Production Speed", value: "40 to 50 Pouches per minute" },
      { label: "Measuring Range", value: "15 to 20 Gram portion pouch packaging" },
      { label: "Bag Geometry", value: "3-Edge Sealing Pouch" },
      { label: "Packaging Material", value: "Any heat-sealable film" },
      { label: "Power Supply", value: "220 V" },
      { label: "Total Power", value: "3 kW" },
      { label: "Process Cycle", value: "Pouch forming, volumetric measuring, filling, count, date/batch print, cutting" },
      { label: "Formula Memory", value: "Stores 5 groups of recipe parameters for swift product switching" },
      { label: "Temperature Control", value: "Separate transverse and longitudinal sealing temperature regulators" }
    ],
    features: [
      "Optimized 15g to 20g portioning accuracy for expensive spice powders and foaming agents",
      "Stores five complete recipe configurations to minimize operator changeover errors",
      "Independent cross and vertical heat jaws ensure airtight seals on tricky barrier films",
      "Rotary cutting mechanism delivering clean, uniform pouch separation",
      "Compact footprint suited for tight factory floor layouts"
    ],
    applications: [
      "All powder materials and spice powders (15/20g)",
      "Liquid foam materials and foaming agents",
      "Single-serve instant beverage mixes",
      "Herbal seasonings and medicinal powders"
    ],
    materials: "Any heat-sealable composite foil, laminated paper, OPP/PE",
    isFeatured: false
  },
  {
    id: "back-seal-feeder-automatic-packing-machine",
    slug: "back-seal-feeder-automatic-packing-machine",
    name: "Back Seal Feeder Automatic Packing Machine (1kg to 2kg)",
    category: "Powder Packaging",
    page: 12,
    image: "/assets/images/machines/back-seal-feeder-packing-machine.png",
    overview: "Heavyweight back-seal packaging system with integrated hopper feeder engineered for packaging bulk bags up to 1kg to 2kg of rice, sugar, washing powder, and free-flowing granules.",
    speed: "20 to 30 bags per minute",
    powerSupply: "220V",
    totalPower: "3 kW",
    specs: [
      { label: "Production Speed", value: "20 to 30 bags per minute" },
      { label: "Max Package Weight", value: "1 kg to 2 kg capacity" },
      { label: "Bag Profile", value: "Back Seal (Pillow-shaped heavy bag)" },
      { label: "Packaging Material", value: "Any heat-sealable material" },
      { label: "Power Supply", value: "220V" },
      { label: "Total Power Energy", value: "3 kW" },
      { label: "Complete Cycle", value: "Bag forming, volumetric measuring, filling, count, date printing, cutting" },
      { label: "Speed Display", value: "Automated digital display of packaging speed" },
      { label: "Waste Prevention", value: "Optical fault interlock: Tray no material / wrapper empty auto shutdown" }
    ],
    features: [
      "High weight capacity handling heavy 1 kg to 2 kg retail and wholesale bags",
      "Integrated bulk feeder chute for smooth transfer of free-flowing granules and heavy powders",
      "Optical anti-waste shutdown prevents empty bagging cycles if supply runs dry",
      "Reinforced heavy-duty back seam seal to withstand drop impacts during bulk transport",
      "Simple 220V 3kW power setup suitable for standard factory wiring"
    ],
    applications: [
      "Food: Snacks, bulk candies, rice, tea, popcorn, dry fruits",
      "Spices & Powders: Various ground spices, milk powder, washing powder",
      "General: Suited for most free-flowing granules and fine industrial powders"
    ],
    materials: "Heavy-gauge heat-sealable composite films, nylon laminates, PE",
    isFeatured: true
  },
  {
    id: "back-cover-powder-screw-packing-machine-50g",
    slug: "back-cover-powder-screw-packing-machine-50g",
    name: "Back Cover Powder Screw Automatic Packing Machine (5g to 50g)",
    category: "Powder Packaging",
    page: 13,
    image: "/assets/images/machines/back-cover-powder-screw-packing-machine-50g.png",
    overview: "High-precision servo auger screw powder packaging machine tailored for fine powders from 5g to 50g with imported PLC and multilingual touchscreen.",
    speed: "30 to 90 bags per minute",
    powerSupply: "220V",
    totalPower: "Integrated high-speed auger drive with PLC control",
    specs: [
      { label: "Measuring Range", value: "5 gram to 50 gram" },
      { label: "Packing Speed", value: "30 to 90 bags per minute" },
      { label: "Applicable Films", value: "Composite films like OPP/CPP, PET/PE, and MST/PE" },
      { label: "Automation Level", value: "Full Automation: Measuring, filling, counting, printing in one cycle" },
      { label: "Smart Controls", value: "Imported PLC system for stable, non-stop parameter adjustments" },
      { label: "Multilingual HMI", value: "Touch screen supports Chinese, English, Russian, and Spanish" },
      { label: "Precision Engineering", value: "Independent temperature controls for horizontal and vertical sealing" },
      { label: "Formula Memory", value: "Stores five different product settings for fast changeovers" },
      { label: "Feeder Assembly", value: "Precision stainless steel screw auger feeder with sealing jaws" }
    ],
    features: [
      "High-accuracy auger screw dosing eliminates dusting and powder cavitation",
      "Impressive speed up to 90 bags per minute for high-cadence powder packing lines",
      "Multilingual interface (English, Chinese, Russian, Spanish) for international operators",
      "Non-stop parameter tuning allows real-time weight adjustments without stopping the line",
      "5-product recipe memory stores optimal speeds and temperatures for instant changeover"
    ],
    applications: [
      "Milk powder and infant formula sachets",
      "Corn starch, tapioca, and flour powders",
      "Tea powder, instant coffee, and matcha",
      "Chemical, cosmetic, and pharmaceutical fine powders"
    ],
    materials: "OPP/CPP, PET/PE, MST/PE, and heat-sealable barrier foils",
    isFeatured: true
  },
  {
    id: "back-cover-powder-screw-packing-machine-1kg",
    slug: "back-cover-powder-screw-packing-machine-1kg",
    name: "Back Cover Powder Screw Automatic Packing Machine (50g to 1kg)",
    category: "Powder Packaging",
    page: 14,
    image: "/assets/images/machines/back-cover-powder-screw-packing-machine-1kg.png",
    overview: "Large-capacity servo auger screw vertical powder packaging system engineered for packaging 50g up to 1kg bags of milk powder, starches, and fine chemical powders.",
    speed: "30 to 90 bags per minute",
    powerSupply: "220V",
    totalPower: "High-torque auger screw motor with imported PLC",
    specs: [
      { label: "Measuring Range", value: "50 gram to 1 kg" },
      { label: "Packing Speed", value: "30 to 90 bags per minute" },
      { label: "Packaging Films", value: "Composite films like OPP/CPP, PET/PE, and MST/PE" },
      { label: "Cycle Automation", value: "Full Automation: Handles measuring, filling, counting, and printing in one cycle" },
      { label: "PLC System", value: "Imported PLC system for stable, non-stop parameter adjustments" },
      { label: "Touchscreen Interface", value: "Multilingual touch screen supporting Chinese, English, Russian, Spanish" },
      { label: "Temperature Regulators", value: "Independent temperature controls for horizontal and vertical sealing" },
      { label: "Recipe Storage", value: "Can store five different product settings for fast changeovers" },
      { label: "Construction", value: "Food-grade stainless steel screw auger and heavy industrial frame" }
    ],
    features: [
      "Wide dosing span accommodating medium to heavy 50g through 1000g powder packages",
      "Heavy-duty auger drive providing dependable torque even with dense, cohesive powders",
      "Touch screen interface with support for English, Chinese, Russian, and Spanish",
      "Independent cross/vertical sealing heating bars for leak-proof powder containment",
      "Five pre-programmed recipe memory channels for rapid product changeover"
    ],
    applications: [
      "Retail milk powder bags",
      "Industrial starch and baking flour",
      "Tea powder, cocoa powder, and beverage mixes",
      "Fine spice blends and curry powders",
      "Chemical powders, pigments, and agrochemicals"
    ],
    materials: "Composite films (OPP/CPP, PET/PE, MST/PE), multi-layer foil pouches",
    isFeatured: true
  }
];

export const PROCESSING_EQUIPMENT = [
  {
    id: "screw-feeder",
    name: "Screw Feeder",
    category: "Processing & Conveying",
    page: 15,
    image: "/assets/images/processing/screw-feeder.png",
    desc: "Stainless steel inclined screw auger elevator designed for automated feeding of powders and fine granules into high-speed packaging machine hoppers."
  },
  {
    id: "z-conveyor",
    name: "Z-Conveyor",
    category: "Processing & Conveying",
    page: 15,
    image: "/assets/images/processing/z-conveyor.png",
    desc: "Z-bucket elevator conveyor system engineered for gentle vertical elevation and non-breakage transfer of fragile chips, snack granules, and candies."
  },
  {
    id: "coating-pan",
    name: "Coating Pan",
    category: "Processing & Conveying",
    page: 15,
    image: "/assets/images/processing/coating-pan.png",
    desc: "Rotary stainless steel spherical coating pan for uniform seasoning, sugar coating, pharmaceutical tablet film coating, and confectionery polishing."
  },
  {
    id: "u-mixer",
    name: "U-Mixer",
    category: "Processing & Conveying",
    page: 15,
    image: "/assets/images/processing/u-mixer.png",
    desc: "Heavy-duty horizontal U-trough industrial mixer engineered for consistent blending of semi-solids, moist compounds, food pastes, and doughs."
  },
  {
    id: "ribbon-mixer",
    name: "Ribbon Mixer",
    category: "Processing & Conveying",
    page: 15,
    image: "/assets/images/processing/ribbon-mixer.png",
    desc: "Precision double-helical ribbon blender delivering fast, homogeneous blending of dry powders, spices, detergents, and industrial chemicals."
  },
  {
    id: "dryer-machine",
    name: "Dryer Machine",
    category: "Processing & Conveying",
    page: 15,
    image: "/assets/images/processing/dryer-machine.png",
    desc: "Industrial vertical spin/fluid hot-air drying unit configured for moisture removal, granule conditioning, and post-wash processing."
  }
];

export const IMPORTED_PRODUCTS = [
  {
    id: "liquid-filling-machine",
    name: "Liquid Filling Machine",
    category: "Imported Equipment",
    page: 16,
    image: "/assets/images/imported-products/liquid-filling-machine.png",
    desc: "Pneumatic piston-driven benchtop dosing filler suitable for precise dispensing of liquid oils, lotions, syrups, and cosmetic pastes."
  },
  {
    id: "dk-1100a-ink-roll-coder",
    name: "DK-1100A Ink Roll Coder",
    category: "Imported Equipment",
    page: 16,
    image: "/assets/images/imported-products/dk-1100a-ink-roll-coder.png",
    desc: "High-speed rotary hot-ink roll contact date and batch number coder designed for integration onto horizontal and vertical bagging machines."
  },
  {
    id: "continuous-band-sealer",
    name: "Continuous Band Sealer",
    category: "Imported Equipment",
    page: 16,
    image: "/assets/images/imported-products/continuous-band-sealer.png",
    desc: "Benchtop motorized continuous band sealer with conveyor belt for hermetically sealing pre-made plastic, foil, and composite bags."
  },
  {
    id: "thermal-ink-jet-printer",
    name: "Thermal Ink-Jet Printer",
    category: "Imported Equipment",
    page: 16,
    image: "/assets/images/imported-products/thermal-ink-jet-printer.png",
    desc: "High-resolution handheld TIJ printer with intuitive touchscreen for on-the-fly printing of barcodes, QR codes, dates, and logos."
  },
  {
    id: "continuous-ink-jet-printer",
    name: "Continuous Ink-Jet Printer",
    category: "Imported Equipment",
    page: 16,
    image: "/assets/images/imported-products/continuous-ink-jet-printer.png",
    desc: "Industrial CIJ non-contact production-line inkjet printer for high-speed date, batch, and serial marking on curved or moving containers."
  },
  {
    id: "horizontal-band-sealer",
    name: "Horizontal Band Sealer",
    category: "Imported Equipment",
    page: 16,
    image: "/assets/images/imported-products/horizontal-band-sealer.png",
    desc: "Heavy-duty continuous motorized horizontal bag sealing machine featuring electronic temperature control and integrated embossing."
  },
  {
    id: "foot-sealer",
    name: "Foot Sealer",
    category: "Imported Equipment",
    page: 16,
    image: "/assets/images/imported-products/foot-sealer.png",
    desc: "Pedal-operated manual impulse heat sealer for rapid, hands-free sealing of poly bags, foil pouches, and heavy sack liners."
  },
  {
    id: "digital-granule-filler",
    name: "Digital Granule Filler",
    category: "Imported Equipment",
    page: 16,
    image: "/assets/images/imported-products/digital-granule-filler.png",
    desc: "Microcomputer-controlled vibratory weighing and dispensing machine for precise small-portion packaging of tea, seeds, and granules."
  },
  {
    id: "sleeve-wrapper-shrink-tunnel",
    name: "Sleeve Wrapper & Shrink Tunnel",
    category: "Imported Equipment",
    page: 16,
    image: "/assets/images/imported-products/sleeve-wrapper-shrink-tunnel.png",
    desc: "Heavy-duty automated sleeve wrapping system and high-temperature circulating shrink tunnel for bundling bottles, cartons, and cans."
  },
  {
    id: "automatic-induction-sealer",
    name: "Automatic Induction Sealer",
    category: "Imported Equipment",
    page: 17,
    image: "/assets/images/imported-products/automatic-induction-sealer.png",
    desc: "In-line electromagnetic induction cap sealer for tamper-evident, hermetic foil sealing of bottles and jars on conveyor lines."
  },
  {
    id: "manual-induction-sealer",
    name: "Manual Induction Sealer",
    category: "Imported Equipment",
    page: 17,
    image: "/assets/images/imported-products/manual-induction-sealer.png",
    desc: "Portable handheld electromagnetic induction sealing unit ideal for low-to-medium volume container foil cap sealing."
  },
  {
    id: "ultrasonic-tube-sealing",
    name: "Ultrasonic Tube Sealing Machine",
    category: "Imported Equipment",
    page: 17,
    image: "/assets/images/imported-products/ultrasonic-tube-sealing.png",
    desc: "Ultrasonic plastic and laminate tube tail sealer with pneumatic trimming for cosmetic creams, toothpaste, and pharmaceutical ointments."
  },
  {
    id: "weighing-machine",
    name: "Weighing Machine",
    category: "Imported Equipment",
    page: 17,
    image: "/assets/images/imported-products/weighing-machine.png",
    desc: "High-precision digital bench scale and batch checking station crafted from food-grade stainless steel for factory quality control."
  },
  {
    id: "online-printer",
    name: "Online Printer",
    category: "Imported Equipment",
    page: 17,
    image: "/assets/images/imported-products/online-printer.png",
    desc: "Inline conveyor-mount high-speed thermal date and lot code printing system with external optical sensor synchronization."
  },
  {
    id: "l-bar-sealer-shrink-tunnels",
    name: "L-Bar Sealer & Shrink Tunnels",
    category: "Imported Equipment",
    page: 17,
    image: "/assets/images/imported-products/l-bar-sealer-shrink-tunnels.png",
    desc: "Combined semi-automatic L-bar film sealer and recirculating hot-air shrink tunnel for clean shrink-wrap packaging of boxed goods."
  },
  {
    id: "semi-auto-round-bottle-sticker-labeller",
    name: "Semi-Auto Round Bottle Sticker Labeller",
    category: "Imported Equipment",
    page: 17,
    image: "/assets/images/imported-products/semi-auto-round-bottle-sticker-labeller.png",
    desc: "Precision motorized benchtop label applicator for wrinkle-free self-adhesive sticker labeling on cylindrical glass and plastic bottles."
  }
];

export const CLIENT_LOGOS = [
  { name: "Lazzat Bhara", image: "/assets/images/clients/client-lazzat-bhara.png", category: "Food & Spices" },
  { name: "Sunder Food", image: "/assets/images/clients/client-sunder-food.png", category: "Confectionery & Food" },
  { name: "Bin Tariq", image: "/assets/images/clients/client-bin-tariq.png", category: "Shopping & Spices" },
  { name: "Adil Foods", image: "/assets/images/clients/client-adil-foods.png", category: "Packaged Foods" },
  { name: "Z&Z Food", image: "/assets/images/clients/client-zz-food.png", category: "Snacks & Food" },
  { name: "Karela Washing Powder", image: "/assets/images/clients/client-karela.png", category: "Detergent & Cleaning" },
  { name: "Markhor", image: "/assets/images/clients/client-markhor.png", category: "Consumer Goods" },
  { name: "Crescent Cotton Industries", image: "/assets/images/clients/client-crescent-cotton.png", category: "Textile & Cotton" },
  { name: "ALM", image: "/assets/images/clients/client-alm.png", category: "Consumer Products" },
  { name: "Chaah Foods", image: "/assets/images/clients/client-chaah-foods.png", category: "Tea & Food" },
  { name: "Foods Premium Quality", image: "/assets/images/clients/client-foods.png", category: "Packaged Foods" },
  { name: "ST", image: "/assets/images/clients/client-st.png", category: "Industrial Products" },
  { name: "Waris Khan Tobacco", image: "/assets/images/clients/client-waris-khan.png", category: "Tobacco Products" },
  { name: "Shehenshah", image: "/assets/images/clients/client-shehenshah.png", category: "Consumer Goods" },
  { name: "999 Nice", image: "/assets/images/clients/client-nice-999.png", category: "Consumer Products" },
  { name: "Chill Filter Khaini", image: "/assets/images/clients/client-chill.png", category: "Pouch Tobacco" },
  { name: "Manzoor Khan Tobacco", image: "/assets/images/clients/client-manzoor-khan.png", category: "Tobacco Products" },
  { name: "Five Star Filter Khaini", image: "/assets/images/clients/client-five-star.png", category: "Pouch Products" },
  { name: "555", image: "/assets/images/clients/client-555.png", category: "Consumer Products" },
  { name: "AH Ameer Hamza Soap", image: "/assets/images/clients/client-ameer-hamza.png", category: "Soaps & Detergents" },
  { name: "Imran Adnan Masala Jat", image: "/assets/images/clients/client-imran-adnan.png", category: "Spices & Seasonings" }
];
