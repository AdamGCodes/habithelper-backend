# 📍 HabitHelper – Product Roadmap

## ✅ MVP (Current Focus)

### 🧱 Core Features
- [x] User authentication (sign up, sign in)
- [x] Temperance timers (create, reset, delete)
- [x] Journal feature (create, edit, delete entries)
- [ ] HabitHelpers (positive habit tracking with frequency and streaks)
- [x] Field-level and form-level error handling
- [x] Frontend and backend deployed

## 🔄 Phase 2 (Next)

### 🏆 Streaks & Awards
- [ ] Streak-based award system (1-day, 7-day, 30-day milestones)
- [ ] Dashboard streak stats (current streak and all-time bests)

### 📓 Journal as a Habit
- [ ] Make journaling a trackable habit with frequency reminders

### 💬 Affirmations & Quotes
- [ ] Add affirmation/quote habits
- [ ] Cycle through built-in or user-submitted quotes

### 📊 Visual Progress Tracking
- [ ] Add charts or visual indicators to show progress and gaps

### 👥 Social Connection Features
- [ ] Add “friends” system (optional connections)
- [ ] Implement lightweight encouragements (e.g. “high five”)
- [ ] Create social habits: contact rotation, prompting outreach

---

## 🧠 Ideas for Phase 3

- [ ] Badge system or gamification beyond streaks
- [ ] Weekly email summaries or check-ins
- [ ] Background customization
- [ ] Option for shared streaks or partner goals

---

## 🔧 Technical Improvements

- [ ] Centralized error system across all forms
- [ ] Add unit and integration tests
- [ ] Add production logging and error reporting

---

## 🧹 Codebase Cleanup & Refactoring

- [ ] Audit and simplify SCSS modules (ensure proper modular styling is used throughout)
- [ ] Refactor any redundant or overly complex components (especially older ones like the modal)
- [ ] Clean up unused files, test data, and leftover code
- [ ] Improve file naming conventions and folder structure for clarity
- [ ] Replace any hardcoded values (e.g. quote text) with config or constants
- [ ] Ensure consistent use of state management across features
- [ ] Re-test all CRUD operations and auth flows
- [ ] Review accessibility (color contrast, keyboard navigation, screen reader friendliness)
- [ ] Double-check responsiveness on different screen sizes
- [ ] Rewrite or polish any unclear logic, especially in dashboard/timer handling
