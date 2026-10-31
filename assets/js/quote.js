// QUOTATION & INQUIRY CONTROLLER FOR ADEEL ENGINEERING WORKS
import { CORE_MACHINES, PROCESSING_EQUIPMENT, IMPORTED_PRODUCTS, COMPANY_INFO } from './products-data.js';

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('quotation-form');
  const machineSelect = document.getElementById('machine-select');
  const urlParams = new URLSearchParams(window.location.search);
  const preselectedMachine = urlParams.get('machine');

  // Populate machine selector
  if (machineSelect) {
    // Add Core Machines optgroup
    const coreGroup = document.createElement('optgroup');
    coreGroup.label = 'Core Packaging Machines (Adeel Engineering)';
    CORE_MACHINES.forEach(m => {
      const opt = document.createElement('option');
      opt.value = m.name;
      opt.textContent = m.name;
      if (preselectedMachine && (preselectedMachine.toLowerCase() === m.slug || preselectedMachine.toLowerCase() === m.name.toLowerCase())) {
        opt.selected = true;
      }
      coreGroup.appendChild(opt);
    });
    machineSelect.appendChild(coreGroup);

    // Add Processing Equipment optgroup
    const procGroup = document.createElement('optgroup');
    procGroup.label = 'Processing & Conveying Equipment';
    PROCESSING_EQUIPMENT.forEach(p => {
      const opt = document.createElement('option');
      opt.value = p.name;
      opt.textContent = p.name;
      if (preselectedMachine && preselectedMachine.toLowerCase() === p.name.toLowerCase()) {
        opt.selected = true;
      }
      procGroup.appendChild(opt);
    });
    machineSelect.appendChild(procGroup);

    // Add Imported Products optgroup
    const impGroup = document.createElement('optgroup');
    impGroup.label = 'Imported Machinery & Accessories';
    IMPORTED_PRODUCTS.forEach(i => {
      const opt = document.createElement('option');
      opt.value = i.name;
      opt.textContent = i.name;
      if (preselectedMachine && preselectedMachine.toLowerCase() === i.name.toLowerCase()) {
        opt.selected = true;
      }
      impGroup.appendChild(opt);
    });
    machineSelect.appendChild(impGroup);
  }

  // Handle Form Submission
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const fullName = document.getElementById('fullname')?.value.trim();
      const company = document.getElementById('company')?.value.trim() || 'N/A';
      const email = document.getElementById('email')?.value.trim();
      const phone = document.getElementById('phone')?.value.trim();
      const country = document.getElementById('country')?.value.trim() || 'Pakistan';
      const industry = document.getElementById('industry')?.value.trim() || 'General';
      const machine = machineSelect?.value || 'Industrial Packaging Machine';
      const material = document.getElementById('material')?.value.trim() || 'Standard packaging material';
      const capacity = document.getElementById('capacity')?.value.trim() || 'Standard factory speed';
      const notes = document.getElementById('notes')?.value.trim() || 'Please provide quotation and specifications.';

      if (!fullName || !phone || !email) {
        alert('Please fill out all required fields (Name, Phone / WhatsApp, Email).');
        return;
      }

      const submitType = e.submitter?.getAttribute('data-action') || 'whatsapp';

      const messageBody = 
`*NEW MACHINERY INQUIRY - ADEEL ENGINEERING WORKS*
---------------------------------------
*Client Name:* ${fullName}
*Company:* ${company}
*Country / City:* ${country}
*Phone / WhatsApp:* ${phone}
*Email:* ${email}
*Industry:* ${industry}
---------------------------------------
*Machine Requested:* ${machine}
*Product / Material to Pack:* ${material}
*Required Production Capacity:* ${capacity}
---------------------------------------
*Additional Notes:*
${notes}`;

      if (submitType === 'email') {
        const mailtoUrl = `mailto:${COMPANY_INFO.email}?subject=${encodeURIComponent(`Quotation Request: ${machine} - ${company}`)}&body=${encodeURIComponent(messageBody)}`;
        window.location.href = mailtoUrl;
      } else {
        // Direct WhatsApp
        const waNumber = '923027012696';
        const waUrl = `https://wa.me/${waNumber}?text=${encodeURIComponent(messageBody)}`;
        window.open(waUrl, '_blank');
      }

      // Show confirmation
      const modal = document.getElementById('inquiry-modal');
      if (modal) {
        modal.style.display = 'flex';
      }
    });
  }

  // Close modal
  document.querySelectorAll('[data-close-modal]').forEach(btn => {
    btn.addEventListener('click', () => {
      const modal = document.getElementById('inquiry-modal');
      if (modal) modal.style.display = 'none';
    });
  });
});
