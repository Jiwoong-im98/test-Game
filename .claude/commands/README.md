# commands

이 프로젝트 전용 슬래시 커맨드(.md)를 넣는 폴더입니다.

## 기본 제공 커맨드
- `/commit` — 변경사항 확인 후 의미 단위로 커밋
- `/catchup` — 최근 커밋/변경 내역으로 프로젝트 현재 상태 파악
- `/todos` — 코드베이스 전체 TODO/FIXME/HACK 주석 목록화
- `/pr-description` — 현재 브랜치 diff로 PR 제목/설명 초안 작성
- `/orchestrate <작업 내용>` — planner → coder → tester → reviewer 서브에이전트를 순서대로 지휘해 작업 처리 (agents/README.md의 "오케스트레이션 파이프라인" 참고)
