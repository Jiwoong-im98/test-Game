# agents

이 프로젝트 전용 커스텀 서브에이전트 정의(.md)를 넣는 폴더입니다.

## 기본 제공 에이전트
- `reviewer` — 읽기 전용, 코드 변경사항의 정확성/중복/효율성 이슈만 리뷰(수정은 안 함)
- `debugger` — 실패하는 테스트/에러를 재현하고 근본 원인을 찾아 최소한의 수정 적용
- `doc-updater` — 코드 변경 후 CLAUDE.md/README.md를 실제 상태에 맞게 갱신(새 문서 작성 X)
- `harness-auditor` — 읽기 전용, 애플리케이션 코드가 아니라 하네스 자체(`.claude/settings.json`의 권한·hook·플러그인 선언, agents/commands/skills 정의, CLAUDE.md 정합성)를 점검(수정은 안 함)

## 오케스트레이션 파이프라인 에이전트
`/orchestrate` 커맨드가 순서대로 지휘하는 4개 역할 (메인 에이전트가 각 단계 결과를 검증하며 다음 단계로 넘김):
- `planner` — 읽기 전용, 작업을 구체적인 단계별 계획으로 분해
- `coder` — 계획의 한 단계씩 좁은 범위로 구현
- `tester` — 구현을 실제로 실행/테스트해서 PASS/FAIL 근거와 함께 검증 (자체 검증 담당)
- `reviewer` — 최종 코드 리뷰 (위 3개와 조합해 재사용)

문제가 반복되면 `tester` → `debugger`로 전환해 근본 원인을 분석한다.

## 검증 수준 선택
- **평소 변경**: `reviewer` 서브에이전트로 충분. 같은 세션 안에서 돌기 때문에 비용이 작다.
- **위험도가 높은 변경** (배포, DB 마이그레이션, 삭제/되돌리기 힘든 작업, 보안·인증 관련 코드): `.claude/skills/cross-verify/SKILL.md`(`/cross-verify`)로 다른 터미널(세션)에게 독립적으로 교차검증시킨다. 두 세션이 각자 전체 컨텍스트를 유지하므로 토큰 비용이 `reviewer` 서브에이전트보다 훨씬 크니, 정말 필요한 경우에만 쓴다. side effect(다른 세션에 메시지 전송)가 있어 `disable-model-invocation: true`로 설정돼 있으므로 사용자가 명시적으로 `/cross-verify`를 호출해야만 실행된다.
