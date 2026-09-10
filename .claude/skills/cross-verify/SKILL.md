---
name: cross-verify
description: Sends a risky or high-stakes change (deployment, database migration, destructive operation, security/auth code) to another open terminal session for independent cross-verification via SendMessage. Use only when the user explicitly asks for cross-session verification or a second-terminal check — not for routine changes, where the reviewer subagent is enough. Has a side effect (messages another session), so only invoke when asked.
disable-model-invocation: true
---

지금까지의 변경사항 "$ARGUMENTS"을(를) 다른 세션에게 독립적으로 검증받아줘.

**먼저 판단**: 이 변경이 정말 2세션 교차검증이 필요한 수준인지 확인해. 배포, DB 마이그레이션, 삭제/되돌리기 힘든 작업, 보안·인증 관련 코드, 큰 아키텍처 변경처럼 실패 비용이 큰 경우에만 아래 절차를 쓰고, 일상적인 변경이면 사용자에게 `reviewer` 서브에이전트로도 충분하다고 알리고 그걸 대신 제안해. (2세션 검증은 서브에이전트 리뷰보다 토큰 비용이 훨씬 크다.)

1. `git diff`, `git diff --staged`, 또는 사용자가 지정한 범위로 검증 대상 변경사항을 파악해.
2. `ListAgents`로 이 머신에 열려있는 다른 세션이 있는지 확인해.
   - **다른 세션이 있으면**: `SendMessage`로 그 세션에 보내. 원본 코드나 diff 전체를 복사해 붙여넣지 말고, 파일 경로와 변경 요지를 요약해서 보내고 "본인 컨텍스트에서 해당 파일을 직접 읽고 독립적으로 검증해달라"고 요청해 (같은 결론을 베끼지 않도록). 구체적으로 무엇을 확인해달라는지 명시해: 정확성, 놓친 엣지케이스, 이 변경이 실제로 의도대로 동작하는지.
   - **다른 세션이 없으면**: 사용자에게 "지금 열려있는 다른 터미널 세션이 없어 진짜 교차검증은 불가능하다"고 알리고, 대신 `reviewer` 서브에이전트를 호출해서 검증한 뒤 결과를 보고해. 진짜 2세션 검증을 원하면 터미널을 하나 더 열어달라고 안내해.
3. 상대 세션의 응답이 올 때까지 기다려. 절대 응답을 지어내거나 추측하지 마 — 실제 알림이 올 때까지는 "검증 요청 중"이라고만 말해.
4. 응답이 오면 지적된 이슈를 정리해서 사용자에게 보고해. 심각한 이슈가 있으면 고칠지 사용자에게 확인하고, 고치기로 하면 최소한의 수정만 적용해.
