import streamlit as st
from openai import OpenAI
from agno.tools.serpapi import SerpApiTools
from textwrap import dedent
import random
import time


# Set up the Streamlit app


# --- Enhanced Cinematic Dark & Colorful UI ---
st.markdown("""
<style>
body, .stApp {
    background: linear-gradient(135deg, #181c2f 0%, #232946 100%) !important;
    color: #f4f4f4 !important;
    font-family: 'Montserrat', 'Segoe UI', Arial, sans-serif !important;
}
.main, .block-container {
    background: transparent !important;
}
.glass {
    background: rgba(36, 40, 61, 0.7);
    border-radius: 18px;
    box-shadow: 0 8px 32px 0 #23294655;
    border: 1.5px solid #ff512f33;
    backdrop-filter: blur(8px);
    padding: 1.5em 2em;
    margin-bottom: 1.5em;
}
.stButton>button {
    background: linear-gradient(90deg, #ff512f 0%, #dd2476 100%);
    color: #fff;
    border: none;
    border-radius: 10px;
    padding: 0.7em 1.7em;
    font-weight: bold;
    font-size: 1.13em;
    box-shadow: 0 2px 12px #0005;
    transition: transform 0.12s, box-shadow 0.12s, background 0.3s;
    cursor: pointer;
    outline: none;
    position: relative;
    overflow: hidden;
}
.stButton>button:after {
    content: '';
    position: absolute;
    left: 50%;
    top: 50%;
    width: 0;
    height: 0;
    background: rgba(255,255,255,0.2);
    border-radius: 100%;
    transform: translate(-50%, -50%);
    transition: width 0.4s ease, height 0.4s ease;
    z-index: 0;
}
.stButton>button:active:after {
    width: 200px;
    height: 200px;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #43cea2 0%, #185a9d 100%);
    transform: scale(1.07) rotate(-1.5deg);
    box-shadow: 0 6px 24px #0007;
}
.character-card {
    background: linear-gradient(120deg, #232946 60%, #393e6b 100%);
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 16px;
    color: #f4f4f4;
    box-shadow: 0 2px 12px #0003;
    border: 2px solid #ff512f55;
    animation: fadeIn 0.7s;
    position: relative;
    overflow: hidden;
}
.character-card:before {
    content: '';
    position: absolute;
    top: -40px; left: -40px;
    width: 80px; height: 80px;
    background: radial-gradient(circle, #ff512f55 0%, transparent 80%);
    z-index: 0;
}
.actor-card {
    background: linear-gradient(120deg, #232946 60%, #185a9d 100%);
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 16px;
    color: #f4f4f4;
    box-shadow: 0 2px 12px #0003;
    border: 2px solid #43cea255;
    animation: fadeIn 0.7s;
    position: relative;
    overflow: hidden;
}
.actor-card:before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 80px; height: 80px;
    background: radial-gradient(circle, #43cea255 0%, transparent 80%);
    z-index: 0;
}
.timeline {
    background: linear-gradient(90deg, #232946 60%, #ff512f22 100%);
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 16px;
    color: #f4f4f4;
    box-shadow: 0 2px 12px #0003;
    border: 2px solid #43cea255;
    animation: fadeIn 0.7s;
}
.stTextInput>div>input, .stTextArea>div>textarea {
    background: #232946 !important;
    color: #f4f4f4 !important;
    border-radius: 10px !important;
    border: 2px solid #ff512f77 !important;
}
.stSlider>div>div>div {
    background: #ff512f !important;
}
.stSelectbox>div>div>div>div {
    background: #232946 !important;
    color: #f4f4f4 !important;
}
.stExpander {
    background: #232946 !important;
    color: #f4f4f4 !important;
    border-radius: 12px !important;
    border: 2px solid #43cea255 !important;
}
.stProgress>div>div>div {
    background: linear-gradient(90deg, #ff512f 0%, #43cea2 100%) !important;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: none; }
}
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
    color: #ff512f !important;
    font-family: 'Montserrat', sans-serif;
    letter-spacing: 1px;
}
.stInfo, .stSuccess, .stWarning, .stError {
    border-radius: 12px !important;
}
.glass-title {
    font-size: 2.2em;
    font-weight: 800;
    color: #ff512f;
    letter-spacing: 2px;
    text-shadow: 0 2px 12px #0007;
    margin-bottom: 0.1em;
}
.glass-sub {
    font-size: 1.2em;
    color: #43cea2;
    margin-bottom: 0.5em;
    font-weight: 600;
    letter-spacing: 1px;
}
</style>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown("""
<div class='glass' style='text-align:center; margin-bottom: 0.5em;'>
    <img src='https://cdn.pixabay.com/photo/2017/01/31/13/14/movie-2023585_1280.png' width='120' style='margin-bottom:0.2em; filter: drop-shadow(0 2px 12px #ff512f88);'/>
    <div class='glass-title'>AI Movie Production Agent 🎬</div>
    <div class='glass-sub'>Direct your next blockbuster with <span style='color:#ff512f;'>AI-powered creativity</span>!</div>
</div>
""", unsafe_allow_html=True)


# Get OpenAI API key from user
openai_api_key = st.text_input("Enter OpenAI API Key to access GPT-3.5 Turbo", type="password")
# Get SerpAPI key from the user
serp_api_key = st.text_input("Enter Serp API Key for Search functionality", type="password")

def get_openai_response(prompt, api_key, temperature=0.2, max_tokens=512):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content.strip()



if openai_api_key and serp_api_key:
    st.sidebar.markdown("## Response Language")
    response_language = st.sidebar.selectbox(
        "Select response language:",
        [
            "English",
            "Hindi",
            "Bhojpuri",
            "Maithili",
            "Bengali",
            "Tamil",
            "Marathi",
            "Telugu"
        ]
    )
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Progress")
    progress = st.sidebar.progress(0)


    st.markdown("## Step 1: Movie Name & Genre")
    if "movie_name" not in st.session_state:
        st.session_state["movie_name"] = ""
    def accept_suggested_name():
        st.session_state["movie_name"] = st.session_state["suggested_movie_name"]
    genre_list = ["Action", "Comedy", "Drama", "Sci-Fi", "Horror", "Romance", "Thriller"]
    mashup_list = ["None"] + genre_list
    col1, col2 = st.columns([2,1])
    with col1:
        movie_name = st.text_input("Enter your movie name (leave blank if unsure):", key="movie_name", value=st.session_state["movie_name"])
        movie_idea = st.text_area("Describe your movie idea in a few sentences:")
    with col2:
        if st.button("🎲 Surprise Me (Genre)"):
            st.session_state["genre"] = random.choice(genre_list)
            st.session_state["mashup_genre"] = random.choice([g for g in mashup_list if g != st.session_state["genre"]])
        genre = st.selectbox("Select the primary movie genre:", genre_list, key="genre")
        mashup_genre = st.selectbox("Select a second genre to mashup (optional):", mashup_list, key="mashup_genre")
    target_audience = st.selectbox("Select the target audience:", ["General", "Children", "Teenagers", "Adults", "Mature"])
    estimated_runtime = st.slider("Estimated runtime (in minutes):", 60, 180, 120)
    progress.progress(10)


    if not st.session_state["movie_name"]:
        colA, colB = st.columns([2,1])
        with colA:
            if st.button("💡 Suggest Movie Name"):
                name_prompt = dedent(f"""
                    Suggest a unique, catchy movie name for the following idea and genre. Respond only in {response_language} language.

                    Movie idea: {movie_idea}
                    Genre: {genre}
                """)
                suggested_name = get_openai_response(name_prompt, openai_api_key, max_tokens=32)
                st.session_state["suggested_movie_name"] = suggested_name
                st.success(f"Suggested Movie Name: {suggested_name}")
        with colB:
            if st.button("🎲 Surprise Me (Name)"):
                st.session_state["suggested_movie_name"] = f"{random.choice(['Project', 'Operation', 'Legend', 'Secret', 'Saga'])} {random.randint(100,999)}"
                st.success(f"Suggested Movie Name: {st.session_state['suggested_movie_name']}")
        if st.session_state.get("suggested_movie_name"):
            st.info(f"Suggested Movie Name: {st.session_state['suggested_movie_name']}")
            st.button("Accept Suggested Name", on_click=accept_suggested_name)
    progress.progress(20)


    st.markdown("---")
    st.markdown("## Step 2: Interactive Character Builder")
    num_characters = st.slider("Number of main characters:", 3, 5, 3)
    character_details = []
    char_cols = st.columns(num_characters)
    for i in range(num_characters):
        with char_cols[i]:
            st.markdown(f"<div class='character-card'><b>Character {i+1}</b>", unsafe_allow_html=True)
            if st.button(f"💡 Suggest Character {i+1}"):
                suggest_prompt = dedent(f"""
                    Suggest a unique character name, trait, and background for a {genre} movie. Return in this format:
                    Name: ...\nTrait: ...\nBackground: ...
                    Movie idea: {movie_idea}
                    Existing characters: {[c['name'] for c in character_details]}
                    Respond only in {response_language} language.
                """)
                suggestion = get_openai_response(suggest_prompt, openai_api_key, max_tokens=128)
                import re
                name_s = re.search(r"Name:\s*(.*)", suggestion)
                trait_s = re.search(r"Trait:\s*(.*)", suggestion)
                background_s = re.search(r"Background:\s*(.*)", suggestion)
                st.session_state[f"name_{i}"] = name_s.group(1).strip() if name_s else ""
                st.session_state[f"trait_{i}"] = trait_s.group(1).strip() if trait_s else ""
                st.session_state[f"background_{i}"] = background_s.group(1).strip() if background_s else ""
            if st.button(f"🎲 Surprise Me (Char {i+1})"):
                st.session_state[f"name_{i}"] = random.choice(["Alex", "Sam", "Jordan", "Riya", "Priya", "Arjun"])
                st.session_state[f"trait_{i}"] = random.choice(["Brave", "Cunning", "Witty", "Kind", "Mysterious"])
                st.session_state[f"background_{i}"] = random.choice(["From a small town", "Secret past", "Lost royalty", "Tech genius", "Street artist"])
            name = st.text_input(f"Name", key=f"name_{i}", value=st.session_state.get(f"name_{i}", ""))
            trait = st.text_input(f"Trait", key=f"trait_{i}", value=st.session_state.get(f"trait_{i}", ""))
            background = st.text_area(f"Background", key=f"background_{i}", value=st.session_state.get(f"background_{i}", ""))
            st.markdown(f"<i>{trait}</i><br><small>{background}</small></div>", unsafe_allow_html=True)
            character_details.append({"name": name, "trait": trait, "background": background})
    progress.progress(30)


    st.markdown("---")
    st.markdown("## Step 3: Budget & Production Planner")
    colb1, colb2, colb3 = st.columns(3)
    with colb1:
        budget = st.number_input("Estimated budget (in USD):", min_value=10000, max_value=100000000, value=1000000, step=10000)
    with colb2:
        location = st.text_input("Preferred shooting location:")
    with colb3:
        timeline = st.slider("Estimated production timeline (months):", 1, 24, 6)
    progress.progress(40)

    if st.button("🚀 Develop Movie Concept"):
        with st.spinner("Developing movie concept..."):
            progress.progress(50)
            # Dynamic Genre Mashup
            genre_text = genre
            if mashup_genre != "None" and mashup_genre != genre:
                genre_text = f"{genre} + {mashup_genre}"
            # ScriptWriter prompt with character details
            char_text = "\n".join([
                f"Name: {c['name']}, Trait: {c['trait']}, Background: {c['background']}" for c in character_details if c['name'] or c['trait'] or c['background']
            ])
            script_prompt = dedent(f"""
                You are an expert screenplay writer. Given the following movie idea, genre (can be a mashup), target audience, estimated runtime, and these main character details, develop a concise hybrid script outline with key plot points, three-act structure, and 2-3 twists. Keep responses brief to minimize token usage and cost.

                Movie idea: {movie_idea}
                Genre: {genre_text}
                Target audience: {target_audience}
                Estimated runtime: {estimated_runtime} minutes
                Main characters:
                {char_text}
                Respond only in {response_language} language.
            """)
            script_outline = get_openai_response(script_prompt, openai_api_key)
            progress.progress(60)

            # Virtual Casting Call
            casting_prompt = dedent(f"""
                You are a talented casting director. Given the following script outline and character descriptions, suggest 2-3 suitable actors for each main role, considering their past performances and current availability. For each actor, provide a short bio and a sample dialogue for their audition. Check actors' current status using Google search. Provide a brief explanation for each casting suggestion. Consider diversity and representation in your casting choices. Keep responses brief to minimize token usage and cost.

                Script outline:
                {script_outline}
                Main characters:
                {char_text}
                Respond only in {response_language} language.
            """)
            casting_suggestions = get_openai_response(casting_prompt, openai_api_key)
            progress.progress(70)

            # Budget & Production Planner prompt
            budget_prompt = dedent(f"""
                You are a professional movie production planner. Given the following script outline, cast, estimated budget, preferred shooting location, and production timeline, estimate a basic production plan. Suggest cost-saving tips, alternative locations, and a timeline breakdown. Keep responses brief to minimize token usage and cost.

                Script outline:
                {script_outline}
                Casting suggestions:
                {casting_suggestions}
                Estimated budget: ${budget}
                Preferred location: {location}
                Production timeline: {timeline} months
                Respond only in {response_language} language.
            """)
            production_plan = get_openai_response(budget_prompt, openai_api_key)
            progress.progress(80)

            # Production Risk Analyzer
            risk_prompt = dedent(f"""
                You are a movie production risk analyst. Analyze the following production plan and highlight potential risks (budget overruns, scheduling conflicts, legal issues). Provide actionable mitigation strategies for each risk.

                Production plan:
                {production_plan}
                Respond only in {response_language} language.
            """)
            risk_analysis = get_openai_response(risk_prompt, openai_api_key, max_tokens=256)
            progress.progress(85)

            # MovieProducer summary prompt
            producer_prompt = dedent(f"""
                You are an experienced movie producer. Summarize the following script outline, casting suggestions, production plan, and risk analysis, and provide a concise movie concept overview. Keep responses brief to minimize token usage and cost.

                Script outline:
                {script_outline}

                Casting suggestions:
                {casting_suggestions}

                Production plan:
                {production_plan}

                Risk analysis:
                {risk_analysis}
                Respond only in {response_language} language.
            """)
            movie_summary = get_openai_response(producer_prompt, openai_api_key)
            progress.progress(90)


            st.markdown("### Script Outline (Hybrid Genre)")
            st.info(script_outline)

            st.markdown("### Virtual Casting Call")
            import re
            actor_blocks = re.split(r'\n(?=Name:)', casting_suggestions)
            actor_votes = {}
            for idx, block in enumerate(actor_blocks):
                if block.strip():
                    name_match = re.search(r'Name:\s*(.*)', block)
                    name = name_match.group(1) if name_match else f"Actor {idx+1}"
                    st.markdown(f"<div class='actor-card'><b>{name}</b>", unsafe_allow_html=True)
                    st.text_area("Bio & Audition", block, height=80, key=f"bio_{idx}")
                    if st.button(f"👍 Vote for {name}", key=f"vote_{idx}"):
                        actor_votes[name] = actor_votes.get(name, 0) + 1
                        st.success(f"You voted for {name}!")
                    with st.expander("Why this actor?"):
                        st.write("AI considered past performances, diversity, and availability.")
                    st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("### Production Plan & Budget")
            st.markdown(f"<div class='timeline'>{production_plan}</div>", unsafe_allow_html=True)
            with st.expander("Show Cost-Saving Tips & Alternatives"):
                st.write("AI suggests alternative locations and cost-saving strategies based on your plan.")

            st.markdown("### Production Risk Analysis")
            risk_level = "success"
            if "overrun" in risk_analysis.lower() or "conflict" in risk_analysis.lower():
                risk_level = "warning"
            if "legal" in risk_analysis.lower() or "critical" in risk_analysis.lower():
                risk_level = "error"
            st.markdown(f"<div class='timeline'><span style='color: {'red' if risk_level=='error' else 'orange' if risk_level=='warning' else 'green'}; font-weight:bold;'>Risk Level: {risk_level.title()}</span></div>", unsafe_allow_html=True)
            with st.expander("Show Risk Mitigation Strategies"):
                st.write(risk_analysis)

            st.markdown("### Movie Concept Overview")
            st.success(movie_summary)
            progress.progress(100)
            # Global Release Planner
            release_prompt = dedent(f"""
                You are a global movie release planner. Based on the following movie concept, cast, and budget, suggest optimal release dates, marketing strategies, and international distribution plans. Include a press release draft and social media campaign ideas.

                Movie concept:
                {movie_summary}
                Cast:
                {casting_suggestions}
                Budget: ${budget}
                Respond only in {response_language} language.
            """)
            release_plan = get_openai_response(release_prompt, openai_api_key, max_tokens=256)
            st.markdown("### Global Release Planner")
            st.write(release_plan)

            # Trailer Script Generator
            trailer_prompt = dedent(f"""
                You are a creative movie trailer writer. Based on the following movie concept, generate a short, dramatic trailer script and a catchy tagline. Make it exciting and suitable for a movie trailer voiceover.

                Movie concept:
                {movie_summary}
                Respond only in {response_language} language.
            """)
            trailer_script = get_openai_response(trailer_prompt, openai_api_key, max_tokens=256)
            st.markdown("### Trailer Script & Tagline")
            st.write(trailer_script)

            # Audience Feedback Simulation
            feedback_prompt = dedent(f"""
                You are simulating audience reviews and social media reactions for the following movie concept. Generate 3-5 short, varied feedback comments as if from viewers and social media users. Include both positive and constructive feedback to help refine the idea. Use a realistic, conversational style.

                Movie concept:
                {movie_summary}
                Respond only in {response_language} language.
            """)
            audience_feedback = get_openai_response(feedback_prompt, openai_api_key, max_tokens=256)
            st.markdown("### Simulated Audience & Social Media Feedback")
            st.write(audience_feedback)

            # Soundtrack & Music Suggestions
            soundtrack_prompt = dedent(f"""
                You are a movie music supervisor. Based on the following movie concept, suggest soundtrack styles, composers, and provide links to royalty-free music or composers suitable for the movie’s mood and genre. If possible, recommend sample music clips or sources.

                Movie concept:
                {movie_summary}
                Respond only in {response_language} language.
            """)
            soundtrack_suggestions = get_openai_response(soundtrack_prompt, openai_api_key, max_tokens=256)
            st.markdown("### Soundtrack & Music Suggestions")
            st.write(soundtrack_suggestions)

            # Legal & Copyright Checklist
            legal_prompt = dedent(f"""
                You are a legal advisor for movie production. Based on the following movie concept, provide a checklist of legal and copyright considerations (e.g., script registration, music rights, actor contracts) to help avoid common legal pitfalls in movie production.

                Movie concept:
                {movie_summary}
                Respond only in {response_language} language.
            """)
            legal_checklist = get_openai_response(legal_prompt, openai_api_key, max_tokens=256)
            st.markdown("### Legal & Copyright Checklist")
            st.write(legal_checklist)

            # Real-Time Collaboration Workspace (Demo)
            st.markdown("### Real-Time Collaboration Workspace (Demo)")
            st.info("Invite collaborators to join your workspace, edit concepts, vote on casting, and chat in real time. (Demo: Shareable link only)")
            share_link = st.text_input("Enter collaborator's email to share your movie concept (demo only):")
            if st.button("Generate Shareable Workspace Link"):
                import uuid
                link = f"https://your-movie-app.com/workspace/{uuid.uuid4()}"
                st.success(f"Share this workspace link with your team: {link}")

            # Budget Breakdown & ROI Estimator
            st.markdown("### Budget Breakdown & ROI Estimator")
            budget_breakdown_prompt = dedent(f"""
                You are a movie finance expert. Based on the following production plan and cast, provide a detailed budget breakdown (cast, crew, locations, marketing, post-production) and estimate potential box office ROI based on genre, cast, and release plan. Respond only in {response_language} language.

                Production plan:
                {production_plan}
                Cast:
                {casting_suggestions}
                Genre: {genre_text}
                Budget: ${budget}
            """)
            budget_breakdown = get_openai_response(budget_breakdown_prompt, openai_api_key, max_tokens=256)
            st.write(budget_breakdown)

            # Talent Discovery & Social Media Integration (Demo)
            st.markdown("### Talent Discovery & Social Media Integration (Demo)")
            talent_prompt = dedent(f"""
                You are a talent scout and social media analyst. Based on the following movie concept and cast, suggest trending or up-and-coming actors, directors, and crew. Provide brief profiles and social reach. Respond only in {response_language} language.

                Movie concept:
                {movie_summary}
                Cast:
                {casting_suggestions}
            """)
            talent_discovery = get_openai_response(talent_prompt, openai_api_key, max_tokens=256)
            st.write(talent_discovery)

            # Festival & Award Strategy Planner
            st.markdown("### Festival & Award Strategy Planner")
            festival_prompt = dedent(f"""
                You are a film festival and award strategist. Based on the following movie concept, genre, and production timeline, suggest film festivals, award shows, and submission deadlines. Generate AI-powered award campaign strategies and press kit drafts. Respond only in {response_language} language.

                Movie concept:
                {movie_summary}
                Genre: {genre_text}
                Production timeline: {timeline} months
            """)
            festival_strategy = get_openai_response(festival_prompt, openai_api_key, max_tokens=256)
            st.write(festival_strategy)