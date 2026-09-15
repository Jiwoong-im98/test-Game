# skills

이 프로젝트 전용 스킬을 넣는 폴더입니다.

## 기본 제공 스킬
- `cross-verify` — 위험도 높은 변경(배포, DB 마이그레이션, 삭제/되돌리기 힘든 작업, 보안·인증 코드)을 다른 세션에게 독립적으로 교차검증시킴. side effect(다른 세션에 메시지 전송)가 있어 `disable-model-invocation: true`로 설정되어 있고, 사용자가 `/cross-verify`로 명시적으로 호출할 때만 실행된다. 자세한 내용은 `agents/README.md`의 "검증 수준 선택" 참고.
