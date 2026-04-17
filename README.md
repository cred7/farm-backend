# � SmartFarm AI – Intelligent Farm Management Platform

A comprehensive farm management solution combining **Django REST API**, **React Native mobile app**, and **AI-powered image analysis** for precision agriculture. Capture farm boundaries via GPS-enabled photos, track activities, and get AI insights on crop health and pest detection.

---

## 🎯 What SmartFarm AI Does

**SmartFarm AI** revolutionizes farm management by:

- **📸 Visual Farm Mapping**: Capture field boundaries and reference points using your phone's camera with automatic GPS extraction
- **🤖 AI-Powered Analysis**: Get instant crop health analysis, pest detection, and treatment recommendations from uploaded images
- **📊 Activity Tracking**: Log farming activities (planting, spraying, harvesting) with photos and AI insights
- **📍 Real-Time Updates**: Live synchronization across devices with WebSocket-powered notifications
- **📱 Offline-First**: Queue operations when offline, sync automatically when connection returns
- **🗺️ Interactive Maps**: Visualize farm boundaries, calculate acreage, and track GPS coordinates
- **👥 Multi-Farm Support**: Manage multiple farms with user isolation and secure data access

---

## ✅ Current Implementation Status

### Backend (Django + AI Pipeline)

- ✅ **User Authentication**: JWT-based auth with secure token management
- ✅ **Farm Management**: Full CRUD operations for farms with crop type and yield tracking
- ✅ **GPS Image Processing**: Automatic EXIF GPS extraction from uploaded photos
- ✅ **Geospatial Calculations**: Precise area calculations using geodesic algorithms (m², hectares, acres)
- ✅ **Activity Logging**: Comprehensive farm activity tracking with image uploads
- ✅ **AI/ML Pipeline**: Asynchronous image analysis with Celery workers and Redis
- ✅ **Real-Time Updates**: WebSocket integration for live farm activity notifications
- ✅ **Database**: PostgreSQL with proper indexing and user data isolation
- ✅ **API**: RESTful endpoints with Django REST Framework and comprehensive serialization

### Frontend (React Native + Expo)

- ✅ **Cross-Platform**: iOS, Android, and Web support via Expo
- ✅ **Authentication Flow**: Secure login/registration with JWT persistence
- ✅ **Farm Operations**: Create, select, and manage multiple farms
- ✅ **Image Capture**: Camera integration with GPS location services
- ✅ **Offline Queue**: Local storage system for offline operation with sync management
- ✅ **Interactive Maps**: Native map components with boundary visualization
- ✅ **Activity Management**: Log farm activities with photo uploads and AI results
- ✅ **Real-Time Sync**: WebSocket integration for live updates
- ✅ **Error Handling**: Comprehensive error boundaries and user feedback

### Infrastructure & DevOps

- ✅ **Containerization**: Full Docker Compose setup with PostgreSQL, Redis, and Nginx
- ✅ **Background Processing**: Celery workers for AI image analysis
- ✅ **WebSocket Support**: Daphne ASGI server for real-time features
- ✅ **Development Tools**: Hot-reload development environment
- ✅ **API Gateway**: Nginx reverse proxy for production-ready deployment

---

## 🚀 Key Features

### 🗺️ Smart Farm Mapping

- **GPS-Enabled Photos**: Upload images to automatically extract latitude/longitude coordinates
- **Boundary Detection**: Mark boundary points vs reference points for accurate mapping
- **Area Calculation**: Automatic calculation in multiple units (square meters, hectares, acres)
- **Geodesic Accuracy**: Uses WGS84 ellipsoid for precise geographic calculations

### 🤖 AI-Powered Insights

- **Crop Analysis**: ML models analyze uploaded images for crop health assessment
- **Pest Detection**: Automatic identification of common pests with confidence scores
- **Treatment Recommendations**: AI-generated suggestions for pest control and crop management
- **Severity Assessment**: Categorize issues as low/medium/high priority

### 📱 Real-Time Farm Management

- **Activity Logging**: Track planting, spraying, fertilizing, and harvesting activities
- **Photo Documentation**: Attach images to activities for visual records
- **Live Updates**: WebSocket notifications when AI analysis completes
- **Multi-Device Sync**: Seamless experience across phone, tablet, and web

### 🔄 Offline-First Architecture

- **Queue System**: Store operations locally when offline
- **Automatic Sync**: Background synchronization when connectivity returns
- **Retry Logic**: Intelligent retry mechanisms for failed uploads
- **Status Tracking**: Visual indicators for sync status and pending operations

---

## 🏗️ Technology Stack

### Backend Architecture

```mermaid
graph TB
    A[React Native App] --> B[REST API / WebSockets]
    B --> C[Django REST Framework]
    C --> D[PostgreSQL Database]
    C --> E[Redis Cache]
    C --> F[Celery Workers]
    F --> G[AI/ML Models]
    F --> H[WebSocket Updates]
```

### Core Technologies

| Component                | Technology                          | Purpose                        |
| ------------------------ | ----------------------------------- | ------------------------------ |
| **Backend Framework**    | Django 6.0.3 + DRF                  | REST API development           |
| **Authentication**       | JWT (djangorestframework-simplejwt) | Secure user sessions           |
| **Database**             | PostgreSQL                          | Relational data storage        |
| **Cache/Message Broker** | Redis                               | Caching & Celery broker        |
| **Background Jobs**      | Celery                              | Asynchronous AI processing     |
| **Real-Time**            | Django Channels + WebSockets        | Live updates                   |
| **Geospatial**           | Shapely + Geopy                     | GPS & area calculations        |
| **Image Processing**     | Pillow + ExifRead                   | Photo metadata extraction      |
| **Frontend**             | React Native + Expo                 | Cross-platform mobile app      |
| **Maps**                 | Expo Maps                           | Interactive farm visualization |
| **Storage**              | AsyncStorage                        | Local data persistence         |
| **Networking**           | Expo Location + ImagePicker         | GPS & camera access            |

---

## 📋 API Endpoints

| Method             | Endpoint                           | Description                     |
| ------------------ | ---------------------------------- | ------------------------------- |
| `POST`             | `/api/auth/register/`              | User registration               |
| `POST`             | `/api/auth/login/`                 | User authentication             |
| `GET/POST`         | `/api/farms/`                      | List/create farms               |
| `GET`              | `/api/farms/{id}/summary/`         | Farm details with activities    |
| `GET`              | `/api/farms/{id}/area/`            | Calculate farm area             |
| `POST`             | `/api/farms/{id}/add_activity/`    | Log farm activity with image    |
| `PATCH`            | `/api/farms/{id}/update_activity/` | Update activity details         |
| `DELETE`           | `/api/farms/{id}/delete_activity/` | Remove activity                 |
| `POST`             | `/api/farm-points/`                | Upload image & create GPS point |
| `GET/PATCH/DELETE` | `/api/farm-points/{id}/`           | Manage individual points        |
| `WS`               | `/ws/farm/{farm_id}/`              | Real-time farm updates          |

---

## 🚀 Quick Start Guide

### Prerequisites

- **Docker & Docker Compose** (for full stack)
- **Python 3.12+** (for local backend)
- **Node.js 18+** (for frontend development)
- **Expo CLI** (`npm install -g expo-cli`)

### Option 1: Full Docker Development Environment

```bash
# Clone and navigate to project
cd /path/to/smartfarm-ai

# Start all services (PostgreSQL, Redis, Django, Celery)
docker-compose up --build

# Services will be available at:
# - Backend API: http://localhost:8000
# - Database: localhost:5111
# - Redis: localhost:6379
```

### Option 2: Local Development Setup

#### Backend Setup

```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Start Django development server
python manage.py runserver
```

#### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start Expo development server
npm start

# Press 'a' for Android emulator
# Press 'i' for iOS simulator
# Press 'w' for web browser
```

### Option 3: Mobile Testing with Ngrok

```bash
# Install Ngrok for mobile testing
npm install -g ngrok

# Expose local backend to internet
ngrok http 8000

# Update ALLOWED_HOSTS in settings.py with ngrok URL
# Update CORS_ALLOWED_ORIGINS in mobile app
```

---

## 📂 Project Structure

```
smartfarm-ai/
├── backend/                    # Django project root
│   ├── settings.py            # Django configuration
│   ├── urls.py                # Main URL routing
│   ├── asgi.py               # ASGI application for WebSockets
│   └── wsgi.py               # WSGI application
├── image/                     # Main farm management app
│   ├── models.py              # Farm, FarmPoint, FarmHistory models
│   ├── views.py               # API endpoints & business logic
│   ├── serializers.py         # DRF serializers
│   ├── urls.py                # App URL patterns
│   ├── services/              # Business logic services
│   │   ├── area.py           # Geospatial calculations
│   │   └── image.py          # EXIF GPS extraction
│   ├── ml/                   # AI/ML pipeline
│   │   └── analyzer.py       # Image analysis (placeholder)
│   ├── celery/               # Background task processing
│   │   ├── tasks.py          # Celery task definitions
│   │   └── ws.py             # WebSocket utilities
│   ├── websocket/            # Real-time features
│   │   ├── consumers.py      # WebSocket consumers
│   │   └── routing.py        # WebSocket URL routing
│   └── migrations/           # Database migrations
├── user/                     # User management app
│   ├── models.py             # Custom User model
│   ├── views.py              # Auth endpoints
│   └── migrations/           # User model migrations
├── frontend/                 # React Native app
│   ├── app/                  # Expo Router screens
│   │   ├── (auth)/          # Authentication screens
│   │   ├── createFarm.tsx   # Farm creation
│   │   ├── farm.tsx         # Farm selection
│   │   ├── farmCapture.tsx  # Image capture & mapping
│   │   ├── farmSummary.tsx  # Farm dashboard
│   │   └── index.tsx        # Home screen
│   ├── components/           # Reusable UI components
│   │   ├── Map.tsx          # Map visualization
│   │   └── ...              # Other components
│   ├── services/            # API client & utilities
│   │   ├── auth.ts          # Authentication helpers
│   │   └── fetch.ts         # API client
│   └── constant/            # App constants & themes
├── media/                   # User-uploaded files
│   └── activity_images/     # Farm activity photos
├── docker-compose.yml       # Multi-service orchestration
├── Dockerfile              # Backend container config
├── nginx.conf              # Production web server
├── requirements.txt        # Python dependencies
└── manage.py               # Django CLI
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# Django Settings
DEBUG=True
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=postgres://user:pass@localhost:5432/smartfarm
ALLOWED_HOSTS=localhost,127.0.0.1,your-ngrok-url.ngrok.io

# External Services (Future)
REDIS_URL=redis://localhost:6379
OPENWEATHER_API_KEY=your-weather-api-key
```

### Database Configuration

The project uses PostgreSQL with PostGIS extension for geospatial operations:

```sql
-- Create database
CREATE DATABASE smartfarm;
CREATE USER smartfarm_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE smartfarm TO smartfarm_user;

-- Enable PostGIS (if using geospatial features)
CREATE EXTENSION postgis;
```

---

## 🤖 AI/ML Pipeline

### Current Implementation

- **Image Analysis**: Placeholder ML model for pest detection and crop health
- **Async Processing**: Celery workers handle image analysis in background
- **Real-Time Results**: WebSocket notifications when analysis completes

### Future Enhancements

```python
# Planned ML features in ml/analyzer.py
def analyze_image(image_path):
    return {
        "crop_health": 0.85,
        "detected_pests": ["aphids", "mites"],
        "severity": "medium",
        "recommendations": [
            "Apply neem oil spray",
            "Increase irrigation frequency"
        ],
        "confidence": 0.92
    }
```

### Integration Points

- **Model Training**: TensorFlow/PyTorch models for crop disease detection
- **Cloud AI**: Google Vision AI / AWS Rekognition integration
- **Offline Models**: TensorFlow Lite for on-device analysis

---

## 📱 Mobile App Features

### Core Screens

1. **Authentication**: Login/Register with JWT persistence
2. **Farm Management**: Create, select, and manage farms
3. **Image Capture**: Camera integration with GPS tagging
4. **Map Visualization**: Interactive boundary mapping
5. **Activity Logging**: Photo-based activity tracking
6. **Offline Queue**: Background sync management

### Key Components

- **Map Integration**: Native maps with polygon drawing
- **Image Processing**: EXIF data extraction and upload
- **Network Handling**: Offline queue with retry logic
- **Real-Time Updates**: WebSocket integration for live data

---

## 🔒 Security & Best Practices

### Authentication

- JWT tokens with access/refresh token pattern
- Secure password hashing with Django's auth system
- Token expiration and automatic refresh

### Data Protection

- User data isolation (users only see their own farms)
- Input validation on all API endpoints
- SQL injection prevention via Django ORM
- XSS protection with Django templates

### API Security

- CORS configuration for allowed origins
- Rate limiting (configurable)
- Request/response logging
- Environment-based security settings

---

## 🚀 Deployment

### Production Docker Setup

```yaml
# docker-compose.prod.yml
version: "3.8"
services:
  web:
    build: .
    command: gunicorn backend.wsgi:application --bind 0.0.0.0:8000
    environment:
      - DEBUG=False
      - SECRET_KEY=${SECRET_KEY}
    volumes:
      - static_files:/app/static
      - media_files:/app/media

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - static_files:/app/static
      - media_files:/app/media
```

### Environment Setup

```bash
# Production environment variables
export DEBUG=False
export SECRET_KEY="your-production-secret-key"
export DATABASE_URL="postgres://user:pass@db:5432/smartfarm"
export REDIS_URL="redis://redis:6379"
export ALLOWED_HOSTS="yourdomain.com,api.yourdomain.com"
```

---

## 🧪 Testing

### Backend Testing

```bash
# Run Django tests
python manage.py test

# Run with coverage
coverage run manage.py test
coverage report
```

### Frontend Testing

```bash
cd frontend
npm test

# E2E testing with Detox (future)
detox test
```

### API Testing

```bash
# Using HTTPie
http POST http://localhost:8000/api/auth/register/ \
  email="farmer@example.com" \
  password="securepass123"

# Using curl
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"farmer@example.com","password":"securepass123"}'
```

---

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** changes: `git commit -m 'Add amazing feature'`
4. **Push** to branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code
- Use TypeScript for React Native components
- Write tests for new features
- Update documentation for API changes
- Ensure mobile app works on iOS, Android, and Web

---

## 📈 Roadmap

### Phase 1: Core Stability ✅

- [x] Basic farm mapping and GPS capture
- [x] User authentication and data isolation
- [x] Real-time updates and offline sync
- [x] AI pipeline foundation

### Phase 2: Enhanced AI & Analytics 📊

- [ ] Advanced ML models for crop disease detection
- [ ] Weather integration and forecasting
- [ ] Yield prediction algorithms
- [ ] Historical data analysis and trends

### Phase 3: Advanced Features 🚀

- [ ] Multi-user farm collaboration
- [ ] IoT sensor integration
- [ ] Drone imagery support
- [ ] Marketplace for farm inputs/outputs

### Phase 4: Enterprise Scale 🏢

- [ ] Multi-tenant architecture
- [ ] Advanced reporting and analytics
- [ ] API for third-party integrations
- [ ] Mobile app store deployment

### Phase 5: Post-Launch Enhancements 🎯

- [ ] Biometric authentication
- [ ] Voice-based activity logging
- [ ] AI-powered yield forecasting
- [ ] Advanced anomaly detection

---

## 📞 Support & Community

- **Issues**: [GitHub Issues](https://github.com/yourusername/smartfarm-ai/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/smartfarm-ai/discussions)
- **Documentation**: [Wiki](https://github.com/yourusername/smartfarm-ai/wiki)

---

## 📄 License

**MIT License** - Free to use for personal and commercial projects.

---

## 🙏 Acknowledgments

- **Django Community** for the excellent web framework
- **React Native & Expo** for seamless cross-platform development
- **Open Source ML Libraries** for AI capabilities
- **Farmers Worldwide** for inspiring this mission to modernize agriculture

---

**Built with ❤️ for farmers, by developers who care about sustainable agriculture.** 🌱🚜
