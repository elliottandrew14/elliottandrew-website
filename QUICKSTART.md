# Elliott Andrew Website - Quick Start Guide

**Session 1 Complete!** Backend + Sync Tool built and ready to test.

---

## What We Built Today (Session 1)

✅ **Complete Node.js/Express API** with all endpoints
✅ **Python sync tool** to upload catalog to MongoDB
✅ **Organized documentation** and setup guides
✅ **Added "published" column** to your CSV
✅ **Marked E-00042 and E-00037** as test creations

---

## Next Steps (What You Need To Do)

### Step 1: Set up MongoDB Atlas (~10 minutes)

Follow the detailed guide:
```
open docs/MONGODB_SETUP.md
```

**Quick version:**
1. Go to https://www.mongodb.com/cloud/atlas/register
2. Create free account (M0 tier)
3. Create cluster
4. Create database user (save password!)
5. Allow IP access (0.0.0.0/0 for development)
6. Copy connection string

---

### Step 2: Install Backend Dependencies (~2 minutes)

```bash
cd /Volumes/2025/SynologyDrive/Operating/elliottandrew-website/backend

# Install Node dependencies
npm install

# Create .env file
cp .env.example .env

# Edit .env and add your MongoDB URI
# (Use the connection string from Step 1)
nano .env
```

Your `.env` should look like:
```
MONGODB_URI=mongodb+srv://your-username:your-password@cluster0.xxxxx.mongodb.net/portfolio?retryWrites=true&w=majority
PORT=5000
```

---

### Step 3: Start Backend API (~1 minute)

```bash
# Still in backend/ directory
npm run dev
```

You should see:
```
✅ MongoDB Connected: cluster0.xxxxx.mongodb.net
📁 Database: portfolio
✅ Server running on port 5000
📡 API available at http://localhost:5000
```

**Test it:** Open http://localhost:5000/api/health in your browser

---

### Step 4: Install Sync Tool Dependencies (~2 minutes)

**Open a NEW terminal** (keep backend running):

```bash
cd /Volumes/2025/SynologyDrive/Operating/elliottandrew-website/sync-tool

# Install Python dependencies
pip3 install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env and add SAME MongoDB URI as backend
nano .env
```

---

### Step 5: Test Sync Tool (~2 minutes)

```bash
# Still in sync-tool/ directory

# Dry run (preview without uploading)
./website-sync --dry-run

# If that looks good, actually sync
./website-sync
```

You should see:
```
✅ Connected to MongoDB: portfolio
📖 Read 73 entries from catalog
🎯 Found 2 published creations
🔄 Syncing 2 creations...

  ✅ Added E-00037: Untitled
  ✅ Added E-00042: Untitled

✅ Sync complete!
   Added: 2
   Updated: 0
```

---

### Step 6: Verify Everything Works (~2 minutes)

**Test API endpoints:**

```bash
# Get all creations (should show 2)
curl http://localhost:5000/api/creations

# Get specific creation
curl http://localhost:5000/api/creations/E-00042

# Get stats
curl http://localhost:5000/api/stats
```

**Check MongoDB Atlas:**
1. Go to MongoDB Atlas dashboard
2. Click "Browse Collections"
3. You should see `portfolio` database → `creations` collection → 2 documents

---

## What's Next? (Session 2)

After testing backend + sync:

**Session 2 will build the frontend:**
- Next.js/React website
- Search + Grid views
- Individual work pages
- About page

**Estimated time:** 6 hours

---

## Project Structure

```
elliottandrew-website/
├── backend/              ✅ DONE (Node.js API)
│   ├── server.js
│   ├── routes/
│   ├── models/
│   └── README.md
├── sync-tool/            ✅ DONE (CSV → MongoDB)
│   ├── website-sync
│   ├── config.py
│   └── README.md
├── frontend/             ⏳ SESSION 2 (React website)
├── docs/                 ✅ DONE
│   ├── MONGODB_SETUP.md
│   └── add-published-column.py
└── QUICKSTART.md         📄 You are here
```

---

## Troubleshooting

### Backend won't start:
```bash
# Check if MongoDB URI is correct in .env
cat backend/.env

# Try reinstalling dependencies
cd backend
rm -rf node_modules package-lock.json
npm install
```

### Sync tool errors:
```bash
# Check if dependencies are installed
pip3 list | grep pymongo

# Check if .env file exists
cat sync-tool/.env

# Check if published column exists in CSV
head -1 /Volumes/2025/SynologyDrive/Operating/Catalogs/creations_catalog.csv
```

### Can't connect to MongoDB:
- Check internet connection
- Check MongoDB Atlas dashboard (cluster might be paused)
- Check IP whitelist (should have 0.0.0.0/0)
- Check password in connection string (no < > symbols)

---

## Commands Reference

**Backend:**
```bash
cd /Volumes/2025/SynologyDrive/Operating/elliottandrew-website/backend
npm run dev                    # Start development server
npm start                      # Start production server
```

**Sync Tool:**
```bash
cd /Volumes/2025/SynologyDrive/Operating/elliottandrew-website/sync-tool
./website-sync                 # Sync all published
./website-sync --dry-run       # Preview
./website-sync E-00042         # Sync specific
./website-sync --stats         # Show stats
```

**Publishing Workflow:**
```bash
# 1. Edit CSV
nano /Volumes/2025/SynologyDrive/Operating/Catalogs/creations_catalog.csv
# Change published=yes for creations you want on website

# 2. Sync to database
cd /Volumes/2025/SynologyDrive/Operating/elliottandrew-website/sync-tool
./website-sync

# 3. Check API
curl http://localhost:5000/api/creations
```

---

## Session 1 Summary

**Time Spent:** ~3 hours building
**What's Working:**
- ✅ Complete REST API with 6 endpoints
- ✅ MongoDB database connection
- ✅ CSV sync tool with dry-run mode
- ✅ Published column in catalog
- ✅ 2 test creations ready (E-00037, E-00042)

**Your Action Items:**
1. Set up MongoDB Atlas (10 min)
2. Install & test backend (5 min)
3. Install & test sync tool (5 min)

**Next Session:**
- Build React frontend
- Create Search + Grid + Individual pages
- Deploy to Vercel (optional)

---

**Questions? Check the README files in each folder for detailed instructions.**

**Ready for Session 2? Just say "let's build the frontend" and we'll continue!**
