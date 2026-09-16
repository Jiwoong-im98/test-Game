# CLAUDE.md

Claude Code가 이 저장소에서 작업할 때 참고하는 가이드입니다.
이 파일은 harness_test 템플릿을 복제해서 새 프로젝트를 시작할 때마다 채워 넣습니다.

## 프로젝트 개요
test-game은 턴제(turn-based)/타일 이동 기반의 픽셀아트 로그라이트 던전 크롤러다. 현재는 고정된 방 하나만 존재하며 절차적 생성(procedural generation)은 아직 구현하지 않았다.

## 구조
- `main.py` — 엔트리 포인트: `Game` 인스턴스를 만들고 `game.run()` 호출
- `game/__init__.py` — `game` 패키지
- `game/game.py` — `Game` 클래스: 초기화(pygame.init, 디스플레이, 클록), 메인 루프(이벤트 처리/QUIT·ESC, 화면 클리어, flip, tick)
- `game/settings.py` — 화면 크기, FPS, `TILE_SIZE`, 색상 팔레트 등 전역 상수
- `assets/images/`, `assets/sounds/` — 이미지/사운드 에셋
- `tests/` — pytest 테스트

## 개발 명령어
- 의존성 설치: `pip install -e ".[dev]"`
- 테스트: `pytest`
- 게임 실행: `python main.py`

## 컨벤션
기본 스택은 Python. 다른 언어로 프로젝트를 시작하면 이 항목들을 그 언어 관용에 맞게 다시 정한다.

- **네이밍**: 함수/변수 `snake_case`, 클래스 `PascalCase`, 상수 `UPPER_SNAKE_CASE`
- **커밋 메시지**: Conventional Commits — `feat:`, `fix:`, `refactor:`, `test:`, `docs:`, `chore:`
- **테스트**: TDD를 강제하진 않음(상황별 판단). 단, **버그 수정은 예외 없이** 재현 테스트를 먼저 작성해 실패를 확인한 뒤 고치고 통과시킨다. 실행 명령은 `개발 명령어` 참고.
- **코드 스타일**: PEP 8, 포맷터 `black`, 린트 `ruff` (저장 시 자동 실행됨 — `.claude/settings.json`의 PostToolUse hook)
- **코드 크기**: 함수는 30~50줄, 파일은 300~400줄 넘으면 분리. 단, 단순 분기/매핑 나열처럼 쪼개도 가독성이 안 좋아지는 경우는 예외 (억지로 쪼개지 말 것)

에이전트의 코딩 습관(가정 명시, 최소 변경, 최소 코드)은 아래 Karpathy 가이드라인이 이미 담당하므로 여기서 중복 작성하지 않는다.

---

<!-- Below: Karpathy-Inspired Claude Code Guidelines (https://github.com/multica-ai/andrej-karpathy-skills) -->

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.
