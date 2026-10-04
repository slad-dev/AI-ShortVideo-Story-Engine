---
name: douyin-script
description: "Create and analyze story-first Douyin/TikTok-style short-video scripts for an 人生副本 account: cinematic character arcs, reversals, emotional payoffs, immersive second-person AI cartoon storyboards, golden 3-second hooks, 5–8-second image cadence, cautionary life stories, captions, subtitles, editing notes, and publishing prompts. Use when drafting or improving scripts about ordinary people, entrepreneurship traps, familiar-person risks, debt, guarantees, franchise scams, relationship costs, human-nature reversals, or other cautionary life-story videos."
---

# 人生副本脚本工厂

Use this skill to build scripts for an AI-cartoon "人生副本" account. The target format is not generic口播; it is a serialized cautionary story that makes viewers feel "this could happen to me".

## Core Positioning

- Account lane: ordinary-person life traps, entrepreneurship lessons, familiar-person trust risks, debt, guarantees, franchise pits, relationship costs, and human-nature reversals.
- Default video canvas: landscape `16:9`, normally `1920×1080`. Use the wider environment to strengthen immersion and let the viewer see the character together with the dorm, shop, street, family, workplace, bills, inventory, or other consequence-bearing context. Only use another aspect ratio when the user explicitly requests it.
- Visual language: AI-generated cartoon/comic scenes throughout, gray-black documentary mood, selective accent color, expressive recurring characters, and commercial information embedded into the animated world rather than presentation slides.
- Narrative voice: mostly second person ("你"), sometimes third person for distance. Make the viewer experience the story as a life simulation.
- Emotional promise: make the viewer feel a specific emotion, not merely understand a point. Default arc: curiosity in the first 3 seconds, desire or hope in the setup, mounting pressure, a justified reversal/payoff, then a clean takeaway.
- Ethics: do not copy a specific creator's script or protected expression. Borrow structure, pacing, and audience psychology; create original scenarios and wording.

## Default Workflow

1. Clarify only essential unknowns. If topic, audience, or length is missing, infer a reasonable default and state it briefly.
2. Choose one episode type:
   - Single episode: one complete 60s, 3min, 5-8min, or 10-15min story.
   - Two-part story: Part 1 ends at the first irreversible trap; Part 2 resolves collapse and lesson.
   - Competitor teardown: analyze an existing video opening, storyboard, subtitles, editing, and retention devices.
3. Complete the mandatory Story-first engine below before writing hooks, narration, or storyboards. Read `references/story-engine.md` for a cinematic/strong-drama story, a longer episode, or when the user asks for more 爽感、电影感 or richer characters. For a 5–10 minute archetype portrait, a “某类人的一生”, or a benchmark with many vivid episodes, also read `references/archetype-longform.md`.
4. Build hooks from the engine's unresolved contradiction. The first frame and first sentence must carry the same contradiction; do not choose a hook first and retrofit the plot around it.
5. Convert each number, formula, and business concept into a character action, story prop, environmental detail, or diegetic interface before writing image prompts.
6. Compose AI images, subtitle safe areas, overlays, and the rendered master directly in landscape `16:9`; do not design a vertical master and crop, pad, or reframe it later. Create platform-native static covers separately, especially for Xiaohongshu, and verify the current thumbnail crop.
7. If benchmark videos are supplied or the user asks for stronger代入感, read `../explain-commercial-models/references/immersive-second-person-and-shot-rhythm.md` (or `references/immersive-second-person-and-shot-rhythm.md` if bundled) and select a variable experience spine before drafting.
8. If the request includes Douyin or Xiaohongshu performance data, read `../explain-commercial-models/references/domestic-retention-diagnostics-douyin-xhs.md` (or `references/domestic-retention-diagnostics-douyin-xhs.md` if bundled); focus on domestic metrics and do not import TikTok/YouTube benchmarks.
9. Output production-ready sections: story engine card, and for archetype stories a persona-feature ledger plus set-piece map; then script, subtitles, AI image prompts, shot durations, motion labels, editing notes, CTA, title, hashtags, and compliance note.

## Story-first engine (mandatory before storyboard)

Treat every episode as a short film first and a knowledge video second. Do not start with “the lesson is…” or turn a premise into a chronological résumé. Build one story contract, then write only scenes that change its meaning.

1. Choose **one dominant emotional promise**: `爽感释放` (a trapped person regains agency), `憋屈反杀` (contempt becomes a deserved reversal), `身份逆转`, `恐惧代入`, `遗憾`, or `治愈`. Name the feeling the last scene must leave, and make the chosen promise fit the topic rather than forcing revenge into it.
2. Write a **story contract** before the hook:
   - protagonist: public identity, private wound, concrete desire, hidden secret or blind spot, self-justification, and price they may have to pay;
   - counterforce: person, system, family pressure, debt, deadline, or social gaze; state the leverage it has over the protagonist;
   - relationship map: who needs whom, who can expose whom, and whose recognition the protagonist craves;
   - one tracked object, line, or place that can return as desire → cost → truth/safeguard;
   - one core reversal that forces the viewer to reinterpret at least two earlier scenes;
   - three visible foreshadowing details, each with a planned payoff.
3. Build a **pressure ladder**, not a list of events: `desire → reasonable choice → credible small win → hidden transfer of cost → false safety → irreversible choice → reversal/payoff → aftermath`. Make the protagonist act at every turn; coincidence may complicate the situation but cannot solve it.
4. Turn every major claim into evidence on screen: an action, prop, silence, social reaction, changed account balance, dialogue, or location detail. If a sentence only labels a person (“he is powerful”, “she is greedy”, “this was unfair”), replace it with a scene that lets the viewer infer it.
5. Run the **emotion-payoff gate** before storyboard: verify that the early reward later changes meaning, the reversal is caused by planted evidence rather than a surprise lecture, the protagonist pays a real price or makes a real choice, and the ending can be understood from the final image before the moral is spoken. If any answer is no, rebuild the engine.

Keep the existing 60–120 second default when no duration is specified. For “电影感故事”, a complete character arc, or a premise that needs breathing room, propose either a 3–8 minute version or a two-part serial rather than flattening it into 60 seconds. Each part must still have its own hook, turn, and emotional payoff.

### Archetype portrait and 5–10 minute gate

For a request such as “顶级嘉豪的一生”, do not stretch one plot mechanism into eight minutes. Treat the episode as an **archetype portrait**: the viewer returns for the next recognisable, escalating behavior, not only for a final reversal.

1. Make a **persona-feature ledger** with at least five non-overlapping traits. Each trait needs a ritual/action, a signature phrase, a body detail or prop, the protagonist's self-interpretation, and the group’s visible real reaction. Do not use labels such as “虚荣” or “中二” as a substitute for behavior.
2. Map four to six **set pieces**, each built as `trigger → self-staging action → inner grand narrative → audience/social countershot → concrete residue → bridge to the next trigger`. A set piece must contain several actions and a change of social scale; it is not a single illustrative shot.
3. Choose the viewer engine explicitly. For cringe/comic-archetype stories, use **dramatic irony**: the viewer sees the social truth before the protagonist does. Repeat `他以为… / 观众已看见…` through action and countershot, without explaining the joke twice.
4. Escalate the arena, not merely the volume: private ritual → small group → digital trace → public crowd → lasting social consequence. Let the same trait become costlier in each new arena.
5. Create a transition ledger. End every set piece with an unmet need, object, physical condition, message, crowd reaction, or self-justifying line that causes the next one. Never jump to a fresh anecdote only because it is another example.
6. Protect the protagonist from flat caricature by giving them one private need and a coherent self-written script, but do not rescue them with an unrelated villain, a lecture, or an unearned redemption. Their repeated choices must generate the consequences.

For an 8-minute archetype episode, require 4–6 set pieces, 16+ meaningful micro-beats, and a micro-turn about every 15–30 seconds. The ending may be a final recognition rather than a conventional redemption; it must complete the escalated pattern.

## Golden 3 Seconds

Always produce 3-5 hook options before the final script unless the user asks for only one. Favor these hook families:

- Money temptation + disaster: "投X万，号称一年赚Y万，半年后你只剩一张欠条。"
- Familiar-person betrayal: "老同学敬你的那杯酒，后来让你还了整整两年债。"
- False bargain: "你以为捡漏，其实接住了别人扔不掉的坑。"
- Reverse identity: "你以为自己要当老板，结果成了给店铺打工的人。"
- Time bomb: "真正让你破产的，不是第一个月亏钱，而是第二周那个小异常。"

For more formulas, read `references/hook-bank.md` when generating many hooks or creating a series plan.

For stories with strong later callbacks, offer one consequence-montage hook: show 3-6 rapid flashes of desire, reward, warning, and collapse; make the identity plus concrete cost readable by about three seconds; stabilize into the main animated scene by roughly three to five seconds. Every flash must return later in the episode. Do not use a random highlight reel or let effects delay the hook.

## Strong-hook retention engine

The golden 3 seconds earns the first pause; the story must then earn every next pause. Build a **question ledger** before writing: what question is asked, what answer is delivered, what sharper question opens next, and which object or line will return with a changed meaning.

Use this default escalation for an immersive commercial/life story:

`反常行为 → 道德误判 → 底层机制 → 观众自我牵连 → 可执行防线`

For a trap or money story, use:

`看似占便宜 → 谁接住风险 → 钱/信息/注意力如何移动 → 我为什么也会接住 → 退出条件`

Every 5–15 seconds, create one meaningful development: a new piece of evidence, a decision, a cost, a reversal, a visual analogy, a mechanism reveal, or a direct implication for the viewer. Do not count a new adjective, background, zoom, or repeated conclusion as development. Give a plausible partial explanation early, but delay the complete mechanism until the viewer has seen a concrete consequence or experiment that makes the first explanation insufficient.

Keep three tension lines alive at once: what the protagonist wants or fears, how the commercial mechanism moves money/resources/incentives, and where the viewer recognizes their own behavior. Return to the opening object or sentence at least twice—first as desire, then as cost, and finally as mechanism or safeguard.

For image-first episodes, each frame must contain a meaningful scene, one main claim, one visible object/action, and one unresolved question. Short top/bottom text bands are allowed when attached to the scene; do not turn the episode into blank slides. Split dense mechanisms across several causal frames and use stable color changes to mark question, risk, mechanism, and action phases.

### 国内平台留存漏斗（抖音 / 小红书）

先写出 2 秒、5 秒、15 秒和 30 秒的预期兑现点，再写完整旁白。首帧、首音、封面/标题和第一句必须指向同一个矛盾：人物+后果物+可读数字同时出现；声音在 0.2 秒内启动；问题在 1.8–2.2 秒内说完；5 秒前给出证据；12 秒前出现第一次奖励或代价；30 秒前完成一次小反转。开头不能用系列名、黑场、纯氛围图或一张静态知识卡拖延。

不要把同一剪辑原样跨平台发布。用户未指定长度时，默认交付 60–120 秒抖音快节奏版和 90–180 秒小红书收藏版；只能做一个母版时，用 90–120 秒并分别包装。抖音长故事优先拆成每集独立兑现的上下集；小红书 3–6 分钟深度版只有在旧数据已证明收藏、涨粉或深度观看价值时保留。抖音用 2 秒跳出 × 5 秒完播定位问题；小红书用封面点击 → 2 秒退出 → 5 秒退出 → 收藏/涨粉诊断，并用 `100%-5秒退出` 换算留存。不同平台和不同时长不共用绝对完播阈值。

小红书要单独交付封面、明确的笔记标题、搜索关键词和 30–60 秒内的收藏锚点。封面只放一个中心矛盾和最多两个关键数字，首帧必须立刻证明封面没有标题党。高点击但低收藏/涨粉说明只制造了好奇；中等点击但高收藏/涨粉说明选题匹配，应先强化封面和前 30 秒；低点击但高评论/分享说明正文有效，应先重做封面。

## Immersive second-person mode

When the viewer should feel “这件事发生在我身上”, make `你` the acting subject, not a cosmetic pronoun swap. Enter through a specific place, time, object, body sensation, or social glance. Let the viewer make a choice that is reasonable in the moment, give a real small reward, then let a social reaction, resource change, relationship response, or account number alter its meaning. Delay explanation until after the viewer has lived through the moment.

Use this internal brief:

> 根据用户选择的主题，让观众直接成为故事里的“你”。从具体地点、时间、动作和身体感受进入；让你做出当下看似合理的选择，得到真实的小奖励，再通过社会目光、资源变化、关系反应或账面数字改变这个选择的含义。每 5–15 秒回答一个旧问题并打开一个更尖锐的新问题。让早期物件至少两次回归，分别代表欲望、代价和机制/防线。结尾才提炼规则，不替观众提前下结论。

Choose one variable spine—countdown, repeated small choices, social-gaze chain, false-win reversal, age/stage jumps, or one tracked object. Do not mechanically complete the default story spine. Keep one primary emotional wound or desire, three to five concrete micro-scenes, and one recurring object or sentence. Prefer “你把、你没有、你听见、你假装、你开始” over biography and abstract labels. Add each micro-scene to a ledger with: place/time, visible action, social response, self-justification, immediate reward/cost, and next question.

### Ending that earns likes and saves

The last 10–20% must do more than summarize. Reframe the opening in one memorable sentence, provide 2–3 concrete checks or safeguards, and give a share line aimed at a specific recipient (a friend, partner, colleague, or family member). Likes come from recognition, saves from future usefulness, and shares from a clear person to warn.

## Story Spine

Use the Story-first engine to choose the spine. The following is a fallback, not a checklist to mechanically complete. Preserve the pressure ladder and character causality even when the setting is business, marriage, family, workplace, or an age-spanning life story.

Use this default sequence unless the user provides another structure:

1. Disaster preview: reveal the ending or cost without explaining it.
2. Ordinary start: viewer recognizes the person, money level, relationship, and desire.
3. Temptation: the opportunity looks rational, not stupid.
4. Trust shortcut: familiar person, social proof, contract, platform, or "everyone is doing it".
5. Early sweetener: first few days/weeks look good.
6. First crack: one abnormal detail appears.
7. Escalation chain: problems compound; each decision is understandable but worsens the trap.
8. Point of no return: money, reputation, health, job, relationship, or family is locked in.
9. Collapse: loss becomes concrete.
10. Aftermath and lesson: what the viewer should remember.

For longer scripts, read `references/story-factory.md`. For reversal types, character construction, scene conversion, and the anti-exposition pass, read `references/story-engine.md`.

When the story naturally contains repeated rewards and consequences, a useful optional pattern is:

`status gap -> tempting shortcut -> first reward -> hidden cost -> temporary relief -> deeper obligation -> deadline -> collapse -> mechanism -> safeguard`

Do not force this pattern. Some stories need one decision and one decisive consequence; others naturally contain several apparent wins. Preserve believable causality instead of inventing false wins, setbacks, or relief beats.

Move quickly on short-video platforms. In the first 30 seconds, aim for a meaningful new development about every 5-10 seconds: a contrast, decision, reward, warning, number, consequence, or reversal. After that, adjust to the story, usually introducing a new development every 10-25 seconds. Cut background that does not change the situation or deepen the commercial mechanism.

## Animation-only Visual Standard

- Keep the production canvas landscape `16:9` by default, normally `1920×1080`. Write every image prompt for a horizontal cinematic composition with meaningful foreground, character, and environmental context. Do not leave empty side areas or stretch a vertical illustration to fill the frame.
- Keep the full episode in one animated visual language. Plot scenes, calculations, business explanations, summaries, and safeguards all need cartoon/comic compositions.
- Ban PPT-style inserts: full-screen headline cards, giant-number slides, formula pages, bullet-list panels, spreadsheet screenshots, chart templates, and dark empty backgrounds used mainly to hold text.
- Show business logic through the story world. Put figures on receipts, wage envelopes, rent notices, POS screens, phones, ledgers, cartons, menus, calendars, or labels beside concrete objects.
- Keep text overlays brief and attached to what the viewer is seeing. The animated scene must still explain the idea if the overlay is removed.
- Default each still image to a 5–8 second shot. Split narration at semantic actions so one image carries one main action, one main evidence object, and one unresolved question. Do not let an unchanged image exceed 8 seconds by default; a justified reflective hold may approach 10 seconds, but cannot be hidden by slow zoom alone.
- When a concept needs several quantities, compose an animated information scene with the protagonist and the relevant objects. Generate a new scene instead of falling back to a data card.

Example: to explain monthly costs, show the owner surrounded by a landlord's rent envelope, employee wage packets, utility bills, and maintenance equipment, each carrying a small numeric label. Do not show a slide titled “monthly fixed costs.”

## Camera and Editing Motion

- Permit one polished entrance in the first three seconds. Use it to strengthen the hook, then stabilize.
- After three seconds, make still frames the default. Use a centered 2-6% keyframed zoom-in or zoom-out only when the story needs emphasis.
- Keep each zoom smooth and one-directional for the full shot. Do not repeatedly zoom in and out.
- Do not use horizontal pans, left-right drift, alternating crop motion, shaking, random parallax, or movement added only to make a still image look busy.
- Create rhythm through new animated compositions, expressions, props, actions, sound, and causal cuts. Use hard cuts at reversals and brief dissolves for time or emotion changes.
- Choose transitions semantically: use a match cut for the same object or causal chain, a 0.20-0.45-second dissolve for time/place/emotion continuity, a brief double exposure for visible reward versus hidden cost, and a hard cut for an irreversible decision, deadline, or mechanism reveal.
- Keep transition effects at shot boundaries. After the transition, stabilize the new image instead of continuing to pan or shake it.

### Audio–subtitle synchronization gate

For the known failure modes and implementation checklist, read `../explain-commercial-models/references/audio-subtitle-sync-postmortem.md` (or `references/audio-subtitle-sync-postmortem.md` if bundled) before rendering or redubbing.

- Generate subtitles from the same TTS pass that creates the audio, using sentence/word boundary timestamps. Do not estimate cue timing by dividing a scene's duration by the number of text chunks.
- Accumulate scene offsets from the actual encoded clip durations. If the renderer uses `-shortest`, do not add nominal padding to the subtitle timeline; it will create cumulative drift after every scene.
- Cache the source narration, voice, rate, pitch, and boundary cues together. Any narration or TTS-parameter change invalidates the old audio and subtitles; never reuse a cached MP3 with a new text timeline.
- If the TTS provider supplies no boundary events, use a subtitle-capable TTS output or a forced-aligner/manual timing pass. Do not publish an estimated timeline.
- Run a sync audit before delivery: no cue should remain on screen more than 150 ms after its spoken boundary, and the first, middle, and final scenes must be checked visually. A mismatch is a release blocker, not a cosmetic issue.

## Two-Part Split Rules

Use a two-part structure when the story is over 3 minutes, has a strong mystery, or the user wants follower conversion.

- Part 1 ending choices:
  - Stop when the first hidden condition is discovered.
  - Stop after the protagonist has paid and cannot easily exit.
  - Stop at a phone call/message that changes the meaning of the opportunity.
  - Stop when a visual clue reveals "this was not a deal, it was a transfer of risk."
- Part 1 CTA: ask for attention without sounding needy. Example: "下一集，你会看到这家店真正亏钱的地方，根本不在房租。"
- Part 2 opening: recap in one sentence, then immediately reveal the consequence.

## Output Format

When drafting a script, use this structure:

```markdown
# 人生副本脚本

## 基本设定
- 主题:
- 目标观众:
- 视频长度:
- 单集/上下集:
- 情绪主线:

## 故事引擎卡（先完成，后写分镜）
- 情绪承诺 / 结尾余味:
- 一句话前提（人物 + 欲望 + 代价）:
- 主角：公开身份 / 私密伤口 / 欲望 / 盲点或秘密 / 自我辩护 / 代价:
- 对抗力量与权力关系:
- 核心反转（会重新解释哪两处前情）:
- 贯穿物件、台词或地点（欲望 → 代价 → 真相）:
- 伏笔回收表（至少 3 条）:
  - 伏笔 → 出现场景 → 回收场景 → 意义如何改变
- 压力阶梯（小赢、假安全、不可逆选择、兑现）:
- 结局画面（即使关掉旁白也看得懂）:

## 人物类型台账（“某类人的一生”或 5 分钟以上人物肖像必填）
| 人物特征 | 可见仪式/动作 | 口头禅 | 身体/道具细节 | 他以为自己是什么 | 别人实际怎么反应 | 在第几场升级 |
|---|---|---|---|---|---|---|

## 场景组地图（“某类人的一生”或 5 分钟以上人物肖像必填）
| 场景组 | 触发 | 自我表演 | 观众先看见的真相 | 留下的具体后果 | 通向下一场的钩子 |
|---|---|---|---|---|---|

## 黄金3秒候选
1. ...
2. ...
3. ...

## 正片脚本
| 时间（单图目标5–8秒） | 动画画面/商业信息场景化 | 旁白 | 字幕 | 镜头运动 | 情绪/剪辑 |
|---|---|---|---|---|---|
| 0-3s | ... | ... | ... | opening entrance | ... |

## AI漫画分镜提示词
| 镜头 | 动画画面提示词 | 商业数字依附物 | 人物表情 | 色彩/氛围 | 镜头运动 |
|---|---|---|---|---|---|

## 剪辑提示
- BGM:
- 音效:
- 字幕:
- 转场:
- 节奏:

## 发布包
- 抖音标题/封面字/话题/置顶评论:
- 小红书独立封面/笔记标题/搜索关键词/收藏锚点/关注承诺:
- 合规声明:
```

When doing competitor teardown, read `references/competitor-teardown.md`. Cover the following in concise prose, selecting only what materially explains the video's performance:

- First-frame hook
- First 3 seconds wording
- Visual style
- Subtitle style
- Audio/editing devices
- Important transition choices when they materially affect the video
- Retention chain
- Major rises, reversals, deadlines, and consequences without forcing a formal tension curve
- Viewer-trigger map: desire, shame, status, secrecy, exact numbers, countdown, and callbacks
- What to imitate structurally
- What to avoid copying
- Adapted hook/script options for our account

When completion is a priority, add a compact **留人账本** to the draft: opening question, each major answer, next open question, mid-video reframe, callback object, and final practical payoff. Use it as a production check rather than a decorative tension curve.

## Quality Checklist

Before finalizing, verify:

- The video master, generated scenes, subtitle layout, and overlays are consistently landscape `16:9` unless the user explicitly chose another ratio; platform covers are separate assets, and the Xiaohongshu cover is verified in its current thumbnail crop.
- The first 3 seconds contain a number, contradiction, danger, or familiar-person pressure.
- The protagonist's first decision feels reasonable.
- A story engine card exists before the hook and storyboard; it names one emotional promise, a character wound/desire, counterforce leverage, a core reversal, one recurring object/line/place, and at least three foreshadowing payoffs.
- The protagonist is active: each escalation follows a choice, refusal, concealment, or attempt to regain control. Do not let coincidence, a narrator lecture, or an off-screen authority create the payoff.
- The early reward or apparent victory changes meaning after the reversal; the payoff is earned by planted evidence rather than an unprepared twist.
- Major character traits are shown through scenes, actions, objects, dialogue, body language, or other characters’ reactions. Remove labels and moralizing exposition that a visual scene can carry.
- For archetype portraits or 5–10 minute episodes, a persona-feature ledger and 4–6 set-piece map exist before prose. Every set piece shows a distinct behavior rather than restating the same trait in a new location.
- For cringe/comic stories, establish dramatic irony early: the viewer can read the social reaction before the protagonist misreads it. Escalate the social arena and concrete residue from scene to scene; do not depend on one late reveal.
- Every scene-group hands a physical, emotional, or causal trigger to the next one. If two adjacent segments can be swapped with no loss, rebuild the transition.
- Every major plot beat creates a new question.
- The script includes concrete costs: money, time, job, health, family, debt, or reputation.
- The ending teaches one sentence the viewer can repeat.
- CTA is tied to story curiosity or practical prevention, not generic "点赞关注".
- If the story is fictionalized, include a clear fictionalized/educational disclaimer.
- Every shot, including calculations and summaries, remains an animated composition; PPT-style slide count is zero.
- After the first three seconds, horizontal drift and shake count are zero.
- Motion labels default to `static`; any zoom is centered, smooth, one-directional, and restrained.
- Business figures are readable because they are attached to story objects or interfaces, not because the video abandons the story for a slide.
- Important stylized transitions support meaning and end on a stable composition; ordinary cuts need no written justification.
- Audio and subtitles are generated from one timing source; equal-duration subtitle splitting, cumulative scene padding, and visible subtitle overhang are prohibited.
- The delivery package includes a machine-readable sync audit with encoded clip duration, cumulative drift, subtitle overhang, and any clamped boundary overlap.
- The shot list records a duration for every image; at least 90% of still shots are 5–8 seconds, no unchanged shot exceeds 10 seconds without an explicit narrative reason, and any long narration segment is split into new semantic images.
- The first five seconds use “你” as the acting subject; the script includes at least three concrete micro-scenes, a believable self-justification before a consequence, and an early object/sentence that returns with changed meaning.
- The plot advances quickly and causally; remove any segment that only restates the setup.
- If the opening uses consequence flashes, they are later callbacks rather than unrelated decoration.
- Every 5–15 seconds in the first minute either answers a question, opens a sharper one, changes the interpretation, raises the cost, adds evidence, or makes the mechanism visible.
- For Douyin/Xiaohongshu, the first frame, first sound, cover/title, and first spoken number carry the same contradiction; audio starts within 0.2s, the question ends by about 1.8–2.2s, evidence appears by 5s, the first reward/cost by 12s, and a small reversal by 30s.
- If the account is new and no length is specified, deliver platform-specific cuts: 60–120s for Douyin and 90–180s for Xiaohongshu, or one 90–120s common master with separate packaging. Longer versions need independent payoffs and data showing saves, follows, or deep viewing justify the duration.
- A post-publication review records Douyin 2s/5s retention and Xiaohongshu cover CTR/2s exit/5s exit separately, then compares average watch, the first two curve lows, likes, comments, shares, saves, and follows. Diagnose “data → observation → hypothesis → one-variable edit,” not “it feels boring.”
- The Xiaohongshu package has an explicit note title, a separately composed and crop-verified cover, searchable topic words, and a saveable calculation/check by 30–60s. Do not leave the title field blank or rely on the 16:9 first frame as the cover.
- The opening object, action, or sentence returns with changed meaning at least twice.
- The ending reinterprets the opening and includes 2–3 concrete safeguards plus a specific share recipient; generic engagement bait is not enough.
- If the topic uses psychology or poverty claims, distinguish evidence, disputed research, analogy, and author inference; never reduce hardship to a character flaw.
- For legal, financial, relationship, or public-event inspirations, fictionalize identifiable private details where needed; show consequences and lawful safeguards, never provide evasion tactics or unverified allegations as fact.
