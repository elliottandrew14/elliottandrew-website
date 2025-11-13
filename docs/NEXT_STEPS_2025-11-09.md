# Website Development - Next Steps (2025-11-09)

**Last Updated**: 2025-11-09 after storage reorganization
**Current Location**: All files now on Google Drive (synced and accessible)

---

## 🎉 Major Update: Files Now on Google Drive!

The website has been successfully moved to Google Drive as part of the storage reorganization:

**New Location**:
```
~/Library/CloudStorage/GoogleDrive-bigeandrew@gmail.com/My Drive/Operating/Systems/Creative Practice System/elliottandrew-website/
```

**Old Location** (now deleted):
```
/Volumes/2025/SynologyDrive/Operating/elliottandrew-website/
```

All files are intact and synced to cloud ✅

---

## ⚙️ Before You Can Continue Development

### 1. Start Backend Server

```bash
cd "$HOME/Library/CloudStorage/GoogleDrive-bigeandrew@gmail.com/My Drive/Operating/Systems/Creative Practice System/elliottandrew-website/backend"

# Install dependencies (if not done)
npm install

# Create .env file if missing
cp .env.example .env

# Start server
npm run dev
```

**Expected output**: "✅ MongoDB Connected" and "Server running on port 3001" (or 5000 depending on .env)

**Troubleshooting**:
- If port is in use: `lsof -ti:5000 | xargs kill -9`
- If MongoDB connection fails: Check .env has valid MONGODB_URI

### 2. Start Frontend Server

**Open a NEW terminal window** (keep backend running):

```bash
cd "$HOME/Library/CloudStorage/GoogleDrive-bigeandrew@gmail.com/My Drive/Operating/Systems/Creative Practice System/elliottandrew-website/frontend"

# Install dependencies (if not done)
npm install

# Start Next.js server
npm run dev
```

**Expected output**: "Ready on http://localhost:3000"

### 3. Open Website

Navigate to: **http://localhost:3000**

You should see the filter page with hamburger menu, search, and view mode options.

---

## 📋 Current Status (60% Complete)

### ✅ What's Working

**Backend (Express + MongoDB)**:
- MongoDB Atlas connection
- Full REST API with 6 endpoints
- Creation schema with all metadata
- Media file serving

**Frontend (Next.js 14 + TypeScript)**:
- Filter page with expandable categories (Year, Medium, Type, Tags, etc.)
- Results page with grid view + thumbnails
- Navigation menu (hamburger)
- ABC Diatype font loaded
- Archive.org aesthetic

### ⏳ Next Priority: Individual Work Pages

**HIGH PRIORITY** - Build `/work/[id]` pages:

The next task is to create individual work detail pages. Currently the results grid links to `/work/E-00037` etc., but those pages just show "TODO".

**What needs to be built**:

1. **Full media display**
   - All images in a gallery
   - Video player for videos
   - Responsive layout

2. **Metadata section**
   - Title, year, medium
   - Tags
   - Locations (created/captured/added)
   - Dimensions/duration

3. **Connected works section**
   - Show related works
   - Use `/api/creations/connections/:id` endpoint

4. **Navigation**
   - Back to results
   - Previous/Next work navigation

---

## 🏗️ How to Build Individual Work Page

### Step 1: Read Current Page File

The page file already exists but is just a placeholder:
```
frontend/app/work/[id]/page.tsx
```

### Step 2: Create Component Structure

Create a new component: `frontend/components/WorkDetail.tsx`

This should:
- Fetch work data using `/api/creations/:id`
- Display all images/videos
- Show all metadata
- Fetch and display connected works

### Step 3: Update page.tsx

Import and use the WorkDetail component in `app/work/[id]/page.tsx`

### Step 4: Style to Match Design

- Use ABC Diatype font
- Archive.org minimal aesthetic
- Red accent color (#d2442e) for interactive elements
- 11px font for UI, 10px for metadata

---

## 📚 Reference Files to Read

Before starting, read these files to understand the current implementation:

1. **frontend/app/results/page.tsx** - See how results page fetches and displays data
2. **frontend/components/FilterPage.tsx** - See component structure and styling patterns
3. **frontend/lib/api.ts** - See API client functions
4. **backend/routes/creations.js** - See API endpoints available

---

## 🔧 API Endpoints Available

```typescript
// Get single work
GET /api/creations/:id
// Returns: { entity_id, title, year, medium, tags, images, videos, ... }

// Get connected works
GET /api/creations/connections/:id
// Returns: Array of connected works

// Serve media files
GET /api/media?path=/Volumes/2025/Creations/E-00037/...
// Returns: Image or video file
```

---

## 💡 Design Patterns to Follow

### 1. Inline Styles for Conditional Colors

Tailwind conditional classes don't work reliably. Use inline styles:

```typescript
<div style={{
  border: selected ? '1px solid #d2442e' : '1px solid #ccc',
  color: selected ? '#d2442e' : '#666'
}}>
```

### 2. ABC Diatype Font Classes

```typescript
className="font-abc-diatype-regular text-[11px]"  // UI elements
className="font-abc-diatype-medium text-[10px]"   // Metadata
className="font-abc-diatype-bold text-[24px]"     // Large text
```

### 3. Image Thumbnail Logic

First image in `images[]` array is the thumbnail:

```typescript
const thumbnail = creation.images?.[0] || null;
const thumbnailUrl = thumbnail
  ? `/api/media?path=${encodeURIComponent(thumbnail)}`
  : '/placeholder.png';
```

---

## 🎯 Acceptance Criteria for Individual Work Page

When complete, the page should:

- ✅ Display work entity ID (E-#####)
- ✅ Show title (or "Untitled")
- ✅ Display year and medium
- ✅ Show all tags
- ✅ Display all location fields
- ✅ Show all images in a gallery
- ✅ Play videos if present
- ✅ Display connected works section
- ✅ Have back to results button
- ✅ Match Archive.org aesthetic
- ✅ Use ABC Diatype font throughout

---

## 📊 Project Progress

**Session 1 (Complete)**: Backend + Sync Tool
**Session 2 (60% Complete)**: Filter + Results pages
**Session 3 (Next)**: Individual work pages ← **YOU ARE HERE**
**Session 4 (Future)**: View modes, search, about pages

---

## 🚀 Quick Start Command

To immediately continue development:

```bash
# Terminal 1 - Backend
cd "$HOME/Library/CloudStorage/GoogleDrive-bigeandrew@gmail.com/My Drive/Operating/Systems/Creative Practice System/elliottandrew-website/backend"
npm run dev

# Terminal 2 - Frontend
cd "$HOME/Library/CloudStorage/GoogleDrive-bigeandrew@gmail.com/My Drive/Operating/Systems/Creative Practice System/elliottandrew-website/frontend"
npm run dev

# Browser
open http://localhost:3000
```

Then say to Claude: "Let's build the individual work detail page"

---

**All files are on Google Drive and ready to use. The reorganization is complete. Let's continue building! 🎨**
