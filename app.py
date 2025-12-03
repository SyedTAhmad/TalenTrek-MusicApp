import streamlit as st

st.set_page_config(layout="wide")


# ------------------ PAGE STATE ------------------
if "page" not in st.session_state:
  st.session_state.page = "question1"
if "score" not in st.session_state:
  st.session_state.responses = {}

# Navigation callbacks

def go_q1():
    st.session_state.page = "question1"

def go_q2():
    st.session_state.page = "question2"

def go_q3():
    st.session_state.page = "question3"

def go_q4():
    st.session_state.page = "question4"

def go_q5():
    st.session_state.page = "question5"

def go_chordsIntroPage():
   st.session_state.page = "chordsIntroPage"

def go_Tq1():
    st.session_state.page = "questionT1"

def go_Tq2():
    st.session_state.page = "questionT2"

def go_Tq3():
    st.session_state.page = "questionT3"

def go_Tq4():
    st.session_state.page = "questionT4"

def go_Tq5():
    st.session_state.page = "questionT5"

def go_summary():
    st.session_state.page = "summary"

# ------------------ Definitions ------------------

def question1():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">I cannot read music at all</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">I can identify basic notes on the staff but read slowly</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">I can read music fluently at a moderate tempo</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">I can sight-read complex pieces at performance tempo</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQ1Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("Question 1")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    Which of the following best describes your experience with reading musical notation?
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q1Key",
        html=html_code,
        js=js_code
    )

    response = component(key="q1Key")

    if response and hasattr(response, "getQ1Response"):
        st.session_state.q1Score = response.getQ1Response

    st.button("Continue", on_click=go_q2, disabled=st.session_state.get("q1Score", None) is None)

def question2():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">How loud or soft the music is</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">The speed of the music</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">The emotional feeling of the music</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">The instrument being played</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQ2Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("Question 2")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    In music, what does the term "tempo" refer to?
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q2Key",
        html=html_code,
        js=js_code
    )

    response = component(key="q2Key")

    if response and hasattr(response, "getQ2Response"):
        st.session_state.q2Score = response.getQ2Response

    st.button("Continue", on_click=go_q3, disabled=st.session_state.get("q2Score", None) is None)

def question3():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">1 beat</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">1.5 beats</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">2 beats</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">3 beats</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQ3Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("Question 3")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
     How many beats does a dotted quarter note receive in 4/4 time?
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q3Key",
        html=html_code,
        js=js_code
    )

    response = component(key="q3Key")

    if response and hasattr(response, "getQ3Response"):
        st.session_state.q3Score = response.getQ3Response

    st.button("Continue", on_click=go_q4, disabled=st.session_state.get("q3Score", None) is None)

def question4():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">C - D - E - F - G - A - B - C</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">C - D - E♭ - F - G - A - B♭ - C</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">C - D - E - F# - G - A - B - C</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">C - D♭ - E♭ - F - G - A♭ - B♭ - C</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQ4Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("Question 4")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    Which of the following is the correct order of notes in a C major scale?
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q4Key",
        html=html_code,
        js=js_code
    )

    response = component(key="q4Key")

    if response and hasattr(response, "getQ4Response"):
        st.session_state.q4Score = response.getQ4Response

    st.button("Continue", on_click=go_q5, disabled=st.session_state.get("q4Score", None) is None)

def question5():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">I've never practiced a musical instrument</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">I've tried learning but practice less than once a month</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">I practice 1-3 times per week</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">I practice daily or almost daily</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQ5Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("Question 5")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    Which of the following best describes your musical practice habits?
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q5Key",
        html=html_code,
        js=js_code
    )

    response = component(key="q5Key")

    if response and hasattr(response, "getQ5Response"):
        st.session_state.q5Score = response.getQ5Response

    st.button("Continue", on_click=go_chordsIntroPage, disabled=st.session_state.get("q5Score", None) is None)

def chordsIntroPage():
    # Use some padding-top to move the text higher
    st.markdown(
        """
        <div style="
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            height: 50vh;
            padding-top: 100px;  /* Adjust this to move text higher or lower */
            background-color: white;
            font-family: Arial, sans-serif;
        ">
            <div style="
                font-size: 48px;
                font-weight: bold;
                margin-bottom: 0px;  /* Space between text and button */
            ">
                Chord Recognition Section
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Streamlit button under the text
    if st.button("Continue"):
        go_Tq1()  # Call your function



def questionT1():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">C Major</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">C Minor</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">A Minor</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">G Major</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQT1Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("question 1")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    What is this Chord: C - E - G?
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q1Tkey",
        html=html_code,
        js=js_code
    )

    response = component(key="q1Tkey")

    if response and hasattr(response, "getQT1Response"):
        st.session_state.q1TScore = response.getQT1Response

    st.button("Continue", on_click=go_Tq2, disabled=st.session_state.get("q1TScore", None) is None)

def questionT2():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">F Major</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">F Minor</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">C Minor</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">D Minor</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQT2Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("question 2")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    What is this Chord: F - A♭ - C
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q2Tkey",
        html=html_code,
        js=js_code
    )

    response = component(key="q2Tkey")

    if response and hasattr(response, "getQT2Response"):
        st.session_state.q2TScore = response.getQT2Response

    st.button("Continue", on_click=go_Tq3, disabled=st.session_state.get("q2TScore", None) is None)

def questionT3():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">G Major</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">G Minor</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">G7</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">C7</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQT3Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("question 3")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    What is this Chord: G - B - D - F
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q3Tkey",
        html=html_code,
        js=js_code
    )

    response = component(key="q3Tkey")

    if response and hasattr(response, "getQT3Response"):
        st.session_state.q3TScore = response.getQT3Response

    st.button("Continue", on_click=go_Tq4, disabled=st.session_state.get("q3TScore", None) is None)

def questionT4():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">E Major</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">A Minor</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">G Major</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">E Minor</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQT4Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("question 4")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    What is this Chord: E - G - B
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q4Tkey",
        html=html_code,
        js=js_code
    )

    response = component(key="q4Tkey")

    if response and hasattr(response, "getQT4Response"):
        st.session_state.q4TScore = response.getQT4Response

    st.button("Continue", on_click=go_Tq5, disabled=st.session_state.get("q4TScore", None) is None)

def questionT5():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">D Minor</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">D Major</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">A Major</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">G Major</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQT5Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("question 5")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    What is this Chord: D - F# - A
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q5Tkey",
        html=html_code,
        js=js_code
    )

    response = component(key="q5Tkey")

    if response and hasattr(response, "getQT5Response"):
        st.session_state.q5TScore = response.getQT5Response

    st.button("Continue", on_click=go_summary, disabled=st.session_state.get("q5TScore", None) is None)

def summary():
    st.title("Summary")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown("**Musical Experience Section**")

    # Define the answer key for questions 2-4
    answer_key = {
        2: "B",
        3: "B",
        4: "A"
    }

    # Collect user choices from session state
    user_choices = {
        2: st.session_state.get("q2Score", None),
        3: st.session_state.get("q3Score", None),
        4: st.session_state.get("q4Score", None)
    }

    # Build the HTML for each question
    html_output = ""
    for q_num, user_choice_num in user_choices.items():
        if user_choice_num is None:
            continue  # skip if no answer

        # Convert numeric choice to letter
        choice_letter = chr(ord("A") + user_choice_num - 1)
        
        # Determine correctness
        correct = choice_letter == answer_key[q_num]
        box_color = "green" if correct else "red"
        
        html_output += f"""
        <div style="
            display: flex; 
            align-items: center; 
            margin-bottom: 8px;
            font-family: Arial, sans-serif;
        ">
            <div style="
                width: 20px; 
                height: 20px; 
                background-color: {box_color}; 
                margin-right: 10px; 
                border-radius: 4px;
            "></div>
            <div style="flex: 1;">Question {q_num}</div>
            <div>Choice: {choice_letter}</div>
        </div>
        """

    # Display the HTML in Streamlit
    st.markdown(html_output, unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.markdown("**Chord Recognition Section**")
    # Define the answer key
    answer_key = {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "B"
    }

    # Collect user choices from session state
    user_choices = {
        1: st.session_state.get("q1TScore", None),
        2: st.session_state.get("q2TScore", None),
        3: st.session_state.get("q3TScore", None),
        4: st.session_state.get("q4TScore", None),
        5: st.session_state.get("q5TScore", None)
    }

    # Build the HTML for each question
    html_output = ""
    for q_num, user_choice_num in user_choices.items():
        if user_choice_num is None:
            continue  # skip if no answer

        # Convert numeric choice to letter
        choice_letter = chr(ord("A") + user_choice_num - 1)
        
        # Determine correctness
        correct = choice_letter == answer_key[q_num]
        box_color = "green" if correct else "red"
        
        html_output += f"""
        <div style="
            display: flex; 
            align-items: center; 
            margin-bottom: 8px;
            font-family: Arial, sans-serif;
        ">
            <div style="
                width: 20px; 
                height: 20px; 
                background-color: {box_color}; 
                margin-right: 10px; 
                border-radius: 4px;
            "></div>
            <div style="flex: 1;">Question {q_num}</div>
            <div>Choice: {choice_letter}</div>
        </div>
        """

    # Display the HTML in Streamlit
    st.markdown(html_output, unsafe_allow_html=True)


# ------------------ Logic ------------------
if st.session_state.page == "question1":
  question1()
elif st.session_state.page == "question2":
  question2()
elif st.session_state.page == "question3":
  question3()
elif st.session_state.page == "question4":
  question4()
elif st.session_state.page == "question5":
  question5()
elif st.session_state.page == "chordsIntroPage":
  chordsIntroPage()
elif st.session_state.page == "questionT1":
  questionT1()
elif st.session_state.page == "questionT2":
  questionT2()
elif st.session_state.page == "questionT3":
  questionT3()
elif st.session_state.page == "questionT4":
  questionT4()
elif st.session_state.page == "questionT5":
  questionT5()
elif st.session_state.page == "summary":
  summary()
