# Elliott Andrew Website - Project Status

**Last Updated**: 2025-11-06
**Current Status**: Filter page and results page complete and functional

## Quick Start

### Start Development Servers

```bash
# Terminal 1 - Backend API (MongoDB + Express)
cd /Volumes/2025/SynologyDrive/Operating/elliottandrew-website/backend
npm run dev
# Runs on: http://localhost:3001

# Terminal 2 - Frontend (Next.js)
cd /Volumes/2025/SynologyDrive/Operating/elliottandrew-website/frontend
npm run dev
# Runs on: http://localhost:3000
```

### View Website
Open browser to: **http://localhost:3000**

## Project Structure

```
elliottandrew-website/
├── backend/                    # Express + MongoDB API
│   ├── models/
│   │   └── Creation.js        # MongoDB schema for artworks
│   ├── routes/
│   │   └── creations.js       # API endpoints (/api/creations)
│   ├── server.js              # Express server + MongoDB connection
│   └── package.json
│
└── frontend/                   # Next.js 14 + TypeScript
    ├── app/
    │   ├── layout.tsx         # Global layout with copyright
    │   ├── globals.css        # ABC Diatype font + Tailwind
    │   ├── page.tsx           # Home (redirects to /filter)
    │   ├── filter/
    │   │   └── page.tsx       # Main filter page (uses FilterPage component)
    │   ├── results/
    │   │   └── page.tsx       # Results grid view
    │   └── work/
    │       └── [id]/
    │           └── page.tsx   # Individual work pages (TODO)
    ├── components/
    │   └── FilterPage.tsx     # Main filter interface component
    ├── lib/
    │   ├── types.ts           # TypeScript interfaces
    │   └── api.ts             # API client functions
    └── public/
        └── fonts/             # ABC Diatype font files
```

## What's Complete

### Backend (MongoDB + Express)
- ✅ MongoDB Atlas connection configured
- ✅ Creation schema with all metadata fields
- ✅ API endpoints:
  - `GET /api/creations` - Get all works
  - `GET /api/creations/filter` - Filter by year/medium/type/tags
  - `GET /api/creations/:id` - Get single work
  - `GET /api/creations/connections/:id` - Get connected works
  - `GET /api/stats` - Collection statistics
  - `GET /api/media?path=...` - Serve media files
- ✅ Data imported (E-00037 and other test creations)

### Frontend Features
- ✅ **Filter Page** (`/filter`)
  - Hamburger menu (≡) top left with navigation
  - Search button (⌕) and help (?) top right
  - Expandable filter categories: Year, Medium, Type, Tags, Locations, Connections
  - Selected filters shown as red-bordered chips
  - View mode selection: Grid, Slideshow, Timeline, Graph, Map (text labels)
  - Arrow (→) button to navigate to results
  - ABC Diatype font throughout

- ✅ **Results Page** (`/results`)
  - Selected filters displayed on left side
  - View mode buttons on right side
  - Back to filters link
  - Grid view with thumbnails (5 columns)
  - 25 items per page with pagination
  - Hover effects showing work metadata
  - Links to individual work pages

- ✅ **Global Layout**
  - Copyright "© 2025 Elliott Andrew" fixed bottom-right
  - No persistent navigation (only on filter/results pages)
  - Clean, minimal aesthetic

### Design System
- ✅ ABC Diatype font (Regular, Medium, Bold + Italics)
- ✅ Color scheme:
  - Accent red: #d2442e (selected items)
  - Gray: #666 (inactive elements)
  - Background: #f5f5f5 (cards)
- ✅ Typography:
  - 11px for UI elements
  - 10px for metadata
  - 24px for arrow button
- ✅ Archive.org inspired minimal aesthetic

## What's NOT Complete (TODO)

### High Priority
1. **Individual Work Pages** (`/work/[id]`)
   - Full work details
   - All images/videos
   - Metadata display
   - Connected works section

2. **View Modes** (currently placeholders)
   - Slideshow view
   - Timeline view
   - Graph view (network visualization)
   - Map view (geographic)

3. **Search Functionality**
   - Currently just a button placeholder
   - Needs search bar + API integration

### Medium Priority
4. **Video Thumbnail Generation**
   - Install FFmpeg on server
   - Generate thumbnails from video files
   - E-00037 currently has no thumbnail

5. **Upload Flow**
   - Admin interface to add new works
   - Thumbnail selection for new uploads

6. **About/News/Email Pages**
   - Linked from hamburger menu
   - Not yet created

### Low Priority
7. **Mobile Responsive Design**
   - Currently desktop-focused
   - Needs mobile optimization

8. **Performance Optimization**
   - Image lazy loading
   - API caching
   - Bundle size optimization

## Known Issues & Technical Notes

### Critical Technical Fixes Applied
1. **Inline Styles Required**: Tailwind conditional classes don't work reliably for borders/colors. Use inline style objects:
   ```typescript
   style={{ border: '1px solid #d2442e', color: '#d2442e' }}
   ```

2. **Backend Route Order**: `/filter` route MUST come before `/:id` route in `backend/routes/creations.js` (lines 40 vs 245)

3. **Filter API Format**: Backend expects comma-separated values:
   ```
   /api/creations/filter?year=2024,2025&medium=video,photography
   ```

4. **Thumbnail Logic**: First image in `images[]` array used as thumbnail:
   ```typescript
   const thumbnail = creation.images?.[0] || null;
   ```

### Environment Variables
**Backend** (`backend/.env`):
```
MONGODB_URI=mongodb+srv://[credentials]
PORT=3001
MEDIA_BASE_PATH=/Volumes/2025
```

**Frontend** (`frontend/.env.local`):
```
NEXT_PUBLIC_API_URL=http://localhost:3001/api
```

## Data Model

### Creation Schema (MongoDB)
```typescript
{
  entity_id: string;           // e.g., "E-00037"
  type: 'object' | 'arrangement';
  title?: string;
  year: number;
  medium: string;              // e.g., "video", "photography", "mixed"
  tags: string[];
  location_created?: string;
  location_captured?: string;
  location_added?: string;
  images: string[];            // File paths
  videos: string[];            // File paths
  outgoing_connections: string[];  // Other entity_ids
  published: boolean;
  created_at: Date;
  updated_at: Date;
}
```

## Common Commands

### Check Running Servers
```bash
# Check if backend is running
curl http://localhost:3001/api/creations

# Check if frontend is running
open http://localhost:3000
```

### Database Operations
```bash
# Connect to MongoDB via mongosh (if needed)
mongosh "mongodb+srv://cluster0.xxxxx.mongodb.net/" --username elliott

# View all creations
use elliott_andrew
db.creations.find({ published: true })
```

### Development Workflow
```bash
# Make changes to frontend
cd /Volumes/2025/SynologyDrive/Operating/elliottandrew-website/frontend
# Edit files in app/ or components/
# Hot reload will update automatically

# Make changes to backend
cd /Volumes/2025/SynologyDrive/Operating/elliottandrew-website/backend
# Edit files in routes/ or models/
# Server will restart automatically (nodemon)
```

## API Endpoints Reference

### GET /api/creations
Get all published works
```bash
curl "http://localhost:3001/api/creations?page=1&limit=25&sort=-year"
```

### GET /api/creations/filter
Filter works by criteria
```bash
curl "http://localhost:3001/api/creations/filter?year=2025&medium=video"
```

### GET /api/creations/:id
Get single work
```bash
curl "http://localhost:3001/api/creations/E-00037"
```

### GET /api/stats
Get collection statistics
```bash
curl "http://localhost:3001/api/stats"
```

### GET /api/media
Serve media files
```bash
curl "http://localhost:3001/api/media?path=/path/to/image.jpg"
```

## Recent Changes (Session 2)

### Last Completed Task
Made view mode text labels (GRID, SLIDESHOW, TIMELINE, GRAPH, MAP) less bold by removing `font-semibold` class. They now appear lighter than filter category headers (YEAR, MEDIUM, TYPE).

### Previous Session Fixes
- Moved hamburger menu to top left
- Fixed arrow button visibility using inline styles
- Fixed filter chips not showing borders (inline styles)
- Fixed backend route order for filter API
- Fixed filter parameter format (comma-separated)
- Moved selected filters to left side of results page
- Replaced view mode symbol buttons with text labels
- Added copyright to bottom-right corner

## Contact & Support

**Developer**: Claude (Anthropic)
**Project Owner**: Elliott Andrew
**MongoDB**: Atlas Cluster (cluster0)
**Hosting**: TBD (currently local development)

## Next Session Checklist

When you return to development:

1. ✅ Start both servers (backend + frontend)
2. ✅ Test filter page at http://localhost:3000
3. ✅ Test results page by selecting filters
4. ⬜ Decide next feature to implement (see TODO list above)
5. ⬜ Consider deploying to production (Vercel for frontend, Railway/Render for backend)

---

**Note**: All development is currently local. No production deployment yet. Data is stored in MongoDB Atlas cloud database, but API and frontend run on localhost.
