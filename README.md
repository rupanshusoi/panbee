# Pangram Bee 🐝

A word puzzle game inspired by the New York Times Spelling Bee, but focused exclusively on finding pangrams - words that use all 7 letters at least once.

## Play Online

Once deployed to GitHub Pages, you can play the game at: `https://[your-username].github.io/spellbee/`

## How to Play

1. **Goal**: Find words that use ALL 7 letters shown (pangrams)
2. **Rules**:
   - Words must be at least 7 letters long
   - Words must include the center letter (highlighted in red/pink)
   - Words must use all 7 different letters at least once
   - Letters can be used multiple times
3. **Controls**:
   - Click letters or type to input your word
   - Press Enter or click Submit to check your word
   - Use Shuffle to rearrange the outer letters
   - Click New Puzzle for a fresh challenge

## Features

- Beautiful hexagon letter display
- Real-time validation
- Progress tracking
- Multiple pangrams per puzzle
- Responsive design for mobile and desktop
- Uses the 3of6game wordlist for puzzle generation

## Deployment to GitHub Pages

1. Push this repository to GitHub
2. Go to Settings → Pages in your repository
3. Under "Source", select "Deploy from a branch"
4. Choose "main" branch and "/ (root)" folder
5. Click Save
6. Your game will be available at `https://[your-username].github.io/[repository-name]/`

## Local Development

To run locally:
```bash
# Clone the repository
git clone [your-repo-url]
cd spellbee

# Start a local server (Python 3)
python3 -m http.server 8000

# Or with Node.js
npx http-server

# Open in browser
# Navigate to http://localhost:8000
```

## Files

- `index.html` - The complete game (HTML, CSS, and JavaScript)
- `3of6game.txt` - Dictionary of valid English words used for puzzle generation
- `analyze_pangrams.py` - Utility script to analyze available pangrams in the wordlist

## Technical Details

- Pure HTML/CSS/JavaScript - no framework dependencies
- Static site compatible with GitHub Pages
- Wordlist preprocessing happens on page load
- Generates puzzles with varying difficulty based on number of possible pangrams

## Credits

- Word list: 3of6game dictionary
- Inspired by the New York Times Spelling Bee
