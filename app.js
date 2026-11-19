// ==========================================================================
// APPLIKASI MINERAPETRO-EXPERT (MINING ENGINEERING MEMORIZATION ENGINE)
// FT-UNIKARTA - Dosen Pengampu: Sundyo, S.T., M.T.
// ==========================================================================

// Global State
const state = {
  soundEnabled: true,
  currentTab: 'kuliah',
  flashcardIndex: 0,
  flashcardCategory: 'ALL',
  filteredCards: [],
  learnedCards: new Set(JSON.parse(localStorage.getItem('minerapetro_learned') || '[]')),
  
  // Mohs game state
  mohsSlots: Array(10).fill(null),
  mohsAvailable: [],
  selectedChip: null,

  // Quiz state
  quizMode: 'pretest', // 'pretest' (10), 'standard' (25), 'full' (60)
  quizQuestions: [],
  quizCurrentIndex: 0,
  quizAnswers: [],
  quizScore: 0,
  quizTimerSeconds: 0,
  quizTimerInterval: null,
  quizInstantFeedback: true,

  // Speech
  synth: window.speechSynthesis || null,
  isSpeaking: false
};

// ==========================================================================
// 1. WEB AUDIO API SYNTHESIZER (No external audio files required!)
// ==========================================================================
class SoundFX {
  constructor() {
    this.ctx = null;
  }

  init() {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) this.ctx = new AudioCtx();
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  playClick() {
    if (!state.soundEnabled) return;
    this.init();
    if (!this.ctx) return;

    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(600, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(800, this.ctx.currentTime + 0.05);

    gain.gain.setValueAtTime(0.12, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.05);

    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.05);
  }

  playFlip() {
    if (!state.soundEnabled) return;
    this.init();
    if (!this.ctx) return;

    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(320, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(450, this.ctx.currentTime + 0.08);

    gain.gain.setValueAtTime(0.15, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.09);

    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.09);
  }

  playCorrect() {
    if (!state.soundEnabled) return;
    this.init();
    if (!this.ctx) return;

    // Harmonic chime: C5 -> E5 -> G5
    const notes = [523.25, 659.25, 783.99];
    notes.forEach((freq, idx) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime + idx * 0.08);

      gain.gain.setValueAtTime(0.15, this.ctx.currentTime + idx * 0.08);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + idx * 0.08 + 0.3);

      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(this.ctx.currentTime + idx * 0.08);
      osc.stop(this.ctx.currentTime + idx * 0.08 + 0.35);
    });
  }

  playIncorrect() {
    if (!state.soundEnabled) return;
    this.init();
    if (!this.ctx) return;

    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(160, this.ctx.currentTime);
    osc.frequency.linearRampToValueAtTime(110, this.ctx.currentTime + 0.25);

    gain.gain.setValueAtTime(0.18, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.25);

    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.25);
  }

  playFanfare() {
    if (!state.soundEnabled) return;
    this.init();
    if (!this.ctx) return;

    const melody = [523.25, 659.25, 783.99, 1046.50];
    melody.forEach((freq, i) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime + i * 0.12);

      gain.gain.setValueAtTime(0.2, this.ctx.currentTime + i * 0.12);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + i * 0.12 + 0.5);

      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(this.ctx.currentTime + i * 0.12);
      osc.stop(this.ctx.currentTime + i * 0.12 + 0.55);
    });
  }
}

const soundFX = new SoundFX();

// ==========================================================================
// 2. BACKGROUND PARTICLE CANVAS (Floating Mineral Crystals)
// ==========================================================================
function initParticleCanvas() {
  const canvas = document.getElementById('particle-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let width = (canvas.width = window.innerWidth);
  let height = (canvas.height = window.innerHeight);

  window.addEventListener('resize', () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  });

  const particles = [];
  const particleCount = Math.min(35, Math.floor(width / 35));

  for (let i = 0; i < particleCount; i++) {
    particles.push({
      x: Math.random() * width,
      y: Math.random() * height,
      size: Math.random() * 8 + 4,
      sides: Math.random() > 0.5 ? 6 : 4, // Hexagonal or Isometric diamond
      speedY: -(Math.random() * 0.4 + 0.15),
      speedX: (Math.random() - 0.5) * 0.2,
      rotation: Math.random() * Math.PI * 2,
      rotSpeed: (Math.random() - 0.5) * 0.015,
      alpha: Math.random() * 0.35 + 0.1,
      color: Math.random() > 0.4 ? '#f59e0b' : (Math.random() > 0.5 ? '#3b82f6' : '#10b981')
    });
  }

  function drawPolygon(x, y, radius, sides, rot, color, alpha) {
    ctx.save();
    ctx.translate(x, y);
    ctx.rotate(rot);
    ctx.beginPath();
    for (let i = 0; i < sides; i++) {
      const angle = (i * 2 * Math.PI) / sides;
      const px = radius * Math.cos(angle);
      const py = radius * Math.sin(angle);
      if (i === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.closePath();
    ctx.fillStyle = color;
    ctx.globalAlpha = alpha;
    ctx.fill();
    ctx.strokeStyle = '#ffffff';
    ctx.globalAlpha = alpha * 0.5;
    ctx.lineWidth = 1;
    ctx.stroke();
    ctx.restore();
  }

  function animate() {
    ctx.clearRect(0, 0, width, height);

    particles.forEach(p => {
      p.y += p.speedY;
      p.x += p.speedX;
      p.rotation += p.rotSpeed;

      if (p.y < -20) {
        p.y = height + 20;
        p.x = Math.random() * width;
      }
      if (p.x < -20) p.x = width + 20;
      if (p.x > width + 20) p.x = -20;

      drawPolygon(p.x, p.y, p.size, p.sides, p.rotation, p.color, p.alpha);
    });

    requestAnimationFrame(animate);
  }

  animate();
}

// ==========================================================================
// 3. CELEBRATION CONFETTI ENGINE (Pure Vanilla JS Canvas)
// ==========================================================================
function launchConfetti() {
  const canvas = document.getElementById('confetti-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  const confettiPieces = [];
  const colors = ['#f59e0b', '#fbbf24', '#10b981', '#3b82f6', '#ec4899', '#ffffff'];

  for (let i = 0; i < 90; i++) {
    confettiPieces.push({
      x: canvas.width / 2,
      y: canvas.height / 2,
      vx: (Math.random() - 0.5) * 16,
      vy: (Math.random() - 0.7) * 18,
      size: Math.random() * 8 + 5,
      color: colors[Math.floor(Math.random() * colors.length)],
      rotation: Math.random() * 360,
      rotSpeed: (Math.random() - 0.5) * 12,
      alpha: 1,
      gravity: 0.35
    });
  }

  let startTime = Date.now();

  function render() {
    const elapsed = Date.now() - startTime;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    let active = false;
    confettiPieces.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;
      p.vy += p.gravity;
      p.rotation += p.rotSpeed;
      p.alpha = Math.max(0, 1 - elapsed / 2800);

      if (p.alpha > 0) {
        active = true;
        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate((p.rotation * Math.PI) / 180);
        ctx.fillStyle = p.color;
        ctx.globalAlpha = p.alpha;
        ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
        ctx.restore();
      }
    });

    if (active) {
      requestAnimationFrame(render);
    } else {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
  }

  render();
}

// ==========================================================================
// 4. LECTURER SPEECH & DOSEN INSIGHTS
// ==========================================================================
const DOSEN_TIPS = [
  "Perhatikan baik-baik: Di lapangan tambang batu bara Kutai Kartanegara, batupasir dengan struktur Cross Bedding dan Graded Bedding sangat penting untuk menentukan arah sedimentasi purba!",
  "Hafalkan rumus kimia Apatit: Ca5(PO4)3F dan Felspar: K(AlSi3O8). Dua mineral ini sering keluar dalam pre-test praktikum!",
  "Ingat perbedaan belahan kuarsa vs kalsit! Kuarsa TIDAK punya belahan (pecahan konkoidal, Mohs 7), sedangkan Kalsit punya belahan rhombohedral sempurna 3 arah (Mohs 3, berbuih kena HCl)!",
  "Tekstur metamorf Slaty Cleavage vs Schistosic: Slaty mikrokristalin sangat halus pada batusabak; Schistosic berbutir sedang-kasar dengan orientasi mika sejajar pada sekis!",
  "Ingat tata tertib laboratorium tambang: Rusak alat akibat kelalaian wajib ganti melalui Berita Acara, dan sanksi E adalah dikeluarkan dari jurusan!"
];

function triggerDosenTip() {
  soundFX.playClick();
  const randomTip = DOSEN_TIPS[Math.floor(Math.random() * DOSEN_TIPS.length)];
  document.getElementById('lecturer-speech-bubble').textContent = `"${randomTip}"`;

  speakIndonesian(randomTip);
}

function speakIndonesian(text) {
  if (!state.synth) return;
  try {
    state.synth.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'id-ID';
    utterance.rate = 1.0;
    utterance.pitch = 0.95;

    // Pick Indonesian voice if available
    const voices = state.synth.getVoices();
    const idVoice = voices.find(v => v.lang.startsWith('id') || v.lang.includes('Indonesian'));
    if (idVoice) utterance.voice = idVoice;

    state.synth.speak(utterance);
  } catch (e) {
    console.log("SpeechSynthesis error:", e);
  }
}

// ==========================================================================
// 5. INITIALIZATION & TAB SWITCHING
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
  initParticleCanvas();
  renderChapters();
  renderMohsGame();
  renderFlashcards();
  renderGlossary();
  updateStatsRibbon();
  setupEventListeners();

  // Load voices
  if (state.synth && state.synth.onvoiceschanged !== undefined) {
    state.synth.onvoiceschanged = () => {};
  }
});

function setupEventListeners() {
  // Navigation Tabs
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      soundFX.playClick();
      const tabTarget = btn.getAttribute('data-tab');
      switchTab(tabTarget);
    });
  });

  // Sound Toggle
  const soundBtn = document.getElementById('btn-toggle-sound');
  if (soundBtn) {
    soundBtn.addEventListener('click', () => {
      state.soundEnabled = !state.soundEnabled;
      soundBtn.innerHTML = state.soundEnabled 
        ? '<i class="fa-solid fa-volume-high"></i> Audio: ON'
        : '<i class="fa-solid fa-volume-xmark"></i> Audio: OFF';
      soundFX.playClick();
    });
  }

  // Dosen Audio Lecture Hero Button
  const dosenBtn = document.getElementById('btn-dosen-lecture');
  if (dosenBtn) {
    dosenBtn.addEventListener('click', () => {
      triggerDosenTip();
    });
  }

  // Dosen Quick Tip Button
  const dosenTipBtn = document.getElementById('btn-dosen-tip');
  if (dosenTipBtn) {
    dosenTipBtn.addEventListener('click', () => {
      triggerDosenTip();
    });
  }

  // Keyboard navigation for Flashcards (Space to flip, Arrows to navigate)
  window.addEventListener('keydown', (e) => {
    if (state.currentTab === 'flashcards') {
      if (e.code === 'Space') {
        e.preventDefault();
        flipFlashcard();
      } else if (e.code === 'ArrowRight') {
        nextFlashcard();
      } else if (e.code === 'ArrowLeft') {
        prevFlashcard();
      }
    }
  });

  // Curriculum Live Search
  const searchInput = document.getElementById('module-search-input');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      filterCurriculum(e.target.value.toLowerCase());
    });
  }

  // Glossary Live Search
  const glossarySearch = document.getElementById('glossary-search-input');
  if (glossarySearch) {
    glossarySearch.addEventListener('input', (e) => {
      filterGlossary(e.target.value.toLowerCase());
    });
  }
}

function switchTab(tabId) {
  state.currentTab = tabId;

  document.querySelectorAll('.tab-btn').forEach(b => {
    b.classList.toggle('active', b.getAttribute('data-tab') === tabId);
  });

  document.querySelectorAll('.tab-pane').forEach(p => {
    p.classList.toggle('active', p.id === `pane-${tabId}`);
  });

  window.scrollTo({ top: 320, behavior: 'smooth' });
}

function updateStatsRibbon() {
  const learnedCount = state.learnedCards.size;
  const totalCards = FLASHCARDS.length;
  const pct = Math.round((learnedCount / totalCards) * 100);

  const learnedEl = document.getElementById('stat-learned-count');
  if (learnedEl) learnedEl.textContent = `${learnedCount} / ${totalCards}`;

  const pctEl = document.getElementById('stat-mastery-pct');
  if (pctEl) pctEl.textContent = `${pct}%`;

  const quizScoreEl = document.getElementById('stat-quiz-best');
  if (quizScoreEl) {
    const best = localStorage.getItem('minerapetro_best_score') || '0';
    quizScoreEl.textContent = `${best}%`;
  }
}

// ==========================================================================
// 6. MODULE & CURRICULUM RENDERER
// ==========================================================================
function renderChapters() {
  const container = document.getElementById('chapters-accordion');
  if (!container) return;

  container.innerHTML = CHAPTERS_DATA.map((ch, idx) => {
    let sectionsHtml = ch.sections.map(sec => {
      let content = '';
      if (sec.points) {
        content += `<ul class="subtopic-points">
          ${sec.points.map(pt => `<li>${pt}</li>`).join('')}
        </ul>`;
      }
      if (sec.table) {
        content += `<div class="table-responsive">
          <table class="curriculum-table">
            <thead>
              <tr>${sec.table.headers.map(h => `<th>${h}</th>`).join('')}</tr>
            </thead>
            <tbody>
              ${sec.table.rows.map(row => `<tr>${row.map(cell => `<td>${cell}</td>`).join('')}</tr>`).join('')}
            </tbody>
          </table>
        </div>`;
      }
      return `<div class="subtopic-block">
        <h5>${sec.heading}</h5>
        ${content}
      </div>`;
    }).join('');

    return `
      <div class="chapter-accordion-item ${idx === 0 ? 'open' : ''}" id="chap-card-${ch.id}" data-text="${(ch.title + ' ' + ch.overview).toLowerCase()}">
        <div class="chapter-header" onclick="toggleChapter('${ch.id}')">
          <div class="chapter-title-group">
            <div class="chap-num-badge" style="background: ${ch.color};">
              ${ch.number}
            </div>
            <div class="chap-text">
              <h4>
                ${ch.title}
                <span class="chap-badge">${ch.badge}</span>
              </h4>
              <p>${ch.overview}</p>
            </div>
          </div>
          <div class="chap-chevron">
            <i class="fa-solid fa-chevron-down"></i>
          </div>
        </div>
        <div class="chapter-body">
          <div class="lecturer-insight-box">
            <h5><i class="fa-solid fa-graduation-cap"></i> Catatan Kuliah Dosen Pengampu (Sundyo, S.T., M.T.)</h5>
            <p>${ch.lecturerNote}</p>
          </div>
          ${sectionsHtml}
        </div>
      </div>
    `;
  }).join('');
}

function toggleChapter(chapId) {
  soundFX.playClick();
  const el = document.getElementById(`chap-card-${chapId}`);
  if (el) {
    el.classList.toggle('open');
  }
}

function filterCurriculum(query) {
  const items = document.querySelectorAll('.chapter-accordion-item');
  items.forEach(it => {
    const text = it.getAttribute('data-text') || '';
    if (!query || text.includes(query)) {
      it.style.display = 'block';
    } else {
      it.style.display = 'none';
    }
  });
}

// ==========================================================================
// 7. FLASHCARDS 3D ENGINE
// ==========================================================================
function renderFlashcards() {
  const categories = ['ALL', ...new Set(FLASHCARDS.map(c => c.category))];
  const filterContainer = document.getElementById('fc-filter-container');

  if (filterContainer) {
    filterContainer.innerHTML = categories.map(cat => `
      <button class="btn-filter ${cat === state.flashcardCategory ? 'active' : ''}" onclick="filterFlashcardCategory('${cat}')">
        ${cat}
      </button>
    `).join('');
  }

  applyFlashcardFilter();
}

function filterFlashcardCategory(cat) {
  soundFX.playClick();
  state.flashcardCategory = cat;
  document.querySelectorAll('.btn-filter').forEach(b => {
    b.classList.toggle('active', b.textContent.trim() === cat);
  });
  applyFlashcardFilter();
}

function applyFlashcardFilter() {
  if (state.flashcardCategory === 'ALL') {
    state.filteredCards = [...FLASHCARDS];
  } else {
    state.filteredCards = FLASHCARDS.filter(c => c.category === state.flashcardCategory);
  }
  state.flashcardIndex = 0;
  displayCurrentFlashcard();
}

function displayCurrentFlashcard() {
  const card = state.filteredCards[state.flashcardIndex];
  if (!card) return;

  const cardElement = document.getElementById('main-flashcard');
  if (cardElement) cardElement.classList.remove('is-flipped');

  document.getElementById('fc-category-label').textContent = card.category;
  document.getElementById('fc-category-back').textContent = card.category;
  document.getElementById('fc-front-title').textContent = card.front;
  
  // Back text with linebreaks converted
  const backHtml = card.back.replace(/\n/g, '<br>');
  document.getElementById('fc-back-answer').innerHTML = backHtml;

  // Counter
  document.getElementById('fc-counter').textContent = `${state.flashcardIndex + 1} / ${state.filteredCards.length}`;

  // Check learned badge
  const isLearned = state.learnedCards.has(card.id);
  const learnedBadge = document.getElementById('fc-learned-badge');
  if (learnedBadge) {
    learnedBadge.style.display = isLearned ? 'inline-block' : 'none';
  }
}

function flipFlashcard() {
  soundFX.playFlip();
  const card = document.getElementById('main-flashcard');
  if (card) {
    card.classList.toggle('is-flipped');
  }
}

function nextFlashcard() {
  soundFX.playClick();
  if (state.flashcardIndex < state.filteredCards.length - 1) {
    state.flashcardIndex++;
  } else {
    state.flashcardIndex = 0; // loop
  }
  displayCurrentFlashcard();
}

function prevFlashcard() {
  soundFX.playClick();
  if (state.flashcardIndex > 0) {
    state.flashcardIndex--;
  } else {
    state.flashcardIndex = state.filteredCards.length - 1;
  }
  displayCurrentFlashcard();
}

function markCardLearned(learned) {
  const card = state.filteredCards[state.flashcardIndex];
  if (!card) return;

  if (learned) {
    soundFX.playCorrect();
    state.learnedCards.add(card.id);
  } else {
    soundFX.playIncorrect();
    state.learnedCards.delete(card.id);
  }

  localStorage.setItem('minerapetro_learned', JSON.stringify([...state.learnedCards]));
  updateStatsRibbon();
  nextFlashcard();
}

function shuffleFlashcards() {
  soundFX.playClick();
  for (let i = state.filteredCards.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [state.filteredCards[i], state.filteredCards[j]] = [state.filteredCards[j], state.filteredCards[i]];
  }
  state.flashcardIndex = 0;
  displayCurrentFlashcard();
}

function resetFlashcardsProgress() {
  if (confirm("Reset semua status hafalan flashcard?")) {
    state.learnedCards.clear();
    localStorage.removeItem('minerapetro_learned');
    updateStatsRibbon();
    displayCurrentFlashcard();
    soundFX.playClick();
  }
}

// ==========================================================================
// 8. MINI-GAME SKALA MOHS & PENGUJIAN LAPANGAN
// ==========================================================================
function renderMohsGame() {
  state.mohsSlots = Array(10).fill(null);
  // Shuffle minerals
  state.mohsAvailable = [...MOHS_SCALE_DRILL].sort(() => Math.random() - 0.5);

  renderMohsSlots();
  renderMohsPool();
  document.getElementById('mohs-result-banner').style.display = 'none';
}

function renderMohsSlots() {
  const container = document.getElementById('mohs-slots-container');
  if (!container) return;

  container.innerHTML = state.mohsSlots.map((item, idx) => {
    const scaleNum = idx + 1;
    let content = '<span style="color: #64748b; font-style: italic;">(Klik mineral di samping untuk menempatkan)</span>';
    if (item) {
      content = `
        <div style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
          <span><strong>${item.name}</strong> <small class="mineral-formula-tag">${item.formula}</small></span>
          <button onclick="removeMohsSlot(${idx})" style="background: none; border: none; color: #f43f5e; cursor: pointer; padding: 2px 6px;">
            <i class="fa-solid fa-xmark"></i>
          </button>
        </div>
      `;
    }
    return `
      <div class="mohs-slot" id="mohs-slot-${idx}" onclick="placeMineralIntoSlot(${idx})">
        <div class="slot-number">${scaleNum}</div>
        <div class="slot-content">${content}</div>
      </div>
    `;
  }).join('');
}

function renderMohsPool() {
  const pool = document.getElementById('mohs-chips-pool');
  if (!pool) return;

  pool.innerHTML = state.mohsAvailable.map(item => `
    <div class="mineral-draggable-chip ${state.selectedChip && state.selectedChip.scale === item.scale ? 'selected' : ''}" 
         onclick="selectMineralChip(${item.scale})">
      <span>${item.name}</span>
      <span class="mineral-formula-tag">${item.formula}</span>
    </div>
  `).join('');
}

function selectMineralChip(scale) {
  soundFX.playClick();
  const mineral = state.mohsAvailable.find(m => m.scale === scale);
  if (!mineral) return;

  state.selectedChip = mineral;
  renderMohsPool();

  // Find first empty slot automatically for convenience
  const emptyIdx = state.mohsSlots.findIndex(s => s === null);
  if (emptyIdx !== -1) {
    placeMineralIntoSlot(emptyIdx);
  }
}

function placeMineralIntoSlot(slotIndex) {
  if (!state.selectedChip) return;

  soundFX.playClick();
  // Place
  state.mohsSlots[slotIndex] = state.selectedChip;
  state.mohsAvailable = state.mohsAvailable.filter(m => m.scale !== state.selectedChip.scale);
  state.selectedChip = null;

  renderMohsSlots();
  renderMohsPool();
}

function removeMohsSlot(slotIndex) {
  soundFX.playClick();
  const mineral = state.mohsSlots[slotIndex];
  if (!mineral) return;

  state.mohsSlots[slotIndex] = null;
  state.mohsAvailable.push(mineral);
  renderMohsSlots();
  renderMohsPool();
}

function checkMohsOrder() {
  let correctCount = 0;
  state.mohsSlots.forEach((item, idx) => {
    const slotEl = document.getElementById(`mohs-slot-${idx}`);
    if (!slotEl) return;

    if (item && item.scale === idx + 1) {
      slotEl.className = 'mohs-slot slot-correct';
      correctCount++;
    } else {
      slotEl.className = 'mohs-slot slot-incorrect';
    }
  });

  const banner = document.getElementById('mohs-result-banner');
  banner.style.display = 'block';

  if (correctCount === 10) {
    soundFX.playFanfare();
    launchConfetti();
    banner.className = 'lecturer-insight-box';
    banner.style.borderColor = 'var(--emerald)';
    banner.innerHTML = `
      <h5 style="color: var(--emerald);"><i class="fa-solid fa-trophy"></i> SEMPURNA! 10 / 10 TEPAT!</h5>
      <p>Luar biasa! Anda telah menghafal seluruh urutan Skala Kekerasan Mohs 1-10 beserta rumus kimianya secara tepat sesuai standar laboratorium FT-UNIKARTA!</p>
    `;
  } else {
    soundFX.playIncorrect();
    banner.className = 'lecturer-insight-box';
    banner.style.borderColor = 'var(--ruby)';
    banner.innerHTML = `
      <h5 style="color: var(--ruby);"><i class="fa-solid fa-triangle-exclamation"></i> Skor: ${correctCount} / 10 Benar</h5>
      <p>Masih ada posisi yang tertukar. Perhatikan slot merah, klik tombol silang (x) untuk mencabut mineral dan susun kembali!</p>
    `;
  }
}

// ==========================================================================
// 9. RESPONSI & UJIAN PRAKTIKUM ENGINE
// ==========================================================================
function startQuiz(mode) {
  soundFX.playClick();
  state.quizMode = mode;
  let pool = [...QUIZ_QUESTIONS];

  // Shuffle pool
  pool.sort(() => Math.random() - 0.5);

  if (mode === 'pretest') {
    state.quizQuestions = pool.slice(0, 10);
  } else if (mode === 'standard') {
    state.quizQuestions = pool.slice(0, 25);
  } else {
    state.quizQuestions = pool; // all 60
  }

  state.quizCurrentIndex = 0;
  state.quizAnswers = Array(state.quizQuestions.length).fill(null);
  state.quizScore = 0;

  // UI Setup
  document.getElementById('quiz-setup-card').style.display = 'none';
  document.getElementById('quiz-active-view').style.display = 'block';
  document.getElementById('quiz-result-view').style.display = 'none';

  renderCurrentQuestion();
}

function renderCurrentQuestion() {
  const q = state.quizQuestions[state.quizCurrentIndex];
  if (!q) return;

  document.getElementById('quiz-progress-text').textContent = 
    `Soal ${state.quizCurrentIndex + 1} dari ${state.quizQuestions.length}`;
  document.getElementById('quiz-chapter-tag').textContent = q.chapter;
  document.getElementById('quiz-question-body').textContent = q.question;

  const optionsContainer = document.getElementById('quiz-options-container');
  const prefixes = ['A', 'B', 'C', 'D'];

  const answered = state.quizAnswers[state.quizCurrentIndex];

  optionsContainer.innerHTML = q.options.map((opt, idx) => {
    let classes = 'quiz-opt-btn';
    if (answered !== null) {
      if (idx === q.answerIndex) classes += ' opt-correct';
      else if (answered === idx) classes += ' opt-incorrect';
    }
    return `
      <button class="${classes}" onclick="handleQuizAnswer(${idx})" ${answered !== null ? 'disabled' : ''}>
        <div class="opt-prefix">${prefixes[idx]}</div>
        <div class="opt-text">${opt}</div>
      </button>
    `;
  }).join('');

  // Explanation box
  const explBox = document.getElementById('quiz-explanation-box');
  const nextBtn = document.getElementById('btn-quiz-next');

  if (answered !== null) {
    explBox.style.display = 'block';
    document.getElementById('quiz-expl-text').textContent = q.explanation;
    nextBtn.style.display = 'inline-flex';
    nextBtn.textContent = state.quizCurrentIndex === state.quizQuestions.length - 1 
      ? 'Selesaikan Ujian & Lihat Nilai' 
      : 'Soal Selanjutnya ❯';
  } else {
    explBox.style.display = 'none';
    nextBtn.style.display = 'none';
  }
}

function handleQuizAnswer(selectedIndex) {
  const q = state.quizQuestions[state.quizCurrentIndex];
  if (!q) return;

  state.quizAnswers[state.quizCurrentIndex] = selectedIndex;

  if (selectedIndex === q.answerIndex) {
    soundFX.playCorrect();
    state.quizScore++;
  } else {
    soundFX.playIncorrect();
  }

  renderCurrentQuestion();
}

function nextQuizQuestion() {
  soundFX.playClick();
  if (state.quizCurrentIndex < state.quizQuestions.length - 1) {
    state.quizCurrentIndex++;
    renderCurrentQuestion();
  } else {
    finishQuiz();
  }
}

function finishQuiz() {
  document.getElementById('quiz-active-view').style.display = 'none';
  document.getElementById('quiz-result-view').style.display = 'block';

  const total = state.quizQuestions.length;
  const score = state.quizScore;
  const pct = Math.round((score / total) * 100);

  // Update best score in storage
  const prevBest = parseInt(localStorage.getItem('minerapetro_best_score') || '0', 10);
  if (pct > prevBest) {
    localStorage.setItem('minerapetro_best_score', pct.toString());
  }
  updateStatsRibbon();

  // Score UI
  document.getElementById('cert-score-value').textContent = pct;
  document.getElementById('cert-correct-stat').textContent = `${score} dari ${total} Soal Benar`;

  const badgeEl = document.getElementById('cert-grade-badge');
  const verdictEl = document.getElementById('cert-verdict-text');

  if (pct >= 85) {
    soundFX.playFanfare();
    launchConfetti();
    badgeEl.className = 'cert-grade-badge grade-a';
    badgeEl.textContent = 'GRADE A (SANGAT MEMUASKAN / CUM LAUDE)';
    verdictEl.textContent = 'Selamat! Anda menguasai seluruh materi modul Mineralogi & Petrologi dengan sangat luar biasa! Anda siap 100% menghadapi responsi laboratorium praktikum.';
  } else if (pct >= 70) {
    soundFX.playFanfare();
    badgeEl.className = 'cert-grade-badge grade-b';
    badgeEl.textContent = 'GRADE B (LULUS MEMUASKAN)';
    verdictEl.textContent = 'Bagus sekali! Pemahaman teori dan konsep batuan Anda telah memenuhi kriteria kelulusan praktikum pertambangan.';
  } else if (pct >= 55) {
    soundFX.playClick();
    badgeEl.className = 'cert-grade-badge grade-c';
    badgeEl.textContent = 'GRADE C (CUKUP)';
    verdictEl.textContent = 'Anda lulus dengan batas nilai cukup. Disarankan untuk memperdalam lagi hafalan 7 sistem kristal dan struktur sedimen!';
  } else {
    soundFX.playIncorrect();
    badgeEl.className = 'cert-grade-badge grade-d';
    badgeEl.textContent = 'GRADE D / E (WAJIB REMEDI RESPONSI)';
    verdictEl.textContent = 'Nilai Anda belum memenuhi batas kelulusan praktikum. Silakan manfaatkan fitur Flashcards 3D dan Kuliah Teori untuk memperkuat hafalan sebelum mengulang responsi!';
  }
}

function restartQuiz() {
  soundFX.playClick();
  document.getElementById('quiz-setup-card').style.display = 'block';
  document.getElementById('quiz-active-view').style.display = 'none';
  document.getElementById('quiz-result-view').style.display = 'none';
}

// ==========================================================================
// 10. GLOSARIUM & KAMUS TAMBANG
// ==========================================================================
const GLOSSARY_ITEMS = [
  { term: "Mineral", cat: "Konsep Dasar", def: "Zat padat homogen, terjadi alamiah, anorganik, dengan komposisi kimia dan susunan atom beraturan." },
  { term: "Petrologi", cat: "Konsep Dasar", def: "Ilmu yang membahas pembentukan batuan, struktur, tekstur, komposisi mineral, dan evolusinya (Yunani: petra = batu)." },
  { term: "Batuan Beku", cat: "Petrologi", def: "Interlocking agregat mineral silikat hasil pembekuan lelehan magma pijar (Latin: igneus = api)." },
  { term: "Batuan Sedimen Klastik", cat: "Sedimen", def: "Batuan hasil pengerjaan kembali (reworking: pelapukan, erosi, transportasi, redeposisi, litifikasi) batuan asal." },
  { term: "Batuan Metamorf", cat: "Metamorf", def: "Perubahan tekstur dan komposisi mineral batuan induk pada fase padat akibat tekanan (P) dan suhu (T)." },
  { term: "Deret Bowen", cat: "Mineralogi", def: "Urutan kristalisasi mineral silikat primer dari magma (Diskontinu: Olivin-Piroksen-Amfibol-Biotit; Kontinu: Anortit-Albit)." },
  { term: "Ferromagnesian", cat: "Silikat", def: "Mineral silikat kaya ion Fe dan Mg, berwarna gelap, BJ 3,2 - 3,6 (Olivin, Piroksen, Amfibol, Biotit)." },
  { term: "Non-Ferromagnesian", cat: "Silikat", def: "Mineral silikat tanpa Fe dan Mg, berwarna terang, BJ ~2,7 (Kuarsa, Ortoklas, Muskovit)." },
  { term: "Pecahan Konkoidal", cat: "Sifat Fisik", def: "Permukaan pecahan melengkung seperti cangkang kerang atau botol pecah (contoh: Kuarsa, Kalsedon)." },
  { term: "Tenacity", cat: "Sifat Fisik", def: "Daya tahan mineral terhadap pembengkokan, pematahan, pengirisan, atau penempaan (Brittle, Fleksibel, Elastis, Daktil, Sektil, Malleable)." },
  { term: "Isometrik", cat: "Kristalografi", def: "Sistem kristal kubus: a = b = c dan α = β = γ = 90° (Emas, Pirit, Galena, Halit)." },
  { term: "Tetragonal", cat: "Kristalografi", def: "Sistem kristal: a = b ≠ c dan α = β = γ = 90° (Rutil, Autunit, Pirolusit)." },
  { term: "Hexagonal", cat: "Kristalografi", def: "Sistem kristal 4 sumbu: a = b = d ≠ c dan α = β = 90°, γ = 120° (Kuarsa, Korundum, Kalsit)." },
  { term: "Orthorhombik", cat: "Kristalografi", def: "Sistem kristal rhombis: a ≠ b ≠ c dan α = β = γ = 90° (Stibnit, Aragonit, Topaz)." },
  { term: "Monoklin", cat: "Kristalografi", def: "Sistem kristal: a ≠ b ≠ c dan α = β = 90° ≠ γ (sudut miring: Gypsum, Azurit, Malakit)." },
  { term: "Triklin", cat: "Kristalografi", def: "Sistem kristal paling asimetris: a ≠ b ≠ c dan α ≠ β ≠ γ ≠ 90° (Albit, Anortit, Kaolinit)." },
  { term: "Faneritik", cat: "Tekstur Beku", def: "Tekstur batuan beku dengan butiran kristal berukuran kasar yang dapat dibedakan mata langsung." },
  { term: "Afanitik", cat: "Tekstur Beku", def: "Tekstur batuan beku dengan butiran sangat halus yang tidak dapat dibedakan dengan mata telanjang." },
  { term: "Holokristalin", cat: "Tekstur Beku", def: "Derajat kristalisasi di mana seluruh massa batuan tersusun oleh kristal." },
  { term: "Holohyalin", cat: "Tekstur Beku", def: "Derajat kristalisasi di mana hampir seluruh batuan tersusun oleh kaca/gelas vulkanik." },
  { term: "Leucocratic", cat: "Batuan Beku", def: "Batuan beku dengan kandungan mineral mafik kurang dari 30% (< 30%)." },
  { term: "Melanocratic", cat: "Batuan Beku", def: "Batuan beku dengan kandungan mineral mafik antara 60% sampai 90%." },
  { term: "Graded Bedding", cat: "Struktur Sedimen", def: "Perlapisan bersusun dengan gradasi ukuran butir vertikal (normal grading: bawah kasar, atas halus)." },
  { term: "Cross Bedding", cat: "Struktur Sedimen", def: "Perlapisan silang siur bersudut miring dengan ketebalan > 5 cm akibat migrasi duna/arus." },
  { term: "Flute Cast", cat: "Struktur Sedimen", def: "Gerusan celah terputus/kantong 2-10 cm akibat arus turbulen terisi pasir pada batuan dasar." },
  { term: "Flame Structure", cat: "Struktur Sedimen", def: "Tonjolan lumpur menyembul ke dalam lapisan batupasir menyerupai lidah api akibat pembebanan dan gaya lateral." },
  { term: "Mud Cracks", cat: "Struktur Sedimen", def: "Retakan poligonal bersegi lima pada lumpur basah yang mengering akibat penguapan dan penyusutan." },
  { term: "Slaty Cleavage", cat: "Struktur Metamorf", def: "Struktur foliasi mikrokristalin dengan belahan planar sangat rapat, teratur, dan sejajar (Batusabak/Slate)." },
  { term: "Phyllitic", cat: "Struktur Metamorf", def: "Foliasi metamorf dengan rekristalisasi lebih besar dari slate dan menampakkan kilap sutera (Filit)." },
  { term: "Schistosic", cat: "Struktur Metamorf", def: "Struktur foliasi penjajaran paralel mineral pipih/prismatik mika berbutir sedang-kasar (Sekis)." },
  { term: "Gneissic", cat: "Struktur Metamorf", def: "Foliasi pita selang-seling terputus antara mineral granular terang dan mineral mafik gelap (Gneis)." },
  { term: "Hornfelsic", cat: "Struktur Metamorf", def: "Struktur non-foliasi mosaik poligonal seragam hasil metamorfosa termal kontak (Batu Tanduk/Hornfels)." },
  { term: "Mylonitic", cat: "Struktur Metamorf", def: "Struktur non-foliasi hasil penggerusan mekanik hebat berbutir sangat halus dan goresan searah (Milonit)." },
  { term: "Lepidoblastik", cat: "Tekstur Metamorf", def: "Tekstur metamorf didominasi mineral berbentuk pipih/tabular seperti mika." },
  { term: "Nematoblastik", cat: "Tekstur Metamorf", def: "Tekstur metamorf didominasi mineral berbentuk prismatik/jarum seperti amfibol." },
  { term: "Poikiloblastik", cat: "Tekstur Metamorf", def: "Porfiroblas kristal besar melingkupi butiran-butiran kristal kecil menyerupai saringan (sieve texture)." }
];

function renderGlossary() {
  const container = document.getElementById('glossary-grid');
  if (!container) return;

  container.innerHTML = GLOSSARY_ITEMS.map(item => `
    <div class="glossary-card" data-text="${(item.term + ' ' + item.def + ' ' + item.cat).toLowerCase()}">
      <div class="glossary-term">
        <span>${item.term}</span>
        <span class="glossary-cat">${item.cat}</span>
      </div>
      <div class="glossary-def">${item.def}</div>
    </div>
  `).join('');
}

function filterGlossary(query) {
  const cards = document.querySelectorAll('.glossary-card');
  cards.forEach(card => {
    const text = card.getAttribute('data-text') || '';
    if (!query || text.includes(query)) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}
