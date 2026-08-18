# DEUTSCHMAP 🗺️

**Interactive German Vocabulary Learning Platform**

DEUTSCHMAP is a free, open-source web application for learning German vocabulary across all CECRL proficiency levels (A1 to C2). Master German through interactive flashcards, vocabulary maps, and comprehensive word lists.

## Features 🎯

- **6 CECRL Levels**: A1 (Beginner) → A2 (Elementary) → B1 (Intermediate) → B2 (Upper Intermediate) → C1 (Advanced) → C2 (Mastery)
- **Interactive Flashcards**: Learn German words with spaced repetition and visual mnemonics
- **Vocabulary Maps**: Visualize word relationships and semantic connections
- **Progress Tracking**: Automatic savings with localStorage + manual Export/Import backups
- **Search & Filter**: Find words by German/English terms or by category
- **Categorized Vocabulary**: 16 topics (Greetings, Family, Food, Time, etc.)
- **100% Free**: No registration, no paywalls, no ads

## Structure 📂

```
deutschmap/
├── index.html          # Homepage with CECRL level overview & level selection
├── deutschmap.html     # Interactive vocabulary application (A1 to C2 study interface)
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
- **index.html**: Main landing page with all CECRL levels
- Click any level card to access the vocabulary trainer
- Use level pills at the top to switch between A1, A2, B1, B2 (A2-B2 coming soon)

### Vocabulary Trainer
1. **Tap/Click a word** to reveal its English translation
2. **Click the status circle** (top-right of each word) to mark:
   - ❌ Unmarked (default)
   - 🟡 Review (yellow) - words you need to practice
   - 🟢 Known (green) - mastered words

3. **Filter & Search**:
   - Use status filter buttons to show only "All", "Unmarked", "Review", or "Known"
   - Search by German or English words
   - Filter by category (Greetings, Family, Food, etc.)

4. **Save & Backup**:
   - Progress auto-saves to localStorage (device-specific)
   - **Export ⬇**: Download your progress as JSON backup
   - **Import ⬆**: Restore progress from JSON file
   - **Reset ↺**: Clear all progress (with confirmation)

## Technology Stack 🛠️

- **Frontend**: Pure HTML, CSS, JavaScript (no frameworks)
- **Storage**: Browser localStorage + JSON export/import
- **Typography**: Google Fonts (Space Grotesk, Inter, IBM Plex Mono)
- **Design System**: Custom CSS tokens for consistency

## Vocabulary Content 📚

### Currently Available (A1)
- 16 Categories
- 400+ German words
- Complete English translations
- Progressive difficulty within each category

### Coming Soon
- A2 Elementary Level (~600 words)
- B1 Intermediate Level (~900 words)
- B2 Upper Intermediate Level (~1200 words)
- C1 Advanced Level (~1500 words)
- C2 Mastery Level (~2000+ words)

## SEO & AI Optimization 🤖

- Schema.org JSON-LD structured data
- Bilingual meta descriptions (FR/EN)
- CECRL-aligned keywords for search engines
- FAQ section for LLM/AI indexing
- Open Graph meta tags for social sharing

## Browser Support 🌐

- Chrome/Edge: ✅ Full support
- Firefox: ✅ Full support
- Safari: ✅ Full support
- Mobile browsers: ✅ Full support (iOS Safari, Chrome Mobile)

## Key Sections in Code 📝

### index.html
- Hero section with CTA
- 6-card CECRL levels grid
- Features showcase
- FAQ section for AI/SEO
- Professional footer

### deutschmap.html (Vocabulary App)
- Level bar with pill buttons
- Header with stats and progress bar
- Search bar with live filtering
- Status filter buttons (All/Unmarked/Review/Known)
- Category filter pills
- Responsive vocabulary grid
- Export/Import buttons for backups
- Hint section with usage instructions

## Data Format 💾

### Export Format (JSON)
```json
{
  "level": "a1",
  "timestamp": "2026-08-18T12:34:56.789Z",
  "status": {
    "a1-0": "known",
    "a1-1": "review",
    "a1-2": "unmarked"
  }
}
```

## Contributing 🤝

Contributions are welcome! Areas for enhancement:
- Additional vocabulary for A2-C2 levels
- Audio pronunciation (German native speakers)
- Spaced repetition algorithm improvements
- Mobile app version
- Multi-language UI
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
