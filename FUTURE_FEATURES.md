## Newsletter Signup

**Feature:** Add newsletter signup overlay/form for email updates

**Nearer Future Priority**

**What:**
- Simple email signup form
- Collect emails for newsletter/updates
- Send updates about new work, exhibitions, prints, etc.

**Implementation:**
- Overlay/modal triggered by button (in menu or footer)
- Simple form: Name, Email
- Store in database or integrate with email service (Mailchimp, ConvertKit, Buttondown, etc.)
- Confirmation email with double opt-in
- Easy unsubscribe option

**Use Cases:**
- Announce new work added to archive
- Exhibition openings and events
- New prints available
- Studio updates
- Quarterly or monthly newsletters

**Benefits:**
- Build direct relationship with collectors and viewers
- Announce new work and exhibitions
- Drive traffic back to website
- Alternative to social media for updates
- Maintain contact with interested visitors

**Priority:** Nearer future

**Date noted:** 2025-11-17

---

## Postcard/Zine Mailing List Signup

**Feature:** Allow visitors to sign up for physical mail (postcards, zines, announcements)

**Far Future Priority**

**Concept:**
- Visitors can sign up to receive physical mail from you
- Could be postcards of new work
- Artist zines or publications
- Exhibition announcements
- Quarterly or annual mailings

**Implementation:**
- Signup form (name, address, preferences)
- Store in database with mailing addresses
- Export to mailing labels or integrate with mailing services
- Preference options: postcards only, zines, all mailings, etc.

**Technical Considerations:**
- Address validation
- Privacy/GDPR compliance for storing addresses
- Opt-in/opt-out management
- Integration with postal services (printing labels, etc.)
- Cost tracking for mailings

**Benefits:**
- Build physical mailing list for exhibitions/events
- Direct connection with collectors and fans
- Tangible marketing/presence
- Alternative to digital-only engagement
- Personal touch that stands out

**Inspiration:**
- Artist mailing lists for exhibition cards
- Quarterly art zines/newsletters
- Limited edition postcard series
- Annual studio update mailings

**Priority:** Far future (explore after other features are stable)

**Date noted:** 2025-11-17

---

## Mobile Version - Simplified Curated Experience

**Feature:** Create a mobile-optimized version with curated content instead of full filter system

**Target Audience:**
- General public / casual viewers (not fine art professionals)
- Quick browsing experience on phones
- Lower engagement/shorter attention span

**Approach:**
- **Desktop:** Keep full filter system for galleries, curators, residency reviewers
- **Mobile:** Simplified curated experience

**Mobile Design:**
- Show works from ONE selection (e.g., "Featured" or "Mobile")
- ONE view mode (grid or scroll - no switching)
- Simple navigation: About, Contact, News only
- No filter options, no complexity
- Individual work pages same as desktop (photos display, videos link out)

**Implementation:**
- Device detection to route mobile users
- Filter by selection field (already exists in database)
- Reuse existing work detail pages
- Simple grid/scroll feed layout

**Benefits:**
- Two audiences, two experiences
- Professionals get deep research tool (desktop)
- General viewers get accessible portfolio (mobile)
- Low friction for casual discovery
- You control what mobile users see via selections

**Alternative Considered:**
- Using Cargo for mobile ($179/year)
- Decided against for now - prefer integrated solution

**Priority:** Future enhancement

**Date noted:** 2025-11-17

---

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
