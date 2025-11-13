# Website Sync Tool

Uploads your creations catalog to MongoDB for the website.

---

## Setup

### 1. Install Dependencies

```bash
cd /Volumes/2025/SynologyDrive/Operating/elliottandrew-website/sync-tool
pip3 install -r requirements.txt
```

### 2. Create .env File

```bash
cp .env.example .env
```

Edit `.env` and add your MongoDB connection string (same as backend):
```
MONGODB_URI=mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/portfolio?retryWrites=true&w=majority
```

---

## Usage

### Sync All Published Creations
```bash
./website-sync
```

### Dry Run (Preview Without Uploading)
```bash
./website-sync --dry-run
```

### Sync Specific Creation
```bash
./website-sync E-00042
```

### Show Stats
```bash
./website-sync --stats
```

### Force Re-sync Everything
```bash
./website-sync --force
```

---

## What It Does

1. **Reads catalog**: `/Volumes/2025/SynologyDrive/Operating/Catalogs/creations_catalog.csv`
2. **Filters published**: Only uploads creations where `published=yes`
3. **Finds media**: Looks for images/videos in `/Volumes/2025/SynologyDrive/Creations/E-#####/`
4. **Uploads to MongoDB**: Creates or updates each creation document
5. **Reports results**: Shows what was added, updated, or had errors

---

## Configuration

Edit `config.py` to customize:
- Catalog CSV path
- Creations base path
- Media output path
- Image optimization settings

---

## How Publishing Works

**To publish a creation:**
1. Edit `creations_catalog.csv`
2. Set `published=yes` for the E-##### you want on website
3. Run `./website-sync`
4. Creation appears on website

**To unpublish:**
1. Set `published=no` in CSV
2. Run `./website-sync --force`
3. Creation removed from website (stays in database but won't show)

---

## Troubleshooting

**"ModuleNotFoundError: No module named 'pymongo'":**
```bash
pip3 install -r requirements.txt
```

**"MongoDB connection failed":**
- Check `.env` file has correct MONGODB_URI
- Check MongoDB Atlas IP whitelist (0.0.0.0/0 for development)
- Make sure backend MongoDB setup is complete

**"Catalog not found":**
- Check catalog path in `config.py`
- Make sure you're running from sync-tool directory

**"No media files found":**
- Check E-##### folders exist in `/Volumes/2025/SynologyDrive/Creations/`
- Script looks in multiple locations (direct, Objects/, Arrangements/)
- Media is optional - creations will still sync without it

**"published column not found":**
- Run: `/Volumes/2025/SynologyDrive/Operating/elliottandrew-website/docs/add-published-column.py`
- This adds the published column to your CSV

---

## Workflow

**Normal workflow:**

1. Create new work → Import to Creations/
2. Add entry to creations_catalog.csv (using add-creation tool)
3. When ready to publish:
   - Edit CSV: Set `published=yes`
   - Run `./website-sync`
4. Check website: http://elliottandrew.com

**Updating existing work:**

1. Edit description/tags in CSV
2. Run `./website-sync E-#####` (specific)
   OR `./website-sync` (all published)
3. Changes appear immediately on website

---

## Next Steps

After syncing:
1. Check MongoDB Atlas dashboard - you should see data in `creations` collection
2. Test API: `http://localhost:5000/api/creations`
3. Build frontend to display your work

---

**Sync tool complete! Ready to populate your database.**
