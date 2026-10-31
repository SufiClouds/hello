import subprocess
import os

def crop(page, geometry, output_path):
    cmd = [
        "convert",
        f"/tmp/page-{page:02d}.png",
        "-crop", geometry,
        "+repage",
        output_path
    ]
    subprocess.run(cmd, check=True)
    print(f"Cropped {output_path} with {geometry}")

# Create output dirs
dirs = [
    "public/assets/images/branding",
    "public/assets/images/machines",
    "public/assets/images/processing",
    "public/assets/images/imported-products",
    "public/assets/images/clients"
]
for d in dirs:
    os.makedirs(d, exist_ok=True)

# 1. Branding: Logo from page 1 and page 4
crop(1, "450x300+40+620", "public/assets/images/branding/logo.png")
crop(4, "250x170+930+50", "public/assets/images/branding/logo-badge.png")
crop(1, "600x700+580+280", "public/assets/images/branding/hero-packaging-line.png")

# 2. Leadership: CEO Adeel Ahmed Niazi from page 2
crop(2, "260x280+70+830", "public/assets/images/branding/ceo-adeel-ahmed-niazi.png")

# 3. Main Machines (Pages 4 - 14)
# Page 4: Filter Tobacco Pouch Packing Machine
crop(4, "560x950+50+220", "public/assets/images/machines/filter-tobacco-pouch-packing-machine.png")

# Page 5: 2in1 Hair Color Pouch Packing Machine
crop(5, "580x950+40+240", "public/assets/images/machines/hair-color-pouch-packing-machine.png")

# Page 6: Multi-Functional & Tray Packing Machine
crop(6, "950x850+150+180", "public/assets/images/machines/multi-functional-tray-packing-machine.png")

# Page 7: 6-line Shampo Packing Machine
crop(7, "580x900+40+200", "public/assets/images/machines/6-line-shampoo-packing-machine.png")

# Page 8: Automatic Liquid Pouch Packing Machine
crop(8, "550x880+50+160", "public/assets/images/machines/automatic-liquid-pouch-packing-machine.png")

# Page 9: Central Seal Packing Machine
crop(9, "580x880+30+250", "public/assets/images/machines/central-seal-packing-machine.png")

# Page 10: Four Edge Sealing Grain Packaging Machine
crop(10, "560x900+40+170", "public/assets/images/machines/four-edge-sealing-grain-packing-machine.png")

# Page 11: Three Edge Sealing Grain Packaging Machine
crop(11, "560x920+40+180", "public/assets/images/machines/three-edge-sealing-grain-packing-machine.png")

# Page 12: Back Seal Feeder Automatic Packing Machine
crop(12, "560x900+40+200", "public/assets/images/machines/back-seal-feeder-packing-machine.png")

# Page 13: Back Cover Powder Screw Automatic Packing Machine 5g-50g
crop(13, "550x920+50+200", "public/assets/images/machines/back-cover-powder-screw-packing-machine-50g.png")

# Page 14: Back Cover Powder Screw Automatic Packing Machine 50g-1kg
crop(14, "550x920+50+200", "public/assets/images/machines/back-cover-powder-screw-packing-machine-1kg.png")

# 4. Processing Equipment (Page 15)
# Row 1 (y: 170-600): Screw Feeder, Z-Conveyor
crop(15, "500x400+80+180", "public/assets/images/processing/screw-feeder.png")
crop(15, "450x420+700+160", "public/assets/images/processing/z-conveyor.png")
# Row 2 (y: 650-1100): Coating Pan, U-Mixer
crop(15, "450x420+100+650", "public/assets/images/processing/coating-pan.png")
crop(15, "450x420+700+650", "public/assets/images/processing/u-mixer.png")
# Row 3 (y: 1150-1600): Ribbon Mixer, Dryer Machine
crop(15, "500x420+80+1150", "public/assets/images/processing/ribbon-mixer.png")
crop(15, "450x420+700+1150", "public/assets/images/processing/dryer-machine.png")

# 5. Imported Products (Page 16 - 3x3 grid)
crop(16, "360x340+60+190", "public/assets/images/imported-products/liquid-filling-machine.png")
crop(16, "360x340+440+190", "public/assets/images/imported-products/dk-1100a-ink-roll-coder.png")
crop(16, "360x340+820+190", "public/assets/images/imported-products/continuous-band-sealer.png")
crop(16, "360x340+60+640", "public/assets/images/imported-products/thermal-ink-jet-printer.png")
crop(16, "360x340+440+640", "public/assets/images/imported-products/continuous-ink-jet-printer.png")
crop(16, "360x340+820+640", "public/assets/images/imported-products/horizontal-band-sealer.png")
crop(16, "360x340+60+1070", "public/assets/images/imported-products/foot-sealer.png")
crop(16, "360x340+440+1070", "public/assets/images/imported-products/digital-granule-filler.png")
crop(16, "360x340+820+1070", "public/assets/images/imported-products/sleeve-wrapper-shrink-tunnel.png")

# 6. Imported Products (Page 17)
crop(17, "520x350+50+210", "public/assets/images/imported-products/automatic-induction-sealer.png")
crop(17, "520x350+650+210", "public/assets/images/imported-products/manual-induction-sealer.png")
crop(17, "360x350+60+630", "public/assets/images/imported-products/ultrasonic-tube-sealing.png")
crop(17, "360x350+440+630", "public/assets/images/imported-products/weighing-machine.png")
crop(17, "360x350+820+630", "public/assets/images/imported-products/online-printer.png")
crop(17, "520x360+50+1060", "public/assets/images/imported-products/l-bar-sealer-shrink-tunnels.png")
crop(17, "520x360+650+1060", "public/assets/images/imported-products/semi-auto-round-bottle-sticker-labeller.png")

# 7. Clients (Page 18)
crop(18, "1150x880+45+240", "public/assets/images/clients/clients-showcase-grid.png")

# 8. Individual client logos crop helper
# Row 1: Lazzat Bhara, Sunder Food, Bin Tariq, Adil Foods
crop(18, "250x180+50+250", "public/assets/images/clients/client-lazzat-bhara.png")
crop(18, "250x180+340+250", "public/assets/images/clients/client-sunder-food.png")
crop(18, "250x180+630+250", "public/assets/images/clients/client-bin-tariq.png")
crop(18, "250x180+920+250", "public/assets/images/clients/client-adil-foods.png")

# Row 2: Z&Z Food, Karela Washing Powder, Markhor, Crescent Cotton
crop(18, "250x180+50+430", "public/assets/images/clients/client-zz-food.png")
crop(18, "250x180+340+430", "public/assets/images/clients/client-karela.png")
crop(18, "250x180+630+430", "public/assets/images/clients/client-markhor.png")
crop(18, "250x180+920+430", "public/assets/images/clients/client-crescent-cotton.png")

# Row 3: ALM, Chaah Foods, Foods, ST
crop(18, "250x160+50+600", "public/assets/images/clients/client-alm.png")
crop(18, "250x160+340+600", "public/assets/images/clients/client-chaah-foods.png")
crop(18, "250x160+630+600", "public/assets/images/clients/client-foods.png")
crop(18, "250x160+920+600", "public/assets/images/clients/client-st.png")

# Row 4: Waris Khan, Shehenshah, 999 Nice, Chill Filter Khaini
crop(18, "250x160+50+750", "public/assets/images/clients/client-waris-khan.png")
crop(18, "250x160+340+750", "public/assets/images/clients/client-shehenshah.png")
crop(18, "250x160+630+750", "public/assets/images/clients/client-nice-999.png")
crop(18, "250x160+920+750", "public/assets/images/clients/client-chill.png")

# Row 5: Manzoor Khan, Five Star, 555, Ameer Hamza Soap, Imran Adnan Masala
crop(18, "230x160+50+900", "public/assets/images/clients/client-manzoor-khan.png")
crop(18, "230x160+270+900", "public/assets/images/clients/client-five-star.png")
crop(18, "230x160+500+900", "public/assets/images/clients/client-555.png")
crop(18, "230x160+720+900", "public/assets/images/clients/client-ameer-hamza.png")
crop(18, "250x160+940+900", "public/assets/images/clients/client-imran-adnan.png")

print("All extractions completed successfully!")
