import path from 'path';
import { defineConfig } from 'vite';

export default defineConfig(() => {
  return {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, '.'),
      },
    },
    server: {
      port: 3000,
      host: '0.0.0.0',
      hmr: process.env.DISABLE_HMR !== 'true',
      watch: process.env.DISABLE_HMR === 'true' ? null : {},
    },
    build: {
      rollupOptions: {
        input: {
          main: path.resolve(__dirname, 'index.html'),
          about: path.resolve(__dirname, 'about.html'),
          history: path.resolve(__dirname, 'history.html'),
          leadership: path.resolve(__dirname, 'leadership.html'),
          missionVision: path.resolve(__dirname, 'mission-vision.html'),
          capabilities: path.resolve(__dirname, 'engineering-capabilities.html'),
          industries: path.resolve(__dirname, 'industries.html'),
          solutions: path.resolve(__dirname, 'solutions.html'),
          clients: path.resolve(__dirname, 'clients.html'),
          products: path.resolve(__dirname, 'products.html'),
          importedProducts: path.resolve(__dirname, 'imported-products.html'),
          requestQuote: path.resolve(__dirname, 'request-quote.html'),
          contact: path.resolve(__dirname, 'contact.html'),
          faq: path.resolve(__dirname, 'faq.html'),
          privacyPolicy: path.resolve(__dirname, 'privacy-policy.html'),
          terms: path.resolve(__dirname, 'terms.html'),
          notFound: path.resolve(__dirname, '404.html'),
          p1: path.resolve(__dirname, 'products/filter-tobacco-pouch-packing-machine.html'),
          p2: path.resolve(__dirname, 'products/2in1-hair-color-pouch-packing-machine.html'),
          p3: path.resolve(__dirname, 'products/multi-functional-tray-packing-machine.html'),
          p4: path.resolve(__dirname, 'products/6-line-shampoo-packing-machine.html'),
          p5: path.resolve(__dirname, 'products/automatic-liquid-pouch-packing-machine.html'),
          p6: path.resolve(__dirname, 'products/central-seal-packing-machine.html'),
          p7: path.resolve(__dirname, 'products/four-edge-sealing-grain-packaging-machine.html'),
          p8: path.resolve(__dirname, 'products/three-edge-sealing-grain-packaging-machine.html'),
          p9: path.resolve(__dirname, 'products/back-seal-feeder-automatic-packing-machine.html'),
          p10: path.resolve(__dirname, 'products/back-cover-powder-screw-packing-machine-50g.html'),
          p11: path.resolve(__dirname, 'products/back-cover-powder-screw-packing-machine-1kg.html'),
        },
      },
    },
  };
});
