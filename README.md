# 🚗 Garage RAMS App

A comprehensive, mobile-friendly Progressive Web App for generating Risk Assessments and Method Statements (RAMS) specifically designed for garage operations. Features intelligent AI-powered suggestions, comprehensive safety databases, and professional PDF export capabilities.

## ✨ **Key Features**

### 🤖 **AI-Powered Intelligence**
- **Comprehensive Activity Database:** 10+ garage activities with detailed safety information
- **Smart Suggestions:** Context-aware hazards, controls, and method steps
- **Confidence Levels:** High/Medium/Low confidence indicators with source information
- **Keyword Pattern Matching:** Intelligent suggestions for custom tasks
- **Offline AI:** No internet required - works completely offline

### 🎯 **Core Functionality**
- **Task Selection:** Choose from predefined templates or create custom tasks
- **Risk Assessment:** Dynamic risk matrix with severity and likelihood calculations
- **Method Statements:** Step-by-step work procedures
- **PDF Export:** Professional, branded documents with company information
- **Review Management:** Automated reminders and tracking

### 📱 **Progressive Web App**
- **Installable:** Add to home screen on any device
- **Offline First:** Works without internet connection
- **Mobile Optimized:** Touch-friendly interface
- **Cross Platform:** Works on Windows, macOS, Linux, iOS, and Android

### ☁️ **Cloud Integration (Optional)**
- **Supabase Backend:** Secure cloud synchronization
- **Multi-device Sync:** Access assessments from anywhere
- **User Management:** Secure authentication and authorization
- **Data Backup:** Automatic cloud backup and recovery

## 🚀 **Quick Start**

### Prerequisites
- Node.js 18+ and npm
- Modern web browser
- Optional: Supabase account for cloud features

### Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd garage-risk

# Install dependencies
npm install

# Start development server
npm run dev

# Open http://localhost:5173 in your browser
```

### Build for Production
```bash
npm run build
npm run preview
```

## 🎯 **How It Works**

### 1. **Task Selection**
- Choose from AI-powered activity suggestions
- Search through comprehensive garage activity database
- Use quick templates for common tasks
- Create custom tasks with intelligent suggestions

### 2. **AI-Powered Suggestions**
- **High Confidence:** Activity-specific database matches
- **Medium Confidence:** Keyword pattern analysis
- **Low Confidence:** Generic safety guidelines
- **Smart Filtering:** Avoid duplicate suggestions

### 3. **Risk Assessment**
- Dynamic risk calculation (Severity × Likelihood)
- Visual risk matrix with color coding
- Automated risk categorization (LOW/MEDIUM/HIGH)
- Risk history tracking and trends

### 4. **Document Generation**
- Professional PDF export with company branding
- Customizable templates and layouts
- Digital sign-off capabilities
- Multi-format export options

## 🗄️ **Activity Database**

The app includes comprehensive safety information for:

| Activity | Hazards | Controls | Method Steps |
|----------|---------|----------|--------------|
| **Engine Repair** | 8 hazards | 8 controls | 9 steps |
| **Brake Service** | 8 hazards | 8 controls | 9 steps |
| **Electrical Work** | 8 hazards | 8 controls | 8 steps |
| **Suspension Service** | 8 hazards | 8 controls | 9 steps |
| **Transmission Work** | 8 hazards | 8 controls | 9 steps |
| **Body & Paint** | 8 hazards | 8 controls | 9 steps |
| **Diagnostics** | 8 hazards | 8 controls | 9 steps |
| **Tire Service** | 8 hazards | 8 controls | 8 steps |
| **AC Service** | 8 hazards | 8 controls | 9 steps |
| **Fuel System** | 8 hazards | 8 controls | 9 steps |

## 🔧 **Configuration**

### Environment Variables
```bash
# Optional: Supabase Configuration
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key

# Optional: AI Endpoint
VITE_AI_ENDPOINT=your_ai_endpoint
VITE_AI_API_KEY=your_ai_api_key
```

### Company Profile
- Company name, address, and contact information
- Logo upload and branding
- Custom PDF templates
- Safety officer details

## 📱 **PWA Features**

### Installation
- **Chrome/Edge:** Click install button in address bar
- **Safari:** Add to home screen from share menu
- **Mobile:** Install prompt appears automatically

### Offline Capabilities
- Full offline functionality
- Service worker caching
- Local data storage
- Background sync when online

## 🏗️ **Project Structure**

```
garage-risk/
├── src/
│   ├── components/          # React components
│   │   ├── TaskPicker.jsx   # AI-powered task selection
│   │   ├── RiskForm.jsx     # Main RAMS form
│   │   ├── AssessmentsList.jsx # Assessment management
│   │   ├── Settings.jsx     # App configuration
│   │   └── CompanySettings.jsx # Company branding
│   ├── lib/                 # Utility libraries
│   │   ├── ai.js           # AI suggestion system
│   │   ├── storage.js      # Local data management
│   │   ├── pdf.js          # PDF generation
│   │   ├── cloud.js        # Supabase integration
│   │   └── branding.js     # Company profile management
│   └── styles.css          # Global styles
├── public/                  # Static assets
│   ├── manifest.webmanifest # PWA manifest
│   ├── sw.js               # Service worker
│   └── icons/              # PWA icons
├── supabase/               # Database schema
└── .github/                # CI/CD workflows
```

## 🚀 **Available Scripts**

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## 🔒 **Security Features**

- **Row Level Security (RLS)** in Supabase
- **User authentication** and authorization
- **Data encryption** at rest and in transit
- **Secure API endpoints** with proper validation
- **Audit logging** for compliance

## 📊 **Risk Model**

### Risk Matrix
| Severity/Likelihood | 1 (Low) | 2 (Medium) | 3 (High) |
|---------------------|----------|-------------|-----------|
| **1 (Low)** | 1 - LOW | 2 - LOW | 3 - MEDIUM |
| **2 (Medium)** | 2 - LOW | 4 - MEDIUM | 6 - HIGH |
| **3 (High)** | 3 - MEDIUM | 6 - HIGH | 9 - HIGH |

### Risk Categories
- **LOW (1-3):** Acceptable risk, proceed with caution
- **MEDIUM (4-6):** Moderate risk, implement controls
- **HIGH (7-9):** High risk, review and improve controls

## 🌐 **Browser Support**

- **Chrome/Edge:** Full support (PWA features)
- **Firefox:** Full support (PWA features)
- **Safari:** Full support (PWA features)
- **Mobile Browsers:** Full support with PWA installation

## 🚀 **Deployment**

### Static Hosting
- Netlify, Vercel, or GitHub Pages
- CDN for global performance
- Automatic HTTPS

### Cloud Deployment
- Supabase for backend services
- Vercel for frontend hosting
- GitHub Actions for CI/CD

## 🎨 **Customization**

### Themes
- Dark theme (default)
- Customizable color schemes
- Responsive design for all devices

### Branding
- Company logo and colors
- Custom PDF templates
- Personalized safety information

## 🔧 **Troubleshooting**

### Common Issues
1. **PWA not installing:** Check browser support and HTTPS
2. **Offline not working:** Clear browser cache and reinstall
3. **PDF export fails:** Check browser compatibility
4. **Sync issues:** Verify Supabase configuration

### Support
- Check the troubleshooting guide
- Review browser console for errors
- Verify environment configuration
- Check network connectivity

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 **License**

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 **Support**

- **Documentation:** Comprehensive guides and tutorials
- **Issues:** GitHub issue tracker
- **Community:** User forums and discussions
- **Email:** Direct support contact

## 🗺️ **Roadmap**

### Version 1.1 (Next Month)
- Enhanced mobile experience
- Additional activity templates
- Improved AI suggestions

### Version 1.2 (3 Months)
- Team collaboration features
- Advanced analytics dashboard
- API endpoints for integration

### Version 2.0 (6 Months)
- Machine learning enhancements
- Advanced reporting system
- Third-party integrations

---

**Built with ❤️ for garage safety professionals**

*The Garage RAMS App makes safety management simple, intelligent, and accessible to everyone.*
