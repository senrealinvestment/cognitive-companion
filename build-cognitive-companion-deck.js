const pptxgen = require("pptxgenjs");
const path = require("path");

const pres = new pptxgen();
pres.defineLayout({ name: "WIDE16x9", width: 10, height: 5.625 });
pres.layout = "WIDE16x9";
pres.author = "Sergio Navarrete, MD · VCU Anesthesiology";
pres.title = "Cognitive Companion";
pres.subject =
  "Camera-free smart-glasses cognitive companion for critical care simulation";

// Palette — clinical night + mint pulse
const C = {
  ink: "071A22",
  deep: "0B2834",
  panel: "0F3442",
  teal: "0E7490",
  mint: "2DD4BF",
  mintSoft: "99F6E4",
  ice: "E8F7F6",
  paper: "F8FBFC",
  white: "FFFFFF",
  slate: "334155",
  muted: "64748B",
  soft: "94A3B8",
  card: "FFFFFF",
  line: "D1E7E7",
  warn: "F59E0B",
  danger: "E11D48",
  ok: "059669",
};

const shadowSoft = () => ({
  type: "outer",
  color: "071A22",
  blur: 10,
  offset: 3,
  opacity: 0.12,
});

function addDarkBg(slide) {
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0,
    y: 0,
    w: 10,
    h: 5.625,
    fill: { color: C.ink },
    line: { color: C.ink },
  });
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 7.2,
    y: 0,
    w: 2.8,
    h: 5.625,
    fill: { color: C.deep },
    line: { color: C.deep },
  });
}

function addLightBg(slide) {
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0,
    y: 0,
    w: 10,
    h: 5.625,
    fill: { color: C.paper },
    line: { color: C.paper },
  });
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0,
    y: 0,
    w: 10,
    h: 0.08,
    fill: { color: C.teal },
    line: { color: C.teal },
  });
}

function footer(slide, n, dark = false) {
  slide.addText(
    "Cognitive Companion  ·  VCU Anesthesiology  ·  Sim-first  ·  Camera-free",
    {
      x: 0.45,
      y: 5.28,
      w: 7.8,
      h: 0.22,
      fontSize: 10,
      fontFace: "Calibri",
      color: dark ? C.soft : C.muted,
      margin: 0,
    }
  );
  slide.addText(String(n), {
    x: 9.1,
    y: 5.28,
    w: 0.5,
    h: 0.22,
    fontSize: 10,
    fontFace: "Calibri",
    color: dark ? C.soft : C.muted,
    align: "right",
    margin: 0,
  });
}

function sectionLabel(slide, text, x = 0.5, y = 0.28) {
  slide.addText(text.toUpperCase(), {
    x,
    y,
    w: 9,
    h: 0.26,
    fontSize: 11,
    fontFace: "Calibri",
    bold: true,
    color: C.teal,
    charSpacing: 2,
    margin: 0,
  });
}

// ═══════════════════════════════════════════════════════════
// 1 — Title
// ═══════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  addDarkBg(s);

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 0.5,
    y: 1.25,
    w: 0.55,
    h: 0.12,
    fill: { color: C.mint },
    line: { color: C.mint },
    rectRadius: 0.06,
  });

  s.addText("COGNITIVE COMPANION", {
    x: 0.5,
    y: 1.55,
    w: 6.5,
    h: 0.65,
    fontSize: 34,
    fontFace: "Arial",
    bold: true,
    color: C.white,
    margin: 0,
  });

  s.addText(
    "Camera-free smart-glasses ambient AI\nfor critical care simulation",
    {
      x: 0.5,
      y: 2.3,
      w: 6.3,
      h: 0.75,
      fontSize: 17,
      fontFace: "Calibri",
      color: C.mintSoft,
      margin: 0,
    }
  );

  s.addText(
    "Real-time protocol cues  ·  Human remains decision-maker  ·  Closed quality loop",
    {
      x: 0.5,
      y: 3.25,
      w: 6.3,
      h: 0.35,
      fontSize: 13,
      fontFace: "Calibri",
      color: C.soft,
      margin: 0,
    }
  );

  const facts = [
    { k: "Stage", v: "Sim lab pilot" },
    { k: "Design law", v: "No wearable camera" },
    { k: "Home", v: "VCU Anesthesiology" },
    { k: "Ask", v: "$12.5k preferred" },
  ];
  facts.forEach((f, i) => {
    const y = 1.05 + i * 0.9;
    s.addText(f.k.toUpperCase(), {
      x: 7.45,
      y,
      w: 2.2,
      h: 0.22,
      fontSize: 10,
      fontFace: "Calibri",
      bold: true,
      color: C.mint,
      charSpacing: 1.2,
      margin: 0,
    });
    s.addText(f.v, {
      x: 7.45,
      y: y + 0.26,
      w: 2.2,
      h: 0.35,
      fontSize: 15,
      fontFace: "Calibri",
      color: C.white,
      margin: 0,
    });
  });

  s.addText("Cognitive Companion  ·  July 2026", {
    x: 0.5,
    y: 5.15,
    w: 6,
    h: 0.25,
    fontSize: 11,
    fontFace: "Calibri",
    color: C.soft,
    margin: 0,
  });
}

// ═══════════════════════════════════════════════════════════
// 2 — Problem
// ═══════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  addLightBg(s);
  sectionLabel(s, "The problem");
  s.addText("Crisis collapses bandwidth", {
    x: 0.5,
    y: 0.55,
    w: 9,
    h: 0.45,
    fontSize: 28,
    fontFace: "Arial",
    bold: true,
    color: C.ink,
    margin: 0,
  });

  const problems = [
    {
      t: "Freeze & fixation",
      d: "Learners stall or tunnel under load. Attendings carry the full cognitive stack.",
      accent: C.teal,
    },
    {
      t: "Delayed, uneven debrief",
      d: "Feedback arrives after the moment. Protocol checks are hard to rehearse at tempo.",
      accent: C.teal,
    },
    {
      t: "Wearable video is a non-starter",
      d: "Face-worn cameras in any ICU are a PHI, consent, and culture problem.",
      accent: C.danger,
    },
    {
      t: "Rare high-stakes events",
      d: "Tx ICU decompensations need reproducible teaching — starting with reperfusion instability.",
      accent: C.teal,
    },
  ];

  problems.forEach((p, i) => {
    const col = i % 2;
    const row = Math.floor(i / 2);
    const x = 0.5 + col * 4.6;
    const y = 1.25 + row * 1.75;

    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x,
      y,
      w: 4.35,
      h: 1.55,
      fill: { color: C.card },
      line: { color: C.line },
      rectRadius: 0.1,
      shadow: shadowSoft(),
    });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: x + 0.25,
      y: y + 0.3,
      w: 0.14,
      h: 0.14,
      fill: { color: p.accent },
      line: { color: p.accent },
      rectRadius: 0.04,
    });
    s.addText(p.t, {
      x: x + 0.55,
      y: y + 0.22,
      w: 3.5,
      h: 0.35,
      fontSize: 16,
      fontFace: "Arial",
      bold: true,
      color: C.ink,
      margin: 0,
    });
    s.addText(p.d, {
      x: x + 0.25,
      y: y + 0.7,
      w: 3.85,
      h: 0.65,
      fontSize: 14,
      fontFace: "Calibri",
      color: C.slate,
      margin: 0,
    });
  });

  footer(s, 2);
}

// ═══════════════════════════════════════════════════════════
// 3 — Solution
// ═══════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  addLightBg(s);
  sectionLabel(s, "The solution");
  s.addText("A pocket protocol whisper — not an AI intensivist", {
    x: 0.5,
    y: 0.55,
    w: 9,
    h: 0.45,
    fontSize: 24,
    fontFace: "Arial",
    bold: true,
    color: C.ink,
    margin: 0,
  });

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 0.5,
    y: 1.15,
    w: 9,
    h: 1.2,
    fill: { color: C.deep },
    line: { color: C.deep },
    rectRadius: 0.1,
  });
  s.addText(
    "Ambient audio from clinician glasses (or phone) feeds a local protocol brain on a nearby phone/iPad that delivers a discrete cue — short HUD text + tone. The clinician acts. We log whether the cue was helpful and accurate for offline training.",
    {
      x: 0.75,
      y: 1.35,
      w: 8.5,
      h: 0.85,
      fontSize: 15,
      fontFace: "Calibri",
      color: C.white,
      margin: 0,
    }
  );

  // IS column
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 0.5,
    y: 2.55,
    w: 4.35,
    h: 2.4,
    fill: { color: C.card },
    line: { color: C.line },
    rectRadius: 0.1,
    shadow: shadowSoft(),
  });
  s.addText("IS", {
    x: 0.75,
    y: 2.75,
    w: 3.8,
    h: 0.3,
    fontSize: 14,
    fontFace: "Arial",
    bold: true,
    color: C.ok,
    margin: 0,
  });
  [
    "Cognitive forcing for decompensations",
    "Sim + learners first",
    "Camera-free wearable path",
    "Closed cue-quality loop",
  ].forEach((item, j) => {
    s.addShape(pres.shapes.OVAL, {
      x: 0.8,
      y: 3.25 + j * 0.38,
      w: 0.12,
      h: 0.12,
      fill: { color: C.ok },
      line: { color: C.ok },
    });
    s.addText(item, {
      x: 1.1,
      y: 3.15 + j * 0.38,
      w: 3.4,
      h: 0.32,
      fontSize: 14,
      fontFace: "Calibri",
      color: C.slate,
      margin: 0,
    });
  });

  // IS NOT column
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 5.15,
    y: 2.55,
    w: 4.35,
    h: 2.4,
    fill: { color: C.card },
    line: { color: C.line },
    rectRadius: 0.1,
    shadow: shadowSoft(),
  });
  s.addText("IS NOT", {
    x: 5.4,
    y: 2.75,
    w: 3.8,
    h: 0.3,
    fontSize: 14,
    fontFace: "Arial",
    bold: true,
    color: C.danger,
    margin: 0,
  });
  [
    "Body-worn video surveillance",
    "Autodiagnosis or auto orders",
    "Always-on cloud wiretap",
    "A replacement for judgment",
  ].forEach((item, j) => {
    s.addShape(pres.shapes.OVAL, {
      x: 5.45,
      y: 3.25 + j * 0.38,
      w: 0.12,
      h: 0.12,
      fill: { color: C.danger },
      line: { color: C.danger },
    });
    s.addText(item, {
      x: 5.75,
      y: 3.15 + j * 0.38,
      w: 3.4,
      h: 0.32,
      fontSize: 14,
      fontFace: "Calibri",
      color: C.slate,
      margin: 0,
    });
  });

  footer(s, 3);
}

// ═══════════════════════════════════════════════════════════
// 4 — Product loop
// ═══════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  addLightBg(s);
  sectionLabel(s, "Product physics");
  s.addText("Sense → Reason → Cue → Act → Label → Train", {
    x: 0.5,
    y: 0.55,
    w: 9,
    h: 0.45,
    fontSize: 24,
    fontFace: "Arial",
    bold: true,
    color: C.ink,
    margin: 0,
  });

  const stages = [
    {
      n: "01",
      t: "Sense",
      d: "Ambient listening via glasses mics and/or phone. Gated when possible.",
    },
    {
      n: "02",
      t: "Reason",
      d: "Cognitive-forcing suggestion. Local protocol pack first; evidence API second.",
    },
    {
      n: "03",
      t: "Cue",
      d: "Tone + ≤8-word HUD text. Discrete in ICU. No free-form speech during crisis.",
    },
    {
      n: "04",
      t: "Act",
      d: "Natural verbal response or clinical action. Human remains decision-maker.",
    },
    {
      n: "05",
      t: "Label",
      d: "Helpful? Accurate? Cost / latency? Required for every fired cue eventually.",
    },
    {
      n: "06",
      t: "Train",
      d: "Offline policy / model update. Never silent online self-mod at bedside.",
    },
  ];

  stages.forEach((st, i) => {
    const col = i % 3;
    const row = Math.floor(i / 3);
    const x = 0.5 + col * 3.1;
    const y = 1.2 + row * 1.85;

    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x,
      y,
      w: 2.95,
      h: 1.65,
      fill: { color: C.card },
      line: { color: C.line },
      rectRadius: 0.1,
      shadow: shadowSoft(),
    });
    s.addText(st.n, {
      x: x + 0.2,
      y: y + 0.18,
      w: 2.5,
      h: 0.28,
      fontSize: 12,
      fontFace: "Calibri",
      bold: true,
      color: C.teal,
      margin: 0,
    });
    s.addText(st.t, {
      x: x + 0.2,
      y: y + 0.48,
      w: 2.5,
      h: 0.32,
      fontSize: 18,
      fontFace: "Arial",
      bold: true,
      color: C.ink,
      margin: 0,
    });
    s.addText(st.d, {
      x: x + 0.2,
      y: y + 0.9,
      w: 2.55,
      h: 0.55,
      fontSize: 12,
      fontFace: "Calibri",
      color: C.slate,
      margin: 0,
    });
  });

  footer(s, 4);
}

// ═══════════════════════════════════════════════════════════
// 5 — Architecture (3 layers)
// ═══════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  addLightBg(s);
  sectionLabel(s, "Architecture");
  s.addText("Where the brain lives", {
    x: 0.5,
    y: 0.55,
    w: 9,
    h: 0.4,
    fontSize: 28,
    fontFace: "Arial",
    bold: true,
    color: C.ink,
    margin: 0,
  });

  const layers = [
    {
      n: "1",
      title: "Glasses",
      sub: "Thin wearable",
      job: "Hear the room + show/play short cue. Tiny computer. No camera.",
      hw: "Display + mics (+ bone conduction)",
      color: C.teal,
    },
    {
      n: "2",
      title: "Edge brain",
      sub: "Phone / iPad nearby",
      job: "Real-time gate → local protocols → safety → send cue. Label taps after.",
      hw: "iPhone or iPad in pocket / belt",
      color: C.deep,
    },
    {
      n: "3",
      title: "Deep consult",
      sub: "Optional cloud",
      job: "Broader evidence on demand — stripped questions, not room audio dumps.",
      hw: "OpenEvidence / UpToDate-class APIs",
      color: C.muted,
    },
  ];

  layers.forEach((L, i) => {
    const x = 0.5 + i * 3.1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x,
      y: 1.15,
      w: 2.95,
      h: 3.7,
      fill: { color: C.card },
      line: { color: C.line },
      rectRadius: 0.12,
      shadow: shadowSoft(),
    });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: x + 0.25,
      y: 1.4,
      w: 0.55,
      h: 0.55,
      fill: { color: L.color },
      line: { color: L.color },
      rectRadius: 0.1,
    });
    s.addText(L.n, {
      x: x + 0.25,
      y: 1.48,
      w: 0.55,
      h: 0.4,
      fontSize: 18,
      fontFace: "Arial",
      bold: true,
      color: C.white,
      align: "center",
      margin: 0,
    });
    s.addText(L.title, {
      x: x + 0.25,
      y: 2.15,
      w: 2.45,
      h: 0.35,
      fontSize: 20,
      fontFace: "Arial",
      bold: true,
      color: C.ink,
      margin: 0,
    });
    s.addText(L.sub, {
      x: x + 0.25,
      y: 2.5,
      w: 2.45,
      h: 0.3,
      fontSize: 13,
      fontFace: "Calibri",
      color: C.teal,
      margin: 0,
    });
    s.addText(L.job, {
      x: x + 0.25,
      y: 3.0,
      w: 2.45,
      h: 1.0,
      fontSize: 13,
      fontFace: "Calibri",
      color: C.slate,
      margin: 0,
    });
    s.addText(L.hw, {
      x: x + 0.25,
      y: 4.2,
      w: 2.45,
      h: 0.45,
      fontSize: 12,
      fontFace: "Calibri",
      bold: true,
      color: C.ink,
      margin: 0,
    });
  });

  footer(s, 5);
}

// ═══════════════════════════════════════════════════════════
// 6 — Design law: no camera
// ═══════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  addLightBg(s);
  sectionLabel(s, "Design law");
  s.addText("No wearable camera in v1", {
    x: 0.5,
    y: 0.55,
    w: 9,
    h: 0.45,
    fontSize: 28,
    fontFace: "Arial",
    bold: true,
    color: C.ink,
    margin: 0,
  });

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 0.5,
    y: 1.15,
    w: 9,
    h: 1.0,
    fill: { color: "FEF2F2" },
    line: { color: "FECACA" },
    rectRadius: 0.1,
  });
  s.addText(
    "A face-worn camera in any ICU is a PHI + consent + culture problem — not just a tech feature. v1 senses with sound only.",
    {
      x: 0.75,
      y: 1.35,
      w: 8.5,
      h: 0.65,
      fontSize: 15,
      fontFace: "Calibri",
      color: C.ink,
      margin: 0,
    }
  );

  const reasons = [
    {
      t: "Consent optics",
      d: "Patients, families, and staff enter frame without clean consent paths.",
    },
    {
      t: "IRB / compliance",
      d: "Harder approvals and unit questions: “what is that recording?”",
    },
    {
      t: "v0 value path",
      d: "Speech + protocol context carry the trigger. Vision can wait for a separate program.",
    },
  ];

  reasons.forEach((r, i) => {
    const x = 0.5 + i * 3.1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x,
      y: 2.4,
      w: 2.95,
      h: 2.35,
      fill: { color: C.card },
      line: { color: C.line },
      rectRadius: 0.1,
      shadow: shadowSoft(),
    });
    s.addText(String(i + 1).padStart(2, "0"), {
      x: x + 0.25,
      y: 2.65,
      w: 2.4,
      h: 0.3,
      fontSize: 12,
      fontFace: "Calibri",
      bold: true,
      color: C.danger,
      margin: 0,
    });
    s.addText(r.t, {
      x: x + 0.25,
      y: 3.05,
      w: 2.45,
      h: 0.4,
      fontSize: 16,
      fontFace: "Arial",
      bold: true,
      color: C.ink,
      margin: 0,
    });
    s.addText(r.d, {
      x: x + 0.25,
      y: 3.55,
      w: 2.45,
      h: 0.9,
      fontSize: 13,
      fontFace: "Calibri",
      color: C.slate,
      margin: 0,
    });
  });

  footer(s, 6);
}

// ═══════════════════════════════════════════════════════════
// 7 — Hardware
// ═══════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  addLightBg(s);
  sectionLabel(s, "Hardware");
  s.addText("Three paths — start before glasses arrive", {
    x: 0.5,
    y: 0.55,
    w: 9,
    h: 0.4,
    fontSize: 24,
    fontFace: "Arial",
    bold: true,
    color: C.ink,
    margin: 0,
  });

  const hw = [
    {
      path: "PILOT LEAN",
      name: "Brilliant Labs Halo",
      tag: "Camera hard-off",
      points: [
        "Open stack + SDKs",
        "Onboard bone conduction",
        "HUD + mics included",
        "Camera powered off in clinical/sim profile",
      ],
      accent: C.deep,
    },
    {
      path: "PRIVACY-NATIVE",
      name: "Even Realities G2",
      tag: "No camera by design",
      points: [
        "Strong discrete text HUD",
        "Four mics",
        "No onboard speakers",
        "Tone via phone / BC earbuds",
      ],
      accent: C.teal,
    },
    {
      path: "DAY ONE",
      name: "Phone only",
      tag: "Valid sim path",
      points: [
        "Mic + headphones",
        "On-screen mock HUD",
        "Same label metrics",
        "No hardware delay risk",
      ],
      accent: C.ok,
    },
  ];

  hw.forEach((h, i) => {
    const x = 0.5 + i * 3.1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x,
      y: 1.15,
      w: 2.95,
      h: 3.7,
      fill: { color: C.card },
      line: { color: C.line },
      rectRadius: 0.12,
      shadow: shadowSoft(),
    });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x,
      y: 1.15,
      w: 2.95,
      h: 0.9,
      fill: { color: h.accent },
      line: { color: h.accent },
      rectRadius: 0.12,
    });
    // cover bottom radius of header
    s.addShape(pres.shapes.RECTANGLE, {
      x,
      y: 1.75,
      w: 2.95,
      h: 0.3,
      fill: { color: h.accent },
      line: { color: h.accent },
    });
    s.addText(h.path, {
      x: x + 0.2,
      y: 1.28,
      w: 2.55,
      h: 0.25,
      fontSize: 11,
      fontFace: "Calibri",
      bold: true,
      color: C.mintSoft,
      charSpacing: 1,
      margin: 0,
    });
    s.addText(h.name, {
      x: x + 0.2,
      y: 1.55,
      w: 2.55,
      h: 0.35,
      fontSize: 15,
      fontFace: "Arial",
      bold: true,
      color: C.white,
      margin: 0,
    });
    s.addText(h.tag, {
      x: x + 0.2,
      y: 2.25,
      w: 2.55,
      h: 0.3,
      fontSize: 13,
      fontFace: "Calibri",
      bold: true,
      color: h.accent,
      margin: 0,
    });
    h.points.forEach((p, j) => {
      s.addShape(pres.shapes.OVAL, {
        x: x + 0.25,
        y: 2.8 + j * 0.42,
        w: 0.1,
        h: 0.1,
        fill: { color: h.accent },
        line: { color: h.accent },
      });
      s.addText(p, {
        x: x + 0.5,
        y: 2.7 + j * 0.42,
        w: 2.2,
        h: 0.35,
        fontSize: 13,
        fontFace: "Calibri",
        color: C.slate,
        margin: 0,
      });
    });
  });

  footer(s, 7);
}

// ═══════════════════════════════════════════════════════════
// 8 — MVP & pilot
// ═══════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  addLightBg(s);
  sectionLabel(s, "12-month pilot");
  s.addText("What we build in the sim lab", {
    x: 0.5,
    y: 0.55,
    w: 9,
    h: 0.4,
    fontSize: 26,
    fontFace: "Arial",
    bold: true,
    color: C.ink,
    margin: 0,
  });

  const mvp = [
    { t: "Sim-only platform", d: "Gated audio → phone edge brain → HUD + tone" },
    {
      t: "Local protocol pack",
      d: "VCU / Tx ICU cards — not cloud-only “AI doctor”",
    },
    {
      t: "Safety rules",
      d: "Advisory language · no orders · camera hard-off",
    },
    {
      t: "Label loop",
      d: "After each scenario: Helpful? Accurate? + short note",
    },
    {
      t: "Metrics",
      d: "Latency · %helpful · %accurate · on vs off preference",
    },
    {
      t: "Year-1 exit",
      d: "Prefer ON on ≥1 scenario class · no harmful action increase · abstract draft",
    },
  ];

  mvp.forEach((m, i) => {
    const col = i % 3;
    const row = Math.floor(i / 3);
    const x = 0.5 + col * 3.1;
    const y = 1.15 + row * 1.85;

    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x,
      y,
      w: 2.95,
      h: 1.65,
      fill: { color: C.card },
      line: { color: C.line },
      rectRadius: 0.1,
      shadow: shadowSoft(),
    });
    s.addText(String(i + 1).padStart(2, "0"), {
      x: x + 0.22,
      y: y + 0.22,
      w: 2.5,
      h: 0.28,
      fontSize: 12,
      fontFace: "Calibri",
      bold: true,
      color: C.teal,
      margin: 0,
    });
    s.addText(m.t, {
      x: x + 0.22,
      y: y + 0.55,
      w: 2.5,
      h: 0.35,
      fontSize: 15,
      fontFace: "Arial",
      bold: true,
      color: C.ink,
      margin: 0,
    });
    s.addText(m.d, {
      x: x + 0.22,
      y: y + 1.0,
      w: 2.5,
      h: 0.45,
      fontSize: 13,
      fontFace: "Calibri",
      color: C.slate,
      margin: 0,
    });
  });

  footer(s, 8);
}

// ═══════════════════════════════════════════════════════════
// 9 — Team + Ask
// ═══════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  addLightBg(s);
  sectionLabel(s, "Team & ask");
  s.addText("VCU Anesthesiology simulation pilot", {
    x: 0.5,
    y: 0.55,
    w: 9,
    h: 0.4,
    fontSize: 24,
    fontFace: "Arial",
    bold: true,
    color: C.ink,
    margin: 0,
  });

  // Team cards
  const team = [
    { role: "PI / Clinical lead", name: "Sergio Navarrete, MD", note: "Tx ICU design · protocols · scholarly output" },
    { role: "Sim lab / Education", name: "Mike Kazior, MD", note: "Curriculum fit · learner access · equipment home" },
    { role: "Resident collaborator", name: "Marjo Beltoja, MD", note: "Scenario ops · learner liaison · labeling" },
  ];

  team.forEach((t, i) => {
    const x = 0.5 + i * 3.1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x,
      y: 1.1,
      w: 2.95,
      h: 1.55,
      fill: { color: C.card },
      line: { color: C.line },
      rectRadius: 0.1,
      shadow: shadowSoft(),
    });
    s.addText(t.role.toUpperCase(), {
      x: x + 0.2,
      y: 1.25,
      w: 2.55,
      h: 0.25,
      fontSize: 10,
      fontFace: "Calibri",
      bold: true,
      color: C.teal,
      charSpacing: 0.8,
      margin: 0,
    });
    s.addText(t.name, {
      x: x + 0.2,
      y: 1.55,
      w: 2.55,
      h: 0.4,
      fontSize: 15,
      fontFace: "Arial",
      bold: true,
      color: C.ink,
      margin: 0,
    });
    s.addText(t.note, {
      x: x + 0.2,
      y: 2.05,
      w: 2.55,
      h: 0.4,
      fontSize: 12,
      fontFace: "Calibri",
      color: C.slate,
      margin: 0,
    });
  });

  // Budget strip
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 0.5,
    y: 2.9,
    w: 9,
    h: 2.0,
    fill: { color: C.deep },
    line: { color: C.deep },
    rectRadius: 0.12,
  });

  s.addText("DEPARTMENTAL ASK", {
    x: 0.8,
    y: 3.1,
    w: 3,
    h: 0.25,
    fontSize: 11,
    fontFace: "Calibri",
    bold: true,
    color: C.mint,
    charSpacing: 1.5,
    margin: 0,
  });

  const budgets = [
    { k: "Preferred", v: "$12,500", d: "Halo ×1–2 + app + scenarios" },
    { k: "Minimum viable", v: "$7,500", d: "Halo ×1 + narrower software" },
    { k: "Phone-only start", v: "$4–5k", d: "If hardware must wait" },
  ];
  budgets.forEach((b, i) => {
    const x = 0.8 + i * 3.0;
    s.addText(b.k, {
      x,
      y: 3.45,
      w: 2.7,
      h: 0.25,
      fontSize: 12,
      fontFace: "Calibri",
      color: C.soft,
      margin: 0,
    });
    s.addText(b.v, {
      x,
      y: 3.75,
      w: 2.7,
      h: 0.4,
      fontSize: 26,
      fontFace: "Arial",
      bold: true,
      color: C.white,
      margin: 0,
    });
    s.addText(b.d, {
      x,
      y: 4.25,
      w: 2.7,
      h: 0.3,
      fontSize: 12,
      fontFace: "Calibri",
      color: C.mintSoft,
      margin: 0,
    });
  });

  footer(s, 9);
}

// ═══════════════════════════════════════════════════════════
// 10 — Roadmap + close
// ═══════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  addDarkBg(s);

  s.addText("NEXT 12 MONTHS", {
    x: 0.5,
    y: 0.45,
    w: 6.3,
    h: 0.3,
    fontSize: 12,
    fontFace: "Calibri",
    bold: true,
    color: C.mint,
    charSpacing: 2,
    margin: 0,
  });
  s.addText("From concept to abstract", {
    x: 0.5,
    y: 0.8,
    w: 6.3,
    h: 0.5,
    fontSize: 28,
    fontFace: "Arial",
    bold: true,
    color: C.white,
    margin: 0,
  });

  const q = [
    { q: "Q1", d: "Halo + cam-off profile · phone app v0 · 2 scenarios · IRB/education path" },
    { q: "Q2", d: "First learner sessions · label data · cue quality iteration" },
    { q: "Q3", d: "3–5 scenarios · on vs off comparison in sim lab" },
    { q: "Q4", d: "Pilot report · abstract · society grants · equipment with Kazior lab" },
  ];

  q.forEach((item, i) => {
    const y = 1.5 + i * 0.75;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: 0.5,
      y,
      w: 0.7,
      h: 0.55,
      fill: { color: C.panel },
      line: { color: C.panel },
      rectRadius: 0.08,
    });
    s.addText(item.q, {
      x: 0.5,
      y: y + 0.12,
      w: 0.7,
      h: 0.35,
      fontSize: 14,
      fontFace: "Arial",
      bold: true,
      color: C.mint,
      align: "center",
      margin: 0,
    });
    s.addText(item.d, {
      x: 1.4,
      y: y + 0.1,
      w: 5.4,
      h: 0.4,
      fontSize: 14,
      fontFace: "Calibri",
      color: C.white,
      margin: 0,
    });
  });

  // Right rail — what department gets
  s.addText("DEPARTMENT GETS", {
    x: 7.4,
    y: 1.05,
    w: 2.3,
    h: 0.3,
    fontSize: 11,
    fontFace: "Calibri",
    bold: true,
    color: C.mint,
    charSpacing: 1,
    margin: 0,
  });
  [
    "Working sim prototype",
    "3+ scenario cards",
    "Pilot report",
    "Abstract draft",
    "Go / no-go for grants",
    "Gear stays in sim program",
  ].forEach((item, i) => {
    s.addText(item, {
      x: 7.4,
      y: 1.5 + i * 0.48,
      w: 2.3,
      h: 0.4,
      fontSize: 13,
      fontFace: "Calibri",
      color: C.white,
      margin: 0,
    });
  });

  s.addText(
    "Advisory · camera-free · education first  ·  github.com/senrealinvestment/cognitive-companion",
    {
      x: 0.5,
      y: 5.15,
      w: 9,
      h: 0.25,
      fontSize: 11,
      fontFace: "Calibri",
      color: C.soft,
      margin: 0,
    }
  );
}

const out = path.join(
  __dirname,
  "Cognitive-Companion-Presentation.pptx"
);
pres
  .writeFile({ fileName: out })
  .then(() => {
    console.log("Wrote", out);
  })
  .catch((err) => {
    console.error(err);
    process.exit(1);
  });
