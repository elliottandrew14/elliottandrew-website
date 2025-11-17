## Native Display for 3D Objects & Projects

**Feature:** Display 3D objects, installations, and other non-photo projects directly on the website instead of linking externally

**Current State:**
- Photos are displayed natively on the website (click → view on site)
- 3D objects, installations, and other projects link externally (Cargo, YouTube, etc.)
- Both types have info pages on the site, but actual content lives elsewhere for non-photos

**Future Goal:**
- Integrate 3D viewers (Sketchfab embeds, three.js, etc.)
- Embed videos directly (instead of linking to Vimeo/YouTube)
- Display project documentation natively
- Provide consistent viewing experience for all work types

**Benefits:**
- Unified user experience
- Keep visitors on your site
- Better control over presentation
- Potential for interactive experiences
- Improved analytics and engagement tracking

**Technical Considerations:**
- 3D file formats and viewers
- Video hosting (self-hosted vs. embedded)
- Page load performance with rich media
- Mobile device compatibility
- Bandwidth and storage costs

**Priority:** Future enhancement (currently subject to change)

**Date noted:** 2025-11-17

---

## Exhibition/Installation History

**Feature:** Add column(s) for tracking when and where works have been exhibited/installed

**Fields to add:**
- `exhibition_history` - List of exhibitions/installations
  - Exhibition name
  - Venue/Location
  - Date (year, month, day)
  - City, State, Country
  - Type (solo, group, installation, screening, etc.)
  
**Example data structure:**
```csv
exhibition_history
"Mirrorchairpipe Watch-ing; Piazza della Signoria; 2024-07-15; Florence; ; Italy; performance | Gallery Show; Art Space; 2024-10-01; St. Louis; MO; United States; group exhibition"
```

**Display on website:**
- Show on individual work info page
- Format: "Exhibition Name, Venue, City, Year"
- Make clickable to filter by venue/city
- Could build a full CV page from this data

**Benefits:**
- Professional presentation
- Track exhibition history
- Auto-generate CV
- Filter works by exhibition venue
- Show which works have been publicly exhibited

**Priority:** Medium (after prints catalog is working)

**Date noted:** 2025-11-15
