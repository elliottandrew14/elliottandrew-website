# Elliott Andrew Creative Archive Website

Independent website for displaying creative work (E-##### creations).

**Status:** Session 2 in progress - Filter & Results pages complete!
**Next:** Individual work pages, view modes, search
**Domain:** elliottandrew.com (currently on Cargo, will migrate)

📘 **[PROJECT_STATUS.md](PROJECT_STATUS.md)** - Complete current status & technical docs

---

## Quick Links

📄 **[QUICKSTART.md](QUICKSTART.md)** - Start here! Setup guide for backend + sync
📚 **[Planning Docs](../../Systems/Creative%20Practice%20System/Website/)** - Complete planning in Google Drive
🔨 **[BUILD_PLAN.md](../../Systems/Creative%20Practice%20System/Website/BUILD_PLAN.md)** - Full 18-20 hour implementation plan
🎨 **[DESIGN_SPECIFICATIONS.md](../../Systems/Creative%20Practice%20System/Website/DESIGN_SPECIFICATIONS.md)** - Archive.org aesthetic, 5 viewing modes

---

## What This Is

An independent archive website that:
- Displays your E-##### creations from your catalog
- Updates from CSV (no AI needed after build)
- Has 5 viewing modes: Search, Grid, List, Slideshow, Standalone
- Features dynamic filtering by year, medium, tags, themes
- Runs independently forever (React + Node + MongoDB)

---

## Architecture

```
CSV Catalog                    MongoDB                    Website
───────────                    ───────                    ───────

creations_catalog.csv    →    Portfolio DB       →    elliottandrew.com
(source of truth)              (live database)          (public display)
     ↓                              ↓                         ↓
published=yes              Node.js API               React Frontend
     ↓                    (serves JSON)             (Search, Grid, etc.)
website-sync                     ↓                         ↓
(run when ready)           Vercel/AWS                   Vercel
                         (backend hosting)          (frontend hosting)
```

---

## Project Structure

```
elliottandrew-website/
├── README.md                  📄 This file
├── QUICKSTART.md              🚀 Setup guide
├── backend/                   ✅ Node.js API (Session 1)
│   ├── server.js
│   ├── routes/creations.js   # All API endpoints
│   ├── models/Creation.js    # MongoDB schema
│   └── README.md
├── sync-tool/                 ✅ CSV → MongoDB (Session 1)
│   ├── website-sync          # Main sync script
│   ├── config.py
│   └── README.md
├── frontend/                  ⏳ React site (Session 2)
│   └── (to be built)
└── docs/                      ✅ Documentation
    ├── MONGODB_SETUP.md       # MongoDB Atlas guide
    └── add-published-column.py
```

---

## Current Status

### ✅ Session 1 Complete (Backend + Sync)

**Built:**
- Complete REST API with 6 endpoints
- MongoDB integration
- Python sync tool
- Documentation

---

### 🚧 Session 2: Frontend (IN PROGRESS)

**✅ Completed:**
- Next.js 14 + TypeScript setup
- ABC Diatype font integration
- **Filter Page** (`/filter`)
  - Hamburger menu with navigation
  - Expandable filter categories (Year, Medium, Type, Tags, Locations, Connections)
  - Multi-select filtering with red-bordered chips
  - View mode selection (Grid, Slideshow, Timeline, Graph, Map)
  - Arrow button navigation to results
- **Results Page** (`/results`)
  - Grid view with thumbnails (5 columns, 25/page)
  - Selected filters displayed on left
  - View mode buttons on right
  - Back to filters navigation
  - Pagination
- Global layout with copyright footer
- Archive.org inspired minimal aesthetic

**⏳ Still TODO:**
- Individual work pages (`/work/[id]`)
- Other view modes (slideshow, timeline, graph, map)
- Search functionality
- Video thumbnail generation
- About/News/Email pages

**To continue development:**
```bash
# Terminal 1
cd /Volumes/2025/SynologyDrive/Operating/elliottandrew-website/backend
npm run dev

# Terminal 2
cd /Volumes/2025/SynologyDrive/Operating/elliottandrew-website/frontend
npm run dev
```
Then open: http://localhost:3000

See: **[PROJECT_STATUS.md](PROJECT_STATUS.md)** for complete technical documentation

---

### ⏳ Session 3: Advanced Features (Later)

**Will Add (~4 hours):**
- List view (sortable table)
- Slideshow view (full-screen)
- Connection tracking
- Performance optimization

---

### ⏳ Session 4: Deploy (Final)

**Will Deploy (~2-3 hours):**
- Backend to Vercel or AWS
- Frontend to Vercel
- Connect elliottandrew.com
- Go live!

---

## API Endpoints (Already Built)

**Backend runs on:** `http://localhost:3001`
**Frontend runs on:** `http://localhost:3000`

```
GET  /api/creations                  # All published works
GET  /api/creations/:id              # Single work (E-00042)
GET  /api/creations/filter           # Filter by year, medium, tags
GET  /api/creations/search           # Text search
GET  /api/creations/connections/:id  # Related works
GET  /api/stats                      # Collection statistics
GET  /api/media?path=...             # Serve media files
```

See: [backend/README.md](backend/README.md)

---

## Sync Tool (Already Built)

**Uploads catalog to MongoDB:**

```bash
cd sync-tool

./website-sync                # Sync all published
./website-sync --dry-run      # Preview
./website-sync E-00042        # Sync specific
./website-sync --stats        # Show stats
```

See: [sync-tool/README.md](sync-tool/README.md)

---

## How Publishing Works

**To publish a creation:**

1. Edit CSV:
   ```bash
   nano /Volumes/2025/SynologyDrive/Operating/Catalogs/creations_catalog.csv
   # Set published=yes for E-##### you want on website
   ```

2. Run sync:
   ```bash
   cd sync-tool
   ./website-sync
   ```

3. Check website:
   - API: http://localhost:3001/api/creations
   - Frontend: http://localhost:3000

**To unpublish:** Set `published=no` and run sync again.

---

## Tech Stack

**Frontend** (Session 2):
- Next.js 14 (React framework)
- Tailwind CSS (Archive.org aesthetic)
- Vercel (hosting - free)

**Backend** (✅ Done):
- Node.js + Express
- MongoDB Atlas (database - free 512MB)

**Tools** (✅ Done):
- Python sync tool
- CSV as source of truth

---

## Design & Features

**Visual Style:**
- Archive.org inspired
- Minimal, clean, functional
- Small typography (10-13px)
- Black/gray/white with red accent (#d2442e)
- Lots of white space

**5 Viewing Modes:**
1. **Search** - Multi-select filters (year, medium, tags)
2. **Grid** - 5×5 thumbnails, 25 per page
3. **Standalone** - Individual work pages with full details
4. **List** - Sortable table (Session 3)
5. **Slideshow** - Full-screen navigation (Session 3)

**Key Features:**
- Dynamic filtering and search
- Connection tracking between works
- Responsive (mobile-friendly)
- Fast loading (WebP images)
- SEO optimized

See: [DESIGN_SPECIFICATIONS.md](../../Systems/Creative%20Practice%20System/Website/DESIGN_SPECIFICATIONS.md)

---

## Independence

**After launch, you can:**
- Add new work: Edit CSV → run sync → work appears
- Update descriptions: Edit CSV → run sync → changes appear
- Unpublish work: Set published=no → run sync → work hidden
- No AI needed for daily operations

**AI only needed for:**
- Bug fixes (rare)
- Adding new features (optional)
- Major redesigns (rare)

**Handoff ready:**
- Standard tech (React, Node, MongoDB)
- Clear documentation
- Can hire any web developer

---

## When You Return

**To pick up where you left off:**

1. Navigate to project:
   ```bash
   cd /Volumes/2025/SynologyDrive/Operating/elliottandrew-website
   ```

2. Read the status docs:
   - [PROJECT_STATUS.md](PROJECT_STATUS.md) - Complete technical documentation
   - Check "Recent Changes" section for what was done last

3. Start the development servers (2 terminals):
   ```bash
   # Terminal 1 - Backend
   cd backend && npm run dev

   # Terminal 2 - Frontend
   cd frontend && npm run dev
   ```

4. Open http://localhost:3000 to see the website

5. Pick next feature from TODO list in PROJECT_STATUS.md

**Next logical tasks:**
- Individual work pages (`/work/[id]`)
- Implement one view mode (slideshow, timeline, graph, or map)
- Add search functionality
- Install FFmpeg for video thumbnails

---

## Documentation

**In this folder:**
- [QUICKSTART.md](QUICKSTART.md) - Setup guide
- [backend/README.md](backend/README.md) - API documentation
- [sync-tool/README.md](sync-tool/README.md) - Sync tool guide
- [docs/MONGODB_SETUP.md](docs/MONGODB_SETUP.md) - MongoDB Atlas setup

**In Google Drive** (`Operating/Systems/Creative Practice System/Website/`):
- README.md - Overview and entry point
- WEBSITE_PLAN.md - Complete planning document
- BUILD_PLAN.md - Detailed 18-20 hour implementation plan
- DESIGN_SPECIFICATIONS.md - Visual design and UX
- CONTENT_SOURCES.md - Where all content lives
- DECISIONS.md - Project decisions log
- WEBSITE_CONTEXT.md - Distribution strategy

---

## Support

**Troubleshooting:**
- Check README files in each folder
- Check QUICKSTART.md for common issues
- Check docs/MONGODB_SETUP.md for database issues
- Check PROJECT_STATUS.md for current technical details

**Session 2 in progress! Filter and results pages complete.**

---

**Started:** 2025-11-05
**Last Updated:** 2025-11-06
**Status:** Backend complete, Frontend filter & results pages complete
**Total Progress:** ~60% complete (Session 2 in progress - 2 of 4 sessions)
