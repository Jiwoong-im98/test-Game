# harness_test

Claude Code로 새 프로젝트를 시작할 때 사용하는 **시작 템플릿** 저장소입니다.
어떤 작업(백엔드, 프론트엔드, 스크립트 등)이든 이 저장소를 복제해서 시작할 수 있도록
프로젝트 성격에 무관한 공용 설정만 담고 있습니다.

## 사용법
1. 이 저장소를 새 프로젝트 이름으로 클론합니다.
   ```
   git clone https://github.com/Jiwoong-im98/harness_test.git my-new-project
   cd my-new-project
   git remote set-url origin <새 프로젝트의 원격 저장소 URL>
   ```
2. `CLAUDE.md`의 "작성 예정" 항목(프로젝트 개요, 구조, 명령어, 컨벤션)을 채웁니다.
3. 필요하면 `.claude/agents`, `.claude/commands`, `.claude/skills`에 프로젝트 전용 커스터마이징을 추가합니다.

## 구조
- `CLAUDE.md` — Claude Code가 이 프로젝트에서 따를 규칙/컨텍스트 (프로젝트마다 채워 넣는 템플릿)
- `.claude/settings.json` — 공용으로 안전한 명령어(git status/diff/log, npm/yarn/pnpm install·run·test, pip, pytest 등) 권한 프롬프트를 줄여주는 기본 allowlist. 팀에 권장하는 플러그인(`andrej-karpathy-skills`, `i-have-adhd`)도 `extraKnownMarketplaces`/`enabledPlugins`로 선언되어 있음
- `.claude/agents/`, `.claude/commands/`, `.claude/skills/` — 프로젝트 전용 서브에이전트/슬래시커맨드/스킬을 넣는 자리
