# 🌱 FarmFlow – Smart Farm Management Platform

A modern, full-stack farm management application combining a **Django REST API backend** with a **React Native cross-platform frontend**. Designed to help farmers efficiently track, manage, and analyze their farmland with precision tools for boundary mapping, crop monitoring, and data-driven insights.

---

## 🎯 Project Vision

**FarmFlow** empowers farmers to:

- **Map & Monitor**: Capture field boundaries and reference points using phone cameras with GPS
- **Track Activities**: Log planting, fertilizing, harvesting, and other farm operations
- **Analyze Data**: Get instant area calculations, crop yield tracking, and seasonal comparisons
- **Make Decisions**: Access weather forecasts, crop recommendations, and activity reminders
- **Collaborate**: Manage multi-farm operations with team roles and permissions

---

## ✅ Current Implementation Status

### Backend (Django REST Framework)

- ✅ User authentication with JWT tokens (`rest_framework_simplejwt`)
- ✅ Custom user model with email-based login
- ✅ Farm CRUD operations with crop type and yield tracking
- ✅ FarmPoint model for boundary and reference points
- ✅ Activity history logging (`FarmHistory` model)
- ✅ EXIF GPS extraction from uploaded images
- ✅ Geodesic-based area calculation (m², hectares, acres)
- ✅ PostgreSQL database with Docker Compose
- ✅ Nginx reverse proxy for API routing
- ✅ User data isolation (farms/points scoped to authenticated user)

### Frontend (React Native + Expo)

- ✅ Login/Registration screens with error handling
- ✅ Farm creation and selection
- ✅ Image capture with gallery picker integration
- ✅ Farm capture screen with boundary/reference point toggle
- ✅ Queue-based offline image storage (partial implementation)
- ✅ Farm summary view with activity feed
- ✅ Map components (web and native views)
- ✅ AsyncStorage for JWT token persistence
- ✅ Cross-platform support (iOS, Android, Web)

### Infrastructure

- ✅ Docker Compose setup with PostgreSQL, Django, Nginx
- ✅ Hot-reload development environment
- ✅ Ngrok tunneling for mobile testing

---

## 📋 Current Limitations & Known Issues

| Issue                                                                        | Impact | Priority |
| ---------------------------------------------------------------------------- | ------ | -------- |
| **EXIF-Only GPS**: Image upload fails if photo lacks GPS metadata            | Medium | High     |
| **No Image Storage**: Points created but photo files not persisted           | Medium | High     |
| **Security**: `ALLOWED_HOSTS = "*"`, hardcoded secrets, no CORS restrictions | High   | High     |
| **Offline Mode**: Queue system incomplete, sync not fully implemented        | Medium | Medium   |
| **UX Polish**: Basic UI, no loading states, limited error messaging          | Low    | Medium   |
| **Manual Points**: Can't create points without image capture                 | Medium | Medium   |
| **No Weather Data**: No weather integration or forecasting                   | Low    | Low      |
| **Permissions**: No team/role-based access control                           | Medium | Low      |

---

## 🚀 Technology Stack

### Backend

- **Framework**: Django 6.0.3 + Django REST Framework
- **Authentication**: djangorestframework-simplejwt (JWT)
- **Database**: PostgreSQL (Docker)
- **Geospatial**: Shapely, Geopy, Pillow (EXIF)
- **CORS**: django-cors-headers

### Frontend

- **Framework**: React Native + Expo
- **Navigation**: Expo Router (file-based routing)
- **Storage**: React Native AsyncStorage
- **Maps**: Expo Maps components
- **Media**: Expo ImagePicker, Expo Location
- **State**: React hooks + AsyncStorage

### Infrastructure

- **Containerization**: Docker Compose
- **Web Server**: Nginx
- **Dev Tools**: Expo CLI, Ngrok tunneling

---

## 🎯 Phase 1: Core Stability (Foundation) – **HIGH PRIORITY**

### Authentication & Security

- [ ] Move `SECRET_KEY` to environment variable (`.env`)
- [ ] Add `ENVIRONMENT` flag (dev/staging/production) in settings
- [ ] Restrict `ALLOWED_HOSTS` to specific domains in prod
- [ ] Restrict `CORS_ALLOWED_ORIGINS` (only client domains)
- [ ] Add HTTPS requirement in production settings
- [ ] Implement JWT token refresh strategy on frontend
- [ ] Add logout endpoint to clear tokens server-side
- [ ] Add rate limiting on auth endpoints (Django Ratelimit)

### Data Validation & Error Handling

- [ ] Add comprehensive input validation on Farm/FarmPoint serializers
- [ ] Validate coordinate ranges (latitude: -90 to 90, longitude: -180 to 180)
- [ ] Add minimum point count (≥3) validation before area calculation
- [ ] Improve error messages (user-friendly responses)
- [ ] Add field-level error details in API responses
- [ ] Handle missing/invalid EXIF data gracefully (allow manual fallback)
- [ ] Add backend logging (Django logging + error tracking)

### Backend Improvements

- [ ] Add `updated_at` timestamp to Farm and FarmPoint models
- [ ] Add Point deletion protection (confirm before delete)
- [ ] Add Farm deletion protection (soft delete or archive)
- [ ] Implement proper pagination on list endpoints
- [ ] Add search/filter on Farm list (by name, crop type)
- [ ] Add test suite (pytest + pytest-django)
- [ ] Add API documentation (Swagger/DRF Spectacular or Postman)

### Frontend Improvements

- [ ] Add global error boundary component
- [ ] Implement consistent error toast/alert messaging
- [ ] Add loading spinners on all API calls
- [ ] Add retry logic with exponential backoff on network failures
- [ ] Sanitize and validate all user inputs (forms)
- [ ] Add confirmation dialogs before destructive actions
- [ ] Add logout confirmation
- [ ] Improve auth error messages (distinguish between network, auth, validation errors)

---

## 🎨 Phase 2: User Experience & Offline Capability – **HIGH PRIORITY**

### Image & Media Management

- [ ] Create Media/Photo model with persistent ImageField storage
- [ ] Save uploaded images to disk/cloud (AWS S3, Azure Blob, or local storage)
- [ ] Implement image thumbnails for gallery preview
- [ ] Add image URL to FarmPoint serializer (reference to stored photo)
- [ ] Support manual coordinate input as fallback when EXIF fails
- [ ] Add image metadata display (timestamp, file size, EXIF data dump)
- [ ] Add ability to re-upload or replace farm point images

### Offline-First Functionality

- [ ] **Complete queue implementation**: Queue images locally when offline
- [ ] Add connection state detection (NetInfo library)
- [ ] Add visual indicator of sync status ("Syncing..." / "Offline")
- [ ] Implement automatic sync when connection is restored
- [ ] Persist queue to local database (SQLite or Realm)
- [ ] Add retry mechanism for failed uploads
- [ ] Add ability to manually trigger sync
- [ ] Show pending/synced status for each point
- [ ] Add local cache expiration and cleanup

### Map & Spatial UI

- [ ] Implement interactive map view with polygon drawing
- [ ] Add point markers on map (drag to move, tap to select)
- [ ] Add boundary polygon visualization (highlighted/color-coded)
- [ ] Add manual polygon creation (tap to add points, double-tap to complete)
- [ ] Add polygon editing (move, remove, reorder vertices)
- [ ] Add GeoJSON export/import for sharing farm boundaries
- [ ] Add map layer controls (satellite, road, hybrid views)
- [ ] Center map on user location on open
- [ ] Add zoom controls and fit-to-bounds

### UI/UX Polish

- [ ] Add loading states to all buttons
- [ ] Add success toast notifications ("Point added!", "Farm created!")
- [ ] Improve form layouts (better spacing, clear labels)
- [ ] Add form validation hints (character limits, required fields)
- [ ] Add pull-to-refresh on farm/point lists
- [ ] Add empty state messaging ("No farms yet. Create one to start!")
- [ ] Add navigation breadcrumbs or clear back buttons
- [ ] Style consistency (colors, fonts, spacing across all screens)
- [ ] Dark mode support (optional)
- [ ] Responsive layout for different screen sizes

### Activity & History

- [ ] Add activity timeline view (visual chronological display)
- [ ] Add filters for activity type (Planting, Spraying, Harvest, etc.)
- [ ] Add date range picker for filtering activities
- [ ] Add photos to activity entries (reference captured images)
- [ ] Add ability to edit activity description
- [ ] Add activity deletion with confirmation
- [ ] Show activity statistics (total count, most recent)

---

## 📊 Phase 3: Advanced Features & Intelligence – **MEDIUM PRIORITY**

### Dashboard & Analytics

- [ ] Create farm dashboard/summary screen showing:
  - [ ] Total farm area (m², hectares, acres)
  - [ ] Point count
  - [ ] Crop type and expected yield
  - [ ] Recent activities (last 10)
  - [ ] Area trend (if multiple seasons)
- [ ] Add farm-level statistics (date range picker)
- [ ] Add comparison tools (farm vs farm, season vs season)
- [ ] Add export to PDF/CSV with formatted report
- [ ] Add data visualization (charts for yield, area trends, activity frequency)

### Weather Integration

- [ ] Integrate OpenWeather or WeatherAPI for farm location
- [ ] Display current weather (temp, humidity, rain, wind)
- [ ] Add weather forecast (next 5-7 days)
- [ ] Add severe weather alerts
- [ ] Cache weather data with TTL
- [ ] Add weather history per farm

### Crop Intelligence

- [ ] Add crop recommendation engine based on location/climate
- [ ] Add planting/harvesting calendar for selected crop
- [ ] Add fertilizer recommendations and schedule alerts
- [ ] Add pest/disease warnings based on weather and crop
- [ ] Add yield estimation based on historical data
- [ ] Add water requirement calculations
- [ ] Link to external crop databases (optional)

### Notifications & Reminders

- [ ] Add notification permission request on app start
- [ ] Implement local push notifications for:
  - [ ] Activity reminders (planting, spraying dates)
  - [ ] Weather alerts
  - [ ] Seasonal task reminders
- [ ] Add notification settings (enable/disable, frequency)
- [ ] Add in-app notification center

### Notes & Documentation

- [ ] Add notes field to each Activity entry
- [ ] Add photos gallery per farm (all captured images)
- [ ] Add document attachment support (PDF, spreadsheets)
- [ ] Add farm details page (size details, contact info, history)
- [ ] Add print-friendly views for reports

---

## 🔐 Phase 4: Production Readiness & Scaling – **MEDIUM PRIORITY**

### Backend Hardening

- [ ] Add API versioning (v1/ prefix on endpoints)
- [ ] Add comprehensive request logging and monitoring
- [ ] Implement database query optimization and indexing
- [ ] Add caching layer (Redis) for frequently accessed data
- [ ] Add user action audit logs
- [ ] Add data backup strategy
- [ ] Add health check endpoints
- [ ] Add API rate limiting (per user, per endpoint)
- [ ] Implement proper exception handling and logging
- [ ] Add database connection pooling

### Frontend Deployment

- [ ] Build for production (Expo managed or EAS Build)
- [ ] Set up EAS Submit for App Store and Google Play
- [ ] Configure app signing certificates
- [ ] Create app store listings (screenshots, descriptions)
- [ ] Set up crash reporting (Sentry or Firebase Crashlytics)
- [ ] Add analytics (Firebase Analytics, Mixpanel, or custom)
- [ ] Create privacy policy and terms of service
- [ ] Add in-app versioning and update strategy

### Server Infrastructure

- [ ] Set up production database with backups
- [ ] Configure SSL/TLS certificate (Let's Encrypt via Docker)
- [ ] Set up environment-based deployment (dev, staging, prod)
- [ ] Implement CI/CD pipeline (GitHub Actions, GitLab CI)
- [ ] Add database migration strategy
- [ ] Set up log aggregation (ELK, Datadog, or cloud logs)
- [ ] Configure CDN for static/media files (AWS CloudFront, Cloudflare)
- [ ] Add monitoring and alerting (uptime, errors, performance)
- [ ] Create runbooks for common operations
- [ ] Set up disaster recovery plan

### Team & Collaboration Features

- [ ] Add multi-farm management per user
- [ ] Implement role-based access control (Admin, Manager, Worker)
- [ ] Add team invitation workflow (email invites)
- [ ] Add user activity log (who did what and when)
- [ ] Add shared farm access (read-only, edit)
- [ ] Add farm-level permissions (view, edit, delete)
- [ ] Add team messaging or commenting on activities

### Code Quality & Testing

- [ ] Add backend test suite (target 80%+ coverage)
- [ ] Add frontend component tests (React Native Testing Library)
- [ ] Add integration tests (API + DB)
- [ ] Add E2E tests (critical user journeys)
- [ ] Set up pre-commit hooks (linting, formatting)
- [ ] Add code style guidelines (Black for Python, Prettier for JS)
- [ ] Add static analysis (ESLint, Mypy, Pylint)
- [ ] Set up automated testing on pull requests

---

## 📱 Phase 5: Post-Launch Enhancements – **LOW PRIORITY**

### Mobile-Specific Features

- [ ] Implement biometric authentication (fingerprint, face)
- [ ] Add home screen widgets (quick farm summary)
- [ ] Add share farm summary to social media
- [ ] Add Apple Watch companion app
- [ ] Add voice-based activity logging

### Data Import/Export

- [ ] Add KML/GeoJSON import for existing farm boundaries
- [ ] Add bulk data import (CSV for multiple farms)
- [ ] Add integration with mapping services (Google Maps, Mapbox)
- [ ] Add sync with external farm management systems

### AI & Machine Learning

- [ ] Add crop disease detection from photos (ML model)
- [ ] Add automated land classification from aerial imagery
- [ ] Add predictive models for yield forecasting
- [ ] Add anomaly detection for unusual activity patterns

---

## 🏃 Quick Start Guide

### Prerequisites

- Docker & Docker Compose
- Node.js 18+
- Python 3.10+
- Expo CLI (`npm install -g expo-cli`)

### Backend Setup

```bash
cd c:\Users\elvis\Desktop\Projects\image_backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend Setup (Local Native)

```bash
cd frontend
npm install
npm run start  # Launches Expo dev tools
# Press 'a' for Android emulator or 'i' for iOS simulator
```

### Docker Compose (Full Stack)

```bash
docker-compose up --build
# Backend: http://localhost:8000
# Frontend: http://localhost:8081
# Database: localhost:5111
```

---

## 📂 Project Structure

```
image_backend/
├── backend/              # Django settings & WSGI config
├── image/                # Farm app (models, views, serializers)
│   ├── models.py         # Farm, FarmPoint, FarmHistory
│   ├── views.py          # FarmViewSet, FarmPointViewSet
│   ├── serializers.py    # API serializers
│   ├── services/         # Business logic
│   │   ├── image.py      # EXIF GPS extraction
│   │   └── area.py       # Geodesic area calculation
│   └── migrations/       # Database migrations
├── user/                 # User auth app
│   ├── models.py         # Custom User model
│   └── views.py          # Auth endpoints
├── frontend/             # React Native with Expo
│   ├── app/              # Screens & routing
│   ├── components/       # Reusable UI components
│   ├── services/         # API clients & helpers
│   └── constant/         # Colors, constants
├── docker-compose.yml    # Docker services
├── Dockerfile            # Django image
├── nginx.conf            # Reverse proxy config
└── manage.py             # Django CLI
```

---

## 🔑 Key API Endpoints

| Method           | Endpoint                        | Description                 |
| ---------------- | ------------------------------- | --------------------------- |
| POST             | `/api/auth/register/`           | Register new user           |
| POST             | `/api/auth/login/`              | Login, get JWT              |
| GET/POST         | `/api/farms/`                   | List/create farms           |
| GET              | `/api/farms/{id}/summary/`      | Full farm summary           |
| GET              | `/api/farms/{id}/area/`         | Calculate farm area         |
| POST             | `/api/farms/{id}/add_activity/` | Log farm activity           |
| POST             | `/api/farm-points/`             | Upload image & create point |
| GET/PATCH/DELETE | `/api/farm-points/{id}/`        | Manage points               |

---

## 🎯 Success Metrics (By Phase)

**Phase 1 Complete**: Secure, stable API with validated inputs; confident mobile experience  
**Phase 2 Complete**: Users can map farms offline, sync seamlessly; delightful UX  
**Phase 3 Complete**: Intelligent recommendations; users make data-driven farming decisions  
**Phase 4 Complete**: Production-ready; millions of users at scale  
**Phase 5 Complete**: Industry-leading farm management platform

---

## 📝 Development Notes

- **Secrets**: Create a `.env` file (add to `.gitignore`):

  ```
  DEBUG=True
  SECRET_KEY=your-secret-here
  DATABASE_URL=postgres://user:pass@localhost:5432/image
  ALLOWED_HOSTS=localhost,127.0.0.1
  ```

- **Database**: Migrations auto-run in Docker. Locally: `python manage.py migrate`

- **Frontend Routes**: Defined in `frontend/app/` using Expo Router file-based routing

- **Image Storage**: Currently in-memory only. Phase 2 will add persistent storage.

---

## 🤝 Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Commit changes: `git commit -am 'Add feature'`
3. Push to GitHub and create a PR
4. Ensure tests pass and code is formatted

---

## 📄 License

MIT License – Free to use and modify.

---

**Built with ❤️ for farmers. Let's make FarmFlow the #1 farm management platform.** 🌾
