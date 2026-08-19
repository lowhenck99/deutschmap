# DEUTSCHMAP 🗺️

**Interactive German Vocabulary Learning Platform**

DEUTSCHMAP is a free, open-source web application for learning German vocabulary across all CECRL proficiency levels (A1 to C2). Master German through interactive flashcards, vocabulary maps, and comprehensive word lists.

## Features 🎯

- **6 CECRL Levels**: A1 (Beginner) → A2 (Elementary) → B1 (Intermediate) → B2 (Upper Intermediate) → C1 (Advanced) → C2 (Mastery)
- **Interactive Flashcards**: Tap a word to reveal its translation, mark it as To Review / Mastered
- **Due for Review**: Lightweight spaced-repetition filter that surfaces "To Review" words not revisited in 3+ days
- **Progress Tracking**: Automatic saving with `localStorage` (per-device, no size limit like cookies)
- **Search & Filter**: Find words by German/English terms, by status, or by category
- **Categorized Vocabulary**: 17 auto-classified topics (Greetings, Family, Food, Time, etc.)
- **Shuffle Mode**: Randomize word order per level
- **Gender Coloring**: der/die/das color-coded to help memorize grammatical gender
- **Audio Pronunciation**: Native `.mp3` clips with a browser `speechSynthesis` fallback
- **Keyboard Accessible**: Flashcards and status toggles are focusable and operable without a mouse
- **100% Free**: No registration, no paywalls, no ads

## Structure 📂

```
deutschmap/
├── index.html          # Homepage with CECRL level overview, level selection & live progress
├── deutschmap.html     # Interactive vocabulary application (A1 to C2 study interface)
├── vocabulary.json     # Word lists per level, each word tagged with a category (cat)
├── audio/              # Native German pronunciation clips (.mp3)
├── favicon.svg          # Site icon
├── sitemap.xml          # SEO sitemap
├── robots.txt           # Crawler rules
├── download_audio.py    # Script used to generate the audio clips (gTTS)
└── README.md           # This file
```

## Getting Started 🚀

### Online (GitHub Pages)
1. Visit: https://github.com/lowhenck99/deutschmap
2. Open `index.html` in your browser or deploy to GitHub Pages

### Local Development
1. Clone the repository:
   ```bash
   git clone https://github.com/lowhenck99/deutschmap.git
   cd deutschmap
   ```

2. Open `index.html` in a web browser:
   - **Windows**: Double-click `index.html` or right-click → Open with browser
   - **Mac/Linux**: `open index.html` or use your preferred browser

3. Start learning! Click on a CECRL level to access the vocabulary trainer

## How to Use 📖

### Navigation
- **index.html**: Main landing page with all CECRL levels and your live progress per level
- Click any level card to access the vocabulary trainer
- Use level pills at the top to switch between A1, A2 (live) and B1-C2 (coming soon)

### Vocabulary Trainer
1. **Tap/Click a word** (or press Enter/Space when focused) to reveal its English translation
2. **Click the status circle** (top-right of each word) to cycle:
   - Unmarked (default) → 🟡 To Review → 🟢 Mastered → back to Unmarked
3. **Filter & Search**:
   - Status filters: All / To Learn / To Review / Mastered / Due for Review
   - Search by German or English words
   - Filter by category (17 auto-classified topics)
   - Shuffle word order for the current level
4. **Save & Backup**:
   - Progress auto-saves to `localStorage` (device-specific)
   - **Export ⬇**: Download your progress as a JSON backup
   - **Import ⬆**: Restore progress from a JSON backup file
   - **Reset ↺**: Clear all saved progress (with confirmation)

## Technology Stack 🛠️

- **Frontend**: Pure HTML, CSS, JavaScript (no frameworks, no build step)
- **Storage**: Browser `localStorage` + manual JSON export/import
- **Typography**: System font stack (`-apple-system`, SF Pro, Helvetica Neue)
- **Design System**: Custom CSS tokens, Apple-inspired minimalist theme

## Vocabulary Content 📚

### Currently Available
- **A1 (Beginner)**: 681 German words, 17 categories
- **A2 (Elementary)**: 594 German words, 17 categories
- Each word: German term, English translation, auto-assigned category, native audio clip

### Coming Soon
- B1 Intermediate Level (~900 words)
- B2 Upper Intermediate Level (~1200 words)
- C1 Advanced Level (~1500 words)
- C2 Mastery Level (~2000+ words)

## SEO 🤖

- Schema.org `LearningResource` JSON-LD structured data
- Open Graph & Twitter Card meta tags for social sharing
- `sitemap.xml` + `robots.txt`
- CECRL-aligned meta description and keywords

## Browser Support 🌐

- Chrome/Edge: ✅ Full support
- Firefox: ✅ Full support
- Safari: ✅ Full support
- Mobile browsers: ✅ Full support (iOS Safari, Chrome Mobile)

## Key Sections in Code 📝

### index.html
- Hero section with CTA
- CECRL levels grid, with live per-level progress bars
- SEO/feature showcase section
- Professional footer

### deutschmap.html (Vocabulary App)
- Level bar with pill buttons
- Header with stats (Mastered / To Review / To Learn / Due Now) and progress bar
- Search bar with live filtering
- Status filter buttons (All / To Learn / To Review / Mastered / Due for Review)
- Category filter pills (auto-generated per level)
- Shuffle + Export/Import/Reset controls
- Responsive, keyboard-accessible vocabulary grid

## Data Format 💾

### vocabulary.json
```json
{
  "A1": {
    "words": [
      { "de": "der Absender", "en": "sender", "cat": "General Vocabulary" }
    ]
  }
}
```

### Export Format (JSON backup)
```json
{
  "level": "a1",
  "timestamp": "2026-08-18T12:34:56.789Z",
  "status": {
    "a1-0": "is-know",
    "a1-1": "is-review"
  },
  "lastSeen": {
    "a1-0": 1755500000000,
    "a1-1": 1755600000000
  }
}
```

## Contributing 🤝

Contributions are welcome! Areas for enhancement:
- Additional vocabulary for B1-C2 levels
- Manual review of the auto-assigned word categories (currently keyword-based, some noise expected)
- Full spaced-repetition scheduling (current "Due for Review" is a simple 3-day heuristic)
- Native-speaker audio recordings to replace/complement the generated clips
- Mobile app version
- Multi-language UI (French, Spanish...)
- Gamification features (badges, streaks)

## License 📄

This project is open source and available under the MIT License.

## Credits & Attribution ✨

- **CECRL Framework**: Council of Europe (language proficiency standards)
- **Goethe-Institut A1 Vocabulary**: Used as reference for A1 level

## Contact & Support 📧

- GitHub: https://github.com/lowhenck99/deutschmap
- Issues: https://github.com/lowhenck99/deutschmap/issues

---

**Happy Learning! Viel Erfolg beim Lernen! 🇩🇪**

Master German vocabulary from beginner to mastery with DEUTSCHMAP.
